# Project Overview

This project uses Django and Django REST Framework (DRF) to handle CRUD operations for different models. It integrates MongoDB as the backend database using Djongo and provides interactive API documentation using drf-yasg.

## Dependencies

- Django
- Django REST Framework (DRF)
- Djongo: Allows the use of MongoDB as the backend for the Django project.
- drf-yasg: Used for generating interactive API documentation.

## Installation

```sh
pip install django djangorestframework djongo drf-yasg
pip install drf-yasg
pip install pymongo==3.12.3
```

## Collections
### Control

- `name`: Unique identifier for the control.
- `description`: Optional description of the control.
- `status`: Optional status of the control.
- `controlset_ref`: Reference to related control sets.

### ControlSet

- `slug`: Unique identifier for the control set.
- `name`: Unique name for the control set.
- `hierarchy_depth`: Optional depth of the hierarchy.

### ControlHierarchy

- `slug`: Unique identifier for the control hierarchy.
- `controlset_ref`: Reference to related control sets.
- `parents`: List of parent controls.
- `children`: List of child controls.


### Migrations
- Run the following commands to create and apply migrations:

```sh
python manage.py makemigrations controlsApp 
python manage.py migrate controlsApp 
```

## API Documentation

- API documentation is available via Swagger and ReDoc
- To access the API documentation, run the server and navigate to the respective endpoints.



