from slothstats.slothstats import SlothstatsDownloader
from sleeper.sleeper import get_nfl_state

if __name__ == "__main__":
    #downloader = SlothstatsDownloader(league_id=1074391942395428864, start_week=1, end_week=2)

    #body = downloader.get_html_body()

    #print(body)

    #downloader.html_to_pdf('out.pdf')

    print(get_nfl_state())

