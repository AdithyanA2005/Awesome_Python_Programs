# We are importing 're' to cancel some characters mentioned below
import re


# We are creating the function 'spaceCancel' to cancel the additional
# spaces made by the user's input
def spaceCancel(Search):
    return Search.replace(" ", "")


# We are creating a dictionary 'dic' to store the meanings of the words, and we will only write the keyword of the
# dictionary in lower case only

dic = {
    spaceCancel("accidial"): "dial someone's number on phone accidentally",
    spaceCancel("agender"): "people do not identify as male or female",
    spaceCancel("airball"): "completely miss the basket, rim, and backboard with a shot",
    spaceCancel("automagically"): "a way that seems magical, especially by computer",
    spaceCancel("awesomesauce"): "extremely good; excellent",
    spaceCancel("bargainous"): "costing less than expected, cheap or relatively cheap",
    spaceCancel("barista"): "a person whose job involves preparing and serving different types of coffee",
    spaceCancel("bedunged"): "has been soiled with or covered in dung; very old or old-fashioned",
    spaceCancel("binge watch"): "watch multiple episodes of a television program in rapid succession",
    spaceCancel("bitcoin"): "an online payment system that does not require an intermediary",
    spaceCancel("bling"): "jewellery, decoration, or clothing that attracts attention because looks expensive",
    spaceCancel("blog"): "regularly updated website or web page, typically one run by an individual or small group",
    spaceCancel("bokeh"): "visual quality of the out-of-focus areas of a photographic image, especially as rendered by a particular lens",
    spaceCancel("bongga"): "extravagant, flamboyant, impressive, stylish, or excellent",
    spaceCancel("brexit"): "a term for the potential or hypothetical departure of the United Kingdom from the European Union",
    spaceCancel("bromance"): "a close but non-sexual relationship between two men",
    spaceCancel("buko"): "coconut, coconut water; a person who is less than 5ft tall and really angry",
    spaceCancel("butt dial"): "inadvertently call on a mobile phone in one's rear pants pocket, as a result of pressure being accidentally applied to buttons on the phone",
    spaceCancel("butt hurt"): "inappropriately strong negative emotional response from a perceived personal insult, strong feelings of shame",
    spaceCancel("buzzkill"): "person or thing that has a depressing effect",
    spaceCancel("catastrophize"): "present a situation as worse than it is",
    spaceCancel("cheeseball"): "lacking taste, style, or originality",
    spaceCancel("chillax"): "calm down and relax",
    spaceCancel("clickbait"): "online content to attract more visitors to a particular website",
    spaceCancel("conlang"): "an invented language intended for human communication",
    spaceCancel("cool hunter"): "one who predicts new styles and trends",
    spaceCancel("crema"): "a brownish foam that forms on the top of freshly made coffee",
    spaceCancel("crowdfund"): "fund a project from lots of people who usually donate a small amount",
    spaceCancel("crunk"): "very excited or full of energy",
    spaceCancel("dark web"): "part of the Internet intentionally hidden from search engines with masked IP addresses, usually illegal content",
    spaceCancel("droolworthy"): "extremely attractive or desirable",
    spaceCancel("ear tickler"): "someone who pleases other people with paying lot of compliments or flattering",
    spaceCancel("echo chamber"): "an environment in which a person encounters only beliefs or opinions that coincide with their own, especially in social media",
    spaceCancel("eggcorn"): "word or phrase that results from a mishearing because of similar sounds",
    spaceCancel("emoji"): "a small digital image or icon used to express an idea, emotion",
    spaceCancel("facepalm"): "cover one's face with the hand as an expression of embarrassment, dismay, or exasperation",
    spaceCancel("facerape"): "hack someone's social-media profile in order to fiddle with its personal information or to post fake status updates",
    spaceCancel("fast fashionan"): "approach that emphasizes making fashion clothing trends quickly and cheaply available to consumers",
    spaceCancel("flash mob"): "brief public gathering for a common purpose, typically organized by the Internet or social media ",
    spaceCancel("fomo"): "the fear of missing out, the anxiety that an exciting or interesting event may currently be happening elsewhere",
    spaceCancel("foodie"): "a person with a particular interest in food; a gourmet",
    spaceCancel("frankenfood"): "genetically modified food",
    spaceCancel("freegan"): "a person who rejects consumerism and seeks to help the environment by reducing waste",
    spaceCancel("frenemy"): "a person with whom one is friendly despite a fundamental dislike",
    spaceCancel("frousin"): "a friend that is a cousin or a cousin that is a friend, very close relationship as family members",
    spaceCancel("froyo"): "frozen yogurt, a slightly sour thick food made from milk, and often sugar and fruit",
    spaceCancel("gig economy"): "a labor market characterized by short-term contracts or work as opposed to permanent jobs",
    spaceCancel("ginger"): "a person with red hair",
    spaceCancel("glamping"): "outdoor camping with amenities and comforts, such as beds and electricity, not usually used when camping",
    spaceCancel("hangry"): "bad-tempered or irritable as a result of hunge",
    spaceCancel("homeshoring"): "moving jobs to employees' homes from offices or factories",
    spaceCancel("humblebrag"): "make a seemingly modest or self-critical to draw attention to something of which one is proud",
    spaceCancel("hyperconnected"): "characterized by the widespread or habitual use of devices that have Internet connectivity",
    spaceCancel("hypermiling"): "altering a car to maximize its fuel economy",
    spaceCancel("idiocracy"): "an act or actions that come from ideas or beliefs that are not smart",
}

# We are taking the input from the user and using it to search the dictionary keyword. We are using the imported "re"
# module to cancel any any special character entered by the user and making the string to lower case as the keyword in
# dictionary is also lowercase.
varSearch = re.sub('[\W_]+', '', str.lower(input("Search \n")))

# now we are making a copy of the variable "varSearch" as "keyword" for searching it in the dictionary with cancelled
# space using function 'spaceCancel' as we have written the dictionary in lower case
keyword = spaceCancel(varSearch)
# if keyword=

# now we are reshowing the keyword to the user which we have used to search the dictionary for the users input
print(f"The meaning of the word {keyword.capitalize()} :-")

# we are using this code to show the meaning of the keyword stored in the dictionary
print(dic[keyword].capitalize())
