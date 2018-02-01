#!/usr/bin/env bash
set -e 

. ~/.virtualenvs/python3/bin/activate

PYTHONPATH=. python -m pystache.commands.test
