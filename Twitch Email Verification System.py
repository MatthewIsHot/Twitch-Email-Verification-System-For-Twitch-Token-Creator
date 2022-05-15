import requests,random,time

class GetEmail:

    def email():

        xname = ''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for i in range(10))

        headers = {
            'authority': 'temporarymail.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'referer': 'https://temporarymail.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }
        response = requests.get('https://temporarymail.com/ajax/?action=requestEmailAccess&value=%s@FreeMailOnline.us' % (xname), headers=headers)
        mailx = response.json()['address']
        key = response.json()['secretKey']
        return mailx, key

#Use GetEmail.email()[0] to get the mail!
#Use GetEmail.email()[1] to get the key!

class CheckMail:

    def check(key):

        headers = {
            'authority': 'temporarymail.com',
            'accept': '*/*',
            'accept-language': 'en-GB,en-US;q=0.9,en;q=0.8',
            'referer': 'https://temporarymail.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="101", "Google Chrome";v="101"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
            'x-requested-with': 'XMLHttpRequest',
        }

        params = {
            'action': 'checkInbox',
            'value': key,
        }
        response = requests.get('https://temporarymail.com/ajax/', params=params, headers=headers)
        while True:
            time.sleep(2)
            if response.json() == []:
                None
            else:
                return response.json()[key]['subject'][0:6]