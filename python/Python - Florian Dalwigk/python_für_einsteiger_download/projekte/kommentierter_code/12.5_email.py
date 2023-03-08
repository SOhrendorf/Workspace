import smtplib  # pip install smtplib
# Hauptprogramm.
if __name__ == "__main__":
  # Benutzername und Passwort festlegen.
  benutzername  = "Benutzername" 
  passwort = "Passwort"
  # Betreff der Mail.
  betreff = "Mail mit Python"
  # Text der Mail.
  nachricht = "Hallo,\n\ndas ist ein Test! :)"
  # Absender festlegen.
  MAIL_FROM = "sender@example.com"
  # Empfänger festlegen.
  RCPT_TO = "empfänger@example.com"
  # E-Mail zusammensetzen.
  DATA = f"From:{MAIL_FROM}\nTo:{RCPT_TO}\nSubject:{betreff}\n\n{nachricht}"
  # Mailserver-Adresse.
  MAIL_SERVER = "secure.email.server"
  # Port für den Mail-Server.
  MAIL_PORT = 587
  # Server-Objekt erzeugen.
  server = smtplib.SMTP(f"{MAIL_SERVER}:{MAIL_PORT}")
  # TLS starten (= sichere Verbindung aufbauen).
  server.starttls()
  # Im Server einloggen.
  server.login(benutzername , passwort)
  # E-Mail versenden.
  server.sendmail(MAIL_FROM, RCPT_TO, DATA)
  # Nachricht, dass die E-Mail erfolgreich versendet wurde. 
  print("Die E-Mail wurde erfolgreich versendet.")
  # Kommunikation mit dem Server beenden.
  server.quit()