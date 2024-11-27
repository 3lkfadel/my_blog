from locust import HttpUser, task, between

# Définir une classe qui simule un utilisateur
class WebsiteUser(HttpUser):
    # Temps d'attente entre chaque tâche (en secondes)
    wait_time = between(1, 3)

    # Tâche 1 : Simuler un accès à la page d'accueil
    @task
    def load_home_page(self):
        self.client.get("/")  # Remplacer par l'URL de votre page d'accueil
    
    # Tâche 2 : Simuler un accès à une page de publication
    @task
    def load_publication_page(self):
        self.client.get("/publication/1")  # Remplacer par une URL spécifique de votre application

    # Tâche 3 : Simuler une soumission de formulaire (par exemple, un enregistrement)
    @task
    def submit_registration(self):
        self.client.post("/register", {
            "username": "test_user",
            "email": "test@example.com",
            "password": "password123"
        })
