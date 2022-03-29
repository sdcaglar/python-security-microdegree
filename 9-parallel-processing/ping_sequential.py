import requests

STATUS_CODES = {
    200: "OK",
    404: "Not Found",
    500: "Internal Server Error",
    524: "A Timeout Occurred"
}

def ping(url):
    res = requests.get(url)
    print(f"{url}:{STATUS_CODES[res.status_code]}")


if __name__ == "__main__":
    with open("input.txt", "r") as f:
        lines = f.readlines()

    for url in lines:
        ping(url[:-1])

