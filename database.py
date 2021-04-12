import json

def get_recipes():
	jsonFile = open("./data.json")
	jsonString = jsonFile.read()
	recette = json.loads(jsonString)
	return recette[:-1]

def get_recipe(requested_id):
	jsonFile = open("./data.json")
	jsonString = jsonFile.read()
	recette = json.loads(jsonString)

	for recipe in recette:
		if recipe["id"] == int(requested_id):
			return recipe

def add_comment(recipe_id, new_comment):
	jsonFile = open("./data.json")
	jsonString = jsonFile.read()
	recette = json.loads(jsonString)

	for recipe in recette:
		if recipe["id"] == int(recipe_id):

			already_in = False
			for comment in recipe["comments"]:
				if comment['author'] == new_comment['author'] and comment['date'] == new_comment['date'] and comment['content'] == new_comment['content']:
					already_in = True

			if not already_in:
				recipe["comments"].append(new_comment)
				with open('data.json', 'w') as outfile:
					json.dump(recette, outfile)

def edit_comment(recipe_id, edited_comment, old_date, old_content):
	jsonFile = open("./data.json")
	jsonString = jsonFile.read()
	recette = json.loads(jsonString)

	for recipe in recette:
		if recipe["id"] == int(recipe_id):

			for comment in recipe["comments"]:
				if comment['author'] == edited_comment['author'] and comment['date'] == old_date and comment['content'] == old_content:
					comment['date'] = edited_comment['date']
					comment['content'] = edited_comment['content']
					with open('data.json', 'w') as outfile:
						json.dump(recette, outfile)

def delete_comment(recipe_id, deleted_comment):
	jsonFile = open("./data.json")
	jsonString = jsonFile.read()
	recette = json.loads(jsonString)

	for recipe in recette:
		if recipe["id"] == int(recipe_id):

			for comment in recipe["comments"]:
				if comment['author'] == deleted_comment['author'] and comment['date'] == deleted_comment['date'] and comment['content'] == deleted_comment['content']:
					recipe["comments"].remove(deleted_comment)
					with open('data.json', 'w') as outfile:
						json.dump(recette, outfile)

