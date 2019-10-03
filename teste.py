import re

def erCasaComDia(subject):
    pattern = r'\"[a-zA-z]{0, } | \t{0, } \"'
    #pattern = r'\"([a-zA-z|0-9]|\t)*\"'
    return re.match(pattern, subject)

#print(erCasaComDia("Ola Ba"))
#assert not erCasaComDia('bom-dia')

#re.match(r'\"([^\\\n]|(\\.))*?\"', "Oi ba")

texto = "Oi ba"
res = re.match(r'\"([a-zA-z]{0, } | \t{0, })\"', texto)
res.group()