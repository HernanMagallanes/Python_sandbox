import json

pythonValue = {"name": "Zophie",
               "isCat": True,
               "miceCaught": 0,
               "felineIQ": None}

stringOfJsonData = json.dumps(pythonValue)
print(stringOfJsonData)
