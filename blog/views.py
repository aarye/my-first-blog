from django.shortcuts import render

# Create your views here.
def post_list(request):
    # tales request amd returns a function render that will render (put together)
    # our template blog/post_list.html
    return render(request, 'blog/post_list.html', {})
