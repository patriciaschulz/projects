class Person
  def initialize(name)
    @name = name
  end

  def name
    @name
  end

  def greet(other)
    puts "Hi " + other.name + "!"
  end
end

person = Person.new("little deer")
friend = Person.new("little racoon")

person.greet(friend)
person.greet(person)
