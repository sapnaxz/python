#random password generator with ascii letters and digits and punctuations

import random
from string import punctuation, ascii_letters, digits


symbols = ascii_letters + digits + punctuation
secure_random = random.SystemRandom()
password ="".join(secure_random.choice(symbols)for i in range(10))
print(password)



