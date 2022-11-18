#%%
from user import User
from timeline import Timeline

timeline = Timeline()

elon = User("elonmusk", "Elon Musk", "Self made", timeline)
pepe = User("pepe", "Pepe", "Not Self made", timeline)
wendy = User("wendy", "Wendy", "", timeline)
fran = User("fran", "Fran", "Hello", timeline)

elon.follow(wendy)
pepe.follow(elon)
wendy.follow(elon)
wendy.follow(fran)
fran.follow(pepe)

elon.tweet("Let that sink in")
fran.tweet("Yes, please")
pepe.tweet("Look at this potato")

timeline.show_tweets_for(fran)

# %%
