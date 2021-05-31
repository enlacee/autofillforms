from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('./chromedriver')
driver.get("https://www.americatv.com.pe/noticias/actualidad/segunda-vuelta-elige-al-ganador-debate-presidencial-jne-n440473")
# https://concursos.americatv.com.pe/concurso/ae/723
# time.sleep(3)

javaScript = "document.getElementById('1').style.display='block'; console.log('loggg');"
driver.execute_script(javaScript)

# inputradio = driver.find_element_by_xpath('//*[@id="register"]/div[2]/div[1]/div/div[1]/label')
inputradio = driver.find_element_by_xpath('//*[@id="1"]')
inputradio.click()

# Submit = driver.find_element_by_xpath('//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div/div/span')
# Submit.click()

