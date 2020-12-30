from pymongo import MongoClient

def connectDB():
    try:
        myclient = MongoClient('localhost',27017)
        mydb = myclient["Dashboard"]
        myclient.close()
        return mydb
    except:
        print('errors in getMongoDBData function')

def getValues():
    numbers = []
    mydb = connectDB()
    for y in tables:
        mycoll=mydb[y]
        for x in mycoll.find({"number":{ "$gte": 0 }}):
          numbers.append(x[u'number'])
    print(numbers)
    return numbers


tables = ["workingDays", "presentations", "moneyEarned", "visitedCountries", "vaccinations"]