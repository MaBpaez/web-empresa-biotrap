from django.shortcuts import render


def flavors(request):
    return render(request, 'flavor/flavors.html')
