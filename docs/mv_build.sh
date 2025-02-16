#!/usr/bin/env bash

# Convenience script for moving content in the build directory
# to the Github Pages deployment repo when cloned adjacent to this one
#
# E.G.
#   repos
#     |- common
#     |- roajonny.github.io/
#
# Make sure virtual environment is active or make won't work

# Build the docs
make

# Clear up everything in Github Pages repo except .git directory and .nojekyll
cd ../../roajonny.github.io/ 
rm -rf !(.git) 
rm -rf .doctrees/
rm .buildinfo
cd -

# Move the build directory into it
mv ./build/{,.[^.]}* ../../roajonny.github.io/
