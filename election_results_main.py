from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd

def extract_data_format_a(browser):
    data = []
    try:
        table = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
        )
        for row in table.find_elements(By.TAG_NAME, 'tr'):
            cols = row.find_elements(By.TAG_NAME, 'td')
            if len(cols) > 6:
                data.append({
                    'area': cols[0].text,
                    'winner': cols[2].text,
                    'winner_party': cols[3].text,
                    'margin': cols[6].text,
                    'runner_up': cols[4].text,
                    'runner_up_party': cols[5].text,
                    'previous_mp': cols[7].text,
                    'previous_party': cols[8].text
                })
    except TimeoutException:
        print("Error: Timed out while fetching data for format A.")
    return data

def extract_data_format_b(browser):
    data = []
    try:
        table = WebDriverWait(browser, 15).until(
            EC.presence_of_element_located((By.TAG_NAME, 'tbody'))
        )
        for row in table.find_elements(By.TAG_NAME, 'tr'):
            cols = row.find_elements(By.TAG_NAME, 'td')
            if len(cols) > 4:
                data.append({
                    'area': cols[0].text,
                    'winner': cols[1].text,
                    'winner_party': cols[2].text,
                    'margin': cols[3].text,
                    'runner_up': cols[4].text,
                    'runner_up_party': cols[5].text,
                    'previous_mp': cols[6].text,
                    'previous_party': cols[7].text
                })
    except TimeoutException:
        print("Error: Timed out while fetching data for format B.")
    return data

urls_and_formats = [
    ('https://results.eci.gov.in/pcresultgenjune2024/statewiseS241.htm', extract_data_format_a),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS041.htm', extract_data_format_a),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS061.htm', extract_data_format_a),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU011.htm', extract_data_format_a),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS021.htm', extract_data_format_a),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS021.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS031.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU021.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS261.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU031.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS051.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU061.htm', extract_data_format_a),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU091.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS111.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS101.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS271.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS271.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU081.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS081.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS081.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS121.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU051.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS131.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS141.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS151.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS161.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS171.htm', extract_data_format_a),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS181.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseU071.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS253.htm', extract_data_format_a),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS281.htm', extract_data_format_a),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS291.htm', extract_data_format_a),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS221.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS211.htm', extract_data_format_b),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS201.htm', extract_data_format_a),
    ('https://results.eci.gov.in/PcResultGenJune2024/statewiseS191.htm', extract_data_format_b)
]

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('--headless')
browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)

collected_data = []

for url, extract_function in urls_and_formats:
    browser.get(url)
    collected_data.extend(extract_function(browser))

browser.quit()

results_df = pd.DataFrame(collected_data)
results_df.to_csv('india_election_results_2024.csv', index=False)

print("Data extraction complete. Results saved to india_election_results_2024.csv")