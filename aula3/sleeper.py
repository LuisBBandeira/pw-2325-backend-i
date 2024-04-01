import time


def timer(func: callable):
    def wrapper(*args,**kwargs):
        start_time = time.perf_counter()
        result = func(*args,**kwargs)
        end_time = time.perf_counter()
        total_time = end_time - start_time
        print(f"Function {func.__name__} {args} {kwargs} Took{total_time:} seconds")
        return result
    return wrapper

@timer
def do_things():
    time.sleep(3)

@timer
def execute()->None:
    do_things()
    time.sleep(1)

if __name__ =="__main__":
    execute()