from ninja import NinjaAPI

from auth_app.api import router as auth_router
from orders_app.api import router as orders_router

api = NinjaAPI()

api.add_router("/auth/", auth_router)  # You can add a router as an object
api.add_router("/orders/", orders_router)  # or by Python path
