import requests
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import JobApplication
from .serializers import JobApplicationSerializer
from django.conf import settings
class JobApplicationViewSet(viewsets.ModelViewSet):
    queryset = JobApplication.objects.all()
    serializer_class = JobApplicationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error: {e}")  # Log error
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class PaymentViewSet(viewsets.ViewSet):

    def create(self, request, *args, **kwargs):
        payment_data = request.data
        payment_type = payment_data.get('payment_type')  # 'paypal' or 'credit_card'
        
        if payment_type == 'paypal':
            return self.process_paypal_payment(payment_data)
        else:
            return Response({"error": "Invalid payment type"}, status=status.HTTP_400_BAD_REQUEST)

    def get_paypal_access_token(self):
        url = f"{settings.PAYPAL_API_URL}/v1/oauth2/token"
        auth = (settings.PAYPAL_CLIENT_ID, settings.PAYPAL_SECRET_KEY)
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }
        data = {
            'grant_type': 'client_credentials'
        }

        response = requests.post(url, headers=headers, data=data, auth=auth)
        if response.status_code == 200:
            return response.json().get('access_token')
        else:
            return None

    def process_paypal_payment(self, payment_data):
        access_token = self.get_paypal_access_token()
        if not access_token:
            return Response({"error": "Unable to obtain PayPal access token"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        url = f"{settings.PAYPAL_API_URL}/v1/payments/payment"
        headers = {
            'Content-Type': 'application/json',
            'Authorization': f'Bearer {access_token}',
        }
        payment_payload = {
            "intent": "sale",
            "payer": {
                "payment_method": "paypal"
            },
            "transactions": [{
                "amount": {
                    "total": "50.00",  # Set your actual amount here
                    "currency": "USD"
                },
                "description": "Job Application Payment"
            }],
            "redirect_urls": {
                "return_url": "http://localhost:3000/payment-success",
                "cancel_url": "http://localhost:3000/payment-cancel"
            }
        }

        response = requests.post(url, json=payment_payload, headers=headers)
        if response.status_code == 201:
            return Response(response.json(), status=status.HTTP_201_CREATED)
        else:
            return Response(response.json(), status=status.HTTP_400_BAD_REQUEST)
