from django.contrib.auth import get_user_model

import graphene
from data_fetcher import PrimaryKeyFetcherFactory

from versionator.changelog.graphql.utils import (
    NonSerializable,
    non_serializable_field,
)


class Version(graphene.ObjectType):
    edited_by = NonSerializable()
    instance = NonSerializable()

    @staticmethod
    @non_serializable_field
    def resolve_edited_by(parent, info):
        try:
            user_id = parent["instance"].edited_by_id
        except AttributeError:
            user_id = None

        if user_id is None:
            return None

        UserModel = get_user_model()
        fetcher = PrimaryKeyFetcherFactory.get_model_by_id_fetcher(
            UserModel
        ).get_instance()
        return fetcher.get(user_id)

    @staticmethod
    @non_serializable_field
    def resolve_instance(parent, _info):
        return parent["instance"]
