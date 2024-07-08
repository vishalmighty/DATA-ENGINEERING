# Q & A (Answered by some industrial experts)
### Q1. I understand the uses of kafka like it helps to decouple two applications/micro services but i'm counfused in the following example.
So consider i need to read cdc data from my mysql db and load it to OLAP db(say clickhouse or anything). Here i'm using flink as my EL tool. So using flink I can directly read data from mysql binlog and write it to clickhouse. Even if flink fails it can restart from old checkpoint which is pointing to my mysql binlog. 
So here why i need to add kafka in between mysql and flink as it was already decoupled , In fact it will increase my resource cost. What is the advatage of adding kafka here?

Answer:
1. by adding Kafka, you can easily introduce additional consumers to the data stream without impacting the primary pipeline

2. If you need to change the downstream system from ClickHouse to another database or add another data processing tool, Kafka allows you to do so without modifying the source data extraction logic

3. Kafka can handle a high throughput of messages and is designed to scale horizontally

4. Kafka's partitioning and replication ensure that data is not lost even if some Kafka brokers fail.

5. by using Kafka, you reduce the load on the source MySQL database since Kafka can distribute the read load across multiple consumers instead of having each consumer directly access MySQL.


### Q2. Kafka uses which protocol for communication between clients and brokers?
binary protocol over TCP


### Q3. Kafka is written in which programming language?
Java

### Q4. Kafka guarantees?
At least-once delivery - correct
Don't confuse with - Exactly-once delivery - wrong

### Q6. Kafka topics are mutable or immutable?
Immutable

### Q7. Which component is responsible for managing metadata and coordinating Kafka brokers?
ZooKeeper

### Q8. Which Kafka component handles data replication and fault tolerance?
Kafka Broker

### Q9. What is the role of a Kafka consumer group?
Grouping multiple Kafka consumers together - Correct
Don't confuse with - Grouping multiple Kafka brokers together - wrong

### Q10. Which component is responsible for storing Kafka topics and maintaining their message logs?
Kafka Broker

### Q11. Kafka partitions are dependent or independent on number of brokers?
Independent of the number of brokers in the cluster

### Q12. Which serialization formats are supported by Kafka?
    JSON
    Avro
    Protobuf

### Q13.  Kafka Connect is used for?
Data integration and movement is the correct answer
Real-time stream processing - wrong