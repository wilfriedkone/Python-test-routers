from fastapi import FastAPI

#importing routers
import routers.router_students
import routers.router_auth
import routers.router_stripe

# Documentation
from documentation.description import api_description
from documentation.tags import tags_metadata

#api init (launch with uvicorn main:api --reload)
app = FastAPI( 
    title="Watches API",
    description=api_description,
    openapi_tags=tags_metadata, # tagsmetadata definit au dessus
    docs_url='/'
)

app.include_router(routers.router_students.router)
app.include_router(routers.router_auth.router)
app.include_router(routers.router_stripe.router)




