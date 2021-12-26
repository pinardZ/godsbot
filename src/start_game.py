import win32api

def startGame():
	log.info("启动游戏")
	win32api.ShellExecute(0, 'open', '.\\Immutable.lnk', '', '', 1) 

def main():
	startGame()

if __name__ == '__main__':
	main()
