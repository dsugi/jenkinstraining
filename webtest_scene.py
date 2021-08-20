from selenium import webdriver

def init_driver():
    global driver
    driver = webdriver.Chrome(executable_path="G:\Training\sdk\chromedriver.exe")
    driver.maximize_window

def test_form_entry():
    driver.get("http://localhost/form.php")
    driver.find_element_by_name("nip").send_keys("40002030")
    driver.find_element_by_name("nama").send_keys("dontbe")
    driver.find_element_by_name("nik").send_keys("03020004")
    driver.find_element_by_name("alamat").send_keys("Indonesia")
    driver.find_element_by_name("perusahaan").send_keys("sat")
    driver.find_element_by_name("tanggal").send_keys("01/01/1980")
    driver.find_element_by_name("alamat").send_keys("Indonesia")
    driver.find_element_by_name("divisi").send_keys("IT")
    driver.find_element_by_name("posisi").send_keys("Developer")
    driver.find_element_by_name("gaji").send_keys("$9999")
    driver.find_element_by_name("atasan").send_keys("Manager")
    driver.find_element_by_name("submit").click()

def close_driver():
    driver.close()
    driver.quit()
    print("Test Selesai ...")
