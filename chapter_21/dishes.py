import multiprocessing


def washer(dishes, output):
    for dish in dishes:
        print(f"washing {dish} dish")
        output.put(dish)


def dryer(input):
    while True:
        dish = input.get()
        print(f"drying {dish} dish")
        input.task_done()


dish_queue = multiprocessing.JoinableQueue()
dryer_proc = multiprocessing.Process(target=dryer, args=(dish_queue,))
dryer_proc.daemon = True
dryer_proc.start()

dises = ["salad", "bread", "entree", "dessert"]
washer(dises, dish_queue)
dish_queue.join()