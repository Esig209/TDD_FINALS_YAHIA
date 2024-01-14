1. **Test Creer compte ** Minute : 00.16.30
   - *Méthode :* `setUp`
   - *Description :* Vérifie que la méthode `créer_compte ` de la classe `CompteBancaire` creér un compte 
  
2. **Test de la Consultation du Solde** Minute : 04.05.00 
   - *Méthode :* `test_consulter_solde`
   - *Description :* Vérifie que la méthode `consulter_solde` de la classe `CompteBancaire` renvoie correctement le solde initial du compte.

3. **Test de l'Effectuation d'un Dépôt** Minute : 6:00 
   - *Méthode :* `test_effectuer_depot`
   - *Description :* Vérifie que la méthode `effectuer_depot` de la classe `CompteBancaire` augmente correctement le solde du compte après un dépôt.

4. **Test de l'Effectuation d'un Retrait** Minute : 9:08:00
   - *Méthode :* `test_effectuer_retrait`
   - *Description :* Vérifie que la méthode `effectuer_retrait` de la classe `CompteBancaire` diminue correctement le solde du compte après un retrait.

5. **Test de Retrait avec Solde Insuffisant** Minute : 11:18:20 
   - *Méthode :* `test_effectuer_retrait_solde_insuffisant`
   - *Description :* Vérifie que la méthode `effectuer_retrait` refuse le retrait si le solde du compte devient négatif, en respectant la limite de découvert.

6. **Test de Retrait avec Solde Suffisant** Minute : 15:58:30
   - *Méthode :* `test_effectuer_retrait_solde_suffisant`
   - *Description :* Vérifie que la méthode `effectuer_retrait` autorise le retrait si le solde du compte est suffisant.

7. **Test de Transfert d'Argent** Minute : 20:07:00
   - *Méthode :* `test_transfert_d_argent`
   - *Description :* Vérifie que la méthode `transfert_d_argent` de la classe `CompteBancaire` transfère correctement le montant spécifié du compte source au compte destinataire.

8. **Test de Consultation de l'Historique des Transactions** Minute : 26:20:00
   - *Méthode :* `test_consulter_historique`
   - *Description :* Vérifie que la méthode `consulter_historique` de la classe `CompteBancaire` retourne un historique correct des transactions, incluant les dépôts et les retraits.

9. **Test de Retrait après Reboot du Découvert** Minute : 29:42:31
   - *Méthode :* `test_retrait_apres_reboot_du_decouvert`
   - *Description :* Vérifie que la méthode `effectuer_retrait` autorise le retrait après un redémarrage du découvert, simulant une période passée depuis le dernier découvert.
