# diabetes-profiling

Profiling and finding variables that are significant to diabetes

## Procedure:
Hierarchical clustering using ward, single and complete linkage

# Analysis
There are several distinctions among the dendrograms generated using ward, complete, and 
single linkage methods:
- Despite the apparent visual resemblance and identical cluster count (3) between the 
complete and ward dendrograms, they exhibit significant differences in the point at which 
they merge. Ward linkage combines clusters at approximately 2500, whereas complete 
linkage merges them much earlier, at around 800.
- Single linkage, unfortunately, proved to be unhelpful in our analysis, resulting in only 
one cluster and providing uninformative node distances.
- Complete linkage, in contrast, was more beneficial as it showcased clear distinctions 
between the nodes.
- Among the three methods, ward linkage emerged as the most effective.
