from random import randrange

from django.http import HttpResponse

from faker import Faker

from .models import Groups


def group_db(request, group_number=10):
    fake = Faker()
    resul = []
    for i in range(group_number):
        resul.append(Groups(
            group_name=fake.job(),
            group_student=randrange(18, 25)
        ))

    Groups.objects.bulk_create(resul)

    group_get = Groups.objects.filter().order_by('-id')[:group_number]
    output = [f"{groups.id} {groups.group_name} {groups.group_student}; \n" for groups in group_get]
    return HttpResponse(output, content_type="text/plain")
