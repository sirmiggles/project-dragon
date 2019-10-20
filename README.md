# Project **DRAGON**

**D**atabase **R**elating to **A**dministration of **G**ames **On** the **N**et

## License

Use of this program and repository falls under the [**GNU General Public License v3.0**](https://github.com/sirmiggles/project-dragon/blob/master/LICENSE)

## Install Instructions

1. Clone this repository with `git clone`
2. From the root directory, run the following commands:

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
functionality and modularizes different aspects of the backend of the website.
These are:
```
    1. dragon
    2. library
    3. members
```

## Dragon
This app provides the 'homepage' and several other pages such as 'FAQ' or 'Committee'. Furthermore,
the base CSS styling for the entire website is defined here, including the background colour, navbar design and font
of the navbar. We will now go into more detail:

The 'static' folder contains a subfolder  which is also named 'dragon'. In here we have the following files:
```
    1. 'base_sytle.css': This file defines the base styling properties such as background colour, font, layout and design
    of the navbar and much more. Any changes to the overall look of the website should be made here and will update the
    look of all dependent pages.
    2. 'item_detail.css': This file defines the the layout properties of the item detail pages (i.e. the detail page
    for every item in the library which are defined in the 'library' app), both for desktop and mobile users
    3. 'lib_style.css': This file defines the basic layout of the library pages which contain a table of any type
    of items. Changes specific to the look of the item, book, game or card game tables should be made here.

```

The 'templates' folder contains another subfolder, which is also called 'dragon'. In here we have all HTML templates
that are rendered when accessing the pages wit the same name/URL. All files in here are simple HTML files which
currently have a static render.





