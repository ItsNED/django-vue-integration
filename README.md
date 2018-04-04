# django-vue-integration

# Process
1. make Normal django project
    - Install Django.
    - django-admin startproject project_name.
    - django-admin startapp app_name.
    - add app in INSTALLED_APPS in settings.py.
    - create templates, static folder in root.
    - copy bootstrap folder into static folder.
    - create layout.html in templates folder and change path for bootstrap to local from cdn.
    - create model, migrate and connect to view.

2. prepare for vue
    - npm init (entry point : App.js)
    - modify package.json
    - prepare to use Vue.js
    - create webpack.config.js
    - npm install
    - create .babelrc
    - made api in django
    - ./node_modules/.bin/webpack to create bundle.js
    - link bundle.js to layout.html