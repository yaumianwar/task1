from db import database 

class PersonalInformation(database.Model):
	__tablename__ = 'personal_information'

	id = database.Column(database.Integer, primary_key = True)
	fullname = database.Column(database.String())
	avatar = database.Column(database.String())
	description = database.Column(database.String())

	def __repr__(self):
		return '<Personal Information {}>'.format(self.fullname)