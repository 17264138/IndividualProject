from joinmech.models import Join
#middleware function to process and trace requests

class ReferMiddleware():
	def process_request(self,request):
		ref_id=request.GET.get("ref")
		try:
			obj = Join.objects.get(ref_id=ref_id)
		except:
			obj=None
		
		#setting a session variable of reference to the object it's referencing
		if obj:
			request.session['join_id_ref'] = obj.id
		

		