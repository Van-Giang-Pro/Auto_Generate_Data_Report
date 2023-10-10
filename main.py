from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import os
import time
import sys
import socket


class Whatsapp:
	search_box_xpath = "//div[@title='Tìm kiếm bằng ô nhập văn bản']"
	message_box_xpath = "//div[@title='Nhập tin nhắn']"
	attachment_icon_xpath = "//div[@title='Đính kèm']"
	image_attachment_xpath = "//input[@accept='image/*,video/mp4,video/3gpp,video/quicktime']"
	send_button_xpath = "//span[@data-icon='send']"

	def __init__(self, url):
		self.url = url
		print(socket.gethostname())
		if socket.gethostname() == "My-Personal-PC":
			chrome_directory = (r"user-data-dir=C:\Users\Admin\AppData\Local\Google"
			                    r"\Chrome\User_Data_For_Auto_Trigger_System")
		elif socket.gethostname() == "FS-35828":
			print("Running Under Company Laptop")
			chrome_directory = (r"user-data-dir=C:\Users\fs120806\AppData\Local"
			                    r"\Google\Chrome\User_Data_For_Auto_Trigger_System")
		else:
			print("Running Under Home PC")
			chrome_directory = (r"user-data-dir=C:\Users\admin\AppData\Local"
			                    r"\Google\Chrome\User_Data_For_Auto_Trigger_System")
		# Access To Whatsapp
		self.chrome_options = Options()
		self.chrome_options.add_argument(chrome_directory)
		self.chrome_options.add_experimental_option("detach", True)
		# Keep the chrome driver open after the program is finished
		self.chrome_driver = webdriver.Chrome(options=self.chrome_options)
		self.wait = WebDriverWait(self.chrome_driver, 100)
		self.chrome_driver.get(self.url)
		page_title = self.chrome_driver.title
		# Get the title of the website
		print(f"The Website You Are Accessing Is {page_title}")
		try:
			self.search_box = self.wait.until(EC.presence_of_element_located((By.XPATH, Whatsapp.search_box_xpath)))
		except TimeoutException:
			print("The Website Is Not Available Or The Internet Connection Is Not Stable")
			self.chrome_driver.quit()

	def enter_into_user_chat_box(self, user):
		self.search_box.clear()
		self.search_box.click()
		self.search_box.send_keys(user)
		self.search_box.send_keys(Keys.ENTER)
		print("Start Sending Message To {0}".format(user))

	def run_script_and_send_message(self, script_folder_path, script_name, message):
		script_path = script_folder_path + "\\" + script_name
		print("Running Script {0}".format(script_path))
		os.startfile(script_path)
		time.sleep(5)
		message_box = self.wait.until(EC.presence_of_element_located((By.XPATH, Whatsapp.message_box_xpath)))
		message_box.clear()
		message_box.send_keys(message)
		message_box.send_keys(Keys.ENTER)
		print("Message Sent")


if __name__ == '__main__':
	whatsapp_url = "https://web.whatsapp.com/"
	whatsapp = Whatsapp(whatsapp_url)
	whatsapp.enter_into_user_chat_box("Data Trigger Fin 1")
	whatsapp.run_script_and_send_message(r"C:\Users\Admin\Desktop\Script Folder", "Script Test Python", "Test")
