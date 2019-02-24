import requests, os, argparse, re
from bs4 import BeautifulSoup

from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def regex(content):
    pattern = "(\"|')(\/[\w\d?\/&=#.!:_-]{1,})(\"|')"
    matches = re.findall(pattern, content)
    response = ""
    i = 0
    for match in matches:
        i += 1
        if i == len(matches):
            response += match[1]
        else:
            response += match[1] + "\n"
    return(response)
print("     _ _                              _____      \n  __| (_)_ __ ___  ___ _ __ __ _ _ __|___ / _ __ \n / _` | | '__/ __|/ __| '__/ _` | '_ \ |_ \| '__|\n| (_| | | |  \__ \ (__| | | (_| | |_) |__) | |   \n \__,_|_|_|  |___/\___|_|  \__,_| .__/____/|_|   \n                                |_|\n\n                        ~Cillian Collins\nOutput:")

parser = argparse.ArgumentParser(description='Extract GET parameters from javascript files.')
parser.add_argument('-u', help='URL of the website to scan.')
parser.add_argument('-o', help='Output file (for results).', nargs="?")
parser.add_argument('-s', help='Silent mode (results not printed).', action="store_true")
parser.add_argument('-d', help='Includes domain name in output.', action="store_true")

args = parser.parse_args()

url = args.u + "/"
try:
    r = requests.get(url, verify=False)
except requests.exceptions.MissingSchema:
    args.u = "http://" + args.u
    url = args.u + "/"
    r = requests.get(url, verify=False)
soup = BeautifulSoup(r.text, 'html5lib')
scripts = soup.find_all('script')

linkArr = [args.u]
dirArr = []

for script in scripts:
    try:
        if script['src'][0] == "/" and script['src'][1] != "/":
            script = url.split("/")[0:2] + script['src']
            linkArr.append(script)
        else:
            pass
    except:
        pass
for link in linkArr:
    res = requests.get(link, verify=False)
    out = regex(res.text).split("\n")
    for line in out:
        pathArr = line.strip().split("/")
        path = ""
        for i in range(len(pathArr)):
            if i == len(pathArr) - 1:
                if "." in pathArr[i]:
                    pass
                else:
                     path += pathArr[i] + "/"
            else:
                  path += pathArr[i] + "/"
        if path != "/" and path != "//":
            dirArr.append(path.replace("//", "/").split("#")[0])
        else:
            pass

for directory in list(set(dirArr)):
    if args.o:
        output = open(args.o, "a")
        if args.d:
            output.write(args.u.split("/")[0] + "//" + args.u.split("/")[2] + directory + "\n")
        else:
            output.write(directory + "\n")
    if args.s:
        pass
    else:
        if args.d:
            print(args.u.split("/")[0] + "//" + args.u.split("/")[2] + directory)
        else:
            print(directory)
