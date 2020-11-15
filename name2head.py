import requests
import base64
import json

# The purpose of this project is to access minecraft player heads and skins given only usernames
# because all of the APIs I've found only take UUID. This script simply cuts the middleman.

def get_uuid(name):
    return requests.get('https://api.mojang.com/users/profiles/minecraft/'+name).json()['id']

def get_playerhead_image_link(name):
    uuid = get_uuid(name)
    return 'https://crafatar.com/avatars/' + uuid + '.png?default=MHF_Steve&overlay'

def get_playerskin_image_link(name):
    uuid = get_uuid(name)
    raw_response = requests.get('https://sessionserver.mojang.com/session/minecraft/profile/' + uuid).json()
    decoded_response = json.loads(base64.b64decode(raw_response['properties'][0]['value']))
    return decoded_response['textures']['SKIN']['url']
