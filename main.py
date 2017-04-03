import sys, getopt
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.action_chains import ActionChains
# import selenium.webdriver.common.keys

# def getElement(driver, name):
# 	elem = None
# 	try:
# 		elem = driver.find_element_by_id(name)
# 		print(name + ' field found successfully')
# 	except NoSuchElementException:
# 		print(name + ' field not found')
#
# 	return elem

def main(argv):
	username = ''
	password = ''
	try:
		opts, args = getopt.getopt(argv, "hu:p:", ["username=", "password="])
	except getopt.GetoptError:
		print ('test.py -i <inputfile> -o <outputfile>')
		sys.exit(2)
	for opt, arg in opts:
		if opt == '-h':
			print ('test.py -u <username> -p <password>')
			sys.exit()
		elif opt in ("-u", "--username"):
			username = arg
		elif opt in ("-p", "--password"):
			password = arg
	# print ('Username is "' + username + "\"")
	# print ('Password is "' + password + "\"")

	if len(username) == 0:
		print ('Username not entered')
		print('test.py -u <username> -p <password>')
		sys.exit()
	if len(password) == 0:
		print('Password not entered')
		print('test.py -u <username> -p <password>')
		sys.exit()

	driver = webdriver.Chrome()
	driver.get("https://www.portfolio123.com/login.jsp?url=/")

	driver.find_element_by_id('LoginUsername').send_keys(username)
	driver.find_element_by_id('LoginPassword').send_keys(password)



if __name__ == "__main__":
	main(sys.argv[1:])