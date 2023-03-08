import smtplib

if __name__ == "__main__":
  benutzername  = "Benutzername " 
  passwort = "Passwort"
  betreff = "Mail mit Python"
  nachricht = "Hallo,\n\ndas ist ein Test! :)"
  
  MAIL_FROM = "sender@example.com"
  RCPT_TO = "empfänger@example.com"
  DATA = f"From:{MAIL_FROM}\nTo:{RCPT_TO}\nSubject:{betreff}\n\n{nachricht}"
  MAIL_SERVER = "secure.email.server"
  MAIL_PORT = 587

  server = smtplib.SMTP(f"{MAIL_SERVER}:{MAIL_PORT}")
  server.starttls()
  server.login(benutzername , passwort)
  server.sendmail(MAIL_FROM, RCPT_TO, DATA)
  print("Die E-Mail wurde erfolgreich versendet.")
  server.quit()