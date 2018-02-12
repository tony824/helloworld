from django.http import HttpResponse

from model.models import django

def testdb(request):
    test1 = django(name='runoob')
    test1.save()
    return HttpResponse("<p>Insert successfully</p>")
