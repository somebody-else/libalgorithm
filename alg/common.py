from datetime import datetime as dt

def ALG_DECORATOR(func):

    def wrapper(*args, **kwargs):
        start = dt.now().timestamp()
        ret = func(*args, **kwargs)
        end = dt.now().timestamp()

        cost = end - start

        print("Cost {} seconds".format(cost))
        return ret

    return wrapper