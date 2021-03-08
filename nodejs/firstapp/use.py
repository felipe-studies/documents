def main():
    import requests, json

    rest_get = input("Show All Users? [Y/n] ")
    rest_get = True if rest_get.lower() == "y" else False

    if rest_get:
        results = json.loads(requests.get('http://127.0.0.1:3000/users').content)
        for i in results:
            print(i)
    else:
        first_name = input("Enter the First Name: ")
        assert type(first_name) == str
        last_name = input("Enter the Last Name: ")
        assert type(last_name) == str
        pload = {'first_name': first_name, 'last_name': last_name}
        requests.post('http://127.0.0.1:3000/user', json=pload)


if __name__ == "__main__":
    main()