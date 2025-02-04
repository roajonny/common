# File :            init_venv.sh
# Title :           init_venv
# 
# Author(s) :       Jonathan Roa
# 
# Description :     Generates the python virtual environment
#                   for working w/ Sphinx
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

# PyPi package installations
# pip install sphinx
# pip install sphinx-rtd-theme
# pip install furo

# If there is a requirements.txt file to install
# all required packages w/ specific versions
pip install -r ./requirements.txt

# List the current installations
pip list
