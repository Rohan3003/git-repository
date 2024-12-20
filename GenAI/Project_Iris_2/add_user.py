from app import db, User

# Create the database and tables if they don't exist
db.create_all()

# Create a new user
new_user = User(username='admin', password='password')  # Change these as needed

# Add and commit the user to the database
db.session.add(new_user)
db.session.commit()

print("User added successfully!")