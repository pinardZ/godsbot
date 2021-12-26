import os
import shutil
from logger import BFLog

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

# 取到账号对应的 cookies 和 config.json 并放在对应目录
def copyLoginFiles():
	# 取出目录中所有账号列表
	account_list = os.listdir(login_files_path)
	account_path_list = [os.path.join(login_files_path, file) for file in account_list]
	# 获取当前索引
	fo = open(index_path, "r+")
	index_content = fo.read()
	index = to_int(index_content)
	if index == False:
		log.warning("index 格式不正确，重置为 0，index: " + index_content)
		index = 0
	if index >= len(account_path_list):
		log.warning("index 越界，重置为 0，index: " + index_content)
		index = 0
	# 取出当前账号的信息
	account_path = account_path_list[index]
	account_file_list = os.listdir(account_path)
	print(account_path_list)
	for file in account_file_list:
		temp_path = os.path.join(account_path, file)
		# 复制账号文件
		log.info("复制账号文件")
		print(temp_path)
		shutil.copy(temp_path, game_account_path)

def main():
	copyLoginFiles()

if __name__ == '__main__':
	main()
