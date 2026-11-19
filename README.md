# Parcial final - Grafos

**Nombre:** Jhonatan Pazos Rodríguez  
**Fecha:** 18/11/2026

## Parte 1. Interpretación del grafo

**1. Vértices:**

V = {1, 2, 3, 4, 5, 6}. El grafo tiene 6 vértices.

**2. Aristas:**

E = {(1,3), (1,2), (1,6), (3,5), (3,4), (5,4), (4,2), (4,6)}.

El grafo tiene 8 aristas.

**3. Tipo de grafo:** Es no dirigido porque sus conexiones no tienen flechas. Por tanto, cada arista puede recorrerse en ambos sentidos.

## Parte 2. Modelado de una situación real

**Situación propuesta:** Red de caminos peatonales entre seis lugares de una universidad. Cada lugar se representa con un vértice y cada camino directo mediante una arista.

| Vértice | Lugar representado |
|---|---|
| 1 | Entrada principal |
| 2 | Biblioteca |
| 3 | Bloque de salones |
| 4 | Cafetería |
| 5 | Laboratorio |
| 6 | Zona deportiva |

Los vértices representan los lugares de la universidad. Las aristas representan caminos directos entre ellos. Por ejemplo, la arista (1,3) indica un camino entre la entrada principal y el bloque de salones. Como los caminos permiten desplazarse en ambos sentidos, el grafo es no dirigido.

## Parte 3. Análisis y toma de decisiones

### Lista de adyacencia

| Vértice | Vecinos |
|---|---|
| 1 | 2, 3, 6 |
| 2 | 1, 4 |
| 3 | 1, 4, 5 |
| 4 | 2, 3, 5, 6 |
| 5 | 3, 4 |
| 6 | 1, 4 |

**Justificación:** El grafo tiene 6 vértices y 8 aristas, por lo que no todas las parejas de vértices están conectadas. La lista de adyacencia guarda únicamente los vecinos de cada vértice y resulta sencilla para recorrer los caminos disponibles. Una matriz de adyacencia de este grafo ocuparía 6 × 6 = 36 posiciones, incluso para las conexiones que no existen. La lista es práctica de implementar con un diccionario de Python o mediante NetworkX.

## Parte 4. Preguntas de análisis obligatorias

### 1. ¿Qué ventajas tiene un grafo dirigido frente a uno no dirigido?

Un grafo dirigido permite indicar el sentido de cada conexión. Es útil cuando una relación solo funciona en una dirección, como una calle de un solo sentido o una tarea que depende de otra. Así se representan con mayor precisión las restricciones de movimiento o de relación entre elementos.

### 2. ¿Qué problemas reales requieren grafos dirigidos y no dirigidos?

Los grafos dirigidos se utilizan para modelar calles de un solo sentido o una sola vía, flujos de trabajo y enlaces que permiten pasar de una página a otra sin garantizar el regreso. Los grafos no dirigidos se utilizan para representar caminos de doble sentido, amistades mutuas y conexiones físicas que pueden recorrerse en ambas direcciones.

## Sustentación

Elegí una red de caminos universitarios porque el dibujo muestra lugares conectados sin flechas. Identifiqué 6 lugares y ocho caminos, conservando exactamente las conexiones de la imagen. La lista de adyacencia permite saber con facilidad a qué lugares se puede llegar directamente desde cada punto.
