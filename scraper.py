import json
import requests
from bs4 import BeautifulSoup

# This is the target web address the robot will eventually scan
URL = "https://example.com" 

def run_robot():
    print("Internet robot is waking up...")
    
    # 1. The robot goes to the website and downloads the raw page text
    try:
        response = requests.get(URL, timeout=15)
        response.raise_for_status()
    except Exception as e:
        print(f"Could not load the website: {e}")
    
    # 2. For our first test run, the robot will package up these two clean, 
    # mock bills to prove that the data pipeline connects properly.
    fresh_bills = [
        {
            "bill_number": "Bill No. 104",
            "title": "Digital Infrastructure Development Bill",
            "status": "passed",
            "status_label": "Passed into Law",
            "ministry": "Electronics & IT",
            "ministry_slug": "meity",
            "date": "2026-05-21",
            "summary": "An act to establish secure data centers and expand high-speed fiber connectivity across rural research blocks."
        },
        {
            "bill_number": "Bill No. 105",
            "title": "National Green Energy Allocation Policy",
            "status": "pending",
            "status_label": "Under Review",
            "ministry": "New & Renewable Energy",
            "ministry_slug": "mnre",
            "date": "2026-05-20",
            "summary": "Proposes a structural subsidy framework for off-grid solar storage systems within agricultural cooperatives."
        }
    ]
    
    # 3. The robot opens your bills.json file, wipes out the old text, 
    # and writes this brand-new information inside it.
    with open("bills.json", "w", encoding="utf-8") as file:
        json.dump(fresh_bills, file, indent=4, ensure_ascii=False)
        
    print("Mission accomplished! Your bills.json file has been updated.")

if __name__ == "__main__":
    run_robot()
