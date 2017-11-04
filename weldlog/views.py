from django.shortcuts import render

from .models import Weld, Welder


# Create your views here.


def homepage(request):
    welds = Weld.objects.all()
    welders = Welder.objects.all()

    return render(request, 'home.html', {'welds': welds,
                                         'welders': welders,
                                         })
