import json
from django.db import models

class Control(models.Model):
    name = models.TextField(primary_key=True, unique=True)
    description = models.TextField(null=True, blank=True)
    status = models.TextField(null=True, blank=True)
    controlset_ref = models.JSONField(default=list)

class ControlSet(models.Model):
    slug = models.TextField(primary_key=True)
    name = models.TextField(unique=True)
    hierarchy_depth = models.IntegerField(null=True, blank=True)

class arrField(models.TextField):
    def from_db_value(self, value, expression, connection):
        if value is None:
            return []
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return []

    def to_python(self, value):
        if isinstance(value, list):
            return value
        if value is None:
            return []
        try:
            return json.loads(value)
        except json.JSONDecodeError:
            return []

    def get_prep_value(self, value):
        if value is None:
            return []
        return json.dumps(value)


class ControlHierarchy(models.Model):
    slug = models.TextField(primary_key=True)
    controlset_ref = models.JSONField(default=list)
    parents = arrField(default=[])
    children = arrField(default=[])
