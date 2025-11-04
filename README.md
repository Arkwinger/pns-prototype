# 📱 Phone Name System (PNS)

> A prototype "DNS for phone numbers" — mapping human-readable handles (like `@arkwinger`) to real phone numbers.

---

## 🌍 Live Demo

- **Frontend:** [https://arkwinger.github.io/pns-prototype/](https://arkwinger.github.io/pns-prototype/)
- **Backend API:** [https://pns-prototype.onrender.com/docs](https://pns-prototype.onrender.com/docs)

*(The backend uses FastAPI on Render — fully live and database-backed.)*

---

##  Features

✅ Register a username and link it to a real phone number  
✅ Resolve any number or handle to its mapped identity  
✅ Data persistence using SQLite (survives app restarts)  
✅ REST API built with **FastAPI**  
✅ Frontend hosted via **GitHub Pages**  
✅ Backend hosted via **Render**

---

##  Concept

Just like **DNS** maps IP addresses to domain names,  
**PNS** maps phone numbers to human-friendly handles.

Instead of seeing `+1-617-555-1234`, you’d see `@arkwinger`.

This could become a universal, privacy-friendly identity layer  
for messaging and caller identification.

---

##  Tech Stack

| Component | Technology |
|------------|-------------|
| Frontend | HTML, JavaScript, CSS (GitHub Pages) |
| Backend | FastAPI (Python) |
| Database | SQLite (via SQLAlchemy) |
| Hosting | Render |
| API Docs | Swagger UI (`/docs`) |

---

##  How to Use

1. Go to the frontend link above.  
2. Register your handle (e.g. `@arkwinger`) and phone number.  
3. Resolve a number or handle — the system instantly returns the mapping.  
4. Try it directly in the backend’s `/docs` interface if you prefer raw API testing.

---

##  Future Plans

- Add authentication for verified users  
- Global namespace for handles (prevent duplicates)  
- Custom domain (pns.io prototype)  
- Encrypted database and API tokens  
- SMS / phone integration for verification  

---

##  Credits

Built by **Arkwinger**  
Created as a prototype experiment for a modern identity layer between phone and web.

---

📦 *Repository:* [https://github.com/Arkwinger/pns-prototype](https://github.com/Arkwinger/pns-prototype)
