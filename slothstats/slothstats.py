# import requests
# import pdfkit

class SlothstatsDownloader:
    def __init__(self, league_id, start_week, end_week):
        self.league_id = league_id
        self.start_week = start_week
        self.end_week = end_week
        self.url = url = f'https://www.slothstats.com/report?leagueId={self.league_id}&startWeek={self.start_week}&endWeek={self.end_week}'


    # def get_html_body(self) -> str:
    #     """
    #     Retrieves the HTML body from a given URL.

    #     Args:

    #     Returns:
    #         str: The HTML body as a string.
    #     """
    #     try:
    #         url = f'https://www.slothstats.com/report?leagueId={self.league_id}&startWeek={self.start_week}&endWeek={self.end_week}'
    #         response = requests.get(url)
    #         response.raise_for_status()  # Raise an exception for bad status codes
    #         return response.text
    #     except requests.RequestException as e:
    #         print(f"Error fetching {url}: {e}")
    #         return None


    # def html_to_pdf(self, output_file: str):
    #     """
    #     Render the given HTML body as a PDF file.

    #     Args:
    #         html_body (str): The HTML content to render.
    #         output_file (str): The path to save the PDF file.
    #     """
    #     options = {
    #         'page-size': 'A4',
    #         'margin-top': '0.75in',
    #         'margin-right': '0.75in',
    #         'margin-bottom': '0.75in',
    #         'margin-left': '0.75in'
    #     }

    #     pdfkit.from_url(self.url, output_file, options=options)