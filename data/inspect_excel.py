#!/usr/bin/env python3
"""Inspecte la structure des fichiers Excel ISEE."""
import pandas as pd
from pathlib import Path

DATA = Path("data")
FILES = {
    "coursnickel.xls": "Cours LME",
    "exportations-nickel.xls": "Exportations",
    "extraction-nickel.xls": "Extraction",
    "marchemondial.xls": "Marché mondial",
    "poids-nickel.xls": "Poids secteur",
}

for fname, label in FILES.items():
    path = DATA / fname
    if not path.exists():
        print(f"⚠️  {fname} manquant")
        continue
    print(f"\n{'='*70}")
    print(f"📄 {label} — {fname}")
    print(f"{'='*70}")
    try:
        sheets = pd.read_excel(path, sheet_name=None, engine="xlrd", header=None)
        for sname, df in sheets.items():
            print(f"\n  📑 Feuille : '{sname}' — {df.shape[0]} lignes × {df.shape[1]} colonnes")
            # Afficher les 15 premières lignes, 8 premières colonnes
            preview = df.iloc[:15, :8].fillna("")
            print(preview.to_string(max_colwidth=25))
    except Exception as e:
        print(f"  ⚠️  Erreur : {e}")