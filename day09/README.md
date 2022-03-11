# Day 9: Biggest Odd Number

Create a function called biggest_odd that takes a string of numbers and returns the biggest odd number in the list. 

For example, if you pass ‘23569’ as an argument, your function should return 9. 

**Use list comprehension.**

## Conda environment from scratch

### Create conda environment

``` bash
conda create --name 50dop-day09 python=3.10 
conda activate 50dop-day09
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
pytest day09/tests/biggest_odd_test.py
```

![Module test](image-day09-test-module.png "Module test")
