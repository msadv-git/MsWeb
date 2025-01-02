from django.shortcuts import render, redirect
import json
from django.http import JsonResponse
from django.core.mail import send_mail
from django.conf import settings


def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def services(request):
    return render(request, 'services.html')
def qna(request):
    return render(request, 'qna.html')


def lead_form_view(request):
    if request.method == 'POST':
        try:
            # Log the request body for debugging purposes
            print("Request body:", request.body)  # This will print the body in the console

            # Get the data from the AJAX request
            data = json.loads(request.body)

            # Check if required fields are present
            name = data.get('name')
            phone = data.get('phone')

            if not name or not phone:
                return JsonResponse({'error': 'Name and Phone are required'}, status=400)

            # Send the email
            subject = f"New Lead from {name}"
            email_message = f"Name: {name}\nPhone: {phone}"

            send_mail(
                subject,
                email_message,
                settings.DEFAULT_FROM_EMAIL,
                ['mayasimonadv@gmail.com'],
            )

            # Return a JSON response to the frontend
            return JsonResponse({'message': 'פנייתכם התקבלה. משרדינו ייצור עמכם קשר בהקדם.'}, status=200)

        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON format'}, status=400)

    return JsonResponse({'errors': 'Invalid request method.'}, status=400)
