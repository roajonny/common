#!/usr/bin/env bash

# File :            init_venv.sh
# Title :           init_venv
# 
# Author(s) :       Jonathan Roa
# 
# Description :     Generates the python virtual environment
#                   for working w/ Sphinx and installs dependencies
#                   for building the documentation
# 
# Revisions 
# 
# Date        Name            REV#        Description 
# ----------  --------------- ----------- --------------------
# (02/02/25)  Jonathan Roa    1.0         Initial Revision

# Generate a directory for the virtual environment
rm -rf .venv/ && python3 -m venv .venv/

# Activate the virtual environment
source ./.venv/bin/activate

# If there is a virtual environment package file to install
# all dependencies w/ specified versions
pip install -r ./pyvenv_packages.txt

# List the current installations
pip list

# Generate the HTML template
# sphinx-build ./docs/source ./docs/build
