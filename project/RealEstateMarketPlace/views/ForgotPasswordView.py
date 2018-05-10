from ..forms import ForgotPasswordForm
from ..models import User
from ..utils import token_encoder

from django.views.generic import View
from django.shortcuts import reverse
from django.shortcuts import render

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib


class ForgotPasswordView(View):

    def get(self, request):
        context = {}
        form = ForgotPasswordForm()
        context['form'] = form
        return render(request, 'forgot_password_template.html', context)

    def post(self, request):
        context = {}
        form = ForgotPasswordForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            return self.send_email(request, email)
        else:
            form = ForgotPasswordForm()
            context['form'] = form
            context['error'] = 'An error has occured.'
            return render(request, 'forgot_password_template.html', context)

        # if form.is_valid():
        #     user = authenticate(email=form.cleaned_data['email'],
        #                         password=form.cleaned_data['password'])

        #     if user:
        #         login(request=request,
        #               user=user)
        #         next_url = request.GET.get('next')
        #         if next_url:
        #             return HttpResponseRedirect(next_url)
        #         else:
        #             return redirect('list_listings')
        #     else:
        #         context['error'] = "The email or password are not correct. Please try again"

    def send_email(self, request, email):
        context = {}
        form = ForgotPasswordForm()
        context['form'] = form

        try:
            user = User.objects.get(email=email)

            reset_token = token_encoder.encode_reset_token(user.email)
            reset_token = str(reset_token)
            reset_token = reset_token[2:len(reset_token) - 1]

            with open('/var/www/smtp.conf', 'r') as f:
                server_email = f.readline().strip()
                server_pass = f.readline().strip()

            print(server_email)
            print(server_pass)

            # insert user info inside email
            message = """
            Hello, %s !

            It seems like you have forgotten your password. Don't worry, we got you covered.

            Access this link right here to set up a new one.

            http://%s/reset-password/?token=%s

            Regards,
            Links Team""" % (user.first_name, request.get_host(), reset_token)

            mailServer = smtplib.SMTP('smtp.gmail.com', 587)
            mailServer.starttls()
            mailServer.login(server_email, server_pass)

            mail = MIMEMultipart()
            mail['From'] = server_email
            mail['To'] = email
            mail['Subject'] = "RealEstateMarketPlace Reset Password"
            mail.attach(MIMEText(message, 'plain'))

            mailServer.sendmail(server_email, email, mail.as_string())

            # tidy up
            mailServer.quit()

            context['error'] = 'An email has been sent to your account with instructions for resetting your password.'

        except User.DoesNotExist:
            context['error'] = 'No account found with this email address.'

        return render(request, 'forgot_password_template.html', context)
