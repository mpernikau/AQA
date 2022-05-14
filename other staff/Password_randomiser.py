import random
from datetime import datetime
from string import punctuation, ascii_letters, digits, ascii_lowercase, ascii_uppercase

symbols = ascii_letters + digits + punctuation+ascii_lowercase+ascii_uppercase

secure_random = random.SystemRandom()
symbols_count = int(input('How many symbols should password has? '))
password = ''.join(secure_random.choice(symbols) for i in range(symbols_count))

date_log = datetime.today().strftime('%d.%m.%Y   %H:%M:%S')

file_opening = open('Password_file.txt', 'a')

for string in password:
    file_opening.write(str(date_log) + '  ------>  ')
    file_opening.write(password + '\n')
    break

print(date_log)
print(password)