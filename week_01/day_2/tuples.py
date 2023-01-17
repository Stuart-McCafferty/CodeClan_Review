#Stuart McCafferty

tuples1 = 'Ford', 'BMW', 'Honda', 'Ford'
tuples2 = ('Ford', 'BMW', 'Honda')
single_tuple = 'Ford',
empty_tuple1 = ()
empty_tuple2 = tuple()

print(tuples1)
print(tuples2)
print(single_tuple)
print(empty_tuple1)
print(empty_tuple2)

# Immutability CANNOT CHANGE

print(tuples1[1])
print(len(tuples1))
print(tuples1.count('Ford'))
print(tuples2.count('Ford'))