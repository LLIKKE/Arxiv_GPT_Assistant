import smtplib
import datetime
from email.mime.text import MIMEText
from email.header import Header
from email.utils import parseaddr, formataddr
import os

# Function to format the email addresses with a name
def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# Function to read the content of an HTML file
def read_html_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()


# Get current date and time in the format: "YYYY-MM-DD HH:MM"
now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")

# Email credentials and server details
from_addr = os.environ.get("FROM_ADDR")
password = os.environ.get("PASSWORD")  # App-specific password
to_addr = os.environ.get("TO_ADDR")# List of recipients
smtp_server = "smtp.qq.com"  # SMTP server for QQ mail


# Read content from two HTML files
html_content_1 = read_html_file('/home/runner/work/Arxiv_GPT_Assistant/Arxiv_GPT_Assistant/dist/en/index.html')
html_content_2 = read_html_file('/home/runner/work/Arxiv_GPT_Assistant/Arxiv_GPT_Assistant/dist/zh/index.html')

# Combine the contents of the two HTML files
combined_html_content = f'''
<html>
  <body>
    {html_content_1}
    <hr>
    中文翻译版本:
    <hr>
    {html_content_2}
  </body>
</html>
'''

# Create a MIMEText object for the combined HTML content
msg = MIMEText(combined_html_content, 'html', 'utf-8')

# Set email headers
msg['From'] = _format_addr(f'Arxiv_GPT_Assistant <{from_addr}>')
msg['To'] = _format_addr(f'Arxiv_GPT_Assistant')
msg['Subject'] = Header(f'ArXiv daily: {now}', 'utf-8').encode()

# Connect to the SMTP server and send the email
try:
    # Establish an SSL connection to the SMTP server on port 465
    server = smtplib.SMTP_SSL(smtp_server, 465)

    # Set debug level to 1 for detailed interaction logs
    server.set_debuglevel(1)

    # Login to the server using the sender's credentials
    server.login(from_addr, password)

    # Send the email
    server.sendmail(from_addr, to_addr, msg.as_string())
    print("Email sent successfully!")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the connection to the SMTP server
    server.quit()
