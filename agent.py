import time

# Constantes
SALE = "SALE"
PROPRE = "PROPRE"

class AgentAspirateur:
    def __init__(self, etat_A, etat_B):
        self.position = "A"
        self.etat = {
            "A": etat_A,
            "B": etat_B
        }
        self.temps = 0
        self.temps_max = 2  # minutes

    def nettoyer(self):
        if self.etat[self.position] == SALE:
            print(f"🧹 Nettoyage de la chambre {self.position}")
            self.etat[self.position] = PROPRE
            
        else:
            print(f"✅ Chambre {self.position} déjà propre")

        self.temps += 1
    def se_deplacer(self):
        self.position = "B" if self.position == "A" else "A"
        print(f"➡️ Déplacement vers la chambre {self.position}")

    def afficher_etat(self):
        print(f"⏱ Temps: {self.temps} min | Position: {self.position} | "
              f"A: {self.etat['A']} | B: {self.etat['B']}")
        print("-" * 50)

    def executer(self):
        print("🚀 Démarrage de la simulation\n")
        self.afficher_etat()

        while self.temps < self.temps_max:
            self.nettoyer()
            self.afficher_etat()
            self.se_deplacer()
            self.afficher_etat()

        print("🛑 Simulation terminée (2 minutes écoulées)")
        print(f"📌 État final : A={self.etat['A']} | B={self.etat['B']}")

## Cas 1 : Les deux chambres sont sales
agent = AgentAspirateur(SALE, SALE)
agent.executer()

## Cas 2 : Chambre A sale, B propre
# agent = AgentAspirateur(SALE, PROPRE)
# agent.executer()

## Cas 3 : Chambre A propre, B sale
# agent = AgentAspirateur(PROPRE, SALE)
# agent.executer()

## Cas 4 : Les deux chambres propres
# agent = AgentAspirateur(PROPRE, PROPRE)
# agent.executer()