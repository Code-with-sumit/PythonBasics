def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ' , '. join(str(arg) for arg in args)
        kwrargs_value = ' , '.join(f"{k} = {v}" for k, v in kwargs.items())
    print(f"Calling: {func.__name__} with args: {args_value} and kwargs: {kwargs_value}")
    return func(*args, **kwargs)
    return wrapper

@debug
def hello():
    print("hello")
@debug 
def greet(name,greeting ="Hello"):
    Print(f"{greeting},{name}")
hello()
greet("Chai", greeting ="hanji")    
