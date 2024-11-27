from website.models import SiteInfo  # Assurez-vous que SiteInfo est importé correctement
from elenizado.models import Publication, Categorie
from django.test import TestCase, Client
from django.urls import reverse

class TimelineViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.categorie = Categorie.objects.create(nom="Technologie")
        self.publication = Publication.objects.create(
            titre="Article Django",
            description="<p>Introduction à Django</p>",
            categorie=self.categorie,
        )
        # Crée un objet SiteInfo dans le modèle website avec les bons champs
        SiteInfo.objects.create(
            email="contact@site.com",
            nom="Site Info",
            telephone=1234567890,
            description="Description du site",
            logo="logo/site/logo.png",  # Assurez-vous que le chemin vers l'image est correct
            status=True
        )

    def test_timeline_view(self):
        response = self.client.get(reverse('timeline'))  # Assurez-vous que le nom de la vue correspond
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Article Django")

class DetailViewTest(TestCase):
    def setUp(self):
        self.client = Client()
        self.categorie = Categorie.objects.create(nom="Technologie")
        self.publication = Publication.objects.create(
            titre="Article Django",
            description="<p>Introduction à Django</p>",
            categorie=self.categorie,
            slug="article-django",
        )
        # Crée un objet SiteInfo dans le modèle website avec les bons champs
        SiteInfo.objects.create(
            email="contact@site.com",
            nom="Site Info",
            telephone=1234567890,
            description="Description du site",
            logo="logo/site/logo.png",  # Assurez-vous que le chemin vers l'image est correct
            status=True
        )

    def test_detail_view(self):
        response = self.client.get(reverse('detail', args=["article-django"]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Article Django")
