from django.core.mail import send_mail
from django.shortcuts import redirect, render
from django.template.loader import render_to_string

from .forms import ContactForm
# Create your views here.


def cont(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)

        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            content = form.cleaned_data['content']

            html = render_to_string('email/contactform.html', {
                'name': name,
                'email': email,
                'content': content
            })

            print('the form was valid')
            send_mail('The contact form subject', 'This is the message',
                      'noreply@codewithstein.com', ['pppawade@gmail.com'], html_message=html)

            return redirect('home')

    else:
        form = ContactForm()

        return render(request, 'contact.html', {
            'form': form
        })
