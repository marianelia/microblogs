from dotenv import load_dotenv
from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient
import uvicorn
from router import router
from hendler.event_hendlers import shutdown, startup

from loader.import_data import import_user_accounts, import_messages

load_dotenv()

app = FastAPI()
app.include_router(router)

app.add_event_handler("startup", startup)
app.add_event_handler("shutdown", shutdown)

'''
if __name__ == "__main__":
    import_user_accounts()
    import_messages()
'''

#if __name__ == "__main__":
#    uvicorn.run("main:app", host="0.0.0.0", port=8001, reload=True)
