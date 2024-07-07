# Q & A (Answered by some industrial experts)
1. I understand the uses of kafka like it helps to decouple two applications/micro services but i'm counfused in the following example.
So consider i need to read cdc data from my mysql db and load it to OLAP db(say clickhouse or anything). Here i'm using flink as my EL tool. So using flink I can directly read data from mysql binlog and write it to clickhouse. Even if flink fails it can restart from old checkpoint which is pointing to my mysql binlog. 
So here why i need to add kafka in between mysql and flink as it was already decoupled , In fact it will increase my resource cost. What is the advatage of adding kafka here?

Answer:
1. by adding Kafka, you can easily introduce additional consumers to the data stream without impacting the primary pipeline

2. If you need to change the downstream system from ClickHouse to another database or add another data processing tool, Kafka allows you to do so without modifying the source data extraction logic

3. Kafka can handle a high throughput of messages and is designed to scale horizontally

4. Kafka's partitioning and replication ensure that data is not lost even if some Kafka brokers fail.

5. by using Kafka, you reduce the load on the source MySQL database since Kafka can distribute the read load across multiple consumers instead of having each consumer directly access MySQL.