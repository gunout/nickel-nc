<div align="center">

# 🥈 Moniteur Nickel — Nouvelle-Calédonie

[![GitHub license](https://img.shields.io/github/license/gunout/nickel-nc?color=blue&style=flat-square)](https://github.com/gunout/nickel-nc/blob/main/LICENSE)
[![GitHub last commit](https://img.shields.io/github/last-commit/gunout/nickel-nc?style=flat-square)](https://github.com/gunout/nickel-nc/commits/main)
[![GitHub repo size](https://img.shields.io/github/repo-size/gunout/nickel-nc?style=flat-square)](https://github.com/gunout/nickel-nc)
[![GitHub stars](https://img.shields.io/github/stars/gunout/nickel-nc?style=flat-square)](https://github.com/gunout/nickel-nc/stargazers)
[![GitHub issues](https://img.shields.io/github/issues/gunout/nickel-nc?style=flat-square)](https://github.com/gunout/nickel-nc/issues)
[![Made with Chart.js](https://img.shields.io/badge/Chart.js-4.x-FF6384?style=flat-square&logo=chartdotjs)](https://www.chartjs.org/)
[![Tailwind CSS](https://img.shields.io/badge/Tailwind-3.x-38B2AC?style=flat-square&logo=tailwind-css)](https://tailwindcss.com/)
[![JavaScript](https://img.shields.io/badge/JavaScript-ES6+-F7DF1E?style=flat-square&logo=javascript)](https://developer.mozilla.org/fr/docs/Web/JavaScript)
[![Open Data](https://img.shields.io/badge/Open%20Data-100%25-18753c?style=flat-square)](https://www.etalab.gouv.fr/licence-ouverte-open-licence)
[![Data: ISEE-NC](https://img.shields.io/badge/Data-ISEE--NC-000091?style=flat-square)](https://isee.nc/)
[![Data: data.gouv.nc](https://img.shields.io/badge/Data-data.gouv.nc-18753c?style=flat-square)](https://data.gouv.nc/)
[![Data: Eurostat](https://img.shields.io/badge/Data-Eurostat-003399?style=flat-square&logo=european-union)](https://ec.europa.eu/eurostat)

> **Moniteur interactif et expert de la filière nickel en Nouvelle-Calédonie.**
> Analyse historique 1970–2025, prévisions, corrélations, points de rupture, saisonnalité, stress-test, risque pays, Monte Carlo et alertes automatiques.
> Données 100 % open data : ISEE, data.gouv.nc, FRED/IMF, BGS/DIMENC, INSG.
</div>

---

## 📊 Aperçu

Le moniteur couvre **9 séries historiques** et **plus de 60 ans de données** sur la filière nickel calédonienne :

| Série | Période | Points | Source |
| :--- | :--- | :--- | :--- |
| 🏗️ Extraction de minerai | 2008–2024 | 17 ans | ISEE/DIMENC |
| 💰 Cours du nickel au LME | 1981–2025 | 45 ans | ISEE |
| 📦 Exportations de minerai | 2008–2025 | 18 ans | ISEE |
| 🏭 Exportations métallurgiques | 2008–2025 | 18 ans | ISEE |
| 🌍 Production mondiale | 1977–2024 | 48 ans | BGS/DIMENC |
| 🌐 Consommation mondiale | 2015–2025 | 11 ans | INSG/DIMENC |
| 📈 Poids économique (PIB) | 1998–2017 | 19 ans | ISEE |
| 💵 Recettes fiscales IS35 | 2002–2019 | 18 ans | Compte administratif NC |
| 📅 Production métallurgique mensuelle | 1985–2026 | 500 mois | data.gouv.nc |

---

## ✨ Fonctionnalités

### 📈 Visualisation interactive
- **6 graphiques historiques** avec double axe (volumes + valeurs)
- **Zoom** (molette), **pan** (glisser), **tooltips** détaillés
- **Légende cliquable** pour masquer/afficher les séries
- **Filtre par période** (curseur double)
- **Sélection d'indicateur** via menu ou clic sur les KPI
- **Mode sombre** avec adaptation des graphiques
- **Reset zoom** en un clic

### 🧠 Analyse experte
- **Matrice de corrélations** (Pearson) entre les séries
- **Prévisions** par régression linéaire sur 3 ans
- **Tendance sur 5 ans** avec CAGR
- **Analyse des écarts YoY** (variations annuelles)
- **Points de rupture** (détection CUSUM avec seuil ±2σ)
- **Saisonnalité** (production mensuelle + cours LME)
- **Stress-test** (5 scénarios + personnalisé)
- **Risque pays** (radar 3 axes + score global)
- **Simulation Monte Carlo** (1 000 à 10 000 itérations)
- **Indicateurs dérivés** :
  - Ratio export/extraction
  - Intensité métallurgique
  - Prix moyen export métal
  - Volatilité 10 ans du cours
  - Valeur ajoutée par tonne
  - Recettes IS35 / VA
  - Dépendance Chine

### 🚨 Alertes automatiques
- Prix LME sous le seuil paramétrable (défaut : 14 000 USD/t)
- Chute d'extraction > 30 % (crise)
- Baisse du cours > 10 %
- Dépendance Chine > 65 %
- Hausse des exportations métallurgiques > 20 %

### 📋 Tableau de données
- Tri par colonne (clic sur en-tête)
- Recherche par année
- Sélection de ligne
- Export CSV des données filtrées
- Export PDF du moniteur complet

---

## 🚀 Déploiement local

### Prérequis
- Python 3.x (ou tout autre serveur HTTP statique)
- Un navigateur moderne (Chrome, Firefox, Edge, Safari)

### Lancement

Ouvrez un terminal, puis exécutez les commandes suivantes :

- **Cloner le dépôt** : git clone https://github.com/gunout/nickel-nc.git
- **Se déplacer dans le dossier** : cd nickel-nc
- **Lancer un serveur local** : python3 -m http.server 8080
- **Ouvrir le navigateur** : http://localhost:8080

> ⚠️ **Important** : le moniteur utilise fetch() pour charger data/moniteur_nickel_nc.json. Il ne fonctionnera donc **pas** en ouvrant index.html directement (file://). Un serveur HTTP est nécessaire.

---

## 📁 Structure du projet

- **index.html** — Moniteur interactif (version experte)
- **README.md** — Ce fichier
- **LICENSE** — Licence open source
- **data/** — Dossier des données
  - **moniteur_nickel_nc.json** — Données consolidées (9 séries)
  - **coursnickel.xls** — Cours annuels et mensuels (ISEE)
  - **extraction-nickel.xls** — Extraction par type de minerai (ISEE)
  - **exportations-nickel.xls** — Exportations minerai + métal (ISEE)
  - **marchemondial.xls** — Production et consommation mondiales (BGS/INSG)
  - **poids-nickel.xls** — PIB, valeur ajoutée, recettes IS35 (ISEE)
  - **production_metallurgique.json** — Production mensuelle (data.gouv.nc)
  - **prix_nickel_fred.csv** — Prix LME mensuel (FRED/IMF)

---

## 🔧 Stack technique

- **Frontend** : HTML5, CSS3, JavaScript (vanilla)
- **UI** : Tailwind CSS (CDN)
- **Graphiques** : Chart.js + chartjs-plugin-zoom + chartjs-plugin-annotation
- **Export PDF** : html2pdf.js
- **Données** : JSON statique (moniteur_nickel_nc.json)
- **Sources** : ISEE-NC, data.gouv.nc, FRED/IMF, BGS/DIMENC, INSG

---

## 📊 Sources de données

| Source | Description | Lien |
| :--- | :--- | :--- |
| **ISEE-NC** | Institut de la statistique et des études économiques de Nouvelle-Calédonie | [isee.nc](https://isee.nc/) |
| **data.gouv.nc** | Portail open data du gouvernement de la Nouvelle-Calédonie | [data.gouv.nc](https://data.gouv.nc/) |
| **FRED/IMF** | Federal Reserve Economic Data — série PNICKUSDM (prix nickel LME) | [fred.stlouisfed.org](https://fred.stlouisfed.org/series/PNICKUSDM) |
| **BGS** | British Geological Survey — production mondiale de nickel | [bgs.ac.uk](https://www.bgs.ac.uk/) |
| **INSG** | International Nickel Study Group — consommation mondiale | [insg.org](https://insg.org/) |
| **DIMENC** | Direction de l'industrie, des mines et de l'énergie (NC) | [dimenc.gouv.nc](https://dimenc.gouv.nc/) |
| **Eurostat** | Office statistique de l'Union européenne — commerce du nickel | [ec.europa.eu/eurostat](https://ec.europa.eu/eurostat) |

---

## 🧪 Modules experts

### 📉 Points de rupture (CUSUM)
Détection des changements structurels dans les séries via la méthode CUSUM (Cumulative Sum of deviations from mean). Seuil : ±2σ. Les points de rupture sont listés avec leur interprétation (hausse/baisse structurelle).

### 📅 Saisonnalité
Calcul des indices saisonniers mensuels sur la production métallurgique (2015–2025) et les cours LME. Indice 100 = moyenne. Mois > 105 (verts) = pics saisonniers, mois < 95 (rouges) = creux.

### ⚠️ Stress-test
5 scénarios préconfigurés + scénario personnalisé :

| Scénario | Impact production | Impact cours | Impact export |
| :--- | :--- | :--- | :--- |
| Choc pétrolier | -15 % | +10 % | -10 % |
| Récession mondiale | -20 % | -25 % | -20 % |
| Embargo chinois | -10 % | -30 % | -50 % |
| Grève générale | -30 % | +5 % | -30 % |
| Crise du nickel | -15 % | -50 % | -25 % |

L'intensité (10–100 %) est ajustable, ainsi que l'année de référence (2023, 2024, 2025).

### 🌍 Risque pays
Radar à 3 axes (économique, social, marché) + score global /100 + niveau (Faible / Modéré / Élevé / Très élevé).

### 🎲 Monte Carlo
1 000 à 10 000 simulations avec volatilité production et cours paramétrables. Histogramme des recettes, percentiles P5/P50/P95, intervalle de confiance 90 %.

---

## 📝 Licence

Ce projet est distribué sous licence **MIT**. Voir [LICENSE](LICENSE) pour plus de détails.

Les **données** restent la propriété de leurs émetteurs respectifs (ISEE, data.gouv.nc, FRED, BGS, INSG, Eurostat). Elles sont utilisées ici dans le cadre de leur licence ouverte (Licence Ouverte / Open Licence, Etalab).

---

## 🙏 Remerciements

- **ISEE-NC** pour la mise à disposition des données historiques
- **data.gouv.nc** pour l'API Opendatasoft
- **FRED/IMF** pour la série de prix nickel
- **BGS/DIMENC** pour la production mondiale
- **INSG/DIMENC** pour la consommation mondiale
- **Etalab** pour la Licence Ouverte

---

## 📬 Contact

Pour toute question ou suggestion : [ouvrir une issue](https://github.com/gunout/nickel-nc/issues).

---

<p align="center">
  <strong>Fait avec ❤️ pour la Nouvelle-Calédonie</strong><br>
  <em>Dernière mise à jour : octobre 2026</em>
</p>

---

<div align="center">

### 🇫🇷 Gunout · 2026

![Made in France](https://img.shields.io/badge/Made_in-France-002395?style=flat-square&labelColor=FFFFFF&logo=data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHZpZXdCb3g9IjAgMCA5MDAgNjAwIj48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjYwMCIgZmlsbD0iIzAwMjM5NSIvPjxyZWN0IHdpZHRoPSI5MDAiIGhlaWdodD0iNDAwIiB5PSIxMDAiIGZpbGw9IiNmZmYiLz48cmVjdCB3aWR0aD0iOTAwIiBoZWlnaHQ9IjIwMCIgeT0iNDAwIiBmaWxsPSIjZWQyOTM5Ii8+PC9zdmc+)
![GitHub](https://img.shields.io/badge/GitHub-gunout-181717?style=flat-square&logo=github&logoColor=white)
![Year](https://img.shields.io/badge/2026-ED2939?style=flat-square&labelColor=FFFFFF)

<sub>© 2026 <strong>Gunout</strong> — Tous droits réservés.</sub>

</div>
