# SauceDemo E-Commerce - QA Manual Testing Portfolio

## Project Overview
Repository ini berisi dokumentasi pengujian manual (Manual Testing artifacts) untuk website e-commerce **[SauceDemo (Swag Labs)](https://www.saucedemo.com/)**.

Project ini dibuat sebagai demonstrasi kemampuan saya dalam:
- Menganalisis kebutuhan sistem dan membuat Skenario Pengujian.
- Menulis **Test Case** yang detail (Positif & Negatif).
- Melakukan eksekusi tes (Test Execution).
- Melaporkan bug (**Bug Reporting**) dengan standar industri.

## 🛠 Tools & Environment
| Category | Tool Used |
| :--- | :--- |
| **Testing Type** | Manual Testing (Black Box) |
| **Test Management** | Microsoft Excel (Spreadsheet) |
| **Browser** | Google Chrome |
| **SUT (Site Under Test)** | https://www.saucedemo.com/ |

## Repository Structure
Berikut adalah penjelasan file yang ada di repository ini:

- **`Test_Cases_SauceDemo.xlsx`**
  Berisi langkah-langkah pengujian detail (Step-by-step), Test Data, dan hasil eksekusi (Pass/Fail) untuk fitur Login.
  - *Coverage:* Valid Login, Locked Out User, Invalid Credentials.

- **`Bug_Report_SauceDemo.xlsx`**
  Laporan temuan bug saat melakukan eksplorasi menggunakan `problem_user`.
  - *Highlight:* Isu tampilan gambar produk (Broken Image) pada halaman Inventory.

## Test Scenarios Highlight
Berikut adalah ringkasan skenario yang telah diuji:

### 1. Login Module
- ✅ **TC-LOG-001:** Verifikasi login sukses dengan user valid (`standard_user`).
- ✅ **TC-LOG-002:** Verifikasi validasi error untuk user yang terkunci (`locked_out_user`).
- ✅ **TC-LOG-003:** Verifikasi keamanan login dengan password yang salah.

### 2. Bug Findings (Temuan Bug)
- **BUG-INV-001:** Gambar produk pada item pertama tidak muncul (menampilkan placeholder anjing) saat login menggunakan `problem_user`. Severity: *Low/Cosmetic*.

---
### Author
Project ini dikerjakan oleh **MasFab**.
Terbuka untuk diskusi terkait QA dan Software Testing.
