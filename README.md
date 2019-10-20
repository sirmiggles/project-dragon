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
structure of a Django project. The code is partitioned into 3 major sections, called `apps`. Each app covers different
functionality and modularizes different aspects of the backend of the website.
These are:
```
    1. dragon
    2. library
    3. members
```

### 1. Dragon
This app provides the `homepage` and several other pages such as `FAQ` or `Committee`. Furthermore,
the base CSS styling for the entire website is defined here, including the background colour, navbar design and font
of the navbar. We will now go into more detail:

The `dragon\static` folder contains a subfolder  which is named `dragon\static\dragon`. In here we have the following
files:
```
    1. base_sytle.css: This file defines the base styling properties such as background colour, font, layout and design
    of the navbar and much more. Any changes to the overall look of the website should be made here and will update the
    look of all dependent pages.

    2. item_detail.css: This file defines the the layout properties of the item detail pages (i.e. the detail page
    for every item in the library which are defined in the 'library' app), both for desktop and mobile users.

    3. lib_style.css: This file defines the basic layout of the library pages which contain a table of any type
    of items. Changes specific to the look of the item, book, game or card game tables should be made here.

```

The `dragon\templates` folder contains another subfolder, which is called `dragon\templates\dragon`. In here we have
all HTML templates that are rendered when accessing the pages with the same name/URL. All files in here are simple HTML
files which currently have a static render.

`dragon\settings.py` contains configuration variables for the Django Project and is used to declare apps, the type of
database to be used, as well as various other settings. For more detail, see
https://docs.djangoproject.com/en/2.2/topics/settings/

`dragon\urls.py` contains a list called `urlpatterns`, which routes URLs to views. For any view declared in `views.py`,
an entry must be made in `urlpatterns` in order to access the view, which in turn renders a page or handles a request.
For more information, see
https://docs.djangoproject.com/en/2.2/topics/http/urls/

`dragon\wsgi.py` is the WSGI configuration file for the project. This file should not be of too much concern when making
changes to the code, but for more information, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/

### 2. Library
This app is mainly focused around rendering all pages related to the library and interacting with the item database.
The display of item tables and searching, filtering and ordering of items is implemented here. Futhermore, each item
has their own description page which lists relevant information. All interations with the item database are defined in
this app.

The `library\templates` folder contains another subfolder, `library\templates\library`. In here, we find 7 further
subfolders, named `book`, `cardgame`, `game`, `item`, `series` and `tags`. As their name suggests, each folder
contains html templates which are specific for a given item or object in the database:

```
    1. book, cardgame and game all contain 4 similar (yet slightly different) templates:
        - all.html is the template which renders the table of the given medium type
        - detail.html is the template which renders the specific detail page of a given item
        - create_form.html is the template which displays a form to add an item to the database
        - edit_form.html renders a form to edit the details of a specific item

    2. tag, series and genre all contain create_form.html and edit_form.html, similar to above

    3. item also contains all.html, details.html, but also contains libview_base.html, which defines the
    generic layout and design of all book, game, card game or item tables.
```

Furthermore, `library\templates\library' also contains 3 further templates:

```
    1. base.html: This template is currently empty, but make in future contain a navbar to easily switch between
    tables.

    2. borrow_detail.html: This template is destined to show the details of a certain item borrow.

    3. borrowed.html: This template is currently not in use, but is destined to display a list of all active borrows.

```








