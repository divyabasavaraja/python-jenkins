#!/usr/bin/env bash
set -e 

. ~/.virtualenvs/python3/bin/activate

PYTHONPATH=. python -m python-jenkins.commands.test
