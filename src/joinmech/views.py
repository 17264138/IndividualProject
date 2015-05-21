from django.shortcuts import render, HttpResponseRedirect, Http404
from .forms import JoinForm
from .models import Join

#this function accepts the user's IP address in two forms
def get_ip(request):
	try:
		x_forward = request.META.get("HTTP_X_FORWARDED_FOR")
		if x_forward:
			ip = x_forward.split(",")[0]
		else:
			ip = request.META.get("REMOTE_ADDR")
	except:
		ip = ""
	return ip

#
import uuid

#this function give a user a unique, uppercase reference ID and validates it
#if the reference ID does exist, the function runs again and gives a new ref id
def get_ref_id():
	ref_id = str(uuid.uuid4())[:11].replace('-', '').upper()
	try:
		id_exists = Join.objects.get(ref_id=ref_id)
		get_ref_id()
	except:
		return ref_id

#this function redirects user to url with ref_id
def share(request, ref_id):
	context = {}
	template = "home.html"
	return render(request,template,context)

#this function controls the view after operations are done on the form and POSTS the input
def home(request):
	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		email = form.cleaned_data['email']
		new_join_old, created = Join.objects.get_or_create(email=email)
		if created:
				new_join_old.ref_id=get_ref_id()
				new_join_old.ip_address=get_ip(request)
				new_join_old.save()
		#redirect here
		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
		#new_join.ip_address = get_ip(request)
		#new_join.save()

	context = {"form": form}
	template = "home.html"
	return render(request, template, context)
