def add_one(number)
    number + 1
end

result = add_one(5)
result = add_one(result)
result = add_one(result)

puts result
