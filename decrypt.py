import os
import glob
from Crypto.Cipher import AES

with open('C:\\key.bin', 'rb') as f:
    key = f.read()

directories = ['C:\\Users\docyo\Pictures\Vid pokemon fleau']

for directory in directories:
    files = glob.glob(os.path.join(directory, '*.cryptox'))

    for file in files:
        with open(file, 'rb') as f:
            encrypted_data = f.read()

        iv = encrypted_data[:AES.block_size]
        encrypted_data = encrypted_data[AES.block_size:]

        cipher = AES.new(key, AES.MODE_CBC, iv=iv)
        decrypted_data = cipher.decrypt(encrypted_data)

        unpadded_data = decrypted_data.rstrip(b'\0')

        original_file = file[:-len('.cryptox')]
        with open(original_file, 'wb') as f:
            f.write(unpadded_data)

    for file in files:
        os.remove(file)



