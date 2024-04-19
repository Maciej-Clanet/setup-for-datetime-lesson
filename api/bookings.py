from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import List

import datetime
import json

router = APIRouter()

#datetime weekday() function returns an index to represent a day, for example if you give it a date of 23/04/2024 it will return "1" for tuesday.
#The below list will allow us to quickly get the day name based on this index.
days = [ "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday" ,"Sunday"]

class BookAppointmentPayload(BaseModel):
    temp: int

class BookingConfirmation(BaseModel):
    temp: str

@router.post("/book", response_model=BookingConfirmation)
async def bookAppointment(data: BookAppointmentPayload):
    print("book appointment endpoint triggered")


    # tempDate = "19/04/2024" 
    # date = datetime.datetime.strptime(tempDate, '%d/%m/%Y')
    # day = days[date.weekday()]

    tempDate = "2024-04-19"  
    #this is the default format html date input field has, useful to use this format on the backend so you dont have to further format the date on the frontend.
    
    try:
        date = datetime.datetime.strptime(tempDate, '%Y-%m-%d')
         #the second argument is the format the date is given in
        #Notice the %Y is capitalised. It means it requires 4 digits, ex: 2024. If you use lowercase y, it will need 2 digits, ex: 24
    
    # except Exception as e:        #<<<< General way to catch exception, not very specific just catches all of them
    except ValueError:              #<<<< This will only catch Value Errors, datetime throws a value error i incorrect date is given. 
        #if there was an error in the code above, for example we received incorrect date format, instead of crashing the application we do the code in this except block
        raise HTTPException(400, detail="wrong date format")
     
   

    day = days[date.weekday()]
    #once we have the datetime object (date), we can access the weekday() functio  to get the day as an index.
    #We pass the index to our days array to convert it to name of the day


    return { "temp" : day}