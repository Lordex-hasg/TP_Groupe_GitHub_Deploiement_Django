from django.test import TestCase
from django.urls import reverse

from .models import Categorie, Produit


class GestionStockTests(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Papeterie")
        self.produit = Produit.objects.create(
            nom="Cahier",
            quantite=3,
            seuil_alerte=5,
            categorie=self.categorie,
        )

    def test_liste_et_filtre_par_categorie(self):
        response = self.client.get(reverse("opp_stock:liste_produits"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cahier")

        autre_categorie = Categorie.objects.create(nom="Informatique")
        Produit.objects.create(
            nom="Clavier",
            quantite=10,
            seuil_alerte=2,
            categorie=autre_categorie,
        )
        response = self.client.get(
            reverse("opp_stock:liste_produits"),
            {"categorie": self.categorie.pk},
        )
        self.assertContains(response, "Cahier")
        self.assertNotContains(response, "Clavier")

    def test_ajout_et_modification_d_un_produit(self):
        url_ajout = reverse("opp_stock:ajouter_produit")
        donnees = {
            "nom": "Stylo",
            "quantite": "0",
            "seuil_alerte": "5",
            "categorie": str(self.categorie.pk),
        }
        response = self.client.post(url_ajout, donnees)
        self.assertRedirects(response, reverse("opp_stock:liste_produits"))
        stylo = Produit.objects.get(nom="Stylo")
        self.assertEqual(stylo.quantite, 0)

        response = self.client.post(
            reverse("opp_stock:modifier_produit", args=[stylo.pk]),
            {**donnees, "quantite": "8"},
        )
        self.assertRedirects(response, reverse("opp_stock:liste_produits"))
        stylo.refresh_from_db()
        self.assertEqual(stylo.quantite, 8)

    def test_la_suppression_exige_post(self):
        url = reverse("opp_stock:supprimer_produit", args=[self.produit.pk])
        self.assertEqual(self.client.get(url).status_code, 405)
        response = self.client.post(url)
        self.assertRedirects(response, reverse("opp_stock:liste_produits"))
        self.assertFalse(Produit.objects.filter(pk=self.produit.pk).exists())

    def test_alerte_uniquement_sous_le_seuil(self):
        egal_au_seuil = Produit.objects.create(
            nom="Classeur",
            quantite=5,
            seuil_alerte=5,
            categorie=self.categorie,
        )
        self.assertFalse(egal_au_seuil.est_en_alerte)
        response = self.client.get(reverse("opp_stock:alertes_stock"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cahier")
        self.assertNotContains(response, "Classeur")
