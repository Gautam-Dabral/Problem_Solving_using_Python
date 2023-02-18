# the order of execution in case of 
# decorator chaining is "from inside to outside".

def python(func):
    def wrapper():
        return func() + " Python"
    return wrapper

def decorator(func):
    def wrapper():
        return func() + " Decorator"
    return wrapper

@python
@decorator
def hello():
    return "hello"

print(hello()) # => hello Decorator Python