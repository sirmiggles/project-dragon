# Project **DRAGON**

**D**atabase **R**elating to **A**dministration of **G**ames **On** the **N**et

## License

Use of this program and repository falls under the [**GNU General Public License v3.0**](https://github.com/sirmiggles/project-dragon/blob/master/LICENSE)

## Directory Structure

## Install Instructions

1. clone this repository with `git clone`
2. from the root directory run the following commands

``` bash
    make environment
    make migrate
```

## Running the Django Instance

Once it is installed run the command

``` bash
    make execute
```

## The code structure

The website was written using Django, a high-level Python web framework. Thus, the code structure follows the general
structure of a Django project. The code is partitioned into 3 major sections, called 'apps'. Each app covers different
functionality and modularizes different aspects of the backend of the website. These are:
``` 1. dragon: This app provides the 'homepage' and several other pages such as 'FAQ' or 'Committee'. Furthermore,
the base CSS styling for the entire website is defined here, including the background colour, navbar design and font
of the navbar.
    2. library
    3. members
```



