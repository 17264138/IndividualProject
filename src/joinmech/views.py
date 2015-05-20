from django.shortcuts import render
from .forms import JoinForm
from .models import Join

def home(request):
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)

	context = {"form": form}
	template = "home.html"
	return render(request, template, context)
