from django.test import TestCase
from elenizado.models import Categorie, Publication, Commentaire, Like, Evenement

class CategorieModelTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(
            nom="Technologie",
            description="Catégorie sur la technologie"
        )

    def test_categorie_creation(self):
        self.assertEqual(self.categorie.nom, "Technologie")
        self.assertTrue(self.categorie.status)

class PublicationModelTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Technologie")
        self.publication = Publication.objects.create(
            titre="Article Django",
            description="<p>Introduction à Django</p>",
            categorie=self.categorie,
        )

    def test_publication_creation(self):
        self.assertEqual(self.publication.titre, "Article Django")
        self.assertEqual(self.publication.categorie.nom, "Technologie")
        self.assertTrue(self.publication.status)

class CommentaireModelTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Technologie")
        self.publication = Publication.objects.create(
            titre="Article Django",
            description="<p>Introduction à Django</p>",
            categorie=self.categorie,
        )
        self.commentaire = Commentaire.objects.create(
            publication=self.publication,
            nom="Alice",
            email="alice@example.com",
            commentaire="Très intéressant !",
        )

    def test_commentaire_creation(self):
        self.assertEqual(self.commentaire.nom, "Alice")
        self.assertEqual(self.commentaire.publication, self.publication)

class LikeModelTest(TestCase):
    def setUp(self):
        self.categorie = Categorie.objects.create(nom="Technologie")
        self.publication = Publication.objects.create(
            titre="Article Django",
            description="<p>Introduction à Django</p>",
            categorie=self.categorie,
        )
        self.like = Like.objects.create(publication=self.publication)

    def test_like_creation(self):
        self.assertEqual(self.like.publication.titre, "Article Django")
