from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# --- SETUP ---
# Membuka browser Chrome
print("Membuka Browser...")
driver = webdriver.Chrome()

# Memaksimalkan layar agar elemen terlihat semua
driver.maximize_window()

# --- LANGKAH TESTING ---

try:
    # 1. Buka Website Target
    driver.get("https://www.saucedemo.com/")
    
    # 2. Cari elemen username & isi data
    # Kita menggunakan ID karena itu locator paling stabil
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    
    # 3. Cari elemen password & isi data
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    
    # 4. Klik tombol Login
    driver.find_element(By.ID, "login-button").click()
    
    # Beri jeda 2 detik agar mata kita sempat melihat prosesnya
    time.sleep(2)

    # --- VALIDASI (ASSERTION) ---
    # Kita cek apakah kita sudah masuk halaman dashboard
    # Caranya: Cari tulisan "Products" di bagian atas halaman
    judul_halaman = driver.find_element(By.CLASS_NAME, "title").text
    
    if judul_halaman == "Products":
        print("✅ TEST PASSED: Berhasil Login dan masuk ke halaman Produk.")
    else:
        print("❌ TEST FAILED: Gagal Login atau halaman tidak sesuai.")

except Exception as e:
    print(f"❌ Terjadi Error: {e}")

finally:
    # --- TEARDOWN ---
    # Tutup browser apapun yang terjadi
    print("Menutup Browser...")
    driver.quit()