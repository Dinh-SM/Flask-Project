# But du projet

Réaliser un code fonctionnel d'une application Web (un site).

Les objectifs suivants ont été atteints :

- Implémenter des requêtes GET/POST.
- Utiliser les patrons HTML Jinja, page de base.
- Implémenter PUT et DELETE.

# Rendu

Le rendu proposé est un site internet présentant des recettes de cuisine, permettant de les consulter, d'ajouter / modifier / supprimer des commentaires sur chacune des recettes et de lancer des recherches de recettes basées sur leur nom ou les ingrédients qu'elles contiennent.

# Exécution

## Configurer l'environnement

Pour configurer l'environnement de développement, exécutez les commandes suivantes dans le dépôt git que vous venez de consulter :

./do serve

Une fois le serveur local lancé, vous aurez alors l'indication de l'adresse à suivre dans un navigateur internet afin d'ouvrir la page d'accueil du site :

http://127.0.0.1:8000/

## Fonctionnalités :

Vous retrouverez sur la barre de navigation en haut à gauche de la page d'accueil trois pages accessibles :

- BIM-Couisine qui permet d'accéder à la page d'accueil du site : http://127.0.0.1:8000/. Elle contient deux sections présentant les recettes mises à l'honneur : Recettes de la semaine et Sélection 4BIM.
- Recettes qui permet d'accéder à la page présentant l'ensemble des recettes présentées sur le site : http://127.0.0.1:8000/recettes
- Contact qui permet d'accéder à la page de contact avec les différents moyens de contacter les gestionnaires du site : http://127.0.0.1:8000/contact

En haut à droite de la page se trouve l'outil de recherche du site. Vous pouvez entrer dans le champ de recherche tout ou partie du nom d'une recette ou d'un ingrédient. Cliquez ensuite sur l'icône à sa droite afin de lancer la recherche. Vous verrez alors toutes les recettes correspondant à votre recherche.

Vous pouvez cliquer sur une recette de votre choix, que ce soit sur la page d'accueil, de l'ensemble des recettes ou après une recherche (si l'élement recherché existe dans la base de données, sinon le résultat est une page mentionnant "Aucune recette trouvée"). Une fois la recette sélectionnée, vous accéderez à la page associée indiquant les ingrédients nécessaires, les quantités associées, les étapes de préparation ainsi qu'une section commentaires. Exemple de page : http://127.0.0.1:8000/recette/3

Vous pouvez ici ajouter un commentaire en indiquant un nom d'utilisateur puis le commentaire dans les champs prévus à cet effet, puis en cliquant sur "Soumettre le commentaire". Ce dernier est alors ajouté à la base de données et affiché.

Vous pouvez également modifier ou supprimer un commentaire existant. Pour ce faire, cliquez sur le commentaire en question puis modifiez le texte et cliquez sur "modifier" afin de valider la modification, ou alors cliquez sur "supprimer" pour l'éliminer.

Vous pouvez réinitialiser la base de données en allant sur l'adresse http://127.0.0.1:8000/reset

Une notification en haut de la page indique le succès de toute opération réalisée sur les commentaires.
