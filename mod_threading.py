
import requests
import concurrent.futures
import time

img_urls = [
    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
    'https://images.unsplash.com/photo-1550439062-609e1531270e',
    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
]

start = time.perf_counter()

def download_image(img_url):
    print(img_url)
    img_bytes = requests.get(img_url).content
    img_name = img_url.split('/')[3]
    img_name = f'{img_name}.jpg'
    with open(img_name, 'wb') as img_file:
        img_file.write(img_bytes)
        print(f'{img_name} was downloaded...')

with concurrent.futures.ThreadPoolExecutor() as executor:
    executor.map(download_image, img_urls)

finish = time.perf_counter()

print(f'Finished in {round(finish-start, 2)} seconds(s)')


#################################################################
#################################################################


# import concurrent.futures
# import time

# start = time.perf_counter()

# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)....')
#     time.sleep(seconds)
#     return f'Done Sleeping...{seconds}'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     seconds = [5, 4, 3, 2, 1]
#     results = executor.map(do_something, seconds)

#     # for r in results:
#     #     print(r)

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')


#################################################################
#################################################################


# import concurrent.futures
# import time

# start = time.perf_counter()

# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)....')
#     time.sleep(seconds)
#     return f'Done Sleeping...{seconds}'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     seconds = [5, 4, 3, 2, 1]
#     results = [executor.submit(do_something, sec) for sec in seconds]
#     # [print(i.result()) for i in results]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')

#################################################################
#################################################################

# import concurrent.futures
# import time

# start = time.perf_counter()

# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)....')
#     time.sleep(seconds)
#     return f'Done Sleeping...{seconds}'

# with concurrent.futures.ThreadPoolExecutor() as executor:
#     results = [executor.submit(do_something, i) for i in range(10)]
#     # [print(i.result()) for i in results]
#     for f in concurrent.futures.as_completed(results):
#         print(f.result())

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')



#################################################################
#################################################################

# import threading
# import time

# start = time.perf_counter()


# def do_something(seconds):
#     print(f'Sleeping {seconds} second(s)....')
#     time.sleep(seconds)
#     print('Done Sleeping')

# threads = []

# for i in range(10):
#     t = threading.Thread(target=do_something, args=[i])
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()


# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')


#################################################################
#################################################################

# import threading
# import time

# start = time.perf_counter()


# def do_something():
#     print('Sleeping 1 second....')
#     time.sleep(1)
#     print('Done Sleeping')

# threads = []

# for _ in range(10):
#     t = threading.Thread(target=do_something)
#     t.start()
#     threads.append(t)

# for t in threads:
#     t.join()


# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')


#################################################################
#################################################################

# import threading
# import time

# start = time.perf_counter()


# def do_something():
#     print('Sleeping 1 second....')
#     time.sleep(1)
#     print('Done Sleeping')


# # t1 = threading.Thread(target=do_something)
# # t2 = threading.Thread(target=do_something)

# # t1.start()
# # t2.start()

# # t1.join()
# # t2.join()


# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')



#################################################################
#################################################################

# import time

# start = time.perf_counter()


# def do_something():
#     print('Sleeping 1 second....')
#     time.sleep(2)
#     print('Done Sleeping')


# do_something()

# finish = time.perf_counter()

# print(f'Finished in {round(finish-start, 2)} seconds(s)')
