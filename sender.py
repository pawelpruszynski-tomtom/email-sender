"""Send email notifications."""
import logging
import smtplib
from email.message import EmailMessage
from email.utils import formatdate, COMMASPACE
import email.utils
from config import Config
# from stats3g.dates import parse_date


def _smtp_send(config, sender, recipients, message):
    smtp = smtplib.SMTP(config.smtp_params()['server'], int(config.smtp_params()['port']))
    if config.smtp_params()['tls']:
        smtp.starttls()

    if config.smtp_params()['username'] is not None:
        smtp.login(config.smtp_params()['username'], config.smtp_params()['password'])
    try:
        smtp.sendmail(sender, recipients, message.as_string())
    except Exception as e:
        logging.error("Failed to send e-mail.")
        logging.error(e, exc_info=True)

    smtp.quit()
    smtp.close()


def _compose_and_send(config, send_to, send_cc, send_bcc, subject, body):
    msg = EmailMessage()
    msg.set_content(body)
    msg['From'] = config.smtp_params()['send_from']
    msg['To'] = send_to if isinstance(send_to, str) else COMMASPACE.join(send_to)
    msg['Cc'] = send_cc if isinstance(send_cc, str) else COMMASPACE.join(send_cc)
    msg['Bcc'] = send_bcc if isinstance(send_bcc, str) else COMMASPACE.join(send_bcc)

    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    _smtp_send(config, config.smtp_params()['send_from'], (send_to+send_cc+send_bcc), msg)


def send_complete_notification(config):
    """Send complete notification for given week."""
    week = config.run_date().isocalendar()[1]
    send_to = config.smtp_params()['success_recipients']
    if len(send_to) == 0:
        logging.info("Empty list of recipients of success notification. Notification skipped.")
        return
    send_cc = config.smtp_params()['success_additional_recipients']
    text = f"< This is an automatically generated email message >\n\n \
    The weekly GLOBAL DB refresh is complete.\n\n \
    All schemas should be available; please notify if you experience any connectivity problems.\n\n \
    Please also check with the the 3G content page for any updates.\n \
    \n\n \
    Contact info:\n \
    Arkadiusz.Maciaszczyk@tomtom.com\n \
    Edyta.Matyszewska@tomtom.com\n\n \
    --\n \
    Regards\n \
    3G Support Team "
    subject = f"INFO: 3G Processing complete - week {week}"
    _compose_and_send(config, send_to, send_cc, [], subject, text)


def send_error_notification(config):
    """Send failure notification for given week."""
    week = config.run_date().isocalendar()[1]
    send_to = config.smtp_params()['failure_recipients']
    if len(send_to) == 0:
        logging.info("Empty list of recipients of failure notification. Notification skipped.")
        return
    send_cc = config.smtp_params()['failure_additional_recipients']
    text = "< This is an automatically generated email message >\n\n \
    Check logs for more details.\n\n \
    --\n \
    Regards\n \
    3G Support Team ".format(week)
    subject = f"ACTION: 3G Processing failed - week {week}"
    _compose_and_send(config, send_to, send_cc, [], subject, text)


if __name__ == '__main__':
    config = Config()
    send_complete_notification(config)

