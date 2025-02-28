Installation du projet :
1. Installer Python 3.8.10 -> https://www.python.org/downloads/release/python-3810/
2. Dans le répertoire racine du projet (tpnote), installer les modules manquants avec la commande 'pip install -r requirements.txt'


Pour exécuter les tests :
1. Ouvrir un terminal dans le répertoire racine (tpnote) du projet
2. Exécuter la commande 'python -m pytest ./src/tests/AdherentsTests.py ./src/tests/AuteursTests.py ./src/tests/EditeursTests.py ./src/tests/FormatsTests.py ./src/tests/LivresTests.py ./src/tests/ReservationsTests.py'


Commande pour avoir le % de coverage :
'python -m pytest ./src/tests/AdherentsTests.py ./src/tests/AuteursTests.py ./src/tests/EditeursTests.py ./src/tests/FormatsTests.py ./src/tests/LivresTests.py ./src/tests/ReservationsTests.py --cov=src'


Pour exécuter l'api web (adhérents seulement):
1. Se déplacer dans le répertoire 'src' du projet
2. Lancer Docker et exécuter 'docker compose up' pour initialiser la base de données
2. Executer la commande 'python -m flask --app app run'
3. Routes disponibles :
	- http://127.0.0.1:5000/adherents/ajouter (POST)
	- http://127.0.0.1:5000/adherents/all (GET)
	- http://127.0.0.1:5000/adherents/<code> (GET) -> remplacer '<code>' par le code adhérent (chaîne numérique de 5 caractères)


Détails supplémentaires :

En mode test, Database utilise une instance de MockHandler.
En mode application, elle utilise une instance de SqlHandler.
Le MockHandler permet de tester avec un jey de données provenant du répertoire 'config/database_filler'.
Le jeu de données n'est pas modifiable, donc les insert, update et delete n'ont pas d'effet.