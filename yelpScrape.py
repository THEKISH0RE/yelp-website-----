# import time
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC

from selenium import webdriver
from selenium.webdriver.common.by import By

class Yelp_Website:

  def __init__(self,browser):
    if browser == "chrome":
      self.driver = webdriver.Chrome(executable_path="D:\\MyDownloads\\chromedriver_win32\\chromedriver.exe")
      print("Activated driver")
    else:
      print("Provide correct browser name")
      self.driver.maximize_window()
      self.driver.implicitly_wait(30)

  def original_window(self):
    original = self.driver.current_window_handle
    self.driver.switch_to.window(original)

  def multi_windows(self):
    new_window = self.driver.window_handles
    self.driver.switch_to.window(new_window[1])

  def get_element(self, locator_type, locator_value):
    if locator_type == "id":
      return self.driver.find_element(By.ID,locator_value)
    elif locator_type == "xpath":
      return self.driver.find_element(By.XPATH, locator_value)
    elif locator_type == "name":
      return self.driver.find_element(By.NAME, locator_value)
    elif locator_type == "class_name":
      return self.driver.find_element(By.CLASS_NAME, locator_value)
    elif locator_type == "link_text":
      return self.driver.find_element(By.LINK_TEXT, locator_value)
    elif locator_type == "partial_link_text":
      return self.driver.find_element(By.PARTIAL_LINK_TEXT, locator_value)
    elif locator_type == "css_selector":
      return self.driver.find_element(By.CSS_SELECTOR, locator_value)
    elif locator_type == "tag_name":
      return self.driver.find_element(By.TAG_NAME, locator_value)
    else:
      print("check a proper locator")
  
  def get_elements(self, locator_type, locator_value):
    if locator_type == "id":
      return self.driver.find_elements(By.ID,locator_value)
    elif locator_type == "xpath":
      return self.driver.find_elements(By.XPATH, locator_value)
    elif locator_type == "name":
      return self.driver.find_elements(By.NAME, locator_value)
    elif locator_type == "class_name":
      return self.driver.find_elements(By.CLASS_NAME, locator_value)
    elif locator_type == "link_text":
      return self.driver.find_elements(By.LINK_TEXT, locator_value)
    elif locator_type == "partial_link_text":
      return self.driver.find_elements(By.PARTIAL_LINK_TEXT, locator_value)
    elif locator_type == "css_selector":
      return self.driver.find_elements(By.CSS_SELECTOR, locator_value)
    elif locator_type == "tag_name":
      return self.driver.find_elements(By.TAG_NAME, locator_value)
    else:
      print("check a proper locator")
  
  def quit(self):
    print("The program will be END")
    self.driver.quit()
    return self

  def open_url(self, url):
    self.driver.get(url)

  def location(self, category, places):
    sector = category
    place = places.replace(" ",'+')
    url =f'https://www.yelp.com/search?find_desc={sector}&find_loc={place}'
    self.open_url(url)
    return self
    
  def close_second_window(self):
    windows = self.driver.window_handles
    for win in windows:
      self.driver.switch_to.window(win)
      # print(self.driver.title)
      if self.driver.title== "Top 10 Best Restaurants in San Francisco, CA - November 2022 - Yelp":
        pass
      else:
        self.driver.close()
        print(".............................................")
        self.driver.switch_to.window(windows[0])


  def company_details(self):
    company_names = yelp.get_elements("class_name", "css-1m051bw")
    company_name_list = []
    company_link_list = []
    company_number_list = []

    for company in company_names[4:14]:
      print("Company name :", company.text)
      company_name_list.append(company.text)
      company.click()
      yelp.multi_windows()
      try:
        company_link = yelp.get_element("partial_link_text", "http")
        print("Company link :",company_link.text)
        company_link_list.append(company_link.text)
      except:
        print("Company Link : - ")
        company_link_list.append("   -   ")
      
      try:
        company_number = yelp.get_element("xpath","//p[contains(text(),'(415) ')]")
        print("Company_number : ",company_number.text)
        company_number_list.append(company_number.text)
      except:
        print("Company_number : - ")
        company_number_list.append("   -   ")

      yelp.close_second_window()
      
      # print(company_name_list)
      # print(company_link_list)
      # print(company_number_list)

yelp = Yelp_Website("chrome")

yelp.location('restaurants', 'united states').company_details()
yelp.quit()



