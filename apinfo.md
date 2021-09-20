## THE X FILES - Season 1 Sentiment API

- This API was created to make sentiment analysis with the dialogues of the episodes from season 1 from The X Files. Also, you're able to add new episodes dialogues and new characters if you wish. Here you you can find all the endpoints to use the data base. 


### ENDPOINTS

- With this endpoints you can get all the phrases by one character, all the phrases in one episode, or select the phrases of one character in one specific episode:

#### Get all the phrases by episode:
/phrasesbyepisode/name


#### Get all the phrases by character name:
/phrasesbycharacter/name


#### Get all the phrases by character name and episode:
/phrases/character/episode

- With this endpoints you can insert a new episode and/or a character, and new phrase:

#### Insert a new phrase by creating a new episode, also you can choose to add a new character (In this case, you'll have to insert the information through a dictionary):
/newphrase


#### Modify an already existing phrase (In this case, you'll also have to insert the information through a dictionary):
/modphrase

#### SENTIMENT ANALYSYS 

- With this endpoints you can get the sentiments of the phrases, you will get a measure of negativeness or positiveness:

#### Get the sentiment of all the phrases from one character in one episode:
/sentiment/character/episode


#### Get the mean sentiment of the phrases from one character in one episode:
/meansentiment/character/episode


#### Get the sentiment of all the phrases from both characters in one episode:
/sentiment/character1/character2/episode


#### Get the mean sentiment of all the phrases from both characters in one episode:
doublemeansentiment/character1/character2/episode