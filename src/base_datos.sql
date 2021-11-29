--creamos la base de datos
CREATE DATABASE bdpractica

-- verificamos que estemos utilizando la base de datos correcta
use bdpractica

--creamos la tabla empleado
CREATE TABLE empleado(
    id int NOT NULL PRIMARY KEY,
    nombre VARCHAR(30) NOT NULL,
    cargo VARCHAR(15) NOT NULL,
    salario int not NULL
)

--al campo id le agreamos unique para que los datos sean unicos 
alter table empleado 
ADD CONSTRAINT UQ_Constrai UNIQUE(id)

--insertamos algunos datos de prueba
INSERT into empleado VALUEs('1','david israel','recepcionista','1500')
INSERT into empleado VALUEs('2','david ','barredor','1500')

--ejecutamos e imprimos la tabla empleado
<