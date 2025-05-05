# COS_598_Homework_6
### Name: 
- Jacob Lorenzo

### Date: 
- 5/4/2025

### Course: 
- COS 542

### Instructor:
- Dr. Dickens

### Assignment: 
- Homework 6

## Quick Start
Within this repository is a make file containing commands for managing the compose yaml files

All of them follow the structure of ```command_yaml``` file.

- run: performs a Docker compose depending on which yaml file you want to use (ex: ```run_basic``` for the base assignment)
- stop: brings down the Docker compose
- restart: brings it down, then starts it up again

### YAML file options:

- **basic** is the base assignment, these files display the coworker bothering the worker

- **grad** is the yaml file for getting the peak to reach 20 hashes/second

- **grad_all** is the yaml file used to  push the Docker coin container to its limits.


## Graduate Student Reflection:


1. Does this increase the current speed (as reported by the webui) by a factor 5? If not, why
not?

    No, because there are several factors playing into the speed. You have the worker that interacts with the hasher and the rng services, so they can only be as fast as as the number of services that can support the workers. There is also the overhead of Docker performing load balancing. Additionally, there is a limitation on computational resources; you can’t multithread your way into better performance if the resources aren’t available to support it.

    I like to think of it like a bicycle factory: if you have 10 bicycle frames but only 2 wheels, you’ll need to constantly move the wheels between the frames. This switching creates overhead and slows down the overall production process.


2. Increase the number of replicas of the other components (except redis and the webui) to reach
a peak rate of at least 20 hashes per second. How many replicas of each were required?

- Local:

    It took 6 workers, 3 hashers, and 3 rng replicas to reach a peak of 20.9 hashes/second on my local machine. 

- Jetstream:

    The same amount of replications were suitable for Jetstream.

3. Increase the number of replicas to obtain the maximum work rate you can achieve. How many
replicas of each were required?

- Local:

    As an experiment to see how far I could take it, I did some overclocking on my personal machine and was able to reach 60 hashes/second using 18 of each.

- Jetstream:

    To see what happens when I run it on jetstream, I used a 2 cpu instance and I was able to get a peak of 55. I got those results with 18 of each service. I tried 25 of each and received noticeably worse results. My thoughts are that the number of services is causing too much overhead leading to decreased performance.


4. What are the factors limiting the peak hashing rate you can achieve?

    From my observations, I believe that the limiting factor is the Redis database. My thought process is that the Redis database is being overloaded by too many simultaneous requests. This idea is reinforced by the fact that the worker is the only service making requests to the Redis database.