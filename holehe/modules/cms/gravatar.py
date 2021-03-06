from holehe.core import *
from holehe.localuseragent import *

def gravatar(email):
    hashed_name =  hashlib.md5(email.encode()).hexdigest()
    r =  requests.get('https://gravatar.com/{hashed_name}.json')
    if r.status_code != 200:
        return({"rateLimit": False, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
    else:
        try:
            data = r.json()
            name = data['entry'][0]['name'].get('formatted')
            others = {
                'FullName': name,
            }

            return({"rateLimit": False, "exists": True, "emailrecovery": None, "phoneNumber": None, "others": others})
        except BaseException:
            return({"rateLimit": True, "exists": False, "emailrecovery": None, "phoneNumber": None, "others": None})
