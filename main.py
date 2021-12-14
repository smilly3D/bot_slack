from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

options = webdriver.ChromeOptions()
options.add_argument("--user-data-dir=/home/matheus/.config/google-chrome")

navegador = webdriver.Chrome(options=options)
navegador.get("https://app.slack.com/client/TQZR39SET/C023ZGZ49LY?selected_team_id=TQZR39SET")
sleep(5)
navegador.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div").click()
sleep(5)
navegador.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div[1]/div/div[1]/p").send_keys("/kenzie checkin")
sleep(5)
navegador.find_element_by_xpath("/html/body/div[2]/div/div[2]/div[3]/div/div[3]/div/div[2]/div/div/div/div[2]/div/div/div/div[2]/div[3]/div/span/button[1]").click()
sleep(5)

navegador.find_element_by_xpath('//*[@id="plain_text_input-action-current_activity"]').send_keys("atividade do dia")

navegador.find_element_by_xpath('//*[@id="radio_buttons-action-has_blockers-false-1"]').click()
navegador.find_element_by_xpath("/html/body/div[7]/div/div/div[3]/div[1]/button[2]").click()
navegador.quit()
