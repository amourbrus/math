from django.shortcuts import render

# Create your views here.
# C:\lizude\temp\github\math\math_project\templates\essence\index.html


def get_essential(request):
    # return render(request, 'publisher_list.html', {'publisher_list': publisher})
    return render(request, 'essence\index.html')


def stuff(request):
    return render(request, 'stuff\index.html')
