# Day 9: Hide my Password

Write a function called hide_password that takes no parameters.

The function takes an input( a password) from a user and returns a
hidden password. 

For example, if the user enters ‘hello’ as a password the function should return ‘****’ as a password and tell the user that the password is 4 characters long.

## Extra Challenge: Strings With a Thousand Separator

Your new company has a list of figures saved in a list. The issue is that these numbers have no separator. 

The numbers are saved in the following format:

```python
[1000000, 2356989, 2354672, 9878098]
```

You have been asked to write a code that will convert each of the numbers in the list into a string. 

Your code should then add a comma on each number as a thousand separator for readability.

When you run your code on the above list, your output should be :

```python
['1,000,000', '2,356,989', '2,354,672', '9,878,098']
```

Write a function called convert_numbers that will take one argument, a list of numbers above.

## Conda environment from scratch

### Create conda environment

``` bash
conda create --name 50dop-day10 python=3.10 
conda activate 50dop-day10
```

### Install libraries

``` bash
conda install -c anaconda pytest
conda install -c conda-forge typer
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

## Test hide my password functionality

``` bash
pytest day10/tests/hide_my_password_test.py
```

![Module test](image-day10-test-module.png "Module test")

## Test CLI app

``` bash
pytest day10/tests/main_test.py
```

![CLI test](image-day10-test-cli.png "CLI test")

# Run cli app

From the root of the codebase

``` bash
python -m day10.app.main
```

![CLI app run](image-day10-run.png "CLI app run")
