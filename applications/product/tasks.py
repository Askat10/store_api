from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model

User = get_user_model()

@shared_task
def notify_about_new_product():
    emails = User.objects.values_list('email', flat=True)
    message = """ 
    In our site have a new product, Check it out right now :) """
    return send_mail(subject='Hello!', 
              message=message,
              from_email='test@test.com',
              recipient_list=emails,
              fail_silently=False)


