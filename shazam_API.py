import requests
import base64

def Get_song():

    # response = requests.get('https://google.com/')
    # print(response)
    #

    # Rapid key api

    url = "https://shazam.p.rapidapi.com/songs/detect"

    payload = "/Users/pedrorodriguezdeledesmajimenez/CodingProjects/Youtube_downloader/The Kings of Connaught - The Rocky Road to Dublin.mp3"

    message_bytes = payload.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)


    headers = {
        "content-type": "text/plain",
        "X-RapidAPI-Host": "shazam.p.rapidapi.com",
        "X-RapidAPI-Key": "2b5b3f1915msh25cfe548727c38dp165370jsn2c747e1c8261"
    }

    response = requests.request("POST", url, data=base64_bytes, headers=headers)

    print(response.text)