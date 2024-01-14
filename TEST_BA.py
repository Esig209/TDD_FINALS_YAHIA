import unittest
from CompteBancaire import CompteBancaire
from datetime import datetime, timedelta


class TestCompteBancaire(unittest.TestCase):
    SOLDE_INITIAL = 1000

    def setUp(self):
        self.compte_a_decouvert = CompteBancaire ("Amine Sai", "Route 317 Esig", solde_initial=100)
        self.compte = CompteBancaire("Yahia Ben Hassine", "Chemin du Loup 23", solde_initial=self.SOLDE_INITIAL)
        self.destinataire = CompteBancaire("Jean du Jardin", "Chemin You Rock", solde_initial=500)

    def test_consulter_solde(self):
        self.assertEqual(self.compte.consulter_solde(),self.SOLDE_INITIAL)

    def test_effectuer_depot(self):
        self.compte.effectuer_depot(500)
        self.assertEqual(self.compte.consulter_solde(),self.SOLDE_INITIAL+500)

    def test_effectuer_retrait(self):
        self.compte.effectuer_retrait(200)
        self.assertEqual(self.compte.consulter_solde(), self.SOLDE_INITIAL - 200)

    def test_effectuer_retrait_solde_insuffisant(self):
        montant_retiré = 1200
        resultat_depasse_limite = self.compte.effectuer_retrait(montant_retiré)
        self.assertFalse(resultat_depasse_limite, f"Retrait {montant_retiré} autorisé")
        self.assertEqual(self.compte.consulter_solde(),1000,"Retrait non autorisé dû à limite de découvert ")

    def test_effectuer_retrait_solde_suffisant(self):
        self.assertTrue(self.compte.effectuer_retrait(500))


    def test_transfert_d_argent(self):
        self.compte.transfert_d_argent(self.destinataire, 300)
        self.assertEqual(self.compte.consulter_solde(), 700)
        self.assertEqual(self.destinataire.consulter_solde(),800)

    def test_consulter_historique(self):
        self.compte.effectuer_depot(300)
        self.compte.effectuer_retrait(100)
        historique = self.compte.consulter_historique()
        self.assertEqual(len(historique),2, "La longueur de l'historique n'est pas correcte")
        self.assertEqual(historique[0]['montant'], 300, "Le montant du dépôt dans l'historique n'est pas correct")
        self.assertEqual(historique[1]['montant'], -100, "Le montant du retrait dans l'historique n'est pas correct")

    def test_retrait_apres_reboot_du_decouvert(self):
        self.compte.effectuer_retrait(300)
        self.compte.date_dernier_decouvert = datetime.now() - timedelta(days=2)
        self.assertTrue(self.compte.effectuer_retrait(500))


if __name__ == '__main__':
    unittest.main()
