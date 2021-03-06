import pymongo

client = pymongo.MongoClient('localhost', 27017)
db = client['yelp']


def find_all(collection_name):
    return db[collection_name].find({})


def find_count(collection_name):
    return db[collection_name].find({}).count()


def find_top_restaurants(num):
    return db['restaurants'].find({}, {'_id': False}).sort([('review_count', pymongo.DESCENDING)]).limit(num)


def find_random_reviews(num):
    random_reviews = db['reviews'].aggregate([{'$sample': {'size': num}}])
    random_reviews = list(random_reviews)

    for review in random_reviews:
        review['restaurant_name'] = db['restaurants'].find_one({'business_id': review['business_id']})['name']
        review['user_name'] = db['users'].find_one({'user_id': review['user_id']})['name']
    return random_reviews
