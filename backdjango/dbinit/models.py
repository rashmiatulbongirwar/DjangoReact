from django.db import models

class UserInfo(models.Model):
	fname = models.CharField(default = "first name",max_length=20)
	mname = models.CharField(default = "NA",max_length=20)
	lname = models.CharField(default = "last name",max_length=20)
	uname = models.CharField(default = "user name",max_length=20, unique = True)
	pwd = models.CharField(default = "sksjdkn",max_length=30)
	address = models.CharField(default = "street number",max_length=50)
	city = models.CharField(default="Tempe",max_length=20)
	state = models.CharField(default="AZ",max_length=20)
	zipcode = models.CharField(default="85281",max_length=5)

	def __str__(self):
		return self.fname

class OrgMem(models.Model):
	orgname = models.ForeignKey('UserInfo', on_delete=models.CASCADE)
	orgname = models.CharField( default = "Organization name", max_length=30)
	
	desc = models.CharField(default = "Description", max_length=30)
	address = models.CharField(default = "address", max_length=30)
	city = models.CharField(default = "city", max_length=20)
	zipcode = models.CharField(default = "zipcode", max_length=5)
	phone = models.CharField(default = "phone number", max_length=10)
	state = models.CharField(default = "state", max_length=20)
	upload = models.FileField(default="empty", upload_to='uploads/')

	def __str__(self):
		return self.orgname