from django.shortcuts import render
from .forms import AuthorForm
from .models import Author, ConfirmCode
from .utils import send_code_to_mail
from django.conf import settings
# Create your views here.

def register(request):
    form = AuthorForm()
    if request.method == 'POST':
        form = AuthorForm(request.POST)
        if form.is_valid():
            author = Author(username = request.POST['username'], email = request.POST['email'])
            author.set_password(request.POST['password'])
            author.save()
            code = ConfirmCode.objects.create(author = author)
            send_code_to_mail(author.email, code.code)
    return render(request, 'main/register.html', {'form': form})

def confirm_email(request, code):
    code = ConfirmCode.objects.filter(code = code)
    message = 'Code is not valid'
    if code:
        if not code.last().confirm:
            code.last().confirm = True
            code.last().save()
            code.last().author.verified = True
            code.last().author.save()
            message = 'Your email confirmed!'
    return render(request, 'main/reply.html', {'message': message})