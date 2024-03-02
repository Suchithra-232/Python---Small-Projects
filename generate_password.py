import random
import string

password_len = 8
string_val = string.ascii_letters + string.digits + string.punctuation

password = "".join([random.choice(string_val) for i in range(password_len)])
print(password)
