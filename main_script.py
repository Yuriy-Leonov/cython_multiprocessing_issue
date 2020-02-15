import multiprocessing

if __name__ == '__main__':
    print("step-1")
    multiprocessing.set_start_method("spawn")
    print("step-2")
    multiprocessing.freeze_support()
    print("step-3")
    manager = multiprocessing.Manager()
    print("step-4")
    s_dict = manager.dict()
    print("finish")
