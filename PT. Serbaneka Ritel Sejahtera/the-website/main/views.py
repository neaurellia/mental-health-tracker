from django.shortcuts import render

def show_main(request):
    context = {
        'Location' : '2306123456',
        'Products': 'Pak Bepe',
        'Job Opportunities': 'PBP E'
    }

    return render(request, "main.html", context)