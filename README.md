# speedtest-plotly

[![Docker Build](https://img.shields.io/docker/automated/trastle/haverland-smartwave-prometheus-exporter.svg)](https://hub.docker.com/r/trastle/speedtest-plotly/)

A container for running an internet speed test and sending the results to [plotly](https://plot.ly/#/).

Based on [Matt's Blog Post](https://www.matt-j.co.uk/2017/09/25/measuring-internet-consistency-with-speedtest-net-plotly-and-docker/)

## Usage


```
docker run -e PLOTLY_USER=xxx -e PLOTLY_API_KEY=xxx speedtest-plotly
```

## Configuration

```
PLOTLY_USER - Your Plotly username
PLOTLY_API_KEY - Your Plotly API key
PLOTLY_GRAPH_NAME - (Optional) The name of your Plotly graph - defaults to SpeedTest
```
