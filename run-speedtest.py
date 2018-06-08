import speedtest
import plotly
import os
import sys

def run_test():
  s = speedtest.Speedtest()
  s.get_servers([])
  s.get_best_server()
  s.download()
  s.upload()
  results_dict = s.results.dict()
  return results_dict

def plot_test_results(results_dict, plotly_user, plotly_api_key, plotly_graph_name):

    plotly.tools.set_credentials_file(username=plotly_user, api_key=plotly_api_key)

    uploadtrace = plotly.graph_objs.Scatter(
        x = results_dict['timestamp'],
        y = results_dict['upload'],
        mode = 'lines+markers',
        name = 'Upload',
        line = dict(color = '#0d25ad'),
    )

    downloadtrace = plotly.graph_objs.Scatter(
        x = results_dict['timestamp'],
        y = results_dict['download'],
        mode = 'lines+markers',
        name = 'Download',
        line = dict(color = '#79357c'),
    )

    latencytrace = plotly.graph_objs.Scatter(
        x = results_dict['timestamp'],
        y = results_dict['ping'],
        mode = 'lines+markers',
        name = 'Latency',
        line = dict(color = '#0d561c'),
    )

    plotdata = [uploadtrace, downloadtrace, latencytrace]
    plot_url = plotly.plotly.plot(plotdata, filename='plotly_graph_name', fileopt='extend', auto_open=False)
    return plot_url

def main():
    if "PLOTLY_USER" not in os.environ or "PLOTLY_API_KEY" not in os.environ:
        print("ERROR: PLOTLY_USER and PLOTLY_API_KEY environment variables required.")
        sys.exit(1)

    plotly_user=os.environ.get("PLOTLY_USER")
    plotly_api_key=os.environ.get("PLOTLY_API_KEY")
    plotly_graph_name=os.environ.get("PLOTLY_GRAPH_NAME", "SpeedTest")

    results_dict = run_test()
    plot_url = plot_test_results(results_dict=results_dict,
                                 plotly_user=plotly_user,
                                 plotly_api_key=plotly_api_key,
                                 plotly_graph_name=plotly_graph_name)
    print(plot_url)

if __name__ == "__main__":
    main()
