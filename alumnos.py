def alumnos():

    alumnos = []

    respuesta = True

    while respuesta:

        alumno = []

        alumno.append(input("Ingresa el nombre del alumno:\n"))
        alumno.append(float(input("Ingresa la primera nota:\n")))
        alumno.append(float(input("Ingresa la segunda nota:\n")))
        alumno.append(float(input("Ingresa la tercera nota:\n")))

        alumnos.append(alumno)

        respuesta = input("¿Desea ingresar otro alumno?\nIngrese s para si.\ningrese cualquier otra cosa para no")
        if respuesta == "s":
            respuesta = True
        else:
            respuesta = False



    if len(alumnos) > 0:
        print("Listado de la nota de los alumnos")
        print("Nombre\nNota1\nNota2\nNota3")
        for alumno in alumnos:
            print(alumno[0]+"\t"+str(alumno[1])+"\t\t"+str(alumno[2])+"\t\t"+str(alumno[3]))

    if len(alumnos) > 0:
        print("\nListado de los promedios de los alumnos")
        print("Nombre\nPromedio")
        for alumno in alumnos:
            promedio = (alumno[1]+alumno[2]+alumno[3])
            print(alumno[0]+"\t" +str(round(promedio,1)))