class RescateDatosCriticos:
    def __init__(self):
        # Definición de tareas con duración (minutos)
        self.tareas = {
            'A': {'desc': 'Identificar servidores afectados', 'duracion': 15, 'dep': []},
            'B': {'desc': 'Priorizar datos críticos', 'duracion': 20, 'dep': ['A']},
            'C': {'desc': 'Activar protocolo de recuperación', 'duracion': 10, 'dep': ['A']},
            'D': {'desc': 'Asignar técnicos a servidores', 'duracion': 5, 'dep': ['B', 'C']},
            'E': {'desc': 'Recuperar datos de servidor 1', 'duracion': 30, 'dep': ['D']},
            'F': {'desc': 'Recuperar datos de servidor 2', 'duracion': 25, 'dep': ['D', 'E']},  # Solo uno a la vez
            'G': {'desc': 'Validar integridad de datos recuperados', 'duracion': 15, 'dep': ['E', 'F']},
            'H': {'desc': 'Generar informe preliminar para dirección', 'duracion': 10, 'dep': ['G']},
            'I': {'desc': 'Comunicar a clientes afectados', 'duracion': 20, 'dep': ['G']},
            'J': {'desc': 'Coordinar con equipo legal', 'duracion': 15, 'dep': ['G']},
            'K': {'desc': 'Preparar plan de contingencia', 'duracion': 25, 'dep': ['G']}
        }
        self.tecnicos_disponibles = 3
        self.tiempo_limite = 120

    def objetivo_proyecto(self):
        return ("Rescatar los datos médicos más críticos en 120 minutos, "
                "optimizando recursos y asegurando comunicación efectiva.")

    def diagrama_flujo(self):
        # Representación simple de dependencias
        print("Diagrama de flujo de tareas y dependencias:")
        for clave, tarea in self.tareas.items():
            print(f"Tarea {clave}: {tarea['desc']} (depende de: {', '.join(tarea['dep']) or 'ninguna'})")

    def nivelacion_recursos(self):
        print(f"Técnicos disponibles: {self.tecnicos_disponibles}")
        print("Solo se puede recuperar datos de un servidor a la vez.")
        print("Asignación óptima: Un técnico por servidor, el resto apoya en validación y comunicación.")

    def plan_comunicacion(self):
        print("Plan de comunicación de crisis:")
        print("- Informe preliminar a dirección tras validación de datos.")
        print("- Comunicación a clientes afectados tras validación.")
        print("- Coordinación con equipo legal y preparación de contingencia.")

    def cronograma(self):
        tiempo = 0
        secuencia = []
        # Simulación simple de ejecución secuencial y dependencias
        completadas = set()
        while len(completadas) < len(self.tareas):
            for clave, tarea in self.tareas.items():
                if clave not in completadas and all(dep in completadas for dep in tarea['dep']):
                    secuencia.append((clave, tarea['desc'], tiempo, tiempo + tarea['duracion']))
                    tiempo += tarea['duracion']
                    completadas.add(clave)
        print("Cronograma estimado de ejecución:")
        for clave, desc, inicio, fin in secuencia:
            print(f"{clave}: {desc} | Inicio: {inicio} min | Fin: {fin} min")

if __name__ == "__main__":
    rescate = RescateDatosCriticos()
    print("Objetivo del Proyecto:")
    print(rescate.objetivo_proyecto())
    print("\n---")
    rescate.diagrama_flujo()
    print("\n---")
    rescate.nivelacion_recursos()
    print("\n---")
    rescate.plan_comunicacion()
    print("\n---")
    rescate.cronograma()