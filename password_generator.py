import string
import random
 
def generate_password(len):
   all_chars = string.ascii_letters + string.digits + string.punctuation
   password = ''
   for char in range(len):
       rand_char = random.choice(all_chars)
       password = password + rand_char
   return password
 
pass_length = int(input('How many characters in your password?'))
new_password = generate_password(pass_length)
print('Your new password: ', new_password)