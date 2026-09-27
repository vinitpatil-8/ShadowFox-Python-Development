import csv
import sys
import requests
from bs4 import BeautifulSoup # type: ignore


def scrape_website(url, output_file="scraped_data.csv"):
    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 "
            "(KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
        )
    }

    # 1. Error Handling: Network Request
    try:
        print(f"Fetching data from: {url}...")
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
    except requests.exceptions.HTTPError as http_err:
        print(f"[HTTP Error] Failed to retrieve web page: {http_err}")
        return
    except requests.exceptions.ConnectionError:
        print("[Connection Error] Failed to connect to the server/URL.")
        return
    except requests.exceptions.Timeout:
        print("[Timeout Error] The request timed out.")
        return
    except requests.exceptions.RequestException as err:
        print(f"[Request Error] An unexpected error occurred: {err}")
        return

    # 2. Parse HTML Content with BeautifulSoup
    try:
        soup = BeautifulSoup(response.content, "html.parser")
    except Exception as parse_err:
        print(f"[Parse Error] Failed to parse page content: {parse_err}")
        return

    extracted_data = []

    # 3. Data Extraction: Target headings, links, and content tags
    cards = soup.find_all(["article", "section", "div"], class_=["card", "content", "course-card"]) 
    
    if not cards:
        headings = soup.find_all(["h1", "h2", "h3", "a"])
        for idx, item in enumerate(headings, start=1):
            title = item.get_text(strip=True)
            link = item.get("href", "N/A")
            if title:
                extracted_data.append({
                    "ID": idx,
                    "Title/Header": title,
                    "Link": link if link.startswith("http") else f"{url.rstrip('/')}/{link.lstrip('/')}"
                })
    else:
        for idx, card in enumerate(cards, start=1):
            title_tag = card.find(["h1", "h2", "h3", "h4"])
            link_tag = card.find("a")
            desc_tag = card.find(["p", "span"])

            title = title_tag.get_text(strip=True) if title_tag else "N/A"
            link = link_tag["href"] if (link_tag and "href" in link_tag.attrs) else "N/A"
            description = desc_tag.get_text(strip=True) if desc_tag else "N/A"

            extracted_data.append({
                "ID": idx,
                "Title": title,
                "Description": description,
                "URL": link
            })

    if not extracted_data:
        print("No data found on the page.")
        return

    print(f"Successfully extracted {len(extracted_data)} items.")

    # 4. Data Storage: Save to CSV
    try:
        fieldnames = list(extracted_data[0].keys())
        with open(output_file, mode="w", newline="", encoding="utf-8") as csv_file:
            writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(extracted_data)
        print(f"Data saved successfully to '{output_file}'.")
    except IOError as io_err:
        print(f"[File I/O Error] Could not write data to CSV: {io_err}")


target_url = "https://www.shadowfox.in"
scrape_website(target_url, output_file="shadowfox_scraped_data.csv")