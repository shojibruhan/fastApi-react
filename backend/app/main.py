from fastapi import FastAPI, status
# from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List
# from .dataabase.data import CATEGORY_DEFINITIONS
from .dataabase.data import CATEGORY_DEFINITIONS, TEST_DATA, PRODUCT_DATABASE

app = FastAPI()



# origins= [
#     "http://localhost:5173"
# ]


# app.add_middleware(
#     CORSMiddleware,
#     allow_origins= origins,
#     allow_methods= ['*'],
#     allow_headers= ['*']
# )


@app.get("/")
def read_root():
    # data= PRODUCT_DATABASE.get(101)
    # response_data= {
    #     "name": data['name'],
    #     **data['fields']
    # }

    

    return PRODUCT_DATABASE

