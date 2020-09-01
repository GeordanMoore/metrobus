import logging
logging.basicConfig(level=logging.DEBUG)

def squared_threes():
    return_value = []
    for value in range(0,99):
        if value %3 == 0:
            return_value.append(value ** 2)
    return return_value

if __name__ == "__main__":
    for value in squared_threes():
        print(value)
