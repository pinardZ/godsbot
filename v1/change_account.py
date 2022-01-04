import os
import shutil
from main.logger import BFLog

login_files_path = ".\\login_files"
index_path = ".\\current_index.py"
game_account_path = "C:\\Users\\wwly\\AppData\\Roaming\\immutable-launcher\\" 

log = BFLog().getLogger()

def to_int(str):
	try:
		int(str)
		return int(str)
	except ValueError: #报类型错误，说明不是整型的
		return False

# 获取账号索引
def getIndex():
	# 获取当前索引
	fo = open(index_path, "r+")
	index_content = fo.read()
	index = to_int(index_content)
	if index != 0 and index == False:
		log.warning("index 格式不正确，重置为 2，index: " + index_content)
		index = 0
	fo.close()
	return index

# 账号索引 +1
def increaseIndex():
	index = getIndex() + 1
	fo = open(index_path, "w")
	fo.write(str(index))
	fo.close()
	return index

# 取到账号对应的 cookies 和 config.json 并放在对应目录
def copyLoginFilesToGame():
	# 取出目录中所有账号列表
	account_list = os.listdir(login_files_path)
	account_path_list = [os.path.join(login_files_path, file) for file in account_list]
	
	index = getIndex()

	if index >= len(account_path_list):
		log.warning("index 越界，重置为 2，index: " + index_content)
		index = 0

	# 取出当前账号的信息
	account_path = account_path_list[index]
	account_file_list = os.listdir(account_path)
	print(account_path_list)
	# 复制账号文件
	log.info("复制账号 cookies 至游戏目录")
	for file in account_file_list:
		temp_path = os.path.join(account_path, file)
		shutil.copy(temp_path, game_account_path)

# 游戏开启后覆盖新的 cookie
def resetLoginFiles():
	# 取出目录中所有账号列表
	account_list = os.listdir(login_files_path)
	account_path_list = [os.path.join(login_files_path, file) for file in account_list]

	index = getIndex()

	account_path = account_path_list[index]

	game_file_list = os.listdir(game_account_path)
	game_file_path_list = [os.path.join(game_account_path, file) for file in game_file_list]

	# 复制账号文件
	log.info("重置账号 cookies")
	for filename in game_file_list:
		if filename == "Cookies" or filename == "config.json":
			file_path = os.path.join(game_account_path, filename)
			shutil.copy(file_path, account_path)


def main():
	copyLoginFilesToGame()

if __name__ == '__main__':
	main()
