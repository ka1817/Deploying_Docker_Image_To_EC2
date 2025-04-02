from fastapi import FastAPI
import uvicorn
app=FastAPI(title="Basic Project to deploy docker image EC2 using github actions")

@app.get("/")
def home():
    return "Hello World1" 

if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0',port=2000)