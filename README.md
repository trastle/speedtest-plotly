speedtest-plotly
================

A container for running an internet speed test and sending the results to [plotly](https://plot.ly/#/).

Based on [Matt's Blog Post](https://www.matt-j.co.uk/2017/09/25/measuring-internet-consistency-with-speedtest-net-plotly-and-docker/)

usage
----

docker run -e PLOTLY_USER=xxx -e PLOTLY_API_KEY=xxx speedtest-plotly
