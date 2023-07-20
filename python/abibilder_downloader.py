import time, webbrowser

for i in list(range(55799,56164)):
    url = "https://www.foto-justo.de/downloader.php?request="
    webbrowser.open(f"https://www.foto-justo.de/downloader.php?request={i}")
    print(i)
    time.sleep(1)
