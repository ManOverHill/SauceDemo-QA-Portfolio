from selenium import webdriver
from selenium.webdriver.common.by import By
import time

print("--- MENJALANKAN NEGATIVE TEST ---")
driver = webdriver.Chrome()

try:
    driver.get("https://www.saucedemo.com/")
    
    # Skenario: Login dengan password salah
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("password_ngawur") # Password salah
    driver.find_element(By.ID, "login-button").click()
    
    time.sleep(1)
    
    # VALIDASI: Kita cari pesan error warna merah
    # Di SauceDemo, pesan error ada di elemen h3 dengan atribut data-test="error"
    error_element = driver.find_element(By.CSS_SELECTOR, "h3[data-test='error']")
    pesan_error = error_element.text
    
    print(f"Pesan Error yang muncul: {pesan_error}")
    
    # Cek apakah pesan errornya sesuai ekspektasi
    if "Username and password do not match" in pesan_error:
        print("✅ TEST PASSED: Sistem berhasil menolak password salah.")
    else:
        print("❌ TEST FAILED: Pesan error tidak sesuai.")

except Exception as e:
    print(f"❌ Terjadi Error: {e}")

finally:
    driver.quit()