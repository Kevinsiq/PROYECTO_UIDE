# Aprendizaje No Supervisado: Segmentación de clientes con K-Means

## Descripción del Proyecto
Este proyecto implementa una arquitectura de **Business Intelligence** para categorizar a los clientes de una tienda online. A través de un análisis **RFM (Recency, Frequency, Monetary)**, el sistema identifica patrones de compra y agrupa a los usuarios en grupos.

## Tecnologías utilizadas
* **Lenguaje:** Python 3.x
* **Gestión de datos:** SQL (Extracción y transformación de métricas RFM)
* **Librerías utilizadas:** * `Pandas` & `NumPy`: Manipulación de datos.
    * `Scikit-learn`: Implementación de K-Means y escalado de datos.
    * `Matplotlib` & `Seaborn`: Visualización.
* **Documentación:** LaTeX: Informe técnico profesional.

## Metodología
1.  **Ingeniería de datos:** Conexión a base de datos local y consolidación de transacciones vía SQL.
2.  **Preprocesamiento:** Tratamiento de outliers, transformación logarítmica para corregir asimetría y normalización Z-score.
3.  **Modelado:** Aplicación de **K-Means** con validación mediante el **método del codo**.
4.  **Análisis de resultados:** Interpretación de los 3 clusters identificados (VIP, Potencial y Ocasional).



## Resultados Clave
* **Cluster VIP:** Clientes leales, recencia promedio de 13 días y alto gasto promedio en la tienda online.
* **Cluster Potencial:** Clientes con actividad moderada.
* **Cluster Ocasional:** Clientes con baja frecuencia y riesgo de abandono.



## Estructura del Repositorio
* `/notebooks`: Jupyter Notebook con el análisis completo de punta a punta.
* `/scripts`: Código Python para la integración con la base de datos SQL.
* `/docs`: Informe técnico final detallado (PDF).
* `/data`: Muestra de los datos utilizados o enlace a la fuente original.

## 👤 Autor
* **Kevin Iza** - [\[Perfil de LinkedIn\]](https://www.linkedin.com/in/keviniq/)