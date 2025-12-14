import json
import os
from datetime import datetime

def _log_path() -> str:
    base = os.path.dirname(__file__)
    return os.path.abspath(os.path.join(base, '.', 'parties.json'))


def enregistrer_partie(pseudo_blanc: str, pseudo_noir: str, pseudo_gagnant: str | None) -> None:
    """Enregistre le résultat d'une partie dans un fichier JSON
       L'entrée contient les pseudos des deux joueurs, la date et le pseudo du gagnant
       (ou la chaîne 'Nul' pour match nul)
    """
    path = _log_path()
    date_str = datetime.now().strftime("%Y:%m:%d %H:%M:%S")
    entree = {
        "blanc": pseudo_blanc,
        "noir": pseudo_noir,
        "gagnant": pseudo_gagnant if pseudo_gagnant is not None else "Nul",
        "date": date_str
    }

    try:
        if os.path.exists(path):
            with open(path, 'r', encoding='utf-8') as f:
                data = json.load(f)
                if not isinstance(data, list):
                    data = []
        else:
            data = []
    except Exception:
        data = []

    data.append(entree)

    os.makedirs(os.path.dirname(path), exist_ok=True)

    with open(path, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def lire_parties() -> list:
    path = _log_path()
    if not os.path.exists(path):
        return []
    try:
        with open(path, 'r', encoding='utf-8') as f:
            return json.load(f)
    except Exception:
        return []

