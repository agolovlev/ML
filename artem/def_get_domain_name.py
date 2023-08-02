"""
def get_domain_name(url):
    begins = ['http://', 'https://']
    for i in begins:
        url = url.replace(i, '')
    if url[0:4] == 'www.':
        url = url[4::]
    url = url[0:url.index('.'):]
    return url
"""
def get_domain_name(url):
    url=url.replace("//", ".")
    url=url.split(".")
    print(url)
    if url[1]!="www":
        return url[1]
    return url[2]


# код ниже не стоит удалять, он нужен для проверки
assert get_domain_name("http://google.com") == "google"
assert get_domain_name("http://google.co.jp") == "google"
assert get_domain_name("www.xakep.ru") == "xakep"
assert get_domain_name("https://youtube.com") == "youtube"

assert get_domain_name("http://github.com/carbonfive/raygun") =='github'
assert get_domain_name("http://www.zombie-bites.com") == 'zombie-bites'
assert get_domain_name("https://www.siemens.com") == 'siemens'
assert get_domain_name("https://www.whatsapp.com") == 'whatsapp'
assert get_domain_name("https://www.mywww.com") == 'mywww'
print('Проверки пройдены')