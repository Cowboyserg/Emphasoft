from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from social_auth_1.forms import Profile
from social_auth_1.models import Account


@login_required()
def index_views(request):
    form = Profile(request.POST, request.FILES or None)
    account = Account.objects.filter(user=request.user).first()
    if account:
        index_path = str(account.avatar).replace('static/', '')
        first_name = account.first_name
        second_name = account.second_name
        third_name = account.third_name
        about_you = account.about_you
    else:
        index_path = ''
        first_name = ''
        second_name = ''
        third_name = ''
        about_you = ''
    if request.method == 'POST':
        if form.is_valid():
            index_path = form.cleaned_data['avatar']
            if account:
                account.first_name = form.cleaned_data['first_name']
                account.second_name = form.cleaned_data['second_name']
                account.third_name = form.cleaned_data['third_name']
                account.about_you = form.cleaned_data['about_you']
                account.avatar = form.cleaned_data['avatar']
            else:
                account = form.save(commit=False)
                account.user = request.user
            account.save()
    return render(request, "index.html", {'form': form,
                                          'path': index_path,
                                          'first_name': first_name,
                                          'second_name': second_name,
                                          'third_name': third_name,
                                          'about_you': about_you})
