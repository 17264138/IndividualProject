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

#this function redirects user to url with ref_id to the share page
def share(request, ref_id):
	try:
		join_obj = Join.objects.get(ref_id=ref_id)
		friends_referred = Join.objects.filter(friend=join_obj)
		count = join_obj.referral.all().count()

		#the ref_url is set here rather than in settings folder
		ref_url = "http://127.0.0.1:8000/?ref=%s" %(join_obj.ref_id)
		context = {"ref_id": join_obj.ref_id, "count": count, "ref_url": ref_url}
		template = "share.html"
		return render(request,template,context)
	#if there is no ref_id, raise exception
	except:
		raise Http404



#this function controls the view after various operations are done on the form and POSTS the input
def home(request):

	#handles initial initial input from primary object
	try:
		join_id = request.session['join_id_ref']
		obj = Join.object.get(id=join_id)
	except:
		obj=None

	form = JoinForm(request.POST or None)
	if form.is_valid():
		new_join = form.save(commit=False)
		email = form.cleaned_data['email']

		#ensure unique email and assigns ref and ip
		new_join_old, created = Join.objects.get_or_create(email=email)
		if created:
				new_join_old.ref_id=get_ref_id()
				# add user's friend (who referred user) to join model (count) if possible
				if not obj == None:
					new_join_old.friend = obj
				new_join_old.ip_address=get_ip(request)
				new_join_old.save()
		
		#redirects user after inputting email
		return HttpResponseRedirect("/%s" %(new_join_old.ref_id))
		#new_join.ip_address = get_ip(request)
		#new_join.save()

	context = {"form": form}
	template = "home.html"
	return render(request, template, context)
