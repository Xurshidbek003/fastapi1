from fastapi import FastAPI
from routers.books import router as book_router
from routers.users import router as user_router
from routers.orders import router as order_router

app = FastAPI()

app.include_router(book_router, tags=["Books"], prefix="/books")
app.include_router(user_router, tags=["Users"], prefix="/users")
app.include_router(order_router, tags=["Orders"], prefix="/orders")