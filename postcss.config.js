// postcss.config.js

const path = require("path");

module.exports = (ctx) => ({
  plugins: [
    require("tailwindcss")(path.resolve(__dirname, "tailwind.config.js")),
    require("autoprefixer"),
    //changed to use FlASK_ENV
    process.env.FLASK_ENV === "production" &&
      require("@fullhuman/postcss-purgecss")({
        // a note on paths: https://jakubsvehla.me/posts/setting-up-tailwind-css-with-flask/
        content: [path.resolve(__dirname, "src/flask_htmx_tailwind/**/*.html")],
        defaultExtractor: (content) => content.match(/[A-Za-z0-9-_:/]+/g) || [],
      }),
  ],
});
