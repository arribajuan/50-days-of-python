# Day 7: A String Range

Write a function called string_range that takes a single number and returns a string of its range.

The string characters should be separated by dots(.)

For example, if you pass 6 as an argument, your function should return ‘0.1.2.3.4.5’.

## Conda environment from scratch

### Create conda environment

``` bash
conda create --name 50dop-day07 python=3.10 
conda activate 50dop-day07
```

### Install libraries

``` bash
conda install -c anaconda pytest
```

# Conda environment import / export

### Save environment to a file

``` bash
conda list --explicit > environment.txt
```

### Create environment from a file

``` bash
conda env create --file environment.txt
```

# Run tests

From the root of the codebase

## Test string range functionality

``` bash
pytest day07/tests/string_range_test.py
```

![Module test](image-day07-test-module.png "Module test")
