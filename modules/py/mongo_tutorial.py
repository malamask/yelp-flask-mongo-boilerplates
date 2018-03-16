import pymongo

client = pymongo.MongoClient('localhost', 27017)

db = client['yelp']


def insert_to_db(json_obj, collection_name):
    db[collection_name].insert(json_obj)


def find_restaurants_by_neighborhood(neighborhood):
    return db['restaurants'].find({'neighborhood': neighborhood})


def find_restaurant_by_id(id):
    return db['restaurants'].find_one({'business_id': id})


if __name__ == '__main__':
    ### Find all restaurants that belong to a neighbourhood
    restaurants = find_restaurants_by_neighborhood('Downtown')
    for r in restaurants:
        print(r)

    ### Find a restaurant by its id
    # id 'v0byOL8VL6v6muGa1anxFA' corresponds to "The Hummus Factory"
    restaurant = find_restaurant_by_id('v0byOL8VL6v6muGa1anxFA')

    # Access the entire json object
    print(restaurant)
    # Access properties based on dot notation
    print(restaurant['name'])

    ### Find