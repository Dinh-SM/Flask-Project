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
		"name": "Couscous R??publicain",
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
			"Beurre concass??",
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
			"1 cuil. ?? soupe",
			"0,5 cuil. ?? soupe",
			"2 cuil. ?? soupe",
			"1 gousse"
		],
		"preparation": [
			"Dans une grande cocotte, faites chauffer l'huile d'olive. Saisissez de chaque c??t?? les  cuisses de poulet et les morceaux de collier d'agneau. Salez et poivrez, puis retirez-les de la cocotte.",
			"Emincez les oignons, faites-les blondir dans la cocotte ?? la place de la viande. Salez et parsemez d'??pices.",
			"Coupez les aubergines, les carottes et les courgettes en cubes, faites-les colorer avec les oignons. Ajoutez les tomates concass??es et l'ail hach?? puis remettez la viande dans la cocotte. Couvrez d'eau ?? hauteur et portez ?? fr??missements 45 min.",
			"Ajoutez les pois chiches ??goutt??s, poursuivez la cuisson 15 min.",
			"Faites griller les merguez dans une po??le antiadh??sive.",
			"Mouillez la semoule dans la moiti?? de son volume d'eau. ??grenez la semoule, ajoutez une cuill??re d???huile d???olive, m??langez puis passez ?? la vapeur pendant 10 minutes. R??p??ter l???op??ration une fois. Ajoutez de l???huile d???olive ?? votre convenance.",
			"Servez le couscous accompagn?? de semoule et de merguez chaudes."
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
		"name": "Merguez ?? la graisse de pneu",
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
			"D??clarez votre mouvement de gr??ve aux camarades",
			"Dans le feu de l???action, br??ler des pneus et r??cup??rer la graisse (la s??questration de votre propri??taire des moyens de production est facultatif ?? cette ??tape).",
			"Au stand des camarades pr??parez un feu dans un barbecue improvis?? sur ce que vous trouvez",
			"Alimentez le feu avec la graisse","Faites carboniser vos merguez ?? votre convenance"
		],
		"image": "merguez.jpeg",
		"comments": [
			{
				"author": "Philou_m",
				"date": "01-05-2021",
				"content": "Super merguez camarade rien de mieux qu???une guezmer pour remobiliser les troupes"
			}
		]
	}

	recette3 = {
		"id": 3,
		"name": "Poulet brais?? ?? la grecque",
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
			"?? envie",
			"?? envie",
			"4 cuil. ?? caf??",
			"1",
			"400 g",
			"5-6 cuil. ?? soupe"
		],
		"preparation": [
			"Faire chauffer l'huile d'olive et le poulet brun tout autour. Ajouter l'oignon r??p?? et remuer les faire frire et, en remuant de temps pour ??viter le brunissement.",
			"Ajouter le vin et r??duire la chaleur. Couvrez la casserole et laisser le sigomageireftei de poulet. Maintenant, puis le contr??le. Si le liquide r??duit moins, ajouter un peu d'eau.",
			"Lorsque le poulet est pr??t, ajouter le jus de citron, sel, poivre et paprika. Faire cuire 2 - 3 minutes. Ajouter le fromage et le persil et retirer du feu.",
			"Servir chaud, avec du riz bouilli ou des pommes de terre. "
		],
		"image": "Poulet_grec.jpeg",
		"comments": [
			{
				"author": "Al??xis_P??rate",
				"date": "25-12-2010",
				"content": "Super recette, ingr??dients un peu chers"
			}
		]
	}

	recette4 = {
		"id": 4,
		"name": "Lasagnes aux l??gumes non v??g??",
		"type": "Plat",
		"ingredients": [
			"Courgettes",
			"Aubergines",
			"Sauce tomate",
			"Concentr?? de tomate",
			"Oignons",
			"Poivre",
			"Huile d'olive",
			"Viande de boeuf h??ch??e",
			"Lasagnes s??ches (en feuille)",
			"Farine",
			"Beurre",
			"Lait"
		],
		"quantities": [
			"3",
			"2",
			"1 pot",
			"1 pot",
			"?? envie",
			"du",
			"2 cuil. ?? soupe",
			"400 g",
			"(feuilles)",
			"50 g",
			"50 g",
			"60 cl"
		],
		"preparation": [
			"Faire la sauce tomate. Emincer finement l'ail et l'oignon. Les faire revenir dans une casserole avec un peu d'huile d'olive. Ajouter un fond de vin blanc. Apr??s 2 minutes de cuisson, ajouter les herbes, puis les tomates concass??es et le concentr?? de tomates. Ajouter 2 cuill??res ?? caf?? de sucre. Saler et poivrer. Laisser mijoter environ 1 heure ?? feu doux, avec un couvercle. La sauce doit rester assez liquide.",
			"Laver les aubergines. Les couper en petits d??s. Peler et couper en d??s les courgettes.",
			"Dans une sauteuse, faire revenir les aubergines avec quelques cuill??res d'huile d'olive, jusqu'?? ce qu'elles soient bien cuites. Saler et poivrer.",
			"Pr??paration de la b??chamel : Faites fondre le beurre dans une casserole ?? fond ??pais. Ajoutez la farine et remuez avec une cuill??re de bois sans laisser colorer. La farine doit juste ??paissir. Versez le lait progressivement, sans cesser de remuer, jusqu'?? ce que la sauce ??paississe. Assaisonnez de sel et poivre.",
			"Dans un plat ?? gratin, d??poser une louche de sauce tomates et une demi-louche de b??chamel. Etaler. D??poser les feuilles de lasagnes. D??poser ensuite dessus les aubergines, puis une autre louche de sauce tomates et une demi-louche de b??chamel. Couvrir de feuilles de lasagnes. Dans la m??me sauteuse, faire cuire la viande hach??e ??miett??e jusqu'?? ce qu'elle soit bien ass??ch??e. Saler et poivrer. Dans le plat, d??poser la viande, puis les poivrons en lani??res. Couvrir de feuilles de lasagnes.",
			"Dans la sauteuse, faire revenir les d??s de courgettes avec un peu d'huile d'olive. Elles doivent ??tre bien tendres. Les d??poser dans le plat ?? gratin. Recouvrir de la moiti?? de la sauce tomate restante. Recouvrir de feuilles de lasagnes.",
			"Finir en couvrant de la sauce restante puis de fromage r??p??. Mettre sous film et laisser reposer 2 heures ou mieux, une nuit au frais. Enlever le film. D??poser des noisettes de beurre sur le dessus, et enfourner 35 minutes."
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
			"Sucre vanill??",
			"Framboises",
			"Biscuits ?? la cuill??re",
			"Amaretto",
			"Chocolat"
		],
		"quantities": [
			"2",
			"250 g",
			"70 g",
			"100 g",
			"10",
			"2 cuil. ?? caf??",
			"1 carr??"
		],
		"preparation": [
			"S??parer les blancs des jaunes. M??langer les jaunes, le sucre et le sucre vanill??.",
			"Ajouter le Mascarpone au fouet.",
			"Monter les blancs en neige et les incorporer d??licatement ?? la spatule au m??lange pr??c??dent.",
			"Tapisser les verrines de biscuits ??miett??s et ajouter l???Amaretto. Recouvrir de coulis et de quelques framboises, ??talez par dessus une couche de cr??me, ??uf, sucre, Mascarpone.",
			"Alterner biscuits, coulis, framboises et cr??me. Terminer par une couche de cr??me. R??per le carr?? de chocolat et saupoudrer."
		],
		"image": "Tiramisu.jpeg",
		"comments": [
			{
				"author": "Juju_KS",
				"date": "01-06-2020",
				"content": "Tr??s bon dessert, id??al pour les fringales nocturnes."
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
			"Cr??me fraiche ??paisse 15% mg",
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
			"6 tranches fum??es",
			"6",
			"1 petit pot",
			"4 cuil. ?? Soupe",
			"1",
			"1/2",
			"1 feuille",
			"A l'envie",
			"1",
			"3"
		],
		"preparation": [
			"Pr??parer la cr??me de ciboulette:",
			"M??langer ?? m??me le pot la cr??me fra??che avec la ciboulette cisel??e, le poivre (du moulin !), le sel et 10 gouttes de tabasco.", "artiner une l??g??re couche sur la moiti?? basse du pain ?? burger.",
			"Dresser le burger:",
			"D??poser sur chaque moiti?? de pain tartin?? quelques feuilles de salade, des lamelles de concombre ??pluch?? (et/ou d'avocat), des lamelles d'oignon rouge ??pluch??, une tranche de saumon pli?? de fa??on ?? ce qu'elle ne d??passe pas du burger, et d??poser une bonne cuill??re de cr??me de ciboulette.",
			"Refermer avec le chapeau du pain ?? burger et d??poser dessus une moiti?? de cornichon coup?? dans la longueur, piquez-le dans le burger pour le maintenir en place.",
			"Servir dans les assiettes avec le reste de salade."
		],
		"image": "Burger_saumon.jpeg",
		"comments": [
			{
				"author": "MC_Ronald",
				"date": "20-10-1986",
				"content": "C tro nul, pa bon, otemps all?? ?? do maque."
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
			"Bo??te de tomates pel??es",
			"Bo??te de lait de coco",
			"Citron",
			"Curry rouge",
			"Gingembre",
			"Coriandre",
			"Huile d'olive",
			"Riz tha??"
		],
		"quantities": [
			"2",
			"6 filets de",
			"1",
			"1",
			"1",
			"2 cuil. ?? soupe",
			"2 cuil. ?? caf??",
			"De la",
			"2 cuil. caf??",
			"250g"
		],
		"preparation": [
			"Dans une casserole, faites cuire le riz conform??ment aux indications figurant sur le paquet.",
			"Dans un wok ou une cocotte, faire revenir les oignons ??minc??s dans l'huile. Ajouter le gingembre et bien m??langer.",
			"D??tailler les filets de poulet en morceaux. Les ajouter dans le wok et les faire revenir quelques minutes. Ajouter le curry et le jus de citron press??.",
			"Ajouter les tomates pel??es et le lait de coco. Laisser cuire 20 minutes ?? feu doux."
		],
		"image": "poulet_coco.jpeg",
		"comments": [
			{
				"author": "Moussier_Tombola",
				"date": "12-12-2002",
				"content": "C???est bon ??a, c???est bon ??aaa"
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
			"Gryu??re r??p??",
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
			"4 cuil. ?? soupe de",
			"1 pinc??e de",
			"Du",
			"1 pinc??e de"
		],
		"preparation": [
			"Beurrez les 8 tranches de pain de mie sur une seule face. Posez 1 tranche de fromage sur chaque tranche de pain de mie. Posez 1 tranche de jambon pli?? en deux sur 4 tranches de pain de mie. Recouvrez avec les autres tartines (face non beurr??e au dessus).",
			"Dans un bol m??langer le fromage r??p?? avec le lait, le sel, le poivre et la muscade.",
			"R??partissez le m??lange sur les croque-monsieur.",
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
		"name": "Salade ni??oise",
		"type": "Entr??e",
		"ingredients": [
			"Sel",
			"Vinaigre de vin rouge",
			"Tomates",
			"Oeufs",
			"Oignons c??bettes",
			"F??vettes",
			"Poivron vert",
			"Thon",
			"Anchois au sel",
			"Olives noires de Nice",
			"Basilic",
			"Radis",
			"Huile d'olive",
			"Artichauts violets ?? l'huile",
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
			"Pour r??aliser la salade ni??oise, il suffit de rassembler tous les ingr??dients, puis de proc??der de la mani??re suivante...", "Faire durcir les oeufs (6 ?? 8 minutes apr??s ??bullition de l'eau), puis les faire bien refroidir ?? l'eau froide.",
			"Hacher les c??bettes et les disposer au fond du plat.",
			"Ajouter les f??vettes, le poivron vert finement coup??, les radis coup??s en rondelles et le thon bien ??gout?? et ??miett??. M??langer grossi??rement tous ces ingr??dients avec du sel et du poivre.",
			"Couper les tomates en fines rondelles et les ajouter ainsi que les artichauts Couper les oeufs durs en quartiers et les disposer sur le dessus et ajouter les filets d'anchois, les olives noires et le basilic finement cisel??.",
			"Enfin, saupoudrer de sel et de poivre, puis arroser d'huile d'olive et de vinaigre de vin.",
			"Mettre au frais 1 heure et bien m??langer la salade juste avant de la servir."
		],
		"image": "salade_nicoise.jpeg",
		"comments": [
			{
				"author": "JCVD",
				"date": "12-06-1996",
				"content": "J???adore Nice, dans 20 ans y en aura plus."
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
			"Boeuf hach??",
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
			"1 petite cuill??re de",
			"1 cuill??re ?? soupe de",
			"Du",
			"3 cuill??res ?? soupe de",
			"35 cl de"
		],
		"preparation": [
			"Pr??paration de la sauce tomate. ??mincer les oignons et les faire blondir dans une petite casserole.",
			"Ajouter les tomates coup??es en gros d??s et 2 bonnes cuill??res ?? soupe d'huile d'olive, la cannelle, le miel, saler et poivrer. Laisser r??duire le tout 25 minutes (ou plus, jusqu'?? arriver ?? la pr??paration de la viande) ?? feu moyen. On doit obtenir une sauce, que l'on peut homog??n??iser avec du coulis de tomate tout pr??t.",
			"Pr??paration des aubergines. D??couper les aubergines en rondelles (sans les peler), saler g??n??reusement, et les laisser d??gorger le temps de l'??tape suivante. Conseil pour faire d??gorger les aubergines : dans un plat, alterner une couche de tranches d'aubergine sal??es et une couche de papier absorbant ou les laisser dans une passoire.",
			"Pr??paration des pommes de terre. Eplucher et d??couper les pommes de terres en fines rondelles.",
			"Disposer les rondelles de pommes de terre au fond d'un plat ?? gratin assez haut, huil??. Arroser les pommes de terres d'un peu (3 cuill??res ?? soupe) du jus rendu par les tomates qui mijotent.",
			"Passer le plat de pommes de terre sous le grill 5 ?? 15 min selon votre four, pour qu'elles dorent.",
			"Maintenant qu'elles ont d??gorg??, passer les rondelles d'aubergine ?? la po??le ?? feu fort pour les faire griller un peu de chaque c??t??, r??server.",
			"Pr??paration de la viande. Dans un faitout, faire revenir la viande hach??e au beurre ?? feu assez fort, saler, poivrer et retirer l'eau rendue par la viande.",
			"Ajouter la sauce tomate-oignons et baisser le feu (tr??s doux).",
			"Sortir le plat de pommes de terres du four et le pr??chauffer le four ?? 200??C (thermostat 6-7).",
			"Pr??paration de la b??chamel. Dans une petite casserole sur feu doux, faire blondir les 20 g de beurre, ajouter la farine et m??langer pour obtenir un appareil homog??ne.",
			"Incorporer petit ?? petit le lait en n'arr??tant jamais de remuer, ??a peut prendre 10 bonnes minutes, on doit obtenir une sauce assez ??paisse.",
			"Saler, poivrer et r??per un peu de noix de muscade (c'est fort, il faut en mettre peu).",
			"Montage de la moussaka. Par dessus la couche de pommes de terre, ??taler la moiti?? de la viande hach??e avec la tomate, puis la moiti?? des aubergines, puis l'autre moiti?? de viande, puis l'autre moiti?? des aubergines, un filet d'huile d'olive et terminer par la b??chamel.",
			"Enfourner le tout dans le four ?? 200??C (thermostat 6-7) et laisser cuire 1h (la b??chamel doit croustiller et ??tre dor??e)."
		],
		"image": "moussaka.jpg",
		"comments": [
			{
				"author": "fakir_m",
				"date": "08-08-2045",
				"content": "Message ?? mon moi du pass?? : girvile te doit de la moula"
			}
		]
	}

	recette11 = {
		"id": 11,
		"name": "Pho, pas de ma m??re",
		"type": "Plat",
		"ingredients": [
			"Etoile de badiane",
			"Boeuf maigre",
			"Citron",
			"Gingembre",
			"Piment",
			"Coriandre",
			"Ciboulette thai",
			"Nouilles de riz fra??ches",
			"bouillon pr??par?? avec 2 cubes de Maggi",
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
			"Lavez, s??chez, ciselez la ciboulette et la coriandre, ??mincez le piment, coupez le citron vert en 4 dans le sens de la longueur et mettez-les en attente dans des coupelles.",
			"Portez ?? ??bullition, le bouillon de boeuf, ajoutez-y l'??toile de badiane, et le morceau de gingembre pel?? et ??minc??. Couvrez et laissez cuire doucement pendant 12 min.",
			"D??taillez le boeuf en fine lamelles, faites cuire les nouilles de riz dans de l'eau bouillante sal??e, respectez les indications sur le paquet.",
			"Dans 4 grands bols versez 1 cuiller??e ?? soupe de sauce Nuoc-m??m, egouttez les nouilles de riz, r??partissez-les dans les bols, posez les lamelles de boeuf, et versez le bouillon de boeuf br??lant, parsemez de ciboulette et de coriandre. Servez aussit??t.",
			"Chacun ajoutera ?? son go??t, citron vert, sauce et piment. Bon app??tit."
		],
		"image": "pho.jpeg",
		"comments": [
			{
				"author": "Sodinhelp",
				"date": "12-04-2020",
				"content": "wola c???est la recette de marmiton mais ma daronne elle fait mijoter au minimum un jour entier, 3andek"
			}
		]
	}

	recette12 = {
		"id": 12,
		"name": "Pain Pita",
		"type": "Entr??e",
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
			"M??langer les deux ingr??dients et demi",
			"Mettre au micro-onde pendant 10m ?? 680W."
		],
		"image": "pita.jpeg",
		"comments": [
			{
				"author": "Virlou",
				"date": "12-10-2011",
				"content": "Incroyable recette fr??ro tu gr"
			}
		]
	}

	recette69 = {
		"id": 69,
		"name": "La Sousoupe du manoir de Soupex",
		"type": "Entr??e",
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
			"Vous ne pouvez pas la faire vous-m??me",
			"Rendez-vous au Manoir de Soupex pour pouvoir d??guster la d??licieuse sousoupe."
		],
		"image": "sousoupe.png",
		"comments": [
			{
				"author": "Alder",
				"date": "09-05-2020",
				"content": "je d??die cette recette ?? tous mes Alder du Br??sil"
			}
		]
	}

	old_recette = [recette1, recette2, recette3, recette4, recette5, recette6, recette7, recette8, recette9, recette10, recette11, recette12, recette69]

	open("data.json", "w").close()
	with open('data.json', 'w') as outfile:
		json.dump(old_recette, outfile)