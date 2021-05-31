#! /usr/bin/env bash

export -n SESSION_MANAGER
mkdir -p ${XDG_RUNTIME_DIR}

python3 ${SNAP}/main.py
