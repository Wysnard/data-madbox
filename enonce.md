Test Data Analyst
==================

Partie 1 : Intégration d'API & Prediction (à faire chez soi)
============================================================

Objectif
--------
L'objectif de ce test est d'évaluer vos compétence à interagir avec une API tierce, récupérer et traiter des données puis les sauvegarder. Vous devrez ensuite afficher ces données dans un outil de DataViz. Finalement, vous devrez effectuer une prédiction en vous basant sur ces données.

Description
-----------
Nous avons mis à votre disposition une API publique permettant de récupérer les données financières d'une entreprise monétisée par du revenue publicitaire entre le 1er Janvier 2019 et le 7 Septembre 2019.
Vous devrez récupérer et stocker les données financières qui vous semblent pertinentes puis prédire le profit quotidien sur la fin de l'année 2019.

Voici la documentation de cette API :

L'API est hebergée à l'adresse suivante : https://data-analyst-test.madboxgames.io
Il dispose d'une unique route accessible en POST : https://data-analyst-test.madboxgames.io/api/public/profit/get

Format de la requête :

===================================================================================================
| Paramètre   |   Exemple      |                              Description                         |
===================================================================================================
| start_date  | 2019-05-01     | Date à partir de laquelle on veut récupérer la donnée            |
---------------------------------------------------------------------------------------------------
| end_date    | 2019-06-30     | Date jusqu'à laquelle on veut récupérer la donnée                |
---------------------------------------------------------------------------------------------------
| columns     | profit,revenue | Colonnes à récupérer séparées par des virgules.                  |
|             |                | Choisir parmi : spend,revenue,profit,margin,nb_impressions,ecpm  |
===================================================================================================

Format de la réponse en cas de succès :

```
{
    "status": 1,
    "data": {
        "data": [
            {
                "profit": 1555.31,
                "date": "2019-05-01"
            },
            {
                "profit": 1430.72,
                "date": "2019-05-02"
            },
            ...
        ]
    },
    "errors": []
```

En cas d'erreur :

```
{
    "status": 0,
    "data": {},
    "errors": [
        {
            "code": 100,
            "message": "Missing Parameter : end_date"
        },
        {
            "code": 100,
            "message": "Missing Parameter : columns"
        }
    ]
}
```

Tech
----
Votre projet sera réalisé en Node.js. Vous êtes libre de choisir votre base de données.

Modalités
---------
Pour que nous puissions évaluer votre code vous utiliserez git pour gérer ce mini-projet et vous rédigerez un README.md expliquant comment installer et lancer votre application. Vous nous fournirez donc simplement un lien vers votre répertoire GitHub/BitBucket.

Dans ce README.md, nous souhaitons aussi que vous détailliez le fonctionnement technique de votre application, les points que vous pensez pouvoir améliorer et comment.

Vous y indiquerez également le temps que vous avez passé à développer ce programme.

-----------------------------------------------------------------------------------------

Partie 2 : Business Intelligence (sur place après validation de la Partie 1)
============================================================================

Objectif
--------
L'objectif de ce test est d'évaluer vos compétences à :
- Rapidement comprendre le fonctionnement d'un business et ses différentes KPIs
- Comprendre comment se construit l'équation économique d'une entreprise
- Naviguer et interroger une source de données.
- Critiquer les données
- Trouver la bonne métrique permettant de répondre à une question
- Vous poser vous-même des questions business-oriented

Description
-----------
Vous aurez à votre disposition des données factices sur Tableau. Vous aurez d'abord une introduction rapide sur l'ensemble des données disponibles. Puis vous devrez naviguer pour répondre à des questions simples. Il sera ensuite attendu de vous de vous poser des questions pertinentes auxquelles la donnée peut répondre et d'en chercher la réponse. Ce sera une évaluation basée sur l'échange et notamment votre capacité à challenger les données et la modélisation business de l'entreprise.