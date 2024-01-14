import uuid
from datetime import datetime, timedelta


class CompteBancaire:

    def __init__(self, proprietaire, adresse, solde_initial=0, limite_decouvert_quotidien=0):
        self.proprietaire = proprietaire
        self.adresse = adresse
        self.solde = solde_initial
        self.historique = []
        self.limite_decouvert_quotidien = limite_decouvert_quotidien
        self.date_dernier_decouvert = datetime.now()

    def consulter_solde(self):
        return self.solde

    def effectuer_depot(self, montant):
        self.solde += montant
        self._ajouter_transaction(montant)

    def effectuer_retrait(self, montant ):
        if self._autoriser_retrait(montant):
            self.solde -= montant
            self._ajouter_transaction(-montant)
            return True
        else:
            return False

    def _autoriser_retrait(self, montant):
        if self.solde - montant >= self._limite_decouvert_reboot(montant):
            return True
        else :
            return False

    def transfert_d_argent(self, destinaire, montant):
        if self._autoriser_retrait(montant):
            self.solde -= montant
            destinaire.effectuer_depot(montant)
            self._ajouter_transaction(-montant, destinaire.proprietaire)
            return True
        else :
            return False

    def consulter_historique(self):
        return self.historique

    def _ajouter_transaction(self, montant, destinataire=None):
        transaction = {'montant': montant, 'date': datetime.now(), 'destinataire': destinataire}
        self.historique.append(transaction)

    def _limite_decouvert_reboot(self, montant):
        maintenant = datetime.now()
        if maintenant - self.date_dernier_decouvert > timedelta(days=1):
            self.solde = max(0, self.solde + self.limite_decouvert_quotidien)
            self.date_dernier_decouvert = maintenant
        return self.solde + montant < -self.limite_decouvert_quotidien




