
import requests
import os 
import webbrowser
from webbrowser import Chrome
#chromePath = 'C:\Program Files\Google\Chrome\Application'

def startChrome():
	chromePath=r'C:\Program Files\Google\Chrome\Application\chrome.exe'
	webbrowser.register('chrome', None, webbrowser.BackgroundBrowser(chromePath))  
	t=webbrowser.get('chrome').open('chrome://history/',new=1,autoraise=True)
	#t=webbrowser.open('chrome://history/')
	print(t,type(t))

#如何伪装浏览器数据,获取历史纪录
def main():
	startChrome()
	#cc()
	
if  __name__ == '__main__':
	main()
	
