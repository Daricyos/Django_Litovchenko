from django.urls import path

from group.views import (
    create_groups,
    group_db,
    list_group,
)

urlpatterns = [
    path('group_db/', group_db, name='group-db'),
    path('list_group/', list_group, name='list-groups'),
    path('create_groups', create_groups, name='create-groups'),
]
