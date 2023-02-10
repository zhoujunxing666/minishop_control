import datetime
import re
#用户信息

user_id = 0#随机生成的ID
user_name = ""#输入用户名
password = ""#输入密码
email = ""#输入邮箱
phone = ""#输入11位数字
shop_name = ""#输入店名
shop_site = ""#输入地址




def validate_input(input_str):#密码只能字母和数字，长度8-32
    pattern = re.compile(r'^[a-zA-Z0-9]+$')
    if len(input_str) < 8 or len(input_str) > 32:
        return False
    elif not pattern.match(input_str):
        return False
    else:
        return True



def validate_email(email):#邮箱验证
    pattern = re.compile(r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$')
    if pattern.match(email):
        return True
    else:
        return False

email = input('请输入电子邮件地址: ')
if validate_email(email):
    print('电子邮件地址有效')
else:
    print('电子邮件地址无效')
