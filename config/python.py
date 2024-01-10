from typing import List


console_scripts: List[str] = [
    "pynetflix=pynetflix.main:main",
]
dev_requires: List[str] = [
    "pypitools",
    "black",
]
config_requires: List[str] = [
    "pyclassifiers",
]
install_requires: List[str] = [
    "pytconf",
    "pylogconf",
    "browser_cookie3",
]
make_requires: List[str] = [
    "pydmt",
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
