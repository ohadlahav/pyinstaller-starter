.PHONY: all build

ROOT_DIR:=$(shell dirname $(realpath $(firstword $(MAKEFILE_LIST))))

PYINSTALLER_CMD_FULL := "pyinstaller --onefile --additional-hooks-dir=. --icon=favicon.ico -n main main.py"
PYINSTALLER_CMD_SHORT = "pyinstaller main.spec"

build:
	docker run -v "${ROOT_DIR}:/src/" cdrx/pyinstaller-windows ${PYINSTALLER_CMD_SHORT}

