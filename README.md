# Nightmare Forms

The goal of this project is to be a minimal example of the best way to implement a complicated form.

The example in this repo will implement an order form for a coffee shop. The order form will demonstrate these aspects of complicated forms:
* The ability to add, remove, and modify existing items. (dynamic form)
* Some fields will toggle other fields. (conditional/dependent fields)
* Some fields will populate other fields with default values.
* Nested fields with paired inputs.
* Disabled checkboxes
* Detect and log changes between previous edits
* Both client-side & server-side validation errors appear next to the appropriate fields.

This repo uses Django for the back-end.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)

## Installation

1. Clone this repository and navigate to the directory.
1. Create virtualenv: `virtualenv .venv`
1. Activate the virtualenv: `source .venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Initialize database schema: `python manage.py migrate`
1. Load initial data: `python manage.py loaddata backend/api/fixtures/*`
1. Create admin user: `python manage.py createsuperuser --email admin@example.com --username admin`
1. `npm install`

## Usage

In the first terminal:
1. `python manage.py runserver`

In the second terminal:
1. Also start front-end: `npm run serve`

In your browser:
1. Visit: http://127.0.0.1:8000/

## Ways To Implement The Complicated Form

### Method 1: Server-Side Form

#### Main Components
* /
    * GET - loads empty order form
    * POST - validates data and saves the changes to the order
* /orderitem/
    * GET w/ parameters - allows reloading an item's form with the available choices and defaults based on the current selections
* /`<id>`/
    * GET - loads order form with existing items
* Django Forms & Formsets - handle rendering the form and processing submission

#### Pros
* It's very easy to get validation errors to appear next to fields.
* Validation code is easily shared between front-end and back-end. (less duplication)
* No extra code for serializing and deserializing. (HTML forms handle this)

#### Cons
* Large portions of the form must be reloaded when changes to some fields occur. This requires a network request and can provide a bad user experience if the response isn't quick.
  * When certain fields are changed, you need javascript to send the item's current values to an endpoint that sends back a replacement for the item's form with the new choices and defaults.
* Requires supporting multiple ways to load the form.
  * On initial GET, the forms must set the initial field values to what's currently stored in the database for existing items.
  * When changing fields, the forms must allow loading a single item (that may not exist yet) with only some of the values filled in, so it can load the item form with the correct choices and defaults based on your current selection. You may need to take some things stored on the existing item into account (your logic may rely on a previously selected value).
  * And the same forms must allow a POST request to modify existing items and/or create new ones.
  * Splitting up this functionality into separate forms may result in a lot of duplicated code.
* The server-side templates need to duplicate all the logic for dynamic fields that you implemented in javascript, because the back-end may need to re-render the form with your current selection when there's invalid submit or when a choice is changed.
* Requires custom django template tags for displaying ChoiceField choices: https://github.com/pawl/django_choicefield_display_example
* Dealing with paired inputs nested in items is difficult.
  * Nested dynamic fields + Django's built-in formsets is really complicated.
* You have to create hidden fields for each possible value and use javascript to show/hide + disable the fields. Or you will need to render the field with javascript and duplicate that logic on the server-side.
* Issues with separation of concerns (display of the form is tightly coupled). This implemention uses the server side form logic to render the form, so having a slightly different implementation of the form in another place (like a mobile app that shows the form in a different layout) is going to require reverse engineering some of the server side logic.
* Disabled checkboxes require some hacks to implement. HTML forms do not submit both disabled checkboxes and unchecked checkboxes.

------------


### Method 2: Client-side Form w/ jQuery

#### Main Components
* /
    * GET - loads base template
* /choices/
    * GET - returns available choices and defaults for item fields
* /order/ -
    * GET  - returns the current state of the order
    * POST - validates data and saves the changes
* Django Forms or DRF Serializers - handle back-end validation

#### Pros
* No need to refresh on each field change
  * Also no need to share state with the back-end on each field change. All the possible choices are loaded just once when the form loads.
* The logic for displaying the form isn't mostly packed into the form.
* Better separation of concerns. You could use the APIs to implement this form in a separate mobile app.
* IE11 compatibility without a complicated build pipeline.

#### Cons
* The jQuery code for keeping the DOM/HTML in sync with the javascript objects quickly becomes very complicated. It also makes refactoring and testing difficult.
* Validation code is duplicated between back-end and front-end.
  * The front-end also needs code to map server side errors to client errors.
    * Potential solutions:
      * Ember Data's JSON-API adapter seems to have a way to do this.
      * https://github.com/rjsf-team/react-jsonschema-form

------------

### Method 3: Client-side Form w/ Vue.js (used by this repo)

#### Main Components
* Mostly same as "Client-side forms w/ jquery" except with Vue.js on the front-end.

#### Pros
* More maintainable than jQuery, because it automatically keeps the DOM/HTML in sync with your javascript objects. Two-way binding makes things easier to refactor. Also encourages you to make things in a more testable way by making you break your code into components and not use global variables. Vue-cli also helps set up linting, ES6 transpiling, webpack, and live reloading for a better development experience.
  * See: https://dev.to/tsanak/make-your-life-easier-with-vuejs-4mj5

#### Cons
* Mostly the same as "Client-side forms w/ jquery" Cons, except without the issues with difficult to maintain front-end code.
* More setup required than just putting a script tag on a page (assuming you want to use webpack and get the code quality assurance benefits of a build pipeline).

------------

## Conclusion

I think server-side forms make simple forms simpler and complex dynamic forms even more complex. So, this repo will use the "Client-side Form w/ Vue.js" method.

## Credit
* Starter template used: https://github.com/gtalarico/django-vue-template
