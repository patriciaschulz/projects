numbers = [1,2,3,4,5,6,7,8,9,10]
numbers = numbers.select { |num| num.even? }
numbers.reverse!
numbers = [numbers] - [6]
p numbers
