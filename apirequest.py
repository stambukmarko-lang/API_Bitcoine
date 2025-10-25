import requests

url= 'https://www.ibm.com/'
r = requests.get(url)
r.status_code
r.request.headers

#print(r.status_code)        # ispis statusnog koda (200 = OK)
#print(r.request.headers)    # ispis headera poslanog zahtjeva

if r.status_code == 200:
    print("Zahtjev uspješan!")
else:
    print(f"Greška: {r.status_code}")
    
print(r.text[:500])  # ispiše prvih 500 znakova HTML-a

print()
encod= r.encoding
header = r.headers

print(encod)
print(header)