nombre = input('Ingrese el nombre del estudiante: ')

num_semestres = int(input('Ingrese el numero de semestres que desea ingresar: '))

promedios_semestres = []
notas_semestres = []    

for i in range (1, num_semestres, 1):
    num_evaluaciones = int(input('Ingrese el numero de evaluaciones del semestre: '))
    
    for n in range (1, num_evaluaciones, 1):
        nota = float(input('Ingrese la nota de la evaluacion: '))
        notas_semestres.append(nota)
        
    promedio_semestre = sum(notas_semestres) / len(notas_semestres)
    promedios_semestres.append(promedio_semestre)
    
