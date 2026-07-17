from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def homepage(request: HttpRequest) -> HttpResponse:
    """Render the static homepage."""
    return render(request, 'pages/index.html')

