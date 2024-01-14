1. **Test Creer compte ** Minute : 
   - *Méthode :* `setUp`
   - *Description :* Vérifie que la méthode `créer_compte ` de la classe `CompteBancaire` creér un compte 
  
2. **Test de la Consultation du Solde** Minute : 
   - *Méthode :* `test_consulter_solde`
   - *Description :* Vérifie que la méthode `consulter_solde` de la classe `CompteBancaire` renvoie correctement le solde initial du compte.

3. **Test de l'Effectuation d'un Dépôt** Minute : 
   - *Méthode :* `test_effectuer_depot`
   - *Description :* Vérifie que la méthode `effectuer_depot` de la classe `CompteBancaire` augmente correctement le solde du compte après un dépôt.

4. **Test de l'Effectuation d'un Retrait** Minute : 
   - *Méthode :* `test_effectuer_retrait`
   - *Description :* Vérifie que la méthode `effectuer_retrait` de la classe `CompteBancaire` diminue correctement le solde du compte après un retrait.

5. **Test de Retrait avec Solde Insuffisant** Minute : 
   - *Méthode :* `test_effectuer_retrait_solde_insuffisant`
   - *Description :* Vérifie que la méthode `effectuer_retrait` refuse le retrait si le solde du compte devient négatif, en respectant la limite de découvert.

6. **Test de Retrait avec Solde Suffisant** Minute : 
   - *Méthode :* `test_effectuer_retrait_solde_suffisant`
   - *Description :* Vérifie que la méthode `effectuer_retrait` autorise le retrait si le solde du compte est suffisant.

7. **Test de Transfert d'Argent** Minute : 
   - *Méthode :* `test_transfert_d_argent`
   - *Description :* Vérifie que la méthode `transfert_d_argent` de la classe `CompteBancaire` transfère correctement le montant spécifié du compte source au compte destinataire.

8. **Test de Consultation de l'Historique des Transactions** Minute : 
   - *Méthode :* `test_consulter_historique`
   - *Description :* Vérifie que la méthode `consulter_historique` de la classe `CompteBancaire` retourne un historique correct des transactions, incluant les dépôts et les retraits.

9. **Test de Retrait après Reboot du Découvert** Minute : 
   - *Méthode :* `test_retrait_apres_reboot_du_decouvert`
   - *Description :* Vérifie que la méthode `effectuer_retrait` autorise le retrait après un redémarrage du découvert, simulant une période passée depuis le dernier découvert.
