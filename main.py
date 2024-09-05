from fastapi import FastAPI
from db.conexion import Base, engine
from starlette.responses import RedirectResponse
from routes import usuarios, auth_usuarios, materias, estudiantes, matriculas

# Crear todas las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI(
    responses={404: {"Mensaje": "No encontrado"}}
)

# Routers
app.include_router(usuarios.router)
app.include_router(auth_usuarios.router)
app.include_router(materias.router)
app.include_router(estudiantes.router)
app.include_router(matriculas.router)

@app.get("/")
def main():
    "Redireccionamiento a la documentación de la API"
    return RedirectResponse(url="/docs/")