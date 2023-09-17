from django.shortcuts import render


# Create your views here.
def nashe_albums(request):
    return render(request, "nashe/explore_tinashe.html")
