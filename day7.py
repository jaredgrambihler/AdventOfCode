
def containsShinyGold(bag, bagToTypes, visited):
    contains = bagToTypes[bag]
    for count, name in contains:
        if name in visited:
            if visited[name]:
                visited[bag] = True
                return
        if name.strip() == "shiny gold":
            visited[bag] = True
            return
        else:
            containsShinyGold(name, bagToTypes, visited)
            if visited[name]:
                visited[bag] = True
                return
    visited[bag] = False

def countInside(bag, bagToTypes):
    if bagToTypes[bag] == []:
        return 0
    else:
        minCount = 9999999
        totalMin = 0
        for count, name in bagToTypes[bag]:
            total = countInside(name, bagToTypes) * count + count
            totalMin += total
            
        print(f"{totalMin} in bag {bag}")
        return totalMin

def solve(inputF):
    with open(inputF, 'r') as f:
        text = f.read()
    bagToTypes = dict()
    for line in text.splitlines():
        if line.strip() == "":
            continue
        line = line[:-1]
        sections = line.split("bags contain")
        bagType = sections[0].strip()
        if "no other bags" == sections[1].strip():
            bagToTypes[bagType] = []
            continue
        inside = [x.strip() for x in sections[1].split(",")]
        insideCounts = [int(x.split()[0]) for x in inside]
        insideNames = [" ".join(x.split()[1:]) for x in inside]
        insideNames = [x.replace("bags", "").replace("bag", "").strip() for x in insideNames]
        bagToTypes[bagType] = [(c, n) for c, n in zip(insideCounts, insideNames)]
    count = 0
    d = dict()
    for bag in bagToTypes.keys():
        containsShinyGold(bag, bagToTypes, d)
    # return sum(d.values())
    start = "shiny gold"
    return countInside(start, bagToTypes)


print(solve("input/day7test2.txt"))
print(solve("input/day7input.txt"))