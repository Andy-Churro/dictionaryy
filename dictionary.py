# dictionary = a cllection of {key:values} pairs' ordered and changeable. No duplicates
capitals={"USA":"Washington D.C.", "India":"New Delhi", "China":"Bejing", "russia":"Moscow"}
# print(dir(capitals))
# # attributes for methods of the dictionary
# print(help(capitals))
# print(capitals.get("USA"))
# if capitals.get("Russia"):print("that capitol exist")
# else:print("that capitol doesn't exist")
# capitals.update({"Germany":"Barlin"})
# capitals.update({"Illinois":"Chicago"})
# capitals.pop("China")
# capitals.clear()
# keys=capitals.keys()
# print(keys)
# values=capitals.values()


# for values in capitals.values():print(values)


# items=capitols.items()
for key, value in capitals.items():print(f"{key}:{value}")