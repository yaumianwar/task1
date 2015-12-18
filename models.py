from db import database 

class PersonalInformation(database.Model):
	__tablename__ = 'personal_information'

	id = database.Column(database.Integer, primary_key = True)
	fullname = database.Column(database.String(20))
	avatar = database.Column(database.String(50))
	description = database.Column(database.String(200))

	def __repr__(self):
		return '<Personal Information {}>'.format(self.fullname)

class BlogList(database.Model):
	__tablename__ = 'listblog'

	id = database.Column(database.Integer, primary_key = True)
	title_post = database.Column(database.String(50))
	content = database.Column(database.String(2000))
	date = database.Column(database.Date)

	def __repr__(self):
		return '<Blog List {}>'.format(self.title_post)