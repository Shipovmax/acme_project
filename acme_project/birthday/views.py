from django.http import HttpRequest, HttpResponse
from django.shortcuts import render


def birthday(request: HttpRequest) -> HttpResponse:
    """Render the birthday form page stub."""
    context: dict[str, object] = {}
    return render(request, "birthday/birthday.html", context=context)
