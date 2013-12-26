from app import db
from db.users import User
import getpass

if __name__ == '__main__':
    email = input("email>")
    firstName = input ("first name>")
    lastName = input ("last name>")
    password = getpass.getpass("password>")
    newUser = User(email, firstName, lastName, password)
    db.session.add(newUser)
    db.session.commit()

