from fastapi import FastAPI
from routes.clientRouter import router as client_router
from routes.pedidoRouter import router as pedido_router
from routes.productoRouter import router as producto_router
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="API Simple Supabase",
    description="API para gestión de clientes, productos y pedidos",
    version="1.0.0"
)

# Configurar CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Incluir routers
app.include_router(client_router, prefix="/api", tags=["Clientes"])
app.include_router(pedido_router, prefix="/api", tags=["Pedidos"])
app.include_router(producto_router, prefix="/api", tags=["Productos"])

@app.get("/")
async def root():
    return {
        "message": "API funcionando correctamente", 
        "docs": "/docs",
        "endpoints": {
            "clientes": "/api/obtener_clientes",
            "productos": "/api/obtener_productos",
            "pedidos": "/api/obtener_pedidos"
        }
    }

@app.get("/health")
async def health_check():
    return {"status": "healthy", "message": "API is running"}

# Para Vercel
app = app