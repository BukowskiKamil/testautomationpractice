import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox()
driver.get("https://testautomationpractice.blogspot.com/")
time.sleep(1)
driver.maximize_window()
#usunięcie powiadomienia
driver.find_element(By.XPATH, '//*[@id="cookieChoiceDismiss"]').click()
time.sleep(1)
#tabela "Name"
driver.find_element(By.XPATH, "//*[@id='name']").send_keys("Jan")
time.sleep(1)
#tabela "Email"
driver.find_element(By.XPATH, "//*[@id='email']").send_keys("Kowalski")
time.sleep(1)
#tabela "Phone"
driver.find_element(By.XPATH, "//*[@id='phone']").send_keys("668453888")
time.sleep(1)
#tabela "Address"
driver.find_element(By.XPATH, "//*[@id='textarea']").send_keys("Wesoła 13, 39-200 Łódź")
time.sleep(1)
#checkbox male/female
driver.find_element(By.XPATH, "//*[@id='male']").click()
time.sleep(1)
#checkbox z wyborem różnych dni tygodnia
dni_tygodnia = driver.find_elements(By.XPATH, "//*[@id='monday' or @id='friday']")
for n in dni_tygodnia:
    n.click()
time.sleep(1)
#lista rozwijania z wyborem kraju
wybor_panstwa = driver.find_element(By.XPATH, "//*[@id='country']")
wybor_panstwa = Select(wybor_panstwa)
wybor_panstwa.select_by_visible_text("Germany")
time.sleep(1)
#lista z wyborem koloru
wybor_koloru = driver.find_element(By.XPATH, "//*[@id='colors']")
wybor_koloru = Select(wybor_koloru)
wybor_koloru.select_by_visible_text("Blue")
time.sleep(1)
#wybór daty
data = driver.find_element(By.XPATH, "//*[@id='datepicker']")
data.send_keys("05/25/2020")
driver.find_element(By.XPATH, "//*[@id='male']").click()
#wywoływanie książek konkretnego autora
liczba_ksiazek = len(driver.find_elements(By.XPATH, "//table[@name='BookTable']/tbody/tr"))
for j in range(2, liczba_ksiazek+1):
    imie_autora = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(j)+"]/td[2]").text
    if imie_autora == "Amit":
        tytul_ksiazki = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(j)+"]/td[1]").text
        cena = driver.find_element(By.XPATH, "//table[@name='BookTable']/tbody/tr["+str(j)+"]/td[4]").text
        print(tytul_ksiazki, " ", imie_autora, " ", cena)
#zaznaczenie odpowiednich cen
liczba_pozycji = len(driver.find_elements(By.XPATH, "//*[@id='productTable']/tbody/tr"))
for k in range(1, liczba_pozycji+1):
    cena2 = driver.find_element(By.XPATH, "//*[@id='productTable']/tbody/tr["+str(k)+"]/td[3]").text
    if cena2 == "$10.99":
        nazwa_produktu = driver.find_element(By.XPATH, "//*[@id='productTable']/tbody/tr["+str(k)+"]/td[2]").text
        print(nazwa_produktu, " ", cena2)
        checkbox = driver.find_element(By.XPATH, "//*[@id='productTable']/tbody/tr[" + str(k) + "]/td[4]/input")
        checkbox.click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='pagination']/li[2]/a").click()

for k in range(1, liczba_pozycji+1):
    cena2 = driver.find_element(By.XPATH, "//*[@id='productTable']/tbody/tr["+str(k)+"]/td[3]").text
    if cena2 == "$10.99":
        nazwa_produktu = driver.find_element(By.XPATH, "//*[@id='productTable']/tbody/tr["+str(k)+"]/td[2]").text
        print(nazwa_produktu, " ", cena2)
        checkbox = driver.find_element(By.XPATH, "//*[@id='productTable']/tbody/tr[" + str(k) + "]/td[4]/input")
        checkbox.click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='pagination']/li[3]/a").click()

for k in range(1, liczba_pozycji+1):
    cena2 = driver.find_element(By.XPATH, "//*[@id='productTable']/tbody/tr["+str(k)+"]/td[3]").text
    if cena2 == "$10.99":
        nazwa_produktu = driver.find_element(By.XPATH, "//*[@id='productTable']/tbody/tr["+str(k)+"]/td[2]").text
        print(nazwa_produktu, " ", cena2)
        checkbox = driver.find_element(By.XPATH, "//*[@id='productTable']/tbody/tr[" + str(k) + "]/td[4]/input")
        checkbox.click()
