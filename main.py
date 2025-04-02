from fastapi import FastAPI
import uvicorn
app=FastAPI(title="Basic Project to deploy docker image EC2 using github actions")

@app.get("/")
def new():
    return "I am Katta Sai Pranav Reddy"

if __name__=="__main__":
    uvicorn.run(app,host='0.0.0.0',port=8000)