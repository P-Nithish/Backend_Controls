from rest_framework import serializers
from .models import Control, ControlSet, ControlHierarchy

class ControlSerializer(serializers.ModelSerializer):
    class Meta:
        model = Control
        fields = ['name', 'description', 'status', 'controlset_ref']

    def validate_name(self, value):
        try:
            if self.instance is None: 
                if Control.objects.filter(name=value).exists():
                    raise serializers.ValidationError("A Control with this name already exists.")
            else:  
                if Control.objects.filter(name=value).exclude(pk=self.instance.pk).exists():
                    raise serializers.ValidationError("A Control with this name already exists.")
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return value

class ControlSetSerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlSet
        fields = ['slug', 'name', 'hierarchy_depth']

    def validate_slug(self, value):
        try:
            if self.instance is None: 
                if ControlSet.objects.filter(slug=value).exists():
                    raise serializers.ValidationError("A ControlSet with this slug already exists.")
            else:  
                if ControlSet.objects.filter(slug=value).exclude(pk=self.instance.pk).exists():
                    raise serializers.ValidationError("A ControlSet with this slug already exists.")
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return value

    def validate_name(self, value):
        try:
            if self.instance is None: 
                if ControlSet.objects.filter(name=value).exists():
                    raise serializers.ValidationError("A ControlSet with this name already exists.")
            else: 
                if ControlSet.objects.filter(name=value).exclude(pk=self.instance.pk).exists():
                    raise serializers.ValidationError("A ControlSet with this name already exists.")
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return value

class ControlHierarchySerializer(serializers.ModelSerializer):
    class Meta:
        model = ControlHierarchy
        fields = ['slug', 'controlset_ref', 'parents', 'children']

    def validate_slug(self, value):
        try:
            if self.instance is None:  
                if ControlHierarchy.objects.filter(slug=value).exists():
                    raise serializers.ValidationError("A ControlHierarchy with this slug already exists.")
            else:  
                if ControlHierarchy.objects.filter(slug=value).exclude(pk=self.instance.pk).exists():
                    raise serializers.ValidationError("A ControlHierarchy with this slug already exists.")
        except Exception as e:
            raise serializers.ValidationError(str(e))
        return value