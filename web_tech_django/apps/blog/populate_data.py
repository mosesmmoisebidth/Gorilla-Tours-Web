import os
import random
from datetime import datetime, timedelta
from .models import Tour
from faker import Faker

# Initialize Faker for generating random data
faker = Faker()

def populate_tours(n=100):
    """Populate the database with n random Tour entries."""
    for _ in range(n):
        name = faker.sentence(nb_words=4)  # Generate a random tour name
        description = faker.paragraph(nb_sentences=5)  # Generate random tour description
        started = faker.date_time_this_decade()  # Generate a random start date
        duration = random.randint(1, 30)  # Random duration in days
        price = random.randint(50, 1000)  # Random price
        image = f'tours/image_{random.randint(1, 50)}.jpg'  # Random image filename

        # Create and save the Tour object
        Tour.objects.create(
            name=name,
            description=description,
            started=started,
            duration=duration,
            price=price,
            image=image
        )

    print(f"{n} tours successfully populated!")

# Run the function
if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'myproject.settings')  # Replace 'myproject' with your project name
    import django
    django.setup()
    populate_tours(500)  # Inject 500 random tours
