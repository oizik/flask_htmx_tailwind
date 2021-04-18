# Flask + HTMX + Tailwind + Poetry

Based on the [Rapid Prototyping with Flask, htmx, and Tailwind CSS by Amal Shaji](https://testdriven.io/blog/flask-htmx-tailwind/) and this [flask-htmx-tailwind repository](https://github.com/testdrivenio/flask-htmx-tailwind)

With a few small changes:

- [poetry](https://python-poetry.org/) for dependency management. Also using a `src` folder based structure
- [Flask Application Factory](https://python-poetry.org/) and [Flask Blueprint](https://flask.palletsprojects.com/en/1.1.x/blueprints/)

Also has a `launch.json` for VSCode Debugging and some minor changes in `postcss.config.js` to use `FLASK_ENV` to determine if [postcss-purgecss](https://github.com/FullHuman/postcss-purgecss) should be applied in `production`.

## Want to use this project?

1. Fork/Clone

1. Install [poetry](https://python-poetry.org/docs/)

1. Install dependencies

   ```sh
   poetry install
   ```

1. Install the Node dependencies:

   ```sh
   npm install
   # you may need to install PostCSS globally as well
   # npm install --global postcss postcss-cli
   ```

1. Run the app:

   ```sh
   poetry shell
   poetry run flask run
   ```

1. Test at [http://localhost:5000/](http://localhost:5000/)
