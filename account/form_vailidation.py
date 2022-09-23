import re
def check_mobile(mobile):
    if len(mobile)==10:
        if mobile.isdigit():
            return True
        else:
            return False
    else:
        return False
    
def check_email(email):
    pattern = '^[a-z0-9]+[\._]?[ a-z0-9]+[@]\w+[. ]\w{2,3}$'
    if re.search(pattern,email):
        return True
    else:
        return False
def check_name(name):
    a=re.findall('\d',name)
    if not a:
        return True
    else:
        return False
