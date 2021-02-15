## **SpatioTemporal Influx Detection (S.T.I.D)**
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

 - Using a sample dataset, create MVP of logic and output

v 0.2

 - Generalize the MVP through a config file that specifies which columns are date, time, date-time and location coordinates
 - Create Default runs (no args)
   - AutoDetect temporal cycles of the dataset and set default binning
   - Set default spatial resolution at 1km hex edge,
   - Set event threshold = Average event count for each space-time bin.
