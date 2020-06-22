![alt text](https://www.syfy.com/sites/syfy/files/styles/2280x1280_hero/public/2019/05/game_of_thrones_the_last_of_the_starks_0.jpg)

# Pipeline Project - Game of Thrones Character Deaths
This program takes the name of any character from the Game of Thrones fictional universe and outputs information related to the character. 

It is tailored towards those who have the read the books more than those who have merely watched the show since the dataset used is focused on the appearance and death of the characters in the book and not the show. However, any GoT fan will enjoy knowing certain facts such as the year of death. It is a very simple program since I spent most of the time wrangling the data and adding the actor names to the dataset. 

The program only takes one parameter: -n, which is the name of the character and must be written in quotes.

## Procedure

I retrieved the data from a Kaggle Game of Thrones dataset which offered raw data regarding the appearance and death of the characters in the books and enriched it with the character actor names for those fans of the show. However, keep in mind that only a handful of the characters in the books are actually portrayed with importance in the TV show. To enrich the dataset with the actors' names I tried using a Game of Thrones API with no luck and therefore had to scrape the character list wikipedia list in order to retrieve the names. 

## Libraries needed
Since all of the data was cleaned and enriched in a jupyter notebook the user will only need to import pandas as pd. 

