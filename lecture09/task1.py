import time
#Реализация таймера через функцию
def timer1(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        print('Время работы функции %s:' %func.__name__ + '\n' +
              str(time.time() - start_time) + ' cекунд.') 
        return result
    return wrapper


#Реализация таймера через класс
class timer2:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start_time = time.time()
        self.func(*args, **kwargs)
        end_time = time.time()

        print('Время выполнения функции %s' %self.func.__name__ + '\n' +
              str(end_time - start_time) + ' секунд.')
        

        
        
    

@timer1
def AnyFunction(k):
    time.sleep(k)

AnyFunction(2)

@timer2
def AnyFunction2(k):
    time.sleep(k)

AnyFunction2(2)


