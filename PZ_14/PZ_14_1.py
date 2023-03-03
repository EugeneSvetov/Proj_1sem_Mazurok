# 15. В исходном текстовом файле(radio_stations.txt) найти все домены из URL-адресов
# (например, в URL-адресе http://stream.hoster.by:8081/pilotfm/audio/icecast.audio
# домен выделен полужирным).

import re

stations = open('radio_stations.txt','r', encoding='utf8')
string_test = stations.read()
stations.close()
print(f"Ваш файл: {string_test}")
print("Ваши домены: ", re.findall(r'http://(.*):',string_test))