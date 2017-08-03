from django.shortcuts import render
from django.template import RequestContext

from contact.forms import

def signup(request):
    if request.method == 'POST':
        uf = UserForm(request.POST, prefix='user')
        upf = UserProfileForm(request.POST, prefix='userprofile')
        if uf.is_valid() * upf.is_valid():
            user = uf.save()
            userprofile = upf.save(commit=False)
            userprofile.user = user
            userprofile.save()
            return django.http.HttpResponseRedirect('/profile.html')
    else:
        uf = UserForm(prefix='user')
        upf = UserProfileForm(prefix='userprofile')
    return django.shortcuts.render_to_response('login/signup.html',
                                               dict(userform=uf,
                                                    userprofileform=upf),
