#author rski


from app import db
    

class User(db.Model):
    email = db.Column(db.String(120), primary_key=True)
    firstName = db.Column(db.String(80))
    lastName = db.Column(db.String(80))
    password = db.Column(db.String(120))

    def __init__(self, email, firstName, lastName, password):
        self.email = email
        self.firstName = firstName
        self.lastName = lastName
        self.password = password

    def __repr__(self):
        return '<User %r %r %r>' % (self.firstName,self.lastName, self.email)


