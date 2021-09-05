from django.shortcuts import render


def upload_file_view(request):
    context = {}
    return render(request, 'csvs/upload.html', context)
