from django.shortcuts import render
from app_two.models import User
from app_two.forms import UserForm

# Create your views here.


def index(request):
    user_form = UserForm()
    if request.method == 'POST':
        user_form = UserForm(request.POST)

        if user_form.is_valid():
            user_form.save(commit=True)

    user_list = User.objects.order_by('first_name')
    user_dict = {'user_records': user_list, 'user_form':user_form}
    return render(request, 'app_two/user.html', context=user_dict)

