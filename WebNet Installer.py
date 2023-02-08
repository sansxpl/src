import os, wget

if not os.path.exists("./WebNet"):
  os.makedirs("./WebNet")

try:
  import wget
except ImportError as err:
  os.system("pip install wget")

if not os.path.isfile("./WebNet/WebNet.exe"):
  wget.download("https://github.com/SansXpl/src/raw/main/WebNet.exe", "./WebNet/")
  
os.chdir("./WebNet/")
os.system("WebNet.exe")