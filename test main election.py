import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://results.eci.gov.in/AcResultGenJune2024/index.htm"
try:
    r = requests.get(url)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "lxml")

   
    parl_link = soup.find(lambda tag: tag.name == 'a' and 'Parliamentary Constituencies' in tag.text)
    
    if parl_link and 'href' in parl_link.attrs:
        parl_url = 'https://results.eci.gov.in/AcResultGenJune2024/' + parl_link['href']
        print(f"Found Parliamentary Constituencies link: {parl_url}")
        
        
        r = requests.get(parl_url)
        r.raise_for_status()
        soup = BeautifulSoup(r.text, "lxml")
        
        
        table = soup.find("table", class_="table")
        
        if table:
            # Process the table
            df = pd.read_html(str(table))[0]
            print("Data scraped successfully:")
            print(df)

            
            csv_filename = "parliamentary_constituencies_election_results.csv"
            df.to_csv(csv_filename, index=False)
            print(f"\nData saved to {csv_filename}")
        else:
            print("Results table not found on the Parliamentary Constituencies page.")
    else:
        print("Couldn't find a link to Parliamentary Constituencies results.")

except requests.RequestException as e:
    print(f"An error occurred while fetching the webpage: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
