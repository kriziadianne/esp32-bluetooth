from django.db import models

class DocReg:

		def __init__(self, famName, firstName, gender, birthdate, email, passw, conf_pass, address, num, MS, lNum): # to set information automatically
			self.famName = famName
			self.firstName = firstName
			self.gender = gender
			self.birthdate = birthdate
			self.email = email
			self.passw = passw
			self.conf_pass = conf_pass
			self.address = address
			self.num = num
			self.MS = MS
			self.lNum = lNum
			self.fullName = famName + firstName
	# famName = request.POST.get('famName')
 #    firstName = request.POST.get('firstName')
 #    gender = request.POST.get("gender")
 #    birthdate = request.POST.get("birthdate")
 #    email = request.POST.get('email')
 #    passw = request.POST.get('password')
 #    conf_pass = request.POST.get('conf_password')
 #    address = request.POST.get("address")
 #    num = '+63' + str(request.POST.get("mobileNum"))
 #    MS=request.POST.getlist('MS')
 #    lNum = request.POST.get("lNum")
 #    fullname = {
 #        'lastName': famName,
 #        'firstname': firstName
 #    }

 #    def __str__(self):
 #    	return self.famName
 #    	return self.firstName
 #    	return self.gender
 #    	return self.birthdate
 #    	return self.email
 #    	return self.passw
 #    	return self.conf_pass
 #    	return self.address
 #    	return self.num
 #    	return self.MS
 #    	return self.lNum
 #    	return self.fullname = famName + firstName