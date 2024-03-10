import DatabaseConnections

db = DatabaseConnections.DatabaseConnect()

user = db.retrieve_from_user("test_user")

print(user["password"])
