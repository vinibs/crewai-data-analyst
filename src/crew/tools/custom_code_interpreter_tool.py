from contextlib import redirect_stdout
from io import StringIO
from typing import List

import docker
from crewai_tools import CodeInterpreterTool


class CustomCodeInterpreterTool(CodeInterpreterTool):
    def __init__(self, *, run_in_docker: bool = True):
        super().__init__()
        self._run_in_docker = run_in_docker
        self._python_lib_os_dependencies = {
            "psycopg2": ["libpq-dev"],
            "mariadb": ["default-libmysqlclient-dev"],
            "mysql-connector-python": ["default-libmysqlclient-dev"],
            "sqlalchemy": ["libpq-dev", "default-libmysqlclient-dev"],
        }

    def _install_libraries(
        self, container: docker.models.containers.Container, libraries: List[str]
    ) -> None:
        """
        Install missing libraries in the Docker container with their OS dependencies
        """
        self._install_os_packages(container, libraries)
        libraries_str = " ".join(libraries)
        container.exec_run(f"pip install {libraries_str}")

    def _install_os_packages(
        self, container: docker.models.containers.Container, libraries: List[str]
    ) -> None:
        """
        Install missing OS packages in the Docker container
        """
        lib_dependencies_list = (
            self._python_lib_os_dependencies[library]
            for library in libraries
            if library in self._python_lib_os_dependencies.keys()
        )

        os_packages = set()
        for lib_dependencies in lib_dependencies_list:
            os_packages.update(lib_dependencies)

        os_packages_str = " ".join(os_packages)
        container.exec_run(f"apt-get update")
        container.exec_run(f"apt-get install -y {os_packages_str}")

    def _run(self, **kwargs) -> str:
        code = kwargs.get("code", self.code)
        libraries_used = kwargs.get("libraries_used", [])

        default_libraries = list(self._python_lib_os_dependencies.keys())
        all_libraries = list(set([*libraries_used, *default_libraries]))

        if self._run_in_docker:
            return self.run_code_in_docker(code, all_libraries)

        return self.run_code_locally(code)

    def run_code_in_docker(self, code: str, libraries_used: List[str]) -> str:
        super()._verify_docker_image()
        container = self._init_docker_container()
        self._install_libraries(container, libraries_used)

        cmd_to_run = ["python3", "-c", f"{code}"]
        exec_result = container.exec_run(cmd_to_run)

        container.stop()
        container.remove()

        if exec_result.exit_code != 0:
            return f"Something went wrong while running the code: \n{exec_result.output.decode('utf-8')}"
        return exec_result.output.decode("utf-8")

    def run_code_locally(self, code: str) -> str:
        output_file_string = StringIO()
        with redirect_stdout(output_file_string):
            try:
                exec(code)

            except Exception as e:
                return str(e)

        return output_file_string.getvalue()
