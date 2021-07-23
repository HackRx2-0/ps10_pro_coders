import pandas as pd

name = ["abhay dhiman", "aaditya singhal", "ayush malik", "amandeep singh",
        "akshita sharma", "rekha verma", "manav dhiman", "raju rastogi"]
phone_number = ["1234567890", "7497827165", "9876543210",
                "9253371017", "5656565656", "1212121212", "1234567890", "1234567890"]
location = ["ambala city", "kurukshetra", "radaur", "ambala cantt",
            "karnal", "chandigarh", "ambala city", "hydrabad"]

id = [i for i in range(1, len(name) + 1)]


df = pd.DataFrame(
    {"id": id, "name": name, "location": location, "phone number": phone_number})
print(df.head())

df.to_csv("find_duplicates.csv", index=False)
