# -*- coding: utf-8 -*-
import os
import webbrowser
import googleapiclient.discovery
from api.secrets import API_KEY


def main():
    # Disable OAuthlib's HTTPS verification when running locally.
    # *DO NOT* leave this option enabled in production.
    os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"

    api_service_name = "youtube"
    api_version = "v3"
    youtube = googleapiclient.discovery.build(
        api_service_name, api_version, developerKey=API_KEY)

    request = youtube.search().list(
        part="id",
        q="[EN VIVO] Urbana Play 104.3 FM"
    )
    response = request.execute()
    id = response["items"][0]["id"]["videoId"]
    webbrowser.open(f"https://www.youtube.com/watch?v={id}")


if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        logpath = os.path.abspath(os.getcwd()) + "\\log.txt"
        with open(logpath, 'a') as txt:
            txt.write(str(e) + "\n")
