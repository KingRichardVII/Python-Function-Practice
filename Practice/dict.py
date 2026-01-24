# dict = keys and values
# create dict by using {"key": value}
# .update({"key": value}) //to update new key/value pair into dict
# {dictName.get("key", "error message if fail to get")} //to access key/value

def main():
    # create keys and values
    car = {"model": "Honda Civic 2015", "color": "Silver", "mileage": 55000}

    # add a key to an existing dictionary
    car["cylinders"] = 4
    print(create_report(car))

    # .update, alternate way to add new key to existing dict
    car.update({"weight": 3, "height": 5})


# .get to grab the value of the key instead of brackets, can return the value you set if key not found ("Unknown" in this case)
def create_report(car):
    return f"""
    ===== Report =====

    Model: {car["model"]} 
    Color: {car["color"]}
    Mileage: {car.get("mileage")} miles
    Cylinders: {car["cylinders"]} cylinders
    Last Oil Change: {car.get("oil change", "Unknown Date")}
    Weight: {car.get("weight", "Unknown Weight")} tons
    Height: {car.get("height", "Unknown Height")} ft

    ==================
    """


main()

# finish dict short and write practice program. Timestamp: 11:35