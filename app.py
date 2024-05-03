"""
In this project, I'm exploring how to test basic endpoints using Flask and Postman. Flask is a web framework for Python, a
nd Postman is a popular API testing tool. The goal is to understand how to create simple APIs using Flask and then test them using Postman.

"""
from flask import Flask , request,jsonify
app = Flask(__name__)

carstores = [
  {
    "city_mpg": 18,
    "class": "midsize car",
    "combination_mpg": 21,
    "cylinders": 4,
    "displacement": 2.2,
    "drive": "fwd",
    "fuel_type": "gas",
    "highway_mpg": 26,
    "make": "toyota",
    "model": "camry",
    "transmission": "a",
    "year": 1993
  },
  {
    "city_mpg": 19,
    "class": "midsize car",
    "combination_mpg": 22,
    "cylinders": 4,
    "displacement": 2.2,
    "drive": "fwd",
    "fuel_type": "gas",
    "highway_mpg": 27,
    "make": "toyota",
    "model": "camry",
    "transmission": "m",
    "year": 1993
  }
]


animalsstores = [
  {
    "name": "Cheetah",
    "taxonomy": {
      "kingdom": "Animalia",
      "phylum": "Chordata",
      "class": "Mammalia",
      "order": "Carnivora",
      "family": "Felidae",
      "genus": "Acinonyx",
      "scientific_name": "Acinonyx jubatus"
    },
    "locations": [
      "Africa",
      "Asia",
      "Eurasia"
    ],
    "characteristics": {
      "prey": "Gazelle, Wildebeest, Hare",
      "name_of_young": "Cub",
      "group_behavior": "Solitary/Pairs",
      "estimated_population_size": "8,500",
      "biggest_threat": "Habitat loss",
      "most_distinctive_feature": "Yellowish fur covered in small black spots",
      "gestation_period": "90 days",
      "habitat": "Open grassland",
      "diet": "Carnivore",
      "average_litter_size": "3",
      "lifestyle": "Diurnal",
      "common_name": "Cheetah",
      "number_of_species": "5",
      "location": "Asia and Africa",
      "slogan": "The fastest land mammal in the world!",
      "group": "Mammal",
      "color": "BrownYellowBlackTan",
      "skin_type": "Fur",
      "top_speed": "70 mph",
      "lifespan": "10 - 12 years",
      "weight": "40kg - 65kg (88lbs - 140lbs)",
      "height": "115cm - 136cm (45in - 53in)",
      "age_of_sexual_maturity": "20 - 24 months",
      "age_of_weaning": "3 months"
    }
  }
]



history = [
  {
    "name": "Julius Caesar",
    "title": "Roman general and statesman",
    "info": {
      "born": "12 July 100 BC Rome Italy",
      "died": "15 March 44 BC Rome, Italy",
      "years": "81-45 BC",
      "awards": "Civic Crown",
      "office": [
        "Consul (59, 48, 46-45, 44 BC)",
        "Dictator (49-44 BC)"
      ],
      "parents": [
        "Gaius Julius Caesar",
        "Aurelia"
      ],
      "spouses": "Cossutia (disputed) Cornelia (m. 84 BC; d. 69 BC) Pompeia (m. 67 BC; div. 61 BC) Calpurnia (m. 59 BC)",
      "children": [
        "Julia",
        "Caesarion (unacknowledged)",
        "Augustus (adoptive)"
      ],
      "partners": "Cleopatra",
      "conflicts": [
        "War against Mytilene Siege of Mytilene",
        "Siege of Mytilene",
        "Third Mithridatic War",
        "Gallic Wars Battle of the Arar Battle of Bibracte Battle of Vosges Battle of the Axona Battle of the Sabis Siege of the Atuatuci Crossing of the Rhine Invasions of Britain Siege of Avaricum Siege of Gergovia Battle of Alesia Siege of Uxellodunum",
        "Battle of the Arar",
        "Battle of Bibracte",
        "Battle of Vosges",
        "Battle of the Axona",
        "Battle of the Sabis",
        "Siege of the Atuatuci",
        "Crossing of the Rhine",
        "Invasions of Britain",
        "Siege of Avaricum",
        "Siege of Gergovia",
        "Battle of Alesia",
        "Siege of Uxellodunum",
        "Caesar's Civil War Siege of Corfinium Siege of Brundisium Siege of Massilia Battle of Ilerda Siege of Oricum Siege of Dyrrhachium Siege of Gomphi Battle of Pharsalus Siege of Alexandria Battle of the Nile Battle of Zela Battle of Ruspina Battle of Thapsus Battle of Munda Siege of Corduba",
        "Siege of Corfinium",
        "Siege of Brundisium",
        "Siege of Massilia",
        "Battle of Ilerda",
        "Siege of Oricum",
        "Siege of Dyrrhachium",
        "Siege of Gomphi",
        "Battle of Pharsalus",
        "Siege of Alexandria",
        "Battle of the Nile",
        "Battle of Zela",
        "Battle of Ruspina",
        "Battle of Thapsus",
        "Battle of Munda",
        "Siege of Corduba"
      ],
      "occupation": [
        "Politician",
        "soldier"
      ],
      "notable_work": [
        "Bellum Gallicum",
        "Bellum Civile"
      ],
      "resting_place": "Temple of Caesar Rome 41deg53'31''N 12deg29'10''E / 41.891943degN 12.486246degE / 41.891943; 12.486246",
      "cause_of_death": "Assassination ( stab wounds )"
    }
  }
]

