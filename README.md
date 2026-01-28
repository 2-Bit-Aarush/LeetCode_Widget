# 📊 LeetCode Stats Widget (Automated)

A minimal Android home-screen widget that automatically tracks my LeetCode progress using GitHub Actions and displays it in real time using KWGT.

This project focuses on **automation, clean data flow, and passive consistency tracking** rather than manual updates.

---

## 🚀 Features

- 📈 Automatically fetches LeetCode problem stats (Easy / Medium / Hard / Total)
- 🔄 Daily auto-update using GitHub Actions (no manual intervention)
- 📱 Custom Android widget built with KWGT
- 🧩 Clean, minimal UI that adapts well to dark themes
- ☁️ Uses GitHub as a stable data layer (JSON)

---



## 🛠️ Tech Stack

- Python (GraphQL API)
- GitHub Actions (CI/CD automation)
- GitHub Raw Content (JSON hosting)
- KWGT (Android widget framework)

---

## 📱 Widget Preview

> Screenshot of the live widget on home screen  
![LeetCode Widget Preview](widget-preview.jpeg)

---

## 🔁 How It Updates

- Stats are fetched automatically once per day
- Widget refreshes by pulling the updated JSON
- Manual refresh possible via GitHub Actions or KWGT

---

## 🎯 Why This Project

I wanted a way to:
- Track consistency without opening dashboards
- Practice real-world automation (CI/CD + data flow)
- Build something small but **actually useful**

---

## 🔮 Future Improvements

- Add streak tracking
- Track daily deltas
- Material You adaptive theming
- README auto-badges

---

Built for learning, consistency, and clean engineering.
