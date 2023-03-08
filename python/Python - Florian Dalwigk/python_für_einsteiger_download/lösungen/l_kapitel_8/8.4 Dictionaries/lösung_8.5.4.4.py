dns = {
  "www.google.com" : "142.251.36.110",
  "www.youtube.com" : "142.251.36.142",
  "www.stackoverflow.com" : "151.101.129.69"
}

dns.update({"www.tryhackme.com" : "104.22.54.228"})

# Wir können uns das Ergebnis anzeigen lassen, um zu überprüfen, ob alles funktioniert hat.
print(dns)