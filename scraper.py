from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.get("http://www.sephora.com/makeup-cosmetics")

driver.implicitly_wait(10)

elem = driver.find_element_by_xpath('//*[@id="banner"]/div/div[2]/div/div[2]/div[1]/ul')

products = elem.find_elements_by_tag_name("li")

count = 0

for product in products:

  if count == 4:
    driver.find_element_by_xpath('//*[@id="banner"]/div/div[2]/div/div[2]/div[3]').click()
    count = 0

  count += 1

  info_div = product.find_element_by_xpath("a/div[3]")
  product_name = info_div.find_element_by_class_name("SkuItem-name").text.replace('\n', '')
  price = info_div.find_element_by_xpath('div[2]/span').text.strip()
  rating = info_div.find_element_by_class_name("StarRating").get_attribute('seph-stars')


  print "PRODUCT: " + product_name
  print "PRICE: " + price
  print "RATING: " + rating + " stars"
  print '\n'
