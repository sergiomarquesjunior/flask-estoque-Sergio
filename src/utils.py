from pathlib import Path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import  sqlalchemy as sa


def existe_esquema(app: Flask)-> bool:
# Se estivéssmos com um SGBD, poderíamos consultar os metadados para ver
# se o esquema do banco existe, com algo como (mariaDB)
# SELECT SCHEMA_NAME FROM INFORMATION_SCHEMA.SCHEMATA WHERE SCHEMA_NAME = '<nome>'
# No caso do SQLite, vamos apenas verificar se existe ou não o arquivo no
# sistema de arquivos
    nome_do_arquivo = Path(app.instance_path) / app.config.get('SQLITE_DB')
    if nome_do_arquivo.is_file():
        return True



        return False

def seeding(db: SQLAlchemy,):
    from src.models.usuario import User

    sentenca = sa.select(User).limit(1)
    rset = db.session.execute(sentenca).scalar_one_or_none()
    if rset is None:
        usuario = User()
        usuario.nome = "Administrador do Sistema"
        usuario.email = "admin@admin.com.br"
        usuario.set_password("admin")
        db.session.add(usuario)
        db.session.commit()