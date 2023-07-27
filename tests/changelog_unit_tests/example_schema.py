from collections import defaultdict

import graphene
from graphene import Boolean, DateTime, Int, List

from sample_app.models import Author, Book
from versionator.changelog.arbitrary_version_pair_fetcher import ArbitraryVersionPairFetcher
from versionator.changelog.consecutive_versions_fetcher import (
    ConsecutiveVersionsFetcher,
    SingleRecordConsecutiveVersionsFetcher,
)
from versionator.changelog.changelog_graphql.types import (
    ChangelogEntry,
    ChangelogPage,
    VersionComparisonEntry,
)
from versionator.changelog.changelog_graphql.util import (
    convert_enum_list_to_dict,
    create_model_enum_type,
    create_model_field_enum_type,
    create_standard_changelog_graphql_mixin,
)
from versionator.changelog.graphql.internal_query_executor_base import InternalQueryExecutorBase

diffable_models = [
    Author,
    Book,
]
RootQuery = create_standard_changelog_graphql_mixin(diffable_models=diffable_models)

schema = graphene.Schema(query=RootQuery, auto_camelcase=False)


class QueryExecutor(InternalQueryExecutorBase):
    schema = schema
