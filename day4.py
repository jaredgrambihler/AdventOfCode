
def solve(inputF):
    with open(inputF, "r") as f:
        text = f.read()
    passports = []
    cur = ""
    for line in text.splitlines():
        if line.strip() == "":
            passports.append(cur)
            cur = ""
        else:
            cur += " " + line
    validCount = 0
    for passport in passports:
        valid = True
        fields = passport.split()
        fieldNames = set(field.split(":")[0] for field in fields)
        for field in ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']:
            if field not in fieldNames:
                print("not present: {}".format(field))
                valid = False
        if valid:
            validCount += 1
    return validCount

def solve2(inputF):
    with open(inputF, "r") as f:
        text = f.read()
    passports = []
    cur = ""
    for line in text.splitlines():
        if line.strip() == "":
            passports.append(cur)
            cur = ""
        else:
            cur += " " + line
    validCount = 0
    for passport in passports:
        valid = True
        fields = passport.split()
        fields = {field.split(":")[0] : field.split(":")[1] for field in fields}
        try:
            byr = int(fields['byr'])
            iyr = int(fields['iyr'])
            eyr = int(fields['eyr'])
            if byr < 1920 or byr > 2002:
                print("invalid byr: {}".format(byr))
                valid = False
                continue
            if iyr < 2010 or iyr > 2020:
                print("Invalid iyr {}".format(iyr))
                valid = False
                continue
            if eyr < 2020 or eyr > 2030:
                print(f"Invalid eyr {eyr}")
                valid = False
                continue
            height = fields['hgt']
            hgtUnit = height[-2:]
            hgtInt = int(height[:-2])
            height = fields['hgt']
            if hgtUnit == "cm" and hgtInt >= 150 and hgtInt <= 193:
                pass
            elif hgtUnit == "in" and hgtInt >= 59 and hgtInt <= 76:
                pass
            else:
                print("Error in height {}".format(height))
                valid = False
            hcl = fields['hcl']
            if hcl[0] != "#":
                print("Hcl missing #")
                valid = False
            if len(hcl[1:]) != 6:
                print("invalid hcl lenght")
                valid = False
            for char in hcl[1:]:
                if char not in [str(x) for x in range(10)] + ['a','b','c','d','e','f','g']:
                    print("illegal hcl char: {}".format(char))
                    valid = False
            if fields['ecl'] not in set(['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']):
                print("invalid elc field {}".format(fields['ecl']))
                valid = False
            if len(fields['pid'].strip()) != 9:
                print("invalid pid")
                valid = False
            foobar = int(fields['pid']) # check it is an int
        except Exception as e:
            print(e)
            valid = False
        if valid:
            validCount += 1
    print("Valid count: {}".format(validCount))
    return validCount
    

print(solve2("input/day4test2.txt"))
print(solve2("input/day4input.txt"))
