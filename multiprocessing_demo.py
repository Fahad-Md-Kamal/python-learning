import concurrent.futures
import time
from PIL import Image, ImageFilter




def do_something(img_name):
    size = (1200, 1200)
    img = Image.open(img_name)
    img = img.filter(ImageFilter.GaussianBlur(15))
    img.thumbnail(size)
    img.save(f'processed/{img_name}')
    print(f"Processed complete {img_name.split('-', 1)[1]}")


if __name__ == '__main__':
    start = time.perf_counter()
    img_names = [
    'photo-1516117172878-fd2c41f4a759qq.jpg',
    'photo-1532009324734-20a7a5813719.jpg',
    'photo-1524429656589-6633a470097c.jpg',
    'photo-1530224264768-7ff8c1789d79.jpg',
    'photo-1564135624576-c5c88640f235.jpg',
    'photo-1541698444083-023c97d3f4b6.jpg',
    'photo-1522364723953-452d3431c267.jpg',
    'photo-1513938709626-033611b8cc03.jpg',
    'photo-1507143550189-fed454f93097.jpg',
    'photo-1493976040374-85c8e12f0c0e.jpg',
    'photo-1504198453319-5ce911bafcde.jpg',
    'photo-1530122037265-a5f1f91d3b99.jpg',
    'photo-1516972810927-80185027ca84.jpg',
    'photo-1550439062-609e1531270e.jpg',
    'photo-1549692520-acc6669e2f0cccccc.jpg'
    ]

    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = executor.map(do_something, img_names)

    finish = time.perf_counter()
    print(f'Finished in {round(finish - start, 2)} second(s)')




# import concurrent.futures
# import time


# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     return f'Done Sleeping {seconds}...'


# if __name__ == '__main__':
#     start = time.perf_counter()

#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         secs = [5, 4, 3, 2, 1]
#         results = executor.map(do_something, secs)
#         [print(result) for result in results]

#     finish = time.perf_counter()
#     print(f'Finished in {round(finish - start, 2)} second(s)')


####################################################################
####################################################################


# import concurrent.futures
# import time


# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     return f'Done Sleeping {seconds}...'


# if __name__ == '__main__':
#     start = time.perf_counter()

#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         results = [executor.submit(do_something, 1) for i in range(10)]
#         for f in concurrent.futures.as_completed(results):
#             print(f.result())

#     finish = time.perf_counter()
#     print(f'Finished in {round(finish - start, 2)} second(s)')


####################################################################
####################################################################


# import concurrent.futures
# import time

# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     return f'Done Sleeping {seconds}...'


# if __name__ == '__main__':
#     start = time.perf_counter()

#     with concurrent.futures.ProcessPoolExecutor() as executor:
#         f1 = executor.submit(do_something, 1)
#         f2 = executor.submit(do_something, 1)
#         print(f1.result())
#         print(f2.result())

#     finish = time.perf_counter()
#     print(f'Finished in {round(finish - start, 2)} second(s)')



####################################################################
####################################################################

# import multiprocessing

# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)...')
#     time.sleep(seconds)
#     print(f'Done Sleeping {seconds}...')


# if __name__ == '__main__':
#     start = time.perf_counter()

#     processes = []

#     for _ in range(10):
#         p = multiprocessing.Process(target=do_something, args=[1.5])
#         p.start()
#         processes.append(p)
    
#     for process in processes:
#         process.join()

#     finish = time.perf_counter()
#     print(f'Finished in {round(finish - start, 2)} second(s)')


####################################################################
####################################################################

# import multiprocessing
# import time


# def do_something():
#     print('Sleeping 1 second...')
#     time.sleep(1)
#     print('Done Sleeping...')

# p1 = multiprocessing.Process(target=do_something)
# p2 = multiprocessing.Process(target=do_something)

# if __name__ == '__main__':
#     start = time.perf_counter()

#     # p1.start()
#     # p2.start()

#     p1.join()
#     p2.join()

#     finish = time.perf_counter()
#     print(f'Finished in {round(finish - start, 2)} second(s)')
