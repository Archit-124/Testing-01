from fastapi import FastAPI, Path
app=FastAPI()

college={
    1:{
        "name":"Archit",
        "age":"22",
        "roll":"01"
    },
    2:{
        "name":"Banti",
        "age":"43",
        "roll":"04"
    },
    3:{
        "name":"Sagar",
        "age":"34",
        "roll":"08"
    }
}

@app.get('/')
def index():
    return {"message":"Hello World"}

@app.get('/get-student/{student_id}')
def index(student_id:int = Path(None,description="Id of the student you want to View")):
    return college[student_id]