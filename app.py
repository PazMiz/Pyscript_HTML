import pymongo

# Replace 'your_username' and 'your_password' with your MongoDB Atlas credentials.
username = "Paz"
password = ""
cluster_name = "atlascluster.vkj98qo.mongodb.net"

# Construct the connection string without the 'srv' option
connection_string = f"mongodb://{username}:{password}@{cluster_name}/"

client = pymongo.MongoClient(connection_string)

# Access the 'car_database' database
db = client['car_database']

# Create a new collection named 'Cars'
collection = db['Cars']

# Insert documents into the 'Cars' collection
documents = [
    {"make": "Toyota", "model": "Corolla", "year": 2020},
    {"make": "Ford", "model": "Mustang", "year": 2019},
    {"make": "Honda", "model": "Civic", "year": 2021},
]

result = collection.insert_many(documents)
print("Inserted IDs:", result.inserted_ids)

# Query documents from the 'Cars' collection
result = collection.find_one({"make": "Ford"})
print("Query Result (One):", result)

results = collection.find({"year": {"$gt": 2020}})
print("Query Results (All):")
for doc in results:
    print(doc)

# Close the connection
client.close()
