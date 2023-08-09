import os
import json
import smtplib
import ssl
from email.mime.text import MIMEText
from email.header import Header

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "HsiangNianian@gmail.com"
receiver_email = "admin@jyunko.cn"
password = os.environ.get("TOKEN", "")

f = open('NEWS.json', 'r',encoding='utf-8')
release_list = json.loads(f.read())
f.close()
release_cover_path = release_list['release_cover_path']
release_name = release_list['release_name']
release_id = release_list['release_id']
release_author = release_list['release_author']

content = """\
    <!DOCTYPE html>
    <html lang="en">

    <head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>(New Release)</title>

    <style>
        body,html,div,ul,li,button,p,img,h1,h2,h3,h4,h5,h6 {
        margin: 0;
        padding: 0;
        }

        body,html {
        background: #fff;
        line-height: 1.8;
        }

        h1,h2,h3,h4,h5,h6 {
        line-height: 1.8;
        }

        .email_warp {
        height: 100vh;
        min-height: 500px;
        font-size: 14px;
        color: #212121;
        display: flex;
        /* align-items: center; */
        justify-content: center;
        }

        .logo {
        margin: 3em auto;
        width: 200px;
        height: 60px;
        }

        h1.email-title {
        font-size: 26px;
        font-weight: 500;
        margin-bottom: 15px;
        color: #252525;
        }

        a.links_btn {
        border: 0;
        background: #4C84FF;
        color: #fff;
        width: 100%;
        height: 50px;
        line-height: 50px;
        font-size: 16px;
        margin: 40px auto;
        box-shadow: 0px 2px 4px 0px rgba(0, 0, 0, 0.15);
        border-radius: 4px;
        outline: none;
        cursor: pointer;
        transition: all 0.3s;
        text-align: center;
        display: block;
        text-decoration: none;
        }

        .warm_tips {
        color: #757575;
        background: #f7f7f7;
        padding: 20px;
        }

        .warm_tips .desc {
        margin-bottom: 20px;
        }

        .qr_warp {
        max-width: 140px;
        margin: 20px auto;
        }

        .qr_warp img {
        max-width: 100%;
        max-height: 100%;
        }

        .email-footer {
        margin-top: 2em;
        }

        #reset-password-email {
        max-width: 500px;
        }
        #reset-password-email .accout_email {
        color: #4C84FF;
        display: block;
        margin-bottom: 20px;
        }
    </style>
    </head>"""+f"""\
    <body>
    <section class="email_warp">
        <div id="reset-password-email">
        <img width="200" align="center" src="{release_cover_path}">
        
        <h1 class="email-title">
            Greeting <span>My fans</span>
        </h1>
        <p>FragmentXwords Records just released <i>{release_name}</i>  by {release_author}, <a href="{release_id}">Check it out here</a>.</p>
        <br>
        <div class="warm_tips">
            <p>You received this 'cause you've subscribed My site.</p>

            <p>Enjoy!✨</p>
        </div>

        <div class="email-footer">
            <p>Sincerely,</p>
            <p>简律纯(HsiangNianian).</p>
        </div>
        <hr />
        <p align="center"><small>Copyright 2018-2023 FragmentXwords, All Rights Reserved.</small></p>
        </div>
    </section>
    </body>
    </html>"""

msg = MIMEText(content, 'html', 'utf-8')
msg['Subject'] = Header('New Release From 简律纯', 'utf-8')
msg['From'] = Header("FragmentXwords(断章)", 'utf-8')

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
