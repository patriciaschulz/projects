def add_one(number)
    number + 1
end

def add_two(number)
    number = add_one(number)
    add_one(number)
end

number = 5
number = add_one(number)
number = add_two(number)
puts number
