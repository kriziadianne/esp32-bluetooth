## my notes
# class is basically a blueprint creating instances
# 
##
class DoctorSignUp:
				# instance, [trailing arguments]
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
	# def fullName(self):
	# 	return '{} {}'.format(self.famName, self.firstName)
doctor = DoctorSignUp('Doe', 'John', 'M', 'January 1, 1890', 'johndoe@gmail.com', 'johndoe', ' johndoe', '123 maplethorpe', 123, 'cardiology', )


class PatientSignUp:
	def __init__(self, famName, firstName, email, address, num, gender, birthdate, btype):
		self.famName = famName
		self.firstName = firstName
		self.email = email
		self.address = address
		self.num = num
		self.gender = gender
		self.birthdate = birthdate
		self.btype = btype
	def fullName(self):
		return '{} {}'.format(self.famName, self.firstName)		
