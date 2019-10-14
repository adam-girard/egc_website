my_list = [1, 2, 3, 4, 5]

my_tuple = (1, 2, 3, 4, 5)

my_set = {1, 2, 3, 4, 5}  # can't repeat

my_dict = {
    "Adam": "Cool Guy",
    "Will": "Also Cool Guy",
    "Gabriella": "Definitely Not Cool Guy",
}


def function(list):
    for i in list:
        yield i


x = lambda a: a + 10

list_ = [x * x for x in range(5)]

print(list_)
