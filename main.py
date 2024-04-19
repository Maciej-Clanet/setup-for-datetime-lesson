from fastapi import FastAPI, APIRouter
from api import bookings

app = FastAPI()

app.include_router(bookings.router, prefix="/bookings", tags=["bookings"] )

@app.get("/")
def read_root():
    return {"hello" : "goobers"}