time.sleep(1)
driver.find_element(By.XPATH, "//*[@id='pagination']/li[4]/a").click()

for k in range(1, liczba_pozycji+1):
    cena2 = driver.find_element(By.XPATH, "//*[@id='productTable']/tbody/tr["+str(k)+"]/td[3]").text
    if cena2 == "$10.99":
        nazwa_produktu = driver.find_element(By.XPATH, "//*[@id='productTable']/tbody/tr["+str(k)+"]/td[2]").text
        print(nazwa_produktu, " ", cena2)
        checkbox = driver.find_element(By.XPATH, "//*[@id='productTable']/tbody/tr[" + str(k) + "]/td[4]/input")
        checkbox.click()
#Wpisanie i wyszukanie
slowo_do_wyszukania = "Poczta Polska"
driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-input']").send_keys(slowo_do_wyszukania)
driver.find_element(By.XPATH, "//*[@id='Wikipedia1_wikipedia-search-form']/div/span[2]/span[2]/input").submit()
time.sleep(1)
#przekierowanie na nową stronę
nowa_strona = driver.find_element(By.XPATH, "//*[@id='HTML4']/div[1]/button")
nowa_strona.click()
time.sleep(1)
#powrót do poprzedniej zakładki
windowsIDs = driver.window_handles
parent_window_id = windowsIDs[0]
child_window_id = windowsIDs[1]
driver.switch_to.window(parent_window_id)
time.sleep(1)
#Alert
driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button[1]").click()
okno_alertu = driver.switch_to.alert
time.sleep(1)
okno_alertu.accept()
#Comfirm Box (Anuluj)
driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button[2]").click()
time.sleep(1)
okno_alertu.dismiss()
#Prompf
driver.find_element(By.XPATH, "//*[@id='HTML9']/div[1]/button[3]").click()
time.sleep(1)
okno_alertu.send_keys("Tester")
time.sleep(1)
okno_alertu.accept()
#Double-click
podwojny = driver.find_element(By.XPATH, "//*[@id='HTML10']/div[1]/button")
akcja_1 = ActionChains(driver)
akcja_1.double_click(podwojny).perform()
time.sleep(1)
#przejście niżej
flaga_1 = driver.find_element(By.XPATH, '//*[@id="HTML10"]/h2')
driver.execute_script("arguments[0].scrollIntoView();", flaga_1)
#przeciąganie
akcja_2 = ActionChains(driver)
co_przenosze = driver.find_element(By. XPATH, "//*[@id='draggable']")
gdzie_przenosze = driver.find_element(By.XPATH, "//*[@id='droppable']")
akcja_2.drag_and_drop(co_przenosze, gdzie_przenosze).perform()
time.sleep(1)
#slider
akcja_3 = ActionChains(driver)
suwak = driver.find_element(By.XPATH, '//*[@id="slider"]/span')
akcja_3.drag_and_drop_by_offset(suwak,50,0).perform()
#przejście niżej
flaga_2 = driver.find_element(By.XPATH, '//*[@id="HTML6"]/h2')
driver.execute_script("arguments[0].scrollIntoView();", flaga_2)
time.sleep(1)
#uzupełnienie danych na innym frame'ie
driver.switch_to.frame("frame-one796456169")
driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-0"]').send_keys('Kamil')
driver.find_element(By.XPATH, '//*[@id="q2"]/table/tbody/tr[1]/td/label').click()
driver.find_element(By.XPATH, '//*[@id="RESULT_TextField-2"]').send_keys("08/16/2023")
driver.find_element(By.XPATH, '//*[@id="RESULT_RadioButton-3"]')
driver.find_element(By.XPATH, '//*[@id="RESULT_RadioButton-3"]').click()
time.sleep(1)
driver.find_element(By.XPATH, '//*[@id="RESULT_RadioButton-3"]/option[4]').click()
driver.find_element(By.XPATH, '//*[@id="FSsubmit"]').click()
time.sleep(1)
driver.switch_to.parent_frame()
#przejście niżej
flaga_3 = driver.find_element(By.XPATH, '//*[@id="HTML3"]')
driver.execute_script("arguments[0].scrollIntoView();", flaga_3)
#zmiana rozmiaru
akcja_4 = ActionChains(driver)
suwak = driver.find_element(By.XPATH, '//*[@id="resizable"]/div[3]')
akcja_4.drag_and_drop_by_offset(suwak,220,300).perform()
time.sleep(1)
print("Test zakończony pomyślnie")
time.sleep(5)
driver.quit()
