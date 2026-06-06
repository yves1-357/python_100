import smtplib

my_email = "yveskwizera31@yahoo.com"
password = "VCrUHBfQbenyP4"
connection = smtplib.SMTP("smtp.yahoo.com", port=587)  
connection.starttls()
connection.login(user=my_email, password=password)
subject = "Test d'envoie"
body="Yola"
connection.sendmail(from_addr=my_email, to_addrs="yves.kelly730@gmail.com", msg="Yola")
connection.close()