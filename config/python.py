""" python deps for this project """

import config.shared

install_requires: list[str] = [
    "pytconf",
    "pylogconf",
    "browser_cookie3",
]
build_requires: list[str] = config.shared.PBUILD
test_requires: list[str] = config.shared.PTEST
requires = install_requires + build_requires + test_requires

scripts: dict[str,str] = {
    "pynetflix": "pynetflix.main:main",
}
