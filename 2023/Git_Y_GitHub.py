# /*
#  * ¡Estoy de celebración! He publicado mi primer libro:
#  * "Git y GitHub desde cero"
#  * - Papel: mouredev.com/libro-git
#  * - eBook: mouredev.com/ebook-git
#  *
#  * ¿Sabías que puedes leer información de Git y GitHub desde la gran
#  * mayoría de lenguajes de programación?
#  *
#  * Crea un programa que lea los últimos 10 commits de este repositorio y muestre:
#  * - Hash
#  * - Autor
#  * - Mensaje
#  * - Fecha y hora
#  *
#  * Ejemplo de salida:
#  * Commit 1 (el más reciente) | 12345A | MoureDev | Este es un commit | 24/04/2023 21:00
#  *
#  * Se permite utilizar librerías que nos faciliten esta tarea.
#  */

import git
from datetime import datetime

def read_last_commits(repo_path, commits_number):
    repo = git.Repo(repo_path)
    commits = list(repo.iter_commits('main', max_count=commits_number))

    for i, commit in enumerate(commits, 1):
        hash_commit = commit.hexsha
        author = commit.author.name
        message = commit.message.strip().split('\n')[0]
        date = datetime.fromtimestamp(commit.committed_date).strftime('%d/%m/%Y %H:%M')

        print(f"Commit {i} | {hash_commit} | {author} | {message} | {date}")

entrance = input("Introduzca la ruta del repositorio: ")

read_last_commits(entrance, 10)





