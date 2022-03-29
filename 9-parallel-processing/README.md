## Section Topics

### 9.1 - What is Parallelism

#### Parallel Processing - Defined

Parallel processing simply means having something done by __multiple agents
simultaneously__.

### 9.2 - First Example in Python

#### Commands used in chapters
```
python3 countdown_sequential.py
# output
Alice is counting down: 5...
Alice is counting down: 4...
Alice is counting down: 3...
Alice is counting down: 2...
Alice is counting down: 1...
Alice finished counting down
Bob is counting down: 5...
Bob is counting down: 4...
Bob is counting down: 3...
Bob is counting down: 2...
Bob is counting down: 1...
Bob finished counting down

python3 countdown_multiprocessing.py
# output
Process Alice is counting down: 5...
Process Alice is counting down: 4...
Process Bob is counting down: 5...
Process Alice is counting down: 3...
Process Bob is counting down: 4...
Process Alice is counting down: 2...
Process Alice is counting down: 1...
Process Alice finished counting down
Process Bob is counting down: 3...
Process Bob is counting down: 2...
Process Bob is counting down: 1...
Process Bob finished counting down
```

### 9.3 - Python Parallelism in Context

- 01 | Definition
    - What parallelism realy is, how it offers speed and responsiveness
- 02 | Current State
    - How parallelism is being used in today's industry
- 03 | Considerations
    - Not all programs can be made parallel

#### Parallelism vs. Concurrency

__Parallelism:__ independent components running separately from each other

__Concurrency:__ components running separately with coordination

#### Parallelism in Today's Industry

__Computer:__ Multi core computers and laptops for smoother processing

__Mobile:__ Multi-core phones, game consoles, Raspberry Pis

__The Web:__ Multi-server websites, servers handle multiple requests simultaneously

__Al & ML:__ GPUs, splitting training data, multi-agent learning

#### Before Applying Parallelism...

* Is the program inherently sequential?
* Which parts of the program can be made parallel?
* What is the best number of threads/processes to run in parallel?

### 9.4 - What is Threading

#### A Thread & Threading

__A thread:__ The smallest unit of executable commands managed by a scheduler.

__Threading:__ Running multiple threads at the same time.

#### Commands used in chapters
```
python3 countdown_threading_v1.py
# output
Thread Alice is counting down: 5...
Thread Alice is counting down: 4...
Thread Bob is counting down: 5...
Thread Alice is counting down: 3...
Thread Bob is counting down: 4...
Thread Alice is counting down: 2...
Thread Alice is counting down: 1...
Thread Alice finished counting down
Thread Bob is counting down: 3...
Thread Bob is counting down: 2...
Thread Bob is counting down: 1...
Thread Bob finished counting down

python3 countdown_threading_v2.py
# output
Thread Alice starting...
Thread Bob starting...
Thread Alice is counting down: 5...
Thread Alice is counting down: 4...
Thread Bob is counting down: 5...
Thread Alice is counting down: 3...
Thread Bob is counting down: 4...
Thread Alice is counting down: 2...
Thread Alice is counting down: 1...
Thread Alice finished counting down
Thread Alice finished
Thread Bob is counting down: 3...
Thread Bob is counting down: 2...
Thread Bob is counting down: 1...
Thread Bob finished counting down
Thread Bob finished
```
### Helpful Resources

[Threading](https://docs.python.org/3/library/threading.html)

### 9.5 - Building a Thread Ping Test

#### Web Requests via A Browser

![Web Requests](web-requests.png)

#### Pinging A Website

![Pinging](pinging-website.png)

#### HTTP Status Codes
- __1xx (Informational):__ The request was received, continuing processes
- __2xx (Successful):__ The request was successfully receivedi understood and
  accepted
- __3xx (Redirection):__ Further action needs to be taken in order to complete
  the request
- __4xx (Client Error):__ The request contains bad syntax or cannot be fulfilled
- __5xx (Server Error):__ The server failed to fulfill an apparently valid request

#### Commands used in chapters
```
python3 ping_sequential.py
# output
http://httpstat.us/200:OK
http://httpstat.us/200?sleep=2000:OK
http://httpstat.us/404:Not Found
http://httpstat.us/500?sleep=3000:Internal Server Error
http://httpstat.us/524:A Timeout Occurred

python3 ping_threading.py
# output
http://httpstat.us/524:A Timeout Occurred
http://httpstat.us/404:Not Found
http://httpstat.us/200:OK
http://httpstat.us/200?sleep=2000:OK
http://httpstat.us/500?sleep=3000:Internal Server Error
```
### Helpful Resources

[Python Requests](https://docs.python-requests.org/en/latest/)

[HTTP Status](http://httpstat.us/)

### 9.6 - The Global Interpreter Lock

#### The GIL CPU-Bound Tasks

* The GIL prevents multiple CPU-bound threads from executing simultaneously
* A CPU-bound program mostly executes inside the CPU
* Typically involves heavy computation, also referred to as __"compute-bound"__

#### Commands used in chapters
```
 python3 big_countdown_sequential.py

 python3 big_countdown_threading.py
```

#### Arguments For The GIL
* Not all threaded programs are affected by the GIL
    - Sleeping
    - Waiting for responses from online server
* Best solution to memory management in Python
* Responsiveness resulting from threading is still possible

### Helpful Resources

[Gilectomy](https://pythoncapi.readthedocs.io/gilectomy.html)