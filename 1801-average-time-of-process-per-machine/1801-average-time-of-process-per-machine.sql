# Write your MySQL query statement below
Select machine_id,Round(AVG(end_time-start_time),3) as processing_time
from (select machine_id,process_id, MAX(CASE WHEN activity_type ='start' THEN timestamp END) AS start_time, MAX(CASE WHEN activity_type ='end' THEN timestamp END) AS end_time
from Activity
Group by machine_id,process_id) as process_times
group by machine_id;
