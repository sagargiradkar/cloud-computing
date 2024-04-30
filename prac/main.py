import os
import json
import urllib
import webapp2
from google.appengine.ext.webapp import template
class MainClass(webapp2.RequestHandler):
		def get(self):
			template_values={}
			path=os.path.join(os.path.dirname(__file__),"index.html")
			self.response.out.write(template.render(path,template_values))
			
		def post(self):
				path=os.path.join(os.path.dirname(__file__),"result.html")
				pincode=self.request.get("pincode")
				url="https://api.postalpincode.in/pincode/"+pincode
				data=urllib.urlopen(url).read()
				data=json.loads(data)
				if(data[0]["Status"]=="Success"):
					name=data[0]["PostOffice"][0]["Name"]
					block=data[0]["PostOffice"][0]["Block"]
					state=data[0]["PostOffice"][0]["State"]

					template_data={
						"name":name,
						"block":block,
						"state":state
					}
					self.response.out.write(template.render(path,template_data))

app=webapp2.WSGIApplication([("/",MainClass)],debug=True)	