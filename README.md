## **SpatioTemporal Influx Detection (Spa.T.I.D)**
A method to detect anomalies across space and time.


## Why is it important?

** 
To help agencies detect "influxes" as they happen and proactively respond to them.

## **How does it work?**

For any dataset containing columns for date-time and location coordinates, this script will

1. Group location components by a Hierarchical Spatial Index using H3 at a certain spatial resolution
1a. Set a resolution for H3 as per [Table of Cell Areas for H3 Resolutions](https://h3geo.org/docs/core-library/restable)
2. Group the temporal components by a specific "window" (Ex: 15,30 or 60 minute windows)
3. Set an event count threshold (Ex: 5)

Based on these 3 parameters, the script shall output a list of "influx events" that indicates a spatiotemporal breach of the given threshold.

Output:


|Time-Bin  | Hex-Code | Event-Count|
|--|--|--|
|YYYYMMDDHHMMSS 1 |ABC123456789  | ### |
|YYYYMMDDHHMMSS 2 |ABC123456789  | ### |
|YYYYMMDDHHMMSS 3 |ABC123456789  | ### |


## **How can it be applied?**

* Detect influxes in Historical Data
* Detect influxes for Streaming Data

## Changelog

v 0.1

 - Create MVP script using a canonical dataset

v 0.2

 - Generalize the MVP script by creating a config-file where users can specify which columns contain (date, time OR date-time) AND (location coordinates)
 - Default runs (no arguments)
   - DEFAULT TIME BIN - AutoDetect temporal frequency of the dataset and set default TIME Bins (ex: 30 mins, 60 mins, 1 day etc)
   - DEFAULT SPACE BIN - H3-9 resolution based on [H3 reference table](https://h3geo.org/docs/core-library/restable)
   - DEFAULT EVENT THRESHOLD - Average out the event counts for each space-time bin.
   
v 0.3

- Demonstrate functionality on streamed spatio-temporal data 
