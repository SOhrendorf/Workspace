dns = {
  "www.google.com" : "142.251.36.110",
  "www.youtube.com" : "142.251.36.142",
  "www.stackoverflow.com" : "151.101.129.69"
}

# Möglichkeit 1
youtube_1 = dns.get("www.youtube.com")

# Möglichkeit 2
youtube_2 = dns["www.youtube.com"]

# Überprüfung (optional)
print(youtube_1 == youtube_2)