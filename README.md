# Nightmare Forms

The goal of this project is to be an example of the best way to implement a complicated form.

The example in this repo will implement a form for customizing drinks. The form will demonstrate these aspects of complicated forms:
* The ability to add, remove, and modify existing items. (dynamic form)
* Some fields will toggle other fields. (conditional/dependent fields)
* Some fields will populate other fields with default values.
* Nested fields with paired inputs.
* Disabled checkboxes
* Detect and log changes between edits
* Both client-side & server-side validation errors appear next to the appropriate fields.

This repo uses Django for the back-end.

## Table of Contents

1. [Installation](#installation)
1. [Usage](#usage)
1. [Ways To Implement The Complicated Form](#ways-to-implement-the-complicated-form)
    1. [Method 1: Mostly Server-side Form w/jQuery](#method-1-mostly-server-side-form-w-jquery)
    1. [Method 2: Client-side Form w/ jQuery](#method-2-client-side-form-w-jquery)
    1. [Method 3: Client-side Form w/ Vue.js](#method-3-client-side-form-w-vuejs-used-by-this-repo)
1. [Conclusion](#conclusion)
1. [Credit](#credit)

## Installation

1. Clone this repository and navigate to the directory.
1. Create virtualenv: `virtualenv .venv`
1. Activate the virtualenv: `source .venv/bin/activate`
1. Install dependencies: `pip install -r requirements.txt`
1. Initialize database schema: `python manage.py migrate`
1. Load initial data: `python manage.py loaddata backend/api/fixtures/*`
1. Create admin user: `python manage.py createsuperuser --email admin@example.com --username admin`
1. Install front-end dependencies: `npm install`

## Usage

Start the back-end in your first terminal:
`python manage.py runserver`

Start the front-end in your the second terminal:
`npm run serve`

In your browser visit: http://127.0.0.1:8000/

## Ways To Implement The Complicated Form

### Method 1: Mostly Server-side Form w/ jQuery

#### Main Components
* /
    * GET - loads empty order form
    * POST - validates data and saves the changes to the order
* /`<id>`/
    * GET - loads order form with existing items
* /orderitem/
    * GET w/ parameters - allows reloading an item's form with the available choices and defaults based on the current selections
* Django Forms & Formsets - handle rendering the form and processing submission
* django-dynamic-formset jQuery library: https://github.com/elo80ka/django-dynamic-formset

#### Pros
* It's very easy to get validation errors to appear next to fields.
* Validation code is easily shared between front-end and back-end. (less duplication)
* No extra code for serializing and deserializing. (HTML forms handle this)

#### Cons
* The server-side templates need to duplicate all the logic for dynamic fields that you implemented in javascript, because the back-end may need to re-render the form with your current selection when there's invalid submit or when a choice is changed.
* Large portions of the form must be reloaded when changes to some fields occur. This requires a network request and can provide a bad user experience if the response isn't quick.
  * When certain fields are changed, you need javascript to send the item's current values to an endpoint that sends back a replacement for the item's form with the new choices and defaults.
* Requires supporting multiple ways to load the form.
  * On initial GET, the forms must set the initial field values to what's currently stored in the database for existing items. This same form must also allow loading an empty form when creating new orders.
  * When changing fields, the forms must allow loading a single item (that may not exist yet) with only some of the values filled in. This allows loading the item form with the new choices and defaults based on your current selection. You may need to take some things stored on the existing item into account (for example: you may clear out some other fields if a certain field is changed to a different value).
  * On POST, the same forms must allow modifying existing items and/or creating new ones.
  * All this logic mainly ends up lumped into two Form objects (one for the order-level and another for the item-level). Splitting up this functionality into different Form objects on the server side may result in a lot of duplicated code for initializing the form.
* Requires custom django template tags for displaying ChoiceField choices: https://github.com/pawl/django_choicefield_display_example
* Dealing with paired inputs nested in items is difficult.
  * Nested dynamic fields + Django's built-in formsets is really complicated.
* You have to create hidden disabled inputs for all possible input that are not currently enabled and use javascript to show/hide + disable those inputs as appropriate. Or you will need to render the field with javascript and duplicate that logic on the server-side. Or you will need to refresh the form to get the server-side to re-render the form.
* Issues with separation of concerns (display of the form is tightly coupled). This implemention uses the server side form logic to render the form, so having a slightly different implementation of the form in another place (like a mobile app that shows the form in a different layout) is going to require reverse engineering some of the server side logic.
* Disabled checkboxes require some hacks to implement. HTML forms do not submit data for both disabled checkboxes and unchecked checkboxes.

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
* Hidden HTML template for the jQuery code to clone/show/hide
* jQuery on the client-side for rendering the form
* Django Forms or DRF Serializers - handle back-end validation

#### Pros
* The current state of the form is stored only the client-side until the form is saved, so no need to refresh on each field change.
  * No need to share the current state back and forth between back-end and front-end when some fields change. All the possible choices are loaded when the form initially loads.
  * Better user experience if the form would be reloading often.
  * I think this makes things easier to understand. Passing around objects only when the form is loaded or saved seems easier to think about.
* You don't need logic for rendering the form on both the client-side and server-side. You just need the code on the client-side for rendering the form and you use the data layer (API endpoint) to get the current state of items and to sync things up with the database (or send back validation errors to display next to fields).
  * No more server-side hacks to render the form with all possible inputs as hidden disabled to be enabled/shown by client-side javascript.
* Better separation of concerns. You could use the APIs to implement this form in a separate mobile app.
* IE11 compatibility without a complicated build pipeline.
* Nested fields (especially nested pairs of fields) are better represented as JSON.

#### Cons
* The jQuery code for cloning + filling in new form components and keeping the DOM/HTML in sync with the javascript objects quickly becomes very complicated with lots of duplicated selectors and scattered helper functions and change events. This can make refactoring difficult. This assumes you're not doing a fancy component structure with ES6.
  * See the jQuery example here: https://dev.to/tsanak/make-your-life-easier-with-vuejs-4mj5
* Validation code is duplicated between back-end and front-end.
  * For example, you need to define the field type for back-end validation and you need to separately define the field on the front-end. This can lead to a mismatch without proper integration testing.
  * The front-end also needs code to map server side errors to client errors.
    * Potential solutions:
      * Ember Data's JSON-API adapter seems to have a way to do this.
      * https://github.com/rjsf-team/react-jsonschema-form
* Requires building data-layer (API endpoints). Although, API endpoints may have some long-term value if you intend to build a mobile app or expose a public API to customers.

------------

### Method 3: Client-side Form w/ Vue.js (used by this repo)

#### Main Components
* Mostly same as "Client-side forms w/ jQuery" except with Vue.js on the front-end.

#### Pros
* More maintainable than jQuery, because it automatically keeps the DOM/HTML in sync with your javascript objects. Two-way binding/reactive programming and being able to reference js objects from templates makes things easier to refactor and doesn't require nearly as much selector and DOM/HTML manipulation code. Vue's component structure also encourages you to make things in a more testable way by making you break your code into components and not use global variables. Vue-cli also helps set up linting, ES6 transpiling, webpack, and live reloading for a better development experience.
  * See: https://dev.to/tsanak/make-your-life-easier-with-vuejs-4mj5

#### Cons
* Mostly the same as "Client-side forms w/ jQuery" Cons, except without the issues with difficult to maintain front-end code.
* More setup required than just putting a script tag on a page (assuming you want to use webpack and get the code quality assurance benefits of a build pipeline).

------------

## Conclusion

I think server-side forms make simple forms simpler and complex dynamic forms even more complex. Vue.js also offers more maintainable client-side code with two-way binding and better code organization. So, this repo will use the "Client-side Form w/ Vue.js" method.

## Credit
* Starter template used: https://github.com/gtalarico/django-vue-template
