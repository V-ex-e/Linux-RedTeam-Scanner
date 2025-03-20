# 🔴 Linux Red Team Recon & Exploitation Toolkit

## 🚀 Overview
This toolkit automates **reconnaissance**, **vulnerability scanning**, and **exploit detection** for Red Team assessments on Linux systems.

✅ **System Recon** – Collects OS, kernel, users, processes, and network info  
✅ **Vulnerability Scanner** – Checks sudo permissions, world-writable directories  
✅ **Exploit Suggester** – Detects weak kernel versions & SUID binaries  
✅ **PDF Report Generator** – Saves all findings in an easy-to-read report  

---

## 📂 Folder Structure
```
📁 Linux-RedTeam-Scanner
 ├── 📄 recon.py         # Collects system & network info
 ├── 📄 vuln_scan.py     # Identifies misconfigurations
 ├── 📄 exploit_sugg.py  # Suggests privilege escalation exploits
 ├── 📄 report.py        # Generates a security report
 ├── 📄 setup.py         # Automates installation & execution
 ├── 📄 requirements.txt # Dependencies
```

---

## 📦 Installation & Usage
### 1️⃣ **Run the Automated Setup**
```bash
python setup.py
```
This will:
- Install dependencies
- Run reconnaissance, vulnerability scanning, and exploit detection
- Generate a **Red Team Report (redteam_report.pdf)**

### 2️⃣ **Manual Execution (Optional)**
```bash
pip install -r requirements.txt
```
Run each script separately:
```bash
python recon.py
python vuln_scan.py
python exploit_sugg.py
python report.py
```

---

## 🔍 Features
- **System Recon:** Collects OS, kernel, user, and network info  
- **Vulnerability Scan:** Detects weak permissions and misconfigurations  
- **Exploit Suggester:** Finds privilege escalation paths  
- **Automated Report:** Saves findings in a professional security report  

---

## 📜 Example Output
```
🔍 Gathering System Info...
  📌 OS: Linux
  📌 Kernel: 5.4.0-90-generic
  📌 User: root

🛡 Running Vulnerability Scan...
  ⚠ World-writable directories found: /tmp
  ⚠ Sudo misconfiguration detected: (ALL) NOPASSWD: ALL

💣 Suggested Exploits...
  🚀 Kernel version is vulnerable to DirtyCOW
  🚀 Found SUID binary: /usr/bin/passwd

📄 Report saved as redteam_report.pdf
```

---

## 🌟 Contributing
Want to improve the toolkit? Feel free to open an issue or submit a pull request!

---

## 📄 License
This project is licensed under the **MIT License**. Modify & use it freely!

---

🚀 **Let’s automate the recon!** 🔥
