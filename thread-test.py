#!/usr/bin/python
# -*- coding: utf-8 -*-

import threading

def worker(stop):
    stop.wait()

def start():
    print('Start')
    pool = []
    stop = threading.Event()

    for i in range(10000):
        try:
            th = threading.Thread(target=worker, args=(stop,))
            th.start()
            pool.append(th)
        except Exception as e:
            break
    stop.set()

    print('Pool %d' % len(pool))
    for th in pool:
        th.join()


if __name__ == '__main__':
    start()