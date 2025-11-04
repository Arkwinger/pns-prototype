from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title="Phone Name System (PNS)")

# In-memory "database"
registry: Dict[str, str] = {}  # handle → phone
reverse_registry: Dict[str, str] = {}  # phone → handle

class Registration(BaseModel):
    handle: str
    phone: str


@app.post("/register")
def register_user(reg: Registration):
    if reg.handle in registry:
        raise HTTPException(status_code=400, detail="Handle already exists")
    if reg.phone in reverse_registry:
        raise HTTPException(status_code=400, detail="Phone already registered")

    registry[reg.handle] = reg.phone
    reverse_registry[reg.phone] = reg.handle
    return {"message": "Registered successfully", "handle": reg.handle, "phone": reg.phone}


@app.get("/resolve")
def resolve_number(number: str = None, handle: str = None):
    if number:
        handle = reverse_registry.get(number)
        if not handle:
            raise HTTPException(status_code=404, detail="Number not found")
        return {"phone": number, "handle": handle}

    elif handle:
        phone = registry.get(handle)
        if not phone:
            raise HTTPException(status_code=404, detail="Handle not found")
        return {"handle": handle, "phone": phone}

    else:
        raise HTTPException(status_code=400, detail="Provide a number or handle to resolve")
