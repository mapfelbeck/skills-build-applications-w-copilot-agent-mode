from django.http import JsonResponse

def api_root(request):
    return JsonResponse({"message": "Welcome to the Octofit API!", "url": "https://scaling-giggle-qv6grx7p76p39jgp-8000.app.github.dev"})