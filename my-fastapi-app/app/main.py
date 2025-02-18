from fastapi import FastAPI

# Import the FastAPI class from the fastapi package and initialize a new FastAPI instance.
app = FastAPI()


# Define a GET endpoint that will return a simple welcome message. 
# Use the @app.get decorator to specify the route and the HTTP method.
@app.get("/") # this endpoint will respond to GET requests at the root URL path (/)
async def read_root(): # defines an asynchronous function named read_root that will handle incoming requests to this endpoint.
    return {"message": "Hello to my first FastAPI endpoint!"} # returns a JSON response

@app.get("/get-current-time")
async def get_current_time():
    return {"The current time is 3pm."}