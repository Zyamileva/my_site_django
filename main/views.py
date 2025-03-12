import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View


def home(request: HttpRequest) -> HttpResponse:
    """Render the home page.

    This view renders the main home page of the website,
    providing a basic welcome or introduction.

    Args:
        request: The incoming HTTP request.

    Returns:
        The rendered HTTP response.
    """
    return render(request, "main/home.html", {"title": "Про нас"})


def about(request: HttpRequest) -> HttpResponse:
    """Render the about page.

    This view renders the about page of the website,
    providing information about the company or organization.

    Args:
        request: The incoming HTTP request.

    Returns:
        The rendered HTTP response.
    """
    context = {
        "title": "Про нас",
        "description": "Купуйте якісну сантехніку за вигідними цінами! Великий вибір ванн, умивальників, змішувачів та аксесуарів. Доставка по всій Україні. Замовляйте онлайн!",
        "mission": "Ми прагнемо зробити покупку сантехніки простою та приємною, забезпечуючи клієнтів якісними товарами, експертними порадами та відмінним сервісом.",
        "last_updated": datetime.datetime.now(),
    }
    return render(request, "main/about.html", context)


class ContactView(View):
    """Renders the contact page.

    This view handles GET requests to display contact information,
    including address, phone number, and email.

    Args:
        request: The incoming HTTP request.

    Returns:
        The rendered HTTP response.
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        contacts = {
            "title": "Контакти",
            "address": "м. Київ, вул. Прикладна, 1",
            "phone": "+380 44 123 4567",
            "email": "info@example.com",
            "has_contacts": True,
        }
        return render(request, "main/contact.html", contacts)


class ServiceView(View):
    """Renders the services page.

    This view handles GET requests to display a list of services
    offered by the company or organization.

    Args:
        request: The incoming HTTP request.

    Returns:
        The rendered HTTP response.
    """

    def get(self, request: HttpRequest) -> HttpResponse:
        services = [
            {"name": "Продаж сантехніки", "description": "..."},
            {"name": "Встановлення та налаштування", "description": "..."},
            {"name": "Консультації та підтримка:", "description": "..."},
            {"name": "Гарантії та сервісне обслуговування", "description": "..."},
            {"name": "Доставка та повернення", "description": "..."},
        ]
        return render(
            request,
            "main/services.html",
            {"title": "Послуги", "services": services, "total_services": len(services)},
        )
