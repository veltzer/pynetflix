from typing import List


console_scripts: List[str] = [
    "pynetflix=pynetflix.main:main",
]
config_requires: List[str] = []
dev_requires: List[str] = [
    "pypitools",
    "black",
]
make_requires: List[str] = [
    "pyclassifiers",
    "pydmt",
]
install_requires: List[str] = [
    "pytconf",
    "pylogconf",
    "browser_cookie3",
]
test_requires: List[str] = [
    "pytest",
    "pytest-cov",
    "pylint",
    "flake8",
    "pymakehelper",
    "mypy",
]
requires = config_requires + install_requires + make_requires + test_requires
