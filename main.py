from email_handler import Email

email_instance = Email(subject="My Subject - TEST - 3 - using secrets",
                       html_content="<html><body><h1>This is my third transactional email </h1></body></html>",
                       sender={"name": "Email sender test", "email": "test@test.com"},
                       to=[{"email": "geopawel90@gmail.com", "name": "Jane Doe"}])

email_instance.send_email()