def reset_database():
	recette1 = {
		"id": 1,
		"name": "Couscous Républicain",
		"type": "Plat",
		"ingredients": [
			"Semoule",
			"Agneau",
			"Poulet",
			"Courgettes",
			"Aubergines",
			"Carottes",
			"Oignons",
			"Pois chiche",
			"Tomates",
			"Beurre concassé",
			"Ras-el-hanout",
			"Cumin moulu",
			"Huile d'olive",
			"Ail"
		],
		"quantities": [
			"200 g (moyenne)",
			"400 g de collier",
			"400 g de cuisses",
			"2",
			"0,5",
			"2",
			"1",
			"100 g",
			"100 g",
			"15 g",
			"1 cuil. à soupe",
			"0,5 cuil. à soupe",
			"2 cuil. à soupe",
			"1 gousse"
		],
		"preparation": [
			"Dans une grande cocotte, faites chauffer l'huile d'olive. Saisissez de chaque côté les  cuisses de poulet et les morceaux de collier d'agneau. Salez et poivrez, puis retirez-les de la cocotte.",
			"Emincez les oignons, faites-les blondir dans la cocotte à la place de la viande. Salez et parsemez d'épices.",
			"Coupez les aubergines, les carottes et les courgettes en cubes, faites-les colorer avec les oignons. Ajoutez les tomates concassées et l'ail haché puis remettez la viande dans la cocotte. Couvrez d'eau à hauteur et portez à frémissements 45 min.",
			"Ajoutez les pois chiches égouttés, poursuivez la cuisson 15 min.",
			"Faites griller les merguez dans une poêle antiadhésive.",
			"Mouillez la semoule dans la moitié de son volume d'eau. Égrenez la semoule, ajoutez une cuillère d’huile d’olive, mélangez puis passez à la vapeur pendant 10 minutes. Répéter l’opération une fois. Ajoutez de l’huile d’olive à votre convenance.",
			"Servez le couscous accompagné de semoule et de merguez chaudes."
		],
		"image": "couscous.jpeg",
		"comments": [
			{
				"author": "Gerald_de_manin",
				"date": "01-04-1793",
				"content": "Super couscous royal, vive la monarchie"
			}
		]
	}

	recette2 = {
		"id": 2,
		"name": "Merguez à la graisse de pneu",
		"type": "Plat",
		"ingredients": [
			"Graisse de pneu",
			"Merguez"
		],
		"quantities": [
			"10 cl",
			"500 g"
		],
		"preparation": [
			"Déclarez votre mouvement de grève aux camarades",
			"Dans le feu de l’action, brûler des pneus et récupérer la graisse (la séquestration de votre propriétaire des moyens de production est facultatif à cette étape).",
			"Au stand des camarades préparez un feu dans un barbecue improvisé sur ce que vous trouvez",
			"Alimentez le feu avec la graisse","Faites carboniser vos merguez à votre convenance"
		],
		"image": "merguez.jpeg",
		"comments": [
			{
				"author": "Philou_m",
				"date": "01-05-2021",
				"content": "Super merguez camarade rien de mieux qu’une guezmer pour remobiliser les troupes"
			}
		]
	}

	recette3 = {
		"id": 3,
		"name": "Poulet braisé à la grecque",
		"type": "Plat",
		"ingredients": [
			"Poulet",
			"Huile d'olive",
			"Oignons",
			"Vin blanc sec",
			"Sel",
			"Poivre",
			"Paprika",
			"Citron",
			"Feta (fromage)",
			"Persil"
		],
		"quantities": [
			"1",
			"1/2 tasse",
			"2",
			"1 tasse",
			"à envie",
			"à envie",
			"4 cuil. à café",
			"1",
			"400 g",
			"5-6 cuil. à soupe"
		],
		"preparation": [
			"Faire chauffer l'huile d'olive et le poulet brun tout autour. Ajouter l'oignon râpé et remuer les faire frire et, en remuant de temps pour éviter le brunissement.",
			"Ajouter le vin et réduire la chaleur. Couvrez la casserole et laisser le sigomageireftei de poulet. Maintenant, puis le contrôle. Si le liquide réduit moins, ajouter un peu d'eau.",
			"Lorsque le poulet est prêt, ajouter le jus de citron, sel, poivre et paprika. Faire cuire 2 - 3 minutes. Ajouter le fromage et le persil et retirer du feu.",
			"Servir chaud, avec du riz bouilli ou des pommes de terre. "
		],
		"image": "Poulet_grec.jpeg",
		"comments": [
			{
				"author": "Aléxis_Pírate",
				"date": "25-12-2010",
				"content": "Super recette, ingrédients un peu chers"
			}
		]
	}

	recette4 = {
		"id": 4,
		"name": "Lasagnes aux légumes non végé",
		"type": "Plat",
		"ingredients": [
			"Courgettes",
			"Aubergines",
			"Sauce tomate",
			"Concentré de tomate",
			"Oignons",
			"Poivre",
			"Huile d'olive",
			"Viande de boeuf hâchée",
			"Lasagnes sèches (en feuille)",
			"Farine",
			"Beurre",
			"Lait"
		],
		"quantities": [
			"3",
			"2",
			"1 pot",
			"1 pot",
			"à envie",
			"du",
			"2 cuil. à soupe",
			"400 g",
			"(feuilles)",
			"50 g",
			"50 g",
			"60 cl"
		],
		"preparation": [
			"Faire la sauce tomate. Emincer finement l'ail et l'oignon. Les faire revenir dans une casserole avec un peu d'huile d'olive. Ajouter un fond de vin blanc. Après 2 minutes de cuisson, ajouter les herbes, puis les tomates concassées et le concentré de tomates. Ajouter 2 cuillères à café de sucre. Saler et poivrer. Laisser mijoter environ 1 heure à feu doux, avec un couvercle. La sauce doit rester assez liquide.",
			"Laver les aubergines. Les couper en petits dés. Peler et couper en dés les courgettes.",
			"Dans une sauteuse, faire revenir les aubergines avec quelques cuillères d'huile d'olive, jusqu'à ce qu'elles soient bien cuites. Saler et poivrer.",
			"Préparation de la béchamel : Faites fondre le beurre dans une casserole à fond épais. Ajoutez la farine et remuez avec une cuillère de bois sans laisser colorer. La farine doit juste épaissir. Versez le lait progressivement, sans cesser de remuer, jusqu'à ce que la sauce épaississe. Assaisonnez de sel et poivre.",
			"Dans un plat à gratin, déposer une louche de sauce tomates et une demi-louche de béchamel. Etaler. Déposer les feuilles de lasagnes. Déposer ensuite dessus les aubergines, puis une autre louche de sauce tomates et une demi-louche de béchamel. Couvrir de feuilles de lasagnes. Dans la même sauteuse, faire cuire la viande hachée émiettée jusqu'à ce qu'elle soit bien asséchée. Saler et poivrer. Dans le plat, déposer la viande, puis les poivrons en lanières. Couvrir de feuilles de lasagnes.",
			"Dans la sauteuse, faire revenir les dés de courgettes avec un peu d'huile d'olive. Elles doivent être bien tendres. Les déposer dans le plat à gratin. Recouvrir de la moitié de la sauce tomate restante. Recouvrir de feuilles de lasagnes.",
			"Finir en couvrant de la sauce restante puis de fromage râpé. Mettre sous film et laisser reposer 2 heures ou mieux, une nuit au frais. Enlever le film. Déposer des noisettes de beurre sur le dessus, et enfourner 35 minutes."
		],
		"image": "lasagnes.jpeg",
		"comments": [
			{
				"author": "Virgile_m",
				"date": "08-09-2019",
				"content": "Lasagnes savoureuses mais titre confus"
			}
		]
	}

	recette5 = {
		"id": 5,
		"name": "Tiramisu aux framboises",
		"type": "Dessert",
		"ingredients": [
			"Oeufs",
			"Mascarpone",
			"Sucre roux",
			"Sucre vanillé",
			"Framboises",
			"Biscuits à la cuillère",
			"Amaretto",
			"Chocolat"
		],
		"quantities": [
			"2",
			"250 g",
			"70 g",
			"100 g",
			"10",
			"2 cuil. à café",
			"1 carré"
		],
		"preparation": [
			"Séparer les blancs des jaunes. Mélanger les jaunes, le sucre et le sucre vanillé.",
			"Ajouter le Mascarpone au fouet.",
			"Monter les blancs en neige et les incorporer délicatement à la spatule au mélange précédent.",
			"Tapisser les verrines de biscuits émiettés et ajouter l’Amaretto. Recouvrir de coulis et de quelques framboises, étalez par dessus une couche de crème, œuf, sucre, Mascarpone.",
			"Alterner biscuits, coulis, framboises et crème. Terminer par une couche de crème. Râper le carré de chocolat et saupoudrer."
		],
		"image": "Tiramisu.jpeg",
		"comments": [
			{
				"author": "Juju_KS",
				"date": "01-06-2020",
				"content": "Très bon dessert, idéal pour les fringales nocturnes."
			}
		]
	}

	recette6 = {
		"id": 6,
		"name": "Burger au saumon",
		"type": "Plat",
		"ingredients": [
			"Piment",
			"Sel",
			"Saumon",
			"Pains pour Hamburger",
			"Crème fraiche épaisse 15% mg",
			"Ciboulette",
			"Oignons",
			"Concombre",
			"Salade",
			"Poivre",
			"Avocat",
			"Cornichons"
		],
		"quantities": [
			"A l'envie",
			"A l'envie",
			"6 tranches fumées",
			"6",
			"1 petit pot",
			"4 cuil. à Soupe",
			"1",
			"1/2",
			"1 feuille",
			"A l'envie",
			"1",
			"3"
		],
		"preparation": [
			"Préparer la crème de ciboulette:",
			"mélanger à même le pot la crème fraîche avec la ciboulette ciselée, le poivre (du moulin !), le sel et 10 gouttes de tabasco.", "artiner une légère couche sur la moitié basse du pain à burger.",
			"Dresser le burger:",
			"déposer sur chaque moitié de pain tartiné quelques feuilles de salade, des lamelles de concombre épluché (et/ou d'avocat), des lamelles d'oignon rouge épluché, une tranche de saumon plié de façon à ce qu'elle ne dépasse pas du burger, et déposer une bonne cuillère de crème de ciboulette.",
			"refermer avec le chapeau du pain à burger et déposer dessus une moitié de cornichon coupé dans la longueur, piquez-le dans le burger pour le maintenir en place.",
			"servir dans les assiettes avec le reste de salade."
		],
		"image": "Burger_saumon.jpeg",
		"comments": [
			{
				"author": "MC_Ronald",
				"date": "20-10-1986",
				"content": "C tro nul, pa bon, otemps allé ô do maque."
			}
		]
	}

	recette7 = {
		"id": 7,
		"name": "Poulet coco curry",
		"type": "Plat",
		"ingredients": [
			"Oignons",
			"Poulet",
			"Boîte de tomates pelées",
			"Boîte de lait de coco",
			"Citron",
			"Curry rouge",
			"Gingembre",
			"Coriandre",
			"Huile d'olive",
			"Riz thaï"
		],
		"quantities": [
			"2",
			"6 filets de",
			"1",
			"1",
			"1",
			"2 cuil. à soupe",
			"2 cuil. à café",
			"De la",
			"2 cuil. café",
			"250g"
		],
		"preparation": [
			"Dans une casserole, faites cuire le riz conformément aux indications figurant sur le paquet.",
			"Dans un wok ou une cocotte, faire revenir les oignons émincés dans l'huile. Ajouter le gingembre et bien mélanger.",
			"Détailler les filets de poulet en morceaux. Les ajouter dans le wok et les faire revenir quelques minutes. Ajouter le curry et le jus de citron pressé.",
			"Ajouter les tomates pelées et le lait de coco. Laisser cuire 20 minutes à feu doux."
		],
		"image": "poulet_coco.jpeg",
		"comments": [
			{
				"author": "Moussier_Tombola",
				"date": "12-12-2002",
				"content": "C’est bon ça, c’est bon çaaa"
			}
		]
	}


	recette8 = {
		"id": 8,
		"name": "Croque-monsieur",
		"type": "Plat",
		"ingredients": [
			"Jambon",
			"Pain de mie",
			"Beurre",
			"Gryuère râpé",
			"Lait",
			"sel",
			"poivre",
			"muscade"
		],
		"quantities": [
			"4 tranches de ",
			"8 tranches de ",
			"50 g",
			"100 g",
			"4 cuil. à soupe de",
			"1 pincée de",
			"Du",
			"1 pincée de"
		],
		"preparation": [
			"Beurrez les 8 tranches de pain de mie sur une seule face. Posez 1 tranche de fromage sur chaque tranche de pain de mie. Posez 1 tranche de jambon plié en deux sur 4 tranches de pain de mie. Recouvrez avec les autres tartines (face non beurrée au dessus).",
			"Dans un bol mélanger le fromage râpé avec le lait, le sel, le poivre et la muscade.",
			"Répartissez le mélange sur les croque-monsieur.",
			"Placez sur une plaque au four sous le grill pendant 10 mn."
		],
		"image": "croque_monsieur.jpeg",
		"comments": [
			{
				"author": "Sarah",
				"date": "20-10-2012",
				"content": "Hmmmm :)"
			}
		]
	}

	recette9 = {
		"id": 9,
		"name": "Salade niçoise",
		"type": "Entrée",
		"ingredients": [
			"Sel",
			"Vinaigre de vin rouge",
			"Tomates",
			"Oeufs",
			"Oignons cébettes",
			"Févettes",
			"Poivron vert",
			"Thon",
			"Anchois au sel",
			"Olives noires de Nice",
			"Basilic",
			"Radis",
			"Huile d'olive",
			"Artichauts violets à l'huile",
			"Poivre"
		],
		"quantities": [
			"Du",
			"Du",
			"4",
			"4",
			"2",
			"8",
			"1",
			"200 g",
			"4 filets de",
			"Des",
			"Une feuille de ",
			"8",
			"",
			"4",
			""
		],
		"preparation": [
			"Pour réaliser la salade niçoise, il suffit de rassembler tous les ingrédients, puis de procéder de la manière suivante...", "Faire durcir les oeufs (6 à 8 minutes après ébullition de l'eau), puis les faire bien refroidir à l'eau froide.",
			"Hacher les cébettes et les disposer au fond du plat.",
			"Ajouter les févettes, le poivron vert finement coupé, les radis coupés en rondelles et le thon bien égouté et émietté. Mélanger grossièrement tous ces ingrédients avec du sel et du poivre.",
			"Couper les tomates en fines rondelles et les ajouter ainsi que les artichauts Couper les oeufs durs en quartiers et les disposer sur le dessus et ajouter les filets d'anchois, les olives noires et le basilic finement ciselé.",
			"Enfin, saupoudrer de sel et de poivre, puis arroser d'huile d'olive et de vinaigre de vin.",
			"Mettre au frais 1 heure et bien mélanger la salade juste avant de la servir."
		],
		"image": "salade_nicoise.jpeg",
		"comments": [
			{
				"author": "JCVD",
				"date": "12-06-1996",
				"content": "J’adore Nice, dans 20 ans y en aura plus."
			}
		]
	}

	recette10 = {
		"id": 10,
		"name": "Moussaka",
		"type": "Plat",
		"ingredients": [
			"Sel",
			"Muscade",
			"Aubergines",
			"Pommes de terre",
			"Boeuf haché",
			"Tomates",
			"Oignons",
			"Huile d'olive",
			"Beurre",
			"Cannelle",
			"Miel",
			"Poivre",
			"Farine",
			"Lait"
		],
		"quantities": [
			"Du ",
			"De la",
			"2",
			"6",
			"500 g",
			"5",
			"1",
			"",
			"50 g",
			"1 petite cuillère de",
			"1 cuillère à soupe de",
			"Du",
			"3 cuillères à soupe de",
			"35 cl de"
		],
		"preparation": [
			"Préparation de la sauce tomate. Émincer les oignons et les faire blondir dans une petite casserole.",
			"Ajouter les tomates coupées en gros dés et 2 bonnes cuillères à soupe d'huile d'olive, la cannelle, le miel, saler et poivrer. Laisser réduire le tout 25 minutes (ou plus, jusqu'à arriver à la préparation de la viande) à feu moyen. On doit obtenir une sauce, que l'on peut homogénéiser avec du coulis de tomate tout prêt.",
			"Préparation des aubergines. Découper les aubergines en rondelles (sans les peler), saler généreusement, et les laisser dégorger le temps de l'étape suivante. Conseil pour faire dégorger les aubergines : dans un plat, alterner une couche de tranches d'aubergine salées et une couche de papier absorbant ou les laisser dans une passoire.",
			"Préparation des pommes de terre. Eplucher et découper les pommes de terres en fines rondelles.",
			"Disposer les rondelles de pommes de terre au fond d'un plat à gratin assez haut, huilé. Arroser les pommes de terres d'un peu (3 cuillères à soupe) du jus rendu par les tomates qui mijotent.",
			"Passer le plat de pommes de terre sous le grill 5 à 15 min selon votre four, pour qu'elles dorent.",
			"Maintenant qu'elles ont dégorgé, passer les rondelles d'aubergine à la poêle à feu fort pour les faire griller un peu de chaque côté, réserver.",
			"Préparation de la viande. Dans un faitout, faire revenir la viande hachée au beurre à feu assez fort, saler, poivrer et retirer l'eau rendue par la viande.",
			"Ajouter la sauce tomate-oignons et baisser le feu (très doux).",
			"Sortir le plat de pommes de terres du four et le préchauffer le four à 200°C (thermostat 6-7).",
			"Préparation de la béchamel. Dans une petite casserole sur feu doux, faire blondir les 20 g de beurre, ajouter la farine et mélanger pour obtenir un appareil homogène.",
			"Incorporer petit à petit le lait en n'arrêtant jamais de remuer, ça peut prendre 10 bonnes minutes, on doit obtenir une sauce assez épaisse.",
			"Saler, poivrer et râper un peu de noix de muscade (c'est fort, il faut en mettre peu).",
			"Montage de la moussaka. Par dessus la couche de pommes de terre, étaler la moitié de la viande hachée avec la tomate, puis la moitié des aubergines, puis l'autre moitié de viande, puis l'autre moitié des aubergines, un filet d'huile d'olive et terminer par la béchamel.",
			"Enfourner le tout dans le four à 200°C (thermostat 6-7) et laisser cuire 1h (la béchamel doit croustiller et être dorée)."
		],
		"image": "moussaka.jpg",
		"comments": [
			{
				"author": "fakir_m",
				"date": "08-08-2045",
				"content": "Message à mon moi du passé : girvile te doit de la moula"
			}
		]
	}

	recette11 = {
		"id": 11,
		"name": "Pho, pas de ma mère",
		"type": "Plat",
		"ingredients": [
			"Etoile de badiane",
			"Boeuf maigre",
			"Citron",
			"Gingembre",
			"Piment",
			"Coriandre",
			"Ciboulette thai",
			"Nouilles de riz fraîches",
			"bouillon préparé avec 2 cubes de Maggi",
			"Sauce nuoc mam",
			"Sauce sriracha",
			"Sauce Hoisin",
			"Poulet"
		],
		"quantities": [
			"1",
			"400 g",
			"1 (vert)",
			"1 morceau",
			"1 petit",
			"1 petit bouquet",
			"1 petit bouquet",
			"400 g",
			"1.5 L",
			"De la",
			"De la",
			"De la",
			"(oskour) du"
		],
		"preparation": [
			"Lavez, séchez, ciselez la ciboulette et la coriandre, émincez le piment, coupez le citron vert en 4 dans le sens de la longueur et mettez-les en attente dans des coupelles.",
			"Portez à ébullition, le bouillon de boeuf, ajoutez-y l'étoile de badiane, et le morceau de gingembre pelé et émincé. Couvrez et laissez cuire doucement pendant 12 min.",
			"Détaillez le boeuf en fine lamelles, faites cuire les nouilles de riz dans de l'eau bouillante salée, respectez les indications sur le paquet.",
			"Dans 4 grands bols versez 1 cuillerée à soupe de sauce Nuoc-mâm, egouttez les nouilles de riz, répartissez-les dans les bols, posez les lamelles de boeuf, et versez le bouillon de boeuf brûlant, parsemez de ciboulette et de coriandre. Servez aussitôt.",
			"Chacun ajoutera à son goût, citron vert, sauce et piment. Bon appétit."
		],
		"image": "pho.jpeg",
		"comments": [
			{
				"author": "Sodinhelp",
				"date": "12-04-2020",
				"content": "wola c’est la recette de marmiton mais ma daronne elle fait mijoter au minimum un jour entier, 3andek"
			}
		]
	}

	recette12 = {
		"id": 12,
		"name": "Pain Pita",
		"type": "Entrée",
		"ingredients": [
			"Pain",
			"Pita",
			"Eau"
		],
		"quantities": [
			"",
			"De la",
			""
		],
		"preparation": [
			"Mélanger les deux ingrédients et demi",
			"Mettre au micro-onde pendant 10m à 680W."
		],
		"image": "pita.jpeg",
		"comments": [
			{
				"author": "Virlou",
				"date": "12-10-2011",
				"content": "Incroyable recette fréro tu gr"
			}
		]
	}

	recette69 = {
		"id": 69,
		"name": "La Sousoupe du manoir de Soupex",
		"type": "Entrée",
		"ingredients": [
			"Nectar de Soupex",
			"Sel de Sard",
			"Eau du puits du domaine",
			"L'ambiance du Chenil"
		],
		"quantities": [
			"La dose de",
			"Du ",
			"",
			""
		],
		"preparation": [
			"Vous ne pouvez pas la faire vous-même",
			"Rendez-vous au Manoir de Soupex pour pouvoir déguster la délicieuse sousoupe."
		],
		"image": "sousoupe.png",
		"comments": [
			{
				"author": "Alder",
				"date": "09-05-2020",
				"content": "je dédie cette recette à tous mes Alder du Brésil"
			}
		]
	}

	old_recette = [recette1, recette2, recette3, recette4, recette5, recette6, recette7, recette8, recette9, recette10, recette11, recette12, recette69]

	open("data.json", "w").close()
	with open('data.json', 'w') as outfile:
		json.dump(old_recette, outfile)