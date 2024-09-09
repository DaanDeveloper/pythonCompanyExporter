import json

company = str(input("Enter a company name: "))

with open("results.json") as result:
   companies = json.load(result)

if company not in companies:
   print("Company not found")

else:
   employers = companies[company]["employers"]

   employees = []

   for employer in employers:
      name = employer["name"]
      website = employer["website"]
      country = employer["country"]
      foundingYear = employer["foundingYear"]
      amountOfEmployees = employer["employees"]

      companyEmployees = {}
      companyEmployees["name"] = name
      companyEmployees["website"] = website
      companyEmployees["country"] = country
      companyEmployees["employees"] = amountOfEmployees

      companyEmployeesDict = {}
      companyEmployeesDict[company] = companyEmployees

      with open(f"{company}.json", "w", encoding="UTF-8") as writeFile:
         json.dump(companyEmployeesDict, writeFile, indent=3)

      employees.append([name, website, country, amountOfEmployees])

   print("Names:".ljust(50)+"Website:".ljust(50)+"Country:".ljust(50)+"Amount Of Employees:".ljust(50))
   print("\n")

   for x in employees:
      for y in x:
         print(y.ljust(50), end="")

      print("")