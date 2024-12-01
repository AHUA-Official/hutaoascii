# 使用 smtplib 模块发送纯文本邮件
import smtplib
import ssl
from email.message import EmailMessage

EMAIL_ADDRESS = "3309719563@qq.com"  # 邮箱的地址
EMAIL_PASSWORD = "gqedgkpjbfuvdbhd"  # 授权码

# 连接到smtp服务器
# smtp = smtplib.SMTP('smtp.qq.com', 587)     # 未加密

# 也可以使用ssl模块的context加载系统允许的证书，在登录时进行验证
context = ssl.create_default_context()

'''
# 为了防止信息在网络传输中泄漏，最好对信息进行加密
smtp = smtplib.SMTP_SSL("smtp.163.com", 465, context=context)       # 完成加密通讯
# 连接成功后使用login方法登录自己的邮箱
smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
# 一、使用 sendmail 方法实现发送邮件信息
sender = EMAIL_ADDRESS      # 用来发送的邮箱地址
receive = ""        # 目标邮箱地址
subject = "邮件标题内容"
body = "邮件主体内容"
msg = f"Subject: {subject}\n\n{body}"
smtp.sendmail(sender, receive, msg)
# 发送完毕后使用 quit 方法关闭连接
smtp.quit()
'''

subject = "邮件标题内容"
body = "邮件主体内容"

msg = EmailMessage()
msg['subject'] = subject  # 邮件标题
msg['From'] = EMAIL_ADDRESS  # 邮件发件人
msg['To'] = "目标邮箱账号"  # 邮件的收件人
msg.set_content(body)  # 使用set_content()方法设置邮件的主体内容

# 为了防止忘记关闭连接也可以使用with语句
with smtplib.SMTP_SSL("gqedgkpjbfuvdbhd", 587, context=context) as smtp:  # 完成加密通讯

    # 连接成功后使用login方法登录自己的邮箱
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)

    '''
    # 方式一：
    # 使用 sendmail 方法实现发送邮件信息
    sender = EMAIL_ADDRESS      # 邮件发件人
    receive = EMAIL_ADDRESS       # 邮件收件人
    subject = "subject"
    body = "body"
    msg = f"Subject: {subject}\n\n{body}"
    print("正在发送。。。。。。。。。。。。。。。。。。")
    smtp.sendmail(sender, receive, msg)
    print("发送成功。。。。。。。。。。。。。。。。。。")
    '''

    # 方式二：使用send_message方法发送邮件信息
    smtp.send_message(msg)
