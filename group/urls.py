from django.urls import path

from group.views import (
    all_groups,
    create_groups,
    group_db,
)

urlpatterns = [
    path('group_db/', group_db, name='group-db'),
    path('create_groups', create_groups, name='create-groups'),
    path('list-group/', all_groups, name='list-group'),
]
