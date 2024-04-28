from django.db import models

class ChangelogConfigField:


def get_field_config_class(field):
    if hasattr(field,'changelog_field_config'):
        return field.changelog_field_config
    
    if isinstance(field, models.ManyToManyField):
        return ManyToManyFieldConfig

    if isinstance(field, (models.ForeignKey, models.OneToOneField)):
        return ForeignKeyFieldConfig
    
    return ScalarFieldConfig


class ScalarFieldConfig:




# diff classes 
    