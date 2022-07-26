import requests
import sys
import json

def main():
    if len(sys.argv) == 2:
        try:
            value = float(sys.argv[1])
        except:
            sys.exit("Command-line argument is not a number")
    else:
        sys.exit("Missing command-line argument")
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        response = r.json()
        amount = response["bpi"]["USD"]["rate_float"] * value
        print(f"${amount:,.4f}")
    except requests.RequestException:
        sys.exit("RequestException")
if __name__ == "__main__":
    main()