# Spark Cluster On-Demand Automation
## Overview
This project automates the lifecycle of a Spark cluster. It creates a Spark cluster on demand, runs a specified Spark job, and then terminates the cluster once the job is completed. This approach significantly reduces costs by eliminating the need to run a Spark cluster 24/7.

## Use Case
The primary use case for this project is cost optimization. By creating and terminating Spark clusters as needed, you avoid the expenses associated with continuously running clusters.

## Trigger Rules (Alternative Options)
one_failed: The task will execute if at least one of its upstream tasks fails.
one_success: The task will execute if at least one of its upstream tasks succeeds.