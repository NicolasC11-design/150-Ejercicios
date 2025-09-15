dic = {"a": 10, "b": 50, "c": 30}
max_clave = max(dic, key=dic.get)
print("Clave con valor máximo:", max_clave)