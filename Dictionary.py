def dictionary_operations():
    students = {
        "Alemu": 20,
        "Barnabas": 21,
        "Melat": 19
    }
    print(f"Original dictionary: {students}")
    students["David"] = 22
    print(f"After adding David: {students}")
    students["Barnabas"] = 22
    print(f"After updating Barnabas's Age: {students}")
    del students["Alemu"]
    print(f"After removing Alemu: {students}")

dictionary_operations()