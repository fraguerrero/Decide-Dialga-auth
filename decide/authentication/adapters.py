from allauth.socialaccount.adapter import DefaultSocialAccountAdapter
from allauth.account.utils import perform_login
from .models import CustomUser


class CustomSocialAccountAdapter(DefaultSocialAccountAdapter):
    def pre_social_login(self, request, sociallogin):
        social_email = sociallogin.account.extra_data.get('email')

        try:
            customer = CustomUser.objects.get(email=social_email)  # if user exists, connect the account to the existing account and login
            sociallogin.state['process'] = 'connect'
            perform_login(request, customer, 'none')
        except CustomUser.DoesNotExist:
            pass

        try:
            customer = CustomUser.objects.get(email1=social_email)  # if user exists, connect the account to the existing account and login
            # sociallogin.state['process'] = 'connect'
            # perform_login(request, customer, 'none')
            if not sociallogin.is_existing:
                sociallogin.connect(request, customer)
        except CustomUser.DoesNotExist:
            pass

        try:
            customer = CustomUser.objects.get(email2=social_email)  # if user exists, connect the account to the existing account and login
            sociallogin.state['process'] = 'connect'
            perform_login(request, customer, 'none')
        except CustomUser.DoesNotExist:
            pass