@app.route("/")
def home():
    return "hello this is project no 3 of test rest API  using postman"

@app.route("/allcars")
def all_sotres():
    return jsonify({"mycarsotres": carstores})
@app.route("/addcars", methods=["POST"])
def add_cars():
    request_add_car = request.get_json()
    new_car = {
        "city_mpg": request_add_car["city_mpg"],
        "class": request_add_car["class"],
        "combination_mpg": request_add_car["combination_mpg"],
        "cylinders": request_add_car["cylinders"],
        "displacement": request_add_car["displacement"],
        "drive": request_add_car["drive"],
        "fuel_type": request_add_car["fuel_type"],
        "highway_mpg": request_add_car["highway_mpg"],
        "make": request_add_car["make"],
        "model": request_add_car["model"],
        "transmission": request_add_car["transmission"],
        "year": request_add_car["year"],
        
    }
    carstores.append(new_car)
    return jsonify(new_car)

@app.route("/allanimals")
def all_animals():
    return jsonify({"animalsotres": animalsstores})

@app.route("/addanimals", methods=["POST"])
def add_animals():
    request_add_animals = request.get_json()
    new_animal={
        "name" : request_add_animals["name"],
        "locations":request_add_animals["locations"],
        "taxonomy": request_add_animals["taxonomy"],
        "characteristics" :request_add_animals["characteristics"]
        
    }
    animalsstores.append(new_animal)
    return jsonify((new_animal))

@app.route("/allhistory")
def all_history():
    return jsonify({"history": history})

@app.route("/addhistory", methods=["POST"])
def add_history():
    request_add_his = request.get_json()
    new_history = {
        "name" : request_add_his["name"],
        "title" : request_add_his["title"],
        "info" : request_add_his["info"]
    }
    history.append(new_history)
    return jsonify(new_history)

if __name__ == "__main__":
    app.run(debug=True,port=4001)
    
    
    
    
    
    """
<<<<<<-------------------------------for  testing the end points of addhistory ------------------------------------>>>>>>>>>   

  {
    "name": "Muhammad Ali Jinnah",
    "title": "Founder of Pakistan",
    "info": {
      "born": "25 December 1876, Karachi, British India",
      "died": "11 September 1948, Karachi, Pakistan",
      "years": "1876-1948",
      "awards": "Father of the Nation",
      "occupation": [
        "Lawyer",
        "Politician"
      ],
      "notable_work": [
        "Leader of All-India Muslim League",
        "Instrumental in the creation of Pakistan"
      ],
      "spouses": [
        "Emibai Jinnah",
        "Rattanbai Petit"
      ],
      "children": [
        "Dina Wadia"
      ],
      "conflicts": [
        "Indian independence movement",
        "Partition of India"
      ],
      "resting_place": "Mazar-e-Quaid, Karachi, Pakistan",
      "cause_of_death": "Tuberculosis"
    }
  },
  {
    "name": "Allama Iqbal",
    "title": "National Poet of Pakistan",
    "info": {
      "born": "9 November 1877, Sialkot, British India",
      "died": "21 April 1938, Lahore, British India",
      "years": "1877-1938",
      "occupation": [
        "Poet",
        "Philosopher",
        "Politician"
      ],
      "notable_work": [
        "The Reconstruction of Religious Thought in Islam",
        "Asrar-e-Khudi",
        "Bang-e-Dra",
        "Shikwa",
        "Jawab-e-Shikwa"
      ],
      "conflicts": [
        "Indian independence movement"
      ],
      "resting_place": "Mausoleum of Allama Iqbal, Lahore, Pakistan",
      "cause_of_death": "Complications from a throat disease"
    }
  }
#<<<<<<<<<<<<<-----------------------for  testing the end points of addhistory    ------------------------>>>>>>>


  {
    "name": "Elephant",
    "locations": [
      "Africa",
      "Asia"
    ],
    "taxonomy": {
      "kingdom": "Animalia",
      "phylum": "Chordata",
      "class": "Mammalia",
      "order": "Proboscidea",
      "family": "Elephantidae",
      "genus": "Elephas",
      "scientific_name": "Elephas maximus"
    },
    "characteristics": {
      "prey": "Grass, leaves, bark, roots",
      "name_of_young": "Calf",
      "group_behavior": "Herd",
      "estimated_population_size": "415,000",
      "biggest_threat": "Habitat loss, poaching",
      "most_distinctive_feature": "Large size, trunk, tusks",
      "gestation_period": "22 months",
      "habitat": "Forest, savannah, grassland",
      "diet": "Herbivore",
      "average_litter_size": "1",
      "lifestyle": "Diurnal",
      "common_name": "Elephant",
      "number_of_species": "3",
      "location": "Africa and Asia",
      "slogan": "The largest land animal on Earth!",
      "group": "Mammal",
      "color": "Gray",
      "skin_type": "Skin",
      "top_speed": "25 mph",
      "lifespan": "60 - 70 years",
      "weight": "2,268kg - 6,350kg (5,000lbs - 14,000lbs)",
      "height": "2.5m - 4m (8.2ft - 13ft)",
      "age_of_sexual_maturity": "10 - 20 years",
      "age_of_weaning": "3 - 4 years"
    }
  }
    
    """