from flask import Flask,request
from db import stores,items
import uuid
from flask_smorest import abort

app = Flask(__name__)


app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///data.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


@app.post("/store")
def addStoreDetail():

    store_data = request.get_json()
     
    if "name" not in store_data:
        abort(400, message="Bad request. Payload does not contain the name")
    

    for store in stores.values():
        if store_data["name"] == store["name"]:
            return {"message": "Store Name already exists"}
        
    
    store_id = uuid.uuid4().hex
    store = {**store_data, "id":store_id}
    stores[store_id] = store
    
    return {"message":"values stored"}



@app.get("/store")
def getStoreList():
    return {"stores": list(stores.values())}


@app.get("/store/<store_id>")
def getStoreId(store_id):
    try:
        return stores[store_id]
    except KeyError:
        return {"message" : "Mentioned Store Id does not exists"}


@app.delete("/store/<store_id>")
def deleteStoreId(store_id):
    try:
        del stores[store_id]
    except KeyError:
        return   {"message" : "Mentioned Store Id deleted"}
    

    

     

    # return {"message":"values stored"}

@app.post("/item")
def createItems():
    item_data = request.get_json()

    if ("name" not in item_data 
        or "price" not in item_data 
        or "store_id" not in item_data) :
        abort(400, message="Bad Request. Payload does not contains name or price or store_id")


    if item_data["store_id"] not in stores:
        return {"message" : "store id does not exist"}


    item_id = uuid.uuid4().hex
    item = {**item_data, "id":item_id}
    items[item_id] = item

    return {"message": "Item Saved"}


@app.get("/item")
def getitemlist():
    return {"items" : list(items.values())}
    

@app.get("/item/<string:item_id>")
def getspecificitem(item_id):
    try:
        return items[item_id]
    except KeyError:
        return {"message": "item does not exists"}



@app.delete("/item/<string:item_id>")
def deletespecificitem(item_id):
    try:
        del stores[item_id]
        return {"message" : "Mentioned Item deleted"}
    except KeyError:
        return   {"message" : "Mentioned Item Id does not exist"}
    

@app.put("/item/<string:item_id>")
def updatespecificitem(item_id):
    item_data = request.get_json()

    if ("name" not in item_data 
        or "price" not in item_data ) :
        abort(400, message="Bad Request. Payload does not contains name or price")

    if (item_id not in items):
        return {"message" : "id does not exists"}

    item = items[item_id]
    item |= item_data

    return {"message": "Item value is updated"}

      
