# Day 8: Odd and Even

Write a function called odd_even that has one parameter and takes a list of numbers as an argument. 

The function returns the difference between the largest even number in the list and the smallest odd number in the list. 

For example, if you pass [1,2,4,6] as an argument the function should return 6 -1= 5.

## Conda environment from scratch

### Create conda environment

``` bash
conda create --name 50dop-day08 python=3.10 
conda activate 50dop-day08
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
pytest day08/tests/odd_and_even_test.py
```

![Module test](image-day08-test-module.png "Module test")
