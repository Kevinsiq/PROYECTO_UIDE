# Librerías necesarias
import pandas as pd
from sqlalchemy import create_engine

# Conexión a SQL
def conectar_db():
    try:
        # Creamos el motor de conexión para SQLite
        engine = create_engine('sqlite:///data/proyecto_pyme.db')
        return engine
    except Exception as e:
        print(f"Error de conexión: {e}")
        return None

# Cargar excel 
def cargar_y_limpiar_datos():
    print("Cargando excel")
    # Leemos el archivo local
    df = pd.read_excel('data/Online_Retail.xlsx')

    # Limpieza de base: eliminamos nulos en CustomerID y convertimos a INT
    df = df.dropna(subset=['CustomerID'])
    df['CustomerID'] = df['CustomerID'].astype(int)

    # Solo ventas reales:
    df = df[df['Quantity'] > 0]
    
    return df

# Procesamos
def ejecutar_proceso():
    engine = conectar_db()
    
    if engine:
        df_ventas = cargar_y_limpiar_datos()
        print(f"Archivo procesado")
        
        print("Exportando a tabla SQL")
        # Guardamos en la base de datos
        df_ventas.to_sql('ventas_pyme', engine, if_exists='replace', index=False)
        
        print("¡Proceso completado con éxito!")

if __name__ == "__main__":
    ejecutar_proceso()