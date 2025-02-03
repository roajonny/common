# File :            init_venv.sh
# Title :           init_venv
# 
# Author(s) :       Jonathan Roa
# 
# Description :     Generates the python virtual environment
#                   for installing all sphinx-related package
#                   dependencies
# 
# Revisions 
# 
# Date        Name            REV#        Description 
# ----------  --------------- ----------- --------------------
# (02/02/25)  Jonathan Roa    1.0         Initial Revision

# Generate a directory for the virtual environment
rm -rf .venv/
mkdir .venv/
cd .venv/

# Generate the Python virtual environment locally
python3 -m venv ./

# Activate the virtual environment
source ./bin/activate

# PyPi package installations
pip install sphinx

# If there is a requirements.txt file to install
# all required packages w/ specific versions
# pip install -r /path/to/requirements.txt

# List the current installations
# pip list
