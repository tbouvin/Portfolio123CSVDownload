import sys, getopt, time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException

def enterText(driver, elementId, text):
	try:
		driver.find_element_by_id(elementId).send_keys(text)
	except NoSuchElementException:
		print("No", elementId, "element")

def clickButton(driver, elementId):
	try:
		driver.find_element_by_id(elementId).click()
	except NoSuchElementException:
		print("No", elementId, "element")

def main(argv):
	username = ''
	password = ''

	try:
		opts, args = getopt.getopt(argv, "hu:p:", ["username=", "password="])
	except getopt.GetoptError:
		print('Invalid option')
		print('test.py -i <inputfile> -o <outputfile>')
		exit()

	for opt, arg in opts:
		if opt == '-h':
			print('test.py -u <username> -p <password>')
			exit()
		elif opt in ("-u", "--username"):
			username = arg
		elif opt in ("-p", "--password"):
			password = arg

	if len(username) == 0:
		print('Username not entered')
		print('test.py -u <username> -p <password>')
		exit()

	if len(password) == 0:
		print('Password not entered')
		print('test.py -u <username> -p <password>')
		exit()

	# if len(csv) == 0:
	# 	print('CSV not entered')
	# 	print('test.py -u <username> -p <password> -c <csv>')
	# 	exit()

#Try using chrome webdriver first. If that fails use Firefox
	driver = None
	# try:
	driver = webdriver.Chrome()
	# except FileNotFoundError:
	# 	print('Chrome web driver not found')
	# 	print('Trying Firefox')
	# 	try:
	# 		driver = webdriver.Firefox()
	# 	except FileNotFoundError:
	# 		print('Firefox web driver not found')
	# 		exit()

#Start selenium and go to login jpage
	driver.get("https://www.portfolio123.com/login.jsp?url=/")

#Enter credentials and login
	enterText(driver, "LoginUsername", username)
	enterText(driver, "LoginPassword", password)
	clickButton(driver, "Login")



if __name__ == "__main__":
	main(sys.argv[1:])