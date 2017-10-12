from django.shortcuts import redirect


def handle_page_not_found(request):
    return redirect('home')
