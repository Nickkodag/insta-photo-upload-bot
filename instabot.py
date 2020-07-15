from instapy_cli import client
from textwrap import dedent

username = "kodag__nilesh" #your username

password = "123456789@NK" #your password 

image = "01.jpg"    #here you can put the image directory

text = dedent("""this is test bitch""")


with client(username, password) as cli:
    cli.upload(image, text)