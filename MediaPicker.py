import random
from time import sleep

Movies = ['12 Monkeys','21 Jump Street','22 Jump Street','American Psycho','An American Pickle','Apollo 13','Archive','Atomic Blonde','Avatar','Baby Driver','Bird Box','Blade Runner','Bloodshot','Casino','Catch Me If You Can','CHAPPiE','Cube','Death On The Nile','Death Wish','Deja Vu','Demolition Man','Dodgeball','Dog','Dont Look Up','Dredd','Edge of Tomorrow','Enders Game','eXistenZ','Ex Machina','Fargo','Ferris Buellers Day Off','Five Feet Apart','Flubber','Forrest Gump','Free Guy','Free Willy','Gattaca','Ghost in the Shell','Good Boys','Good Will Hunting','Green Lantern','Grosse Pointe Blank','Groundhog Day','Guns Akimbo','Hacker','Hackers','Hamilton','Hancock','Happy Gilmore','Heat','Hobo With a Shotgun','Holmes & Watson','Home Alone','I Am Mother','iBoy','Infinity Chamber','In Time','I, Robot','Jaws','Jolt','Knives Out','legally Blonde','Liar Liar','Limitless','Looper','Lucy','Minority Report','Monty Python and the Holy Grail','Nobody','Office Space','Passengers','Peppermint','Pretty in Pink','Pulp Fiction','Ready Player One','Run','Shaun of the Dead','Shooter','Short Circuit','Snakes on a Plane','Spaceballs','Stowaway','Stripes','The Adam Project','The Cloverfield Paradox','The Gentleman','The Goonies','The Greatest Showman','The Great Outdoors','The Martian','The Michells vs The Machines','The Shawshank Redemption','The Truman Show','The Wolf of Wall Street','Tommy Boy','Top Gun','Total Recall','Transendence','Uncharted','Uncle Buck','Upgrade','WALL-E','War Dogs','Wargames','Wedding Crashers','Weird Science','Youve Got Mail','Back to The Future (Series)','Die Hard (Series)','Divergent (Series)','Final Destination (Series)','Harry Potter (Series)','Iron Man (Series)','John Wick (Series)','Men In Black (Series)','Spider-Man (Series)','Star Wars (Series)','Terminator (Series)','The Hunger Games (Series)','The Kingsman (Series)','The Matrix (Series)']

Random_Movie = random.choice(Movies)

TVShows = ['13 Reasons Why (2017)','Away (2020)','Brave New World (2020)','Breaking Bad (2008)','Brooklyn Nine-Nine (2013)','Containment (2016)','House M.D. (2004)','Inside Job (2021)','Invincible (2021)','Looking for Alaska (2019)','Lost in Space (2018)','Modern Family (2009)','Mr. Robot (2015)','Reacher (2022)','Rick and Morty (2013)','Silicon Valley (2014)','Space Force (2020)','The Big Bang Theory (2007)','The IT Crowd (2006)','The Office (2005)','Upload (2020)']

Random_TVShow = random.choice(TVShows)

Audiobook = ['13 Reasons Why','1984','Brave New World','Dry','Fahrenheit 451','Five Feet Apart','Hidden Figures','Looking for Alaska','Providence','Ready Player One','Ready Player Two','The Giver','The Martian','The Program','Divergent (Series)','Harry Potter (Series)','UNWIND (Series)']

Random_Audiobook = random.choice(Audiobook)

print("What kind of media do you want? (Movie, TV Show, Audiobook) - ")
media = input(" ")

if media == ("Movie"):
    print(' --- ')
    print(Random_Movie)
    print( )

if media == ("TV Show"):
    print(' --- ')
    print(Random_TVShow)
    print( )

if media == ("Audiobook"):
    print(' --- ')
    print(Random_Audiobook)
    print( )
