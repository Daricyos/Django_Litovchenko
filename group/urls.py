from django.urls import path

from group.views import (
    CreateGroupsView,
    GenerateStudentView,
    GroupsListView,
)

urlpatterns = [
    path('group_db/<int:group_number>', GenerateStudentView.as_view(), name='group-db'),
    path('create_groups', CreateGroupsView.as_view(), name='create-groups'),
    path('list-group/', GroupsListView.as_view(), name='list-group'),
]
