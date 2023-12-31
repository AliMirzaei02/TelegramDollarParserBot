import requests
from bs4 import BeautifulSoup

def dollarParser():
    # Making a GET request
    url = "https://www.tgju.org/currency"
    #headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36"}
    response = requests.get(url)#, headers=headers)

    if response.status_code == 200:
        # Parsing the HTML
        soup = BeautifulSoup(response.content, "html.parser")
        # Finding $ price
        dollar_info = soup.find("tr", {"data-market-row":"price_dollar_rl"})
        dollar_dt = dollar_info.find_all("td")
        dollar_pr = dollar_dt[0].text
        dollar_ch = dollar_dt[1].text
        dollar_ls = dollar_dt[2].text
        dollar_tp = dollar_dt[3].text

        #print(dollar_pr)
        if dollar_pr is not None:
            return f"The current dollar price in rials is: {dollar_pr}"
        else:
            return "Unable to find dollar price on website."
    else:
        return "Unable to connect to website."