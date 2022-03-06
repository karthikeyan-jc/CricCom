import requests
from bs4 import BeautifulSoup
import re
from gtts import gTTS
import playsound
import os
import sys

URL= sys.argv[1]
last_comment =""
while (2>1):
    page=requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    result = soup.find("div",class_="d-flex match-comment-padder align-items-center")
    is_updated = (last_comment !=result.text)
    if(re.match(r"^[0-9]{2}[.][0-9]", result.text) and result.find("div",class_="match-comment-long-text") is not None and is_updated):
        ball = result.find("span",class_="match-comment-over")
        comment = result.find("div",class_="match-comment-short-text")
        description = result.find("div", class_="match-comment-long-text")
        commentary = ball.text + " " + comment.text + " " + description.text
        last_comment=result.text
        tts = gTTS(commentary)
        tts.save("comment.mp3")
        playsound.playsound("comment.mp3")
        os.remove("comment.mp3")






    