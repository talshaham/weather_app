import requests


def app_reachable_test():
    try:
        res = requests.get("http://16.171.116.132:80").status_code
    except requests.exceptions.ConnectionError:
        print("website isn't reachable")
    else:
        assert res in range(200, 400)
        print("website is reachable")


app_reachable_test()
