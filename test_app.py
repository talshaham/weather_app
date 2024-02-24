import requests


def app_reachable_test():
    try:
        res = requests.get("http://51.20.60.83/").status_code
    except requests.exceptions.ConnectionError:
        print("website isn't reachable")
    else:
        assert res in range(200, 400)
        print("website is reachable")


app_reachable_test()
