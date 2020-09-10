-- este scrip lo copiamos y lo ejecutamos en la hoja de sql phadmin.
CREATE DATABASE IF NOT EXISTS master_python;
USE master_python;

CREATE TABLE USUARIOS(
    ID INT(25) AUTO_INCREMENT NOT NULL,
    NOMBRE VARCHAR(100),
    APELLIDOS VARCHAR(255),
    EMAIL VARCHAR(255) NOT NULL,
    PASSWORD VARCHAR(255) NOT NULL,
    FECHA DATE NOT NULL,
    CONSTRAINT PK_USUARIOS PRIMARY KEY(ID),
    CONSTRAINT UQ_EMAIL UNIQUE(EMAIL)
)ENGINE=InnoDb;

CREATE TABLE NOTAS(
    ID INT(25) AUTO_INCREMENT NOT NULL,
    USUARIO_ID INT(25) NOT NULL,
    TITULO VARCHAR(255) NOT NULL,
    DECRIPCION MEDIUMTEXT,
    FECHA DATE NOT NULL,
    CONSTRAINT PK_NOTAS PRIMARY KEY(ID),
    CONSTRAINT FK_NOTA_USUARIO FOREIGN KEY (USUARIO_ID) REFERENCES USUARIOS(ID)

)