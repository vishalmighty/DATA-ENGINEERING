# Kafka
## What is kafka
This is a messaging queue(Distributed streaming platform)

### Usage
Transfer data from one application/micro-service to another

### How it works
Messages are queued non-synchronously between the messaging system and client applications


### Two types of messaging patterns
1. Point to Point -  More than one consumer can consume but one particular message can be consumed by only one consumer
2. Publish Subscribe(Pub-Sub) - More the one consumer can consume the same message

## Components of kafka

### kafka cluster
1. Multiple interconnected kafka brokers are called cluster

### kafka broker
1. Distributed system that stores and manages the data(messages).

2. Handles data distribution , read/write requests from producers and consumers and also ensures falut tolerance.

### kafka zookeeper
1. cluster coordination & metadata management

2. Keeps brokers in sync

3. Helps in broker failover recovery and leader election

### kafka producer
1. Handles