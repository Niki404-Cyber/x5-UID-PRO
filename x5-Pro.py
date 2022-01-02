import os, platform
try:
    import requests
except:
    os.system('pip2 install requests')

import requests
bit = platform.architecture()[0]
if bit == '64bit':
    from nologin import subscribe
    subscribe()
elif bit == '32bit':
    from niki.so import subscribe
    subscribe()
