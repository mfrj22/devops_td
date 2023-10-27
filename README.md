[![Python application](https://github.com/mfrj22/devops_td/actions/workflows/python-app.yml/badge.svg)](https://github.com/mfrj22/devops_td/actions/workflows/python-app.yml)
[![license: Apache 2.0](https://img.shields.io/badge/license-Apache_2.0-green)](LICENSE)

[![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=mfrj22_devops_td&metric=reliability_rating)](https://sonarcloud.io/summary/new_code?id=mfrj22_devops_td)
[![Duplicated Lines (%)](https://sonarcloud.io/api/project_badges/measure?project=mfrj22_devops_td&metric=duplicated_lines_density)](https://sonarcloud.io/summary/new_code?id=mfrj22_devops_td)
[![Vulnerabilities](https://sonarcloud.io/api/project_badges/measure?project=mfrj22_devops_td&metric=vulnerabilities)](https://sonarcloud.io/summary/new_code?id=mfrj22_devops_td)
[![Bugs](https://sonarcloud.io/api/project_badges/measure?project=mfrj22_devops_td&metric=bugs)](https://sonarcloud.io/summary/new_code?id=mfrj22_devops_td)
[![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=mfrj22_devops_td&metric=security_rating)](https://sonarcloud.io/summary/new_code?id=mfrj22_devops_td)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=mfrj22_devops_td&metric=sqale_rating)](https://sonarcloud.io/summary/new_code?id=mfrj22_devops_td)
[![Code Smells](https://sonarcloud.io/api/project_badges/measure?project=mfrj22_devops_td&metric=code_smells)](https://sonarcloud.io/summary/new_code?id=mfrj22_devops_td)
[![Lines of Code](https://sonarcloud.io/api/project_badges/measure?project=mfrj22_devops_td&metric=ncloc)](https://sonarcloud.io/summary/new_code?id=mfrj22_devops_td)
[![Technical Debt](https://sonarcloud.io/api/project_badges/measure?project=mfrj22_devops_td&metric=sqale_index)](https://sonarcloud.io/summary/new_code?id=mfrj22_devops_td)

# Rendu

Ce projet est composé de 2 types de tests unitaires ayant des structures différentes :
- 1 fichier code + 1 fichier test
- 1 fichier regroupant code et test

## Installations

### Python 
Assurez-vous d'avoir Python installé sur votre machine avec une version compatible (Python 3.12 ou supérieur recommandé). Vous pouvez vérifier si Python est installé en exécutant `python --version` dans votre terminal. 
Dans le cas où Python n'est pas installé, vous pouvez le faire en suivant les instructions sur le site officiel de Python : [Installation de Python](https://www.python.org/downloads/).

### Pytest
Pytest est un framework de tests Python, il peut être utilisé pour écrire divers types de tests logiciels, notamment des tests unitaires.
Vous pouvez installer Pytest en lançant votre terminal de commande puis en entrant cette ligne de commande :

```
pip install -U pytest
```

 Vous pouvez vérifier si pytest est installé en exécutant `pytest --version` dans votre terminal.

 ## Utilisation des fonctions de test
Afin de pouvoir tester les fonctions, vous pouvez ouvrir un terminal depuis la racine de votre projet puis effectuer les commandes suivantes :

```
cd tests
pytest
```

Après avoir lancer vos différents tests, vous obtiendrez cet aperçu :

collected 2 items                                                                                                    

tests\test_helloworld.py .                                                                                    [ 50%] 
tests\test_sample.py .                                                                                        [100%] 

================================================ 2 passed in 0.02s =================================================

Le [100 %] fait référence à la progression globale de l'exécution de tous les scénarios de test. 
Dans notre cas, nous pouvons remarquer que nos deux tests ont été validés ("2 passed").

## Descriptions des fonctions

### helloword.py
#### hello()

Cette fonction retourne "Hello Khaoula !".

### test_helloworld.py
#### test_hello()
Cette fonction appelle la fonction "hello()" et vérifie qu'elle retourne bien "Hello Khaoula !" grâce à une assertion.

### test_sample.py
#### func(x)
Cette fonction prend en entrée un entier et l'incrémente de 1. Elle retourne le résultat de l'addition.
#### test_answer()
Cette fonction appele la fonction "func(3)" et vérifie que le résultat est 4. (3+1=4)

---

**L'équipe Devops**
