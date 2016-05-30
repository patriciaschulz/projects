class Person
  def initialize(name)
    @name = name
  end

  def name
    @name
  end

  def email=(email)
    @email = email
  end

  def email
    @email
  end
end

ada = Person.new("Ada Lovelace")
ada.email=("ada@lovelace.com")
puts ada.name
puts ada.email
