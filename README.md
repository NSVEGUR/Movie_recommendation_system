# Movie recommendation system

They are information filtering systems , where they improve quality of search results and provides items that are more related to the search or based on the previous history of the user. They are determined based on `rating` and `preferences` that a user would give to them. Even Amazon, youtube and facebook uses these recommendation systems to provide good results for the end users.

Over the top (OTT) platforms like Netflix and Prime Video use movie recommendation systems as their base strategy for success. In this project lets try to build a simple movie recommendation system.

![Netflix](Data/netflix.jpg)

There are three types of movie recommendation systems.

**👉🏻** **_Demographic filtering_**

> Here we offer generalized recommendation to every user just based on popularity and ratings of the movie and genre. This method simply assumes that a movie is most likely interested by user if average users got interested in that one.

**👉🏻** **_Content based filtering_**

> In this system we use users metadata, like his previous watch history and interests to recommend movies. This is a `supervised learning`.

**👉🏻** **_Collaborative filtering_**

> Here when metadata is not available, we match users with similar interests to one other and recommend systems. This is a `unsupervised learning`.

In this project we use tmdb 5000 movies and credits data set for training and evaluation.
