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
