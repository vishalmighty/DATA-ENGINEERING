## What is Data Skewness ?
Uneven distribution of data between different worker machine


## Why skew is formed ?
1. Available storage vary greatly. eg: one worker has 50Gb of free space and remaning workers has only 10 GB of free space
2. When the data of India is high(50M) and you have partitioned based on country column but the data of remaining countries are very low like 50K
3. we got the same hash value for 75% of the data

## To prevent Data Skewness
1. Use homogeneous machines(Machines with similar resource configureations) for workers

## Solution for Data Skewness
1. Salting
2. Broadcast join(expensive)


### Salting
We will generate random numbers for every data(row) and repartition the data to reduce skew.
Here you may get a question that purpose of partitioning is itself lost if we do random paritioning but that is not the case here. Here we are not paritioning to reduce read size here we are partitioning to increase parallelism. 

### Brocast Join
It will load the whole data to all the executors which is memory expensive but this will also reduce skew

