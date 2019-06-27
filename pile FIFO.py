from collections import deque

graph = {}

graph["you"] = ["alice","bob","claire"]
graph["bob"] = ["anuj","peggy"]
graph["alice"] = ["peggy"]
graph["claire"] = ["tom","jonny"]
graph["anuj"] = []
graph["peggy"] = []
graph["tom"] = []
graph["jonny"] = []



def person_is_seller(name):
  return name[-1] == "m"

def chercher(name):
  search_queue = deque()
  search_queue += graph[name]
  deja_vu = []
  while search_queue:
    person = search_queue.popleft()
    if not person in deja_vu:
      if person_is_seller(person):
        print(person + " is a mengo seller")
        return True
      else:
        search_queue += graph[person]
        deja_vu.append(person)
  return False
