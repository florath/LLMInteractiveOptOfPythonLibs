# Source Code for the paper "Human-Language Model Collaboration for Source Code Optimization: Some Practical Spotlights"

This repository contains the source code for the paper "Human-Language
Model Collaboration for Source Code Optimization: Some Practical
Spotlights".

## Structure

### Directory "src"

The `src` directory contains the source code which was used to measure
the results in chapter "4. Measurements".  It also contains the source
code for validation.

### Directory "lib"

This directory contains commonly used utilities. You might want to
include this into your PYTHONPATH, like

    export PYTHONPATH=${PWD}/lib

### Directory "Generalization"

This directory contains the source code for chapter "5. Generalization
of Findings".  Each subdirectory contains the sources of a sub-chapter.

### Directory "MethodTransfer"

This directory contains the source code for chapter "6. Method
Transferability".

# Setup

You might want to create a python virtualenv. Use the following
command to install the needed requirements.

    pip install -r requirements.txt

# Propose

This source code is used for research only.  The propose is to
elaborate on the findings described in the paper.  It is not
production code!

# License

See the LICENSE file for the license of the files in this repository.

Copyright 2023 by Andreas.Florath@telekom.de
