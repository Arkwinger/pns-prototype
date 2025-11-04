from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
import sqlite3

app = FastAPI(title="Phone Name System (PNS)")

# --- Enable CORS ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # allow all for now (frontend, etc.)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- SQLite setup ---
# Use Render’s persistent path so the database survives restarts/redeploys
DB_PATH = "/opt/render/project/src/pns.db"
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS registry (
    handle TEXT PRIMARY KEY,
    phone TEXT UNIQUE
)
""")
conn.commit()

# --- Data Model ---
class Registration(BaseModel):
    handle: str
    phone: str

# --- Register Endpoint ---
@app.post("/register")
def register_user(reg: Registration):
    try:
        cursor.execute(
            "INSERT INTO registry (handle, phone) VALUES (?, ?)",
            (reg.handle, reg.phone)
        )
        conn.commit()
        return {
            "message": "Registered successfully",
            "handle": reg.handle,
            "phone": reg.phone
        }
    except sqlite3.IntegrityError as e:
        if "UNIQUE constraint failed: registry.handle" in str(e):
            raise HTTPException(status_code=400, detail="Handle already exists")
        elif "UNIQUE constraint failed: registry.phone" in str(e):
            raise HTTPException(status_code=400, detail="Phone already registered")
        else:
            raise HTTPException(status_code=500, detail="Database error")

# --- Resolve Endpoint ---
@app.get("/resolve")
def resolve_number(number: str = None, handle: str = None):
    if number:
        cursor.execute("SELECT handle FROM registry WHERE phone=?", (number,))
        row = cursor.fetchone()
        if row:
            return {"phone": number, "handle": row[0]}
        raise HTTPException(status_code=404, detail="Number not found")

    elif handle:
        cursor.execute("SELECT phone FROM registry WHERE handle=?", (handle,))
        row = cursor.fetchone()
        if row:
            return {"handle": handle, "phone": row[0]}
        raise HTTPException(status_code=404, detail="Handle not found")

    else:
        raise HTTPException(status_code=400, detail="Provide a number or handle to resolve")

# --- Root Route (Friendly Homepage) ---
@app.get("/")
def root():
    return {
        "message": "📱 Welcome to the Phone Name System API!",
        "endpoints": {
            "Register": "/register",
            "Resolve": "/resolve",
            "Docs": "/docs"
        }
    }
