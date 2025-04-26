from setuptools import find_packages, setup
from typing import List

hypen_dot = "-e ."


def get_requirements(file_path: str) -> List[str]:
    """retorna lista de requerimentos

    Args:
        file_path (str): caminho dos requerimentos

    Returns:
        List[str]: lista de requerimentos
    """
    requirements = []
    with open(file_path, "r") as file_obj:
        requirements = file_obj.readlines()
        requirements = [
            req.strip() for req in file_obj if req.strip() and req.strip() != hypen_dot
        ]
    return requirements


setup(
    name="ml_project",
    version="0.0.1",
    author="Luiz Angelo",
    author_email="luizgsangelo@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt"),
)
