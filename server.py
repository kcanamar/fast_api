
# * Import dependencies
from fastapi import FastAPI
import uvicorn
# * Import the Router
from controllers import routes

# * Create the App object
app = FastAPI()

# * Mount the router
app.include_router(routes)

# * Create Server Listener
uvicorn.run(app, port=4000)