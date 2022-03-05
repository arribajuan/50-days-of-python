# Day 3 - Register Check

Write a function called register_check that checks how many students are in school.

The function takes a dictionary as a parameter. If the student is in school, the dictionary says ‘yes’. If the student
is not in school, the dictionary says ‘no’.

Your function should return the number of students in school.

Use the dictionary below. Your function should return 3.

``` python
register = {'Michael':'yes','John': 'no',
           'Peter':'yes', 'Mary': 'yes'}
```

## Conda environment from scratch

### Create conda environment

``` bash
conda create --name 50dop-day03 python=3.10 
conda activate 50dop-day03
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

``` bash
pytest register_check_test.py
```


