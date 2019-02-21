# Dirscraper
Dirscraper is an OSINT scanning tool which assists penetration testers in identifying hidden, or previously unknown, directories on a domain or subdomain. This helps greatly in the recon stage of pentesting as it provide pentesters with a larger attack surface for the specific domain.

## How does it work?
Dirscraper works by initially visiting the domain provided by the user. From there, it locates all relative script tags hosted on the website. After this, it reads source code of all those javascript files and locates interesting subdomains and endpoints used in those javascript files. A lot of website developers will not make endpoints publically available but will still allow users to interact with them through javascript when appropriate. Sometimes it takes a rare corner case for this criteria to be met (and for a tool such as Burp Suite to pick up the request to the end point) and it becomes unpractical to manually locate these endpoints.

# Getting Started
## Installation
To install dirscraper, simply download the python file and make your in the terminal to the directory containing the file. From ther, run the following installation command:

  pip install -r requirements.txt
  
## Running the program
To run the program, you will need to open the directory containing the file with your terminal. From there, run the following command containing the URL of the site you wish to scan:

  python dirscraper.py -u <URL>
  
## Outputting to a file
When outputting to a file, you must select a filename (if it already exists, it will append results to the bottom, if it doesn't exist it will create the new file). This flag is optional.

  python dirscraper.py -u <URL> -o <FILE>
  
## Silent mode
If you are scanning a website and do not wish to see the results displayed in the terminal, then you can set this flag. If you are not outputting to a file, then using this flag will make it impossible to see your results. This flag is optional.

  python dirscraper.py -u <URL> -o <FILE> -s
