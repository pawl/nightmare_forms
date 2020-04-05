# Nightmare Forms

The goal of this project is to be a collection of minimal examples of the various ways to make a complicated form.

The examples in this repo will implement the same order form for a coffee shop. The order form will demonstrate ways to implement these aspects of complicated forms:
* The ability to add, remove, and modify items. (dynamic form)
* Some fields will toggle other fields. (conditional/dependent fields)
* Some fields will populate other fields with default values.
* Nested fields with paired inputs.
* Disabled checkboxes
* Detect changes

All examples must at least have server-side validation and validation errors must appear next to the appropriate fields.

Nice to have:
* IE11 compatibility without a complicated build pipeline. (so it's easy to implement in legacy apps)

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)

## Installation

1. Clone this repository and navigate to the directory.
1. Create virtualenv: `virtualenv .venv`
1. Activate the virtualenv: `source .venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Ensure postgres is running (I use postgres.app on mac)
1. Create the database with psql: `create database nightmare_forms;`
1. Initialize database schema: `python manage.py migrate`
1. Load initial data: `python manage.py loaddata coffee/fixtures/*`
1. Create admin user: `python manage.py createsuperuser --email admin@example.com --username admin`

## Usage

1. `python manage.py runserver`
1. Visit: http://127.0.0.1:8000/

## Example Descriptions

### Method 1: Server-Side Form

<path>

#### Main Components
* /
    * GET - loads empty order form
    * POST - validates data and saves the changes to the order
* /orderitem/
    * GET w/ parameters - allows reloading an item's form with the available choices and defaults based on the current selections
* /<id>/
    * GET - loads order form with existing items
* Django Formsets
* Reloading the form when changes are made
* Disabling fields

#### Pros
* It's very easy to get validation errors to appear next to fields.
* Validation code is easily shared between front-end and back-end. (less duplication)
* No extra code for serializing and deserializing. (HTML forms handle this)

#### Cons
* Large portions of the form must be reloaded when changes to some fields occur.
** You need javascript to send in the item's current values to an endpoint that sends back a new version of the item's form with the new choices and defaults then replaces the existing form.
* Requires supporting multiple ways to load the form.
** Forms must be built to allow loading a single item (that may not exist yet) with only some of the values filled in, so it can load the item form with the correct choices and defaults based on your current selection.
** Forms must also be built to set the initial field values to what's currently stored in the database, so we can detect what changed.
* The page must be reloaded when the form is submitted.
* Dealing with paired inputs nested in items is difficult.
** Nested formsets are really complicated, so you end up creating a field for each possible value.
* Issues with separation of concerns (display of the form is tightly coupled). This implemention uses the server side form logic to render the form, so having a slightly different implementation of the form in another place (like a mobile app that shows the form in a different layout) is going to require reverse engineering some of the server side logic.
* Disabled checkboxes are difficult to implement. HTML forms do not submit disabled checkboxes, so your server side code needs to account for this and apply appropriate defaults.

### Method 2: Client-side Form w/ jquery

#### Main Components
* /
    * GET - loads base template
* /choices/
    * GET - returns available choices and defaults for item fields
* /order/ -
    * GET  -
    * POST - validates data and saves the changes

#### Pros
* No need to refresh on each field change
** Also no need to share state with the back-end on each field change. All the possible choices are loaded just once when the form loads.
* The logic for displaying the form isn't mostly packed into the form.
* Better separation of concerns. You could use the APIs to implement this form in a separate mobile app.

#### Cons
* The jQuery code for keeping the DOM/HTML in sync with the javascript objects quickly becomes very complicated. It also makes refactoring and testing difficult.
* Validation code is duplicated between back-end and front-end.
** The front-end also needs code to map server side errors to client errors.
*** Potential solutions:
**** Ember Data's JSON-API adapter seems to have a way to do this.
**** https://github.com/rjsf-team/react-jsonschema-form

### Method 3: Client-side Form w/ Vue.js:

#### Main Components
* Mostly same as "Client-side forms w/ jquery" except with Vue.js on the front-end.

#### Pros
* More maintainable than jQuery, because it automatically keeps the DOM/HTML in sync with your javascript objects. Two-way binding makes things easier to refactor. Also encourages you to make things in a more testable way by making you break your code into components and not use global variables.
** See: https://dev.to/tsanak/make-your-life-easier-with-vuejs-4mj5

#### Cons
* Mostly the same as "Client-side forms w/ jquery" Cons, except without the issues with difficult to maintain front-end code.

### Conclusion

I think server-side forms make simple forms simpler and complex dynamic forms even more complex.
