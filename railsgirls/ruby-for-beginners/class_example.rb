class Person
  def initialize(name, email)
    @name = name
    @email = email
  end

  def name
    @name
  end
end

one = Person.new("Ada Lovelace", "ada@lovelace.com")
other = Person.new("Yukihiro Matsumoto", "matz@ruby.org")

puts one.name
puts other.name
