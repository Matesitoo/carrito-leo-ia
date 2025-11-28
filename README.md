# API Carrito + Supabase + Vercel

API simple para gestion de clientes, productos y pedidos construida con FastAPI, desplegada en Vercel y usando Supabase como base de datos.

## Caracteristicas

- **FastAPI** - Framework moderno y rapido
- **Supabase** - Base de datos PostgreSQL en la nube
- **Vercel** - Plataforma de deployment
- **CORS habilitado** - Para consumo desde frontends

## Endpoints

### Clientes
- `GET /api/obtener_clientes`
- `GET /api/obtener_cliente/{id}`
- `POST /api/crear_cliente`
- `PUT /api/modificar_cliente/{id}`
- `DELETE /api/eliminar_cliente/{id}`

### Productos
- `GET /api/obtener_productos`
- `POST /api/crear_productos`
- `PUT /api/modificar_producto/{id}`
- `DELETE /api/eliminar_producto/{id}`

### Pedidos
- `GET /api/obtener_pedidos`
- `GET /api/obtener_pedido/{id}`
- `POST /api/crear_pedido`
- `GET /api/obtener_pedido_por_cliente/{cliente_id}`
- `GET /api/total_por_pedido/{pedido_id}`
- `GET /api/filtrar_pedido_por_cliente/{cliente_id}`
