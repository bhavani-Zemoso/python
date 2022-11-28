import bcrypt
 
password = b'password@educative'
 
salt_generation = bcrypt.gensalt(10)
print("Randomly generated salt after 10 rounds: ")
print(salt_generation)

password_hash = bcrypt.hashpw(password, salt_generation)
print("Password hashed after random generation of salt:")
print(password_hash)

password_match = bcrypt.checkpw(password, password_hash)
print("if the password matches with already hashed password:")
print(password_match)