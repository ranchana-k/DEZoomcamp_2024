# Homework

Ingested data of green taxi trip in August 2019, as done in `Homework Week 01.ipynb`
then answered question 3 - 6 by queries as followings:

## Question 3
To find total number of trips totally occured in `2019-09-18`.

```
SELECT COUNT(*)
FROM green_taxi_trip
WHERE DATE(lpep_pickup_datetime) = '2019-09-18' AND 
DATE(lpep_dropoff_datetime) = '2019-09-18';
```

## Question 4
To find the date that had the longest distance.

``` 
SELECT *
FROM green_taxi_trip
WHERE trip_distance = (SELECT MAX(trip_distance) FROM green_taxi_trip);
```

## Question 5 
To find Three biggest pick up Boroughs that had a sum of total_amount superior to 50000.

```
SELECT pickup_borough, SUM(total_amount) AS borough_total_amount
FROM (SELECT trip.*, zone."Borough" as pickup_borough
        FROM green_taxi_trip AS trip
        LEFT JOIN zone
        ON trip."PULocationID" = zone."LocationID") AS temp
        WHERE DATE(lpep_pickup_datetime) = '2019-09-18'
        GROUP BY pickup_borough 
        HAVING SUM(total_amount) > 50000
        ORDER BY 2 DESC
LIMIT 3;
```

## Question 6 
Based on pick up zone at 'Astoria', find a drop off zone that has the larget tip.

```
SELECT pu_zone, do_zone,tip_amount
FROM (SELECT trip.*, zone."Zone" as pu_zone, zone2."Zone" as do_zone
	  	FROM green_taxi_trip AS trip
	  	LEFT JOIN zone
	  	ON trip."PULocationID" = zone."LocationID"
		LEFT JOIN zone AS zone2
		ON trip."DOLocationID" = zone2."LocationID"
	  	WHERE zone."Zone" = 'Astoria'
	  ) AS temp
ORDER BY tip_amount DESC
LIMIT 1;
```
