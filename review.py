# Review 1
def add_to_list(value, my_list=[]):
    my_list.append(value)
    return my_list


# Changed 1
def add_to_list_changed(value, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(value)
    return my_list


"""
Explain & Examples

@Explain:
my_list=[] means: we have a global empty list,and when you invoke the function,and the list will add the value continually.
So now we change it into default list
1.If we don't input my_list parameter,and we just add the value.
2.Next we input my_list parameter,and we will add the value at the ending of the list.

@Examples:
As follows
"""
print("------review 1 starts------")
print(add_to_list_changed(1))
print(add_to_list_changed(2))
print(add_to_list_changed(3, [1, 2]))
print("------review 1 ends------")
print("")


# Review 2
def format_greeting(name, age):
    return "Hello, my name is {name} and I am {age} years old."


# Changed 2
def format_greeting_changed(name, age):
    return f"Hello, my name is {name} and I am {age} years old."


"""
Explain & Examples

@Explain:
Name and age can't replace into the {name} and {age},
We need to use python grammar:"f-string" to implement the function.

@Examples:
As follows
"""
print("------review 2 starts------")
print(format_greeting_changed("ChuLin", 25))
print("------review 2 ends------")
print("")


# Review 3
class Counter:
    count = 0

    def __init__(self):
        self.count += 1

    def get_count(self):
        return self.count


# Changed 3
class CounterChanged:
    count = 0

    def __init__(self):
        CounterChanged.count += 1

    def get_count(self):
        return self.count


"""
Explain & Examples

@Explain:
Counter is a class, count is a variable that belongs to the class.
but when you create an Object, 'self.count' is a variable belongs to the Object, and you invoke the method:get_count(), the result is 1.
And you create an Object again, and invoke again, the result is still 1.
So i want to express it is 1 forever, no matter how many times you created.
So change "self.count" into "CounterChanged.count" in the "__init__" method.
And when you invoke the class, and will count times.

@Examples:
As follows
"""
print("------review 3 starts------")
a = CounterChanged()
print(f"The {a.get_count()} time to invoke the class")
b = CounterChanged()
print(f"The {b.get_count()} time to invoke the class")
print("------review 3 ends------")
print("")

# Review 4
import threading


class SafeCounter:
    def __init__(self):
        self.count = 0

    def increment(self):
        self.count += 1


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter = SafeCounter()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

# Changed 4
import threading


class SafeCounterChanged:
    def __init__(self):
        self.count = 0
        self.lock = threading.Lock()

    def increment(self):
        with self.lock:
            self.count += 1


def worker(counter):
    for _ in range(1000):
        counter.increment()


counter_changed = SafeCounterChanged()
threads = []
for _ in range(10):
    t = threading.Thread(target=worker, args=(counter_changed,))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

"""
Explain & Examples

@Explain:
The original question didn't manage multi-threading,in concurrent scenarios,the accumulation of numbers may generate 
errors, which could lead to the data loss and so on.We need to add lock to avoid this situation.
So I add the lock into "__init__" method not class,because when we create two object,we just have only one lock,the
performance is low,so we add it into "__init__",and different objects will have their own lock.
@Examples:
As follows
"""
print("------review 4 starts------")
print(counter_changed.count)
print("------review 4 ends------")
print("")


# Review 5
def count_occurrences(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] = + 1
        else:
            counts[item] = 1
    return counts


# Changed 5
def count_occurrences_changed(lst):
    counts = {}
    for item in lst:
        if item in counts:
            counts[item] += 1
        else:
            counts[item] = 1
    return counts


"""
Explain & Examples

@Explain:
counts[item] = + 1 : This will make the count keep 1 forever.
But we want to add 1 every time to record the times that it exists.
So change "=+" into "+="
@Examples:
As follows
"""
print("------review 5 starts------")
print(count_occurrences_changed([1, 2, 3, 4, 3, 2]))
print("------review 5 ends------")
print("")
