import shelve
with shelve.open('ShelfTest')as fruit:
    fruit['orange'] = "a sweet, orange , citrus fruit"
    fruit['apple'] = "good for making cider"
    fruit['lemon'] = "a sour, yellow , citrus fruit"
    fruit['grape'] = "a small,sweet fruit, growing in bunches"
    fruit['lime'] = "a sweet, orange , citrus fruit"

    print(fruit["lemon"])
    print(fruit["grape"])