from bs4 import BeautifulSoup
import requests
import random
import mail

response = requests.get("https://moirecepti.mk/category/rucek/%d0%bb%d0%b5%d1%81%d0%bd%d0%be")

soup = BeautifulSoup(response.text, "html.parser")

recipes = soup.findAll(name="li", class_="post")
random_recipe = random.choice(recipes)

recipe_title = random_recipe.find(name="h2").find(name="a").get("title")
recipe_link = random_recipe.find(name="h2").find(name="a").get("href")
print(recipe_title)
print(recipe_link)

# mail.send_mail(
#     subject="Предлог за ручек",
#     body=f"Име на јадењето: {recipe_title}\nЛинк од рецептот: {recipe_link}\n"
# )
