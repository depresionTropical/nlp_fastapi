from fastapi import FastAPI, Request, Response, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from pymongo import MongoClient
from dotenv import dotenv_values
from handle_db import Database

config = dotenv_values(".env")

app = FastAPI()

template = Jinja2Templates(directory="./view")

@app.get("/",response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.post("/",response_class=HTMLResponse)
def root(req: Request):
    return template.TemplateResponse("index.html", {"request": req})

@app.get("/signup",response_class=HTMLResponse)
def signup(req: Request):
    return template.TemplateResponse("signup.html", {"request": req})

@app.get("/user",response_class=HTMLResponse)
def user(req: Request):
    return RedirectResponse(url="/", status_code=303)
    #return template.TemplateResponse("user.html", {"request": req})

@app.post("/user",response_class=HTMLResponse)
def user(req: Request):
    return "RedirectResponse(url="/", status_code=303)"
    #return template.TemplateResponse("user.html", {"request": req})

# Database
@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["ATLAS_URI"])
    app.database = app.mongodb_client[config["DB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()


# User
@app.post("/data-processing")
def data_processing(
    firstname: str=Form(),
    lastname: str=Form(),
    username : str=Form(),
    country: str=Form(),
    password_user: str=Form()
):
    db=Database()
    data_user = {
        "firstname": firstname,
        "lastname": lastname,
        "username": username,
        "country": country,
        "password_user": password_user
    }
    db.insert_one(data_user)
    return RedirectResponse(url="/", status_code=303)

