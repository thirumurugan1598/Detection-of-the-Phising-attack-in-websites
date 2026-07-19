<div align="center">

# 🛡️ Phishing URL Detector

<img src="https://readme-typing-svg.demolab.com?font=Inter&weight=600&size=28&duration=3000&pause=1000&color=10A37F&center=true&vCenter=true&width=900&lines=Detect+Suspicious+URLs+Before+They+Become+Threats;Cybersecurity+%7C+Python+%7C+URL+Analysis;Heuristic-Based+Phishing+Detection;Built+for+Learning+and+Security"/>

<p align="center">

<img src="https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
<img src="https://img.shields.io/badge/Cybersecurity-Project-10A37F?style=for-the-badge"/>
<img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge"/>
<img src="https://img.shields.io/badge/License-MIT-blue?style=for-the-badge"/>

</p>

</div>

---

# 🚀 Overview

This project is a lightweight **Python-based phishing URL detector** that analyzes URLs using multiple heuristic techniques to identify potentially suspicious websites.

Instead of relying on external APIs, it evaluates several URL characteristics and assigns a **risk score** to determine whether a website appears **Low**, **Medium**, or **High** risk.

---

# ✨ Features

- 🔒 HTTPS Validation
- 🌐 IP Address Detection
- 📂 Suspicious Subdomain Detection
- 🔍 Phishing Keyword Analysis
- 📏 Long URL Detection
- 📊 Risk Score Calculation
- ⚠️ Threat Classification
- 📝 Human-readable Explanation

---

# ⚡ Detection Workflow

```text
               User URL
                  │
                  ▼
         URL Parsing Module
                  │
      ┌───────────┼────────────┐
      ▼           ▼            ▼
 HTTPS Check   IP Check   Keyword Scan
      │           │            │
      └───────────┼────────────┘
                  ▼
        Subdomain Analysis
                  │
                  ▼
         URL Length Check
                  │
                  ▼
         Risk Score Engine
                  │
                  ▼
   Low • Medium • High Risk
```

---

# 📊 Detection Techniques

| Check | Purpose |
|--------|---------|
| 🔒 HTTPS | Detects insecure websites |
| 🌐 IP Address | Finds URLs using raw IPs |
| 📂 Subdomains | Detects excessive subdomains |
| 🔍 Keywords | Finds phishing-related words |
| 📏 URL Length | Detects unusually long URLs |

---

# 🎯 Risk Levels

| Score | Level |
|--------|-------|
| 🟢 0–2 | Low Risk |
| 🟡 3–5 | Medium Risk |
| 🔴 6+ | High Risk |

---

# 🖥️ Technologies

<p align="center">

<img src="https://skillicons.dev/icons?i=python,vscode,git,github"/>

</p>

---

# 📁 Project Structure

```text
Phishing-URL-Detector/
│
├── phishing_detector.py
├── README.md
└── requirements.txt
```

---

# ▶️ Example

### Input

```python
detect_phishing("http://192.168.1.1/login/verify/account")
```

### Output

```text
Website:
http://192.168.1.1/login/verify/account

Risk Score: 8

⚠️ High Risk

Reasons:
• Website is not using HTTPS
• Uses IP Address
• Contains keyword login
• Contains keyword verify
• Contains keyword account
```

---

# 🛡️ Future Enhancements

- 🤖 Machine Learning Detection
- 🌍 Domain Reputation Lookup
- 🔐 SSL Certificate Validation
- 📜 WHOIS Analysis
- 🧠 AI-powered Classification
- 🌐 Streamlit Web Dashboard
- 🧩 Browser Extension
- ☁️ Threat Intelligence Integration

---

# 📈 Roadmap

```text
✔ URL Parsing

✔ HTTPS Check

✔ IP Detection

✔ Keyword Detection

✔ Risk Scoring

⬜ Machine Learning

⬜ Streamlit Dashboard

⬜ Browser Extension

⬜ Threat Intelligence
```

---

# 🤝 Contributing

Contributions are welcome!

1. Fork the repository
2. Create a new branch
3. Commit your changes
4. Submit a Pull Request

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

---

<div align="center">

<img src="https://readme-typing-svg.demolab.com?font=Inter&size=22&duration=3000&pause=1000&color=10A37F&center=true&vCenter=true&width=700&lines=Secure+Browsing+Starts+with+Awareness.;Stay+Safe.+Stay+Secure.;Happy+Coding!"/>

</div>
