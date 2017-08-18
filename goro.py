#
import urllib
import re
import vk
import time
def hz(url, url2):
    f = urllib.urlopen(url)
    f = f.read()
    print "good get"
    find = re.findall('(.+)\n.+<p id="morespeciallink"><a href="'+ url2 +'">',f)
    zz = find[0].replace("</p>","")
    return zz
session = vk.Session()
session = vk.AuthSession('5001234', "89999696689", "PoPcorN698h", scope='wall, users, status, messages')
vk_api = vk.API(session)
api = vk.API(session)
while True:
    arina = hz("http://orakul.com/horoscope/astrologic/general/aries/today.html", "http://orakul.com/horoscope/astrologic/more/aries/today.html")
    alina = hz("http://orakul.com/horoscope/astrologic/general/pisces/today.html","http://orakul.com/horoscope/astrologic/more/pisces/today.html")
    amir =  hz("http://orakul.com/horoscope/astrologic/general/aquarius/today.html", "http://orakul.com/horoscope/astrologic/more/aquarius/today.html")
    artur = alina
    vk_api.messages.send(user_id = "281141220", message = "Овен: " + arina)
    vk_api.messages.send(user_id = "281141220", message = "Рыба: " + alina)
    vk_api.messages.send(user_id = "266599633", message = "Рыба: " + alina)
    vk_api.messages.send(user_id = "281141220", message = "Водолей: " + amir)
    time.sleep(43200)
