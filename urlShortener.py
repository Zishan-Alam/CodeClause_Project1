import requests


def shorten_link(full_link, link_name):
    API_KEY = '565da92358f55b7f0b5427109d0cc89dad8a6'
    BASE_URL = 'https://cutt.ly/api/api.php'

    payload = {'key': API_KEY, 'short': full_link, 'name': link_name}
    response = requests.get(BASE_URL, params=payload)
    data = response.json()

    print()

    try:
        title = data['url']['title']
        short_link = data['url']['shortLink']
        print('Title:', title)
        print('Link:', short_link)
    except KeyError:
        status = data['url']['status']
        print("Error Status:", status)


link = input("Enter a link: >> ")
name = input("Give your link a name: >> ")

shorten_link(link, name)



#Following are the status code description for the program.
# url => status: 1	the shortened link comes from the domain that shortens the link, i.e. the link has already been shortened
# url => status: 2	the entered link is not a link
# url => status: 3	the preferred link name is already taken
# url => status: 4	Invalid API key
# url => status: 5	the link has not passed the validation. Includes invalid characters
# url => status: 6	The link provided is from a blocked domain
# url => status: 7	OK - the link has been shortened
# url => status: 8	You have reached your monthly link limit. You can upgrade your subscription plan to add more links.