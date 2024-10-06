import requests
from datetime import datetime
# Your 2Captcha API key
API_KEY = 'fa03c56xxxxxxxxxxxxxxxxxxxxxxxxx'
 
# The site key from the reCAPTCHA you want to solve
SITE_KEY = '6Le-wvkSAAAAAPBMRTvw0Q4Muexq9bi0DJwx_mJ-'
# The URL of the page with the reCAPTCHA
URL = 'https://www.google.com/recaptcha/api2/demo'

def solve_recaptcha(api_key, site_key, url):
    # Step 1: Request a new CAPTCHA
    captcha_payload = {
        'key': api_key,
        'method': 'userrecaptcha',
        'googlekey': site_key,
        'pageurl': url,
        'json': 1
    }
    
    response = requests.post('https://2captcha.com/in.php', data=captcha_payload)
    result = response.json()

    if result['status'] != 1:
        print('Error: ', result['request'])
        return None

    # Get the captcha ID
    captcha_id = result['request']
    print('Captcha ID:', captcha_id)

    # Step 2: Wait for the CAPTCHA to be solved
    print('Checking for captcha solution...')

    while True:
        result_payload = {
            'key': api_key,
            'action': 'get',
            'id': captcha_id,
            'json': 1
        }

        result_response = requests.post('https://2captcha.com/res.php', data=result_payload)
        result_data = result_response.json()

        if result_data['status'] == 1:
            print('Captcha Solved! Token:', result_data['request'])
            return result_data['request']
        elif result_data['request'] == 'CAPCHA_NOT_READY':
            continue  # Keep checking
        else:
            print('Error: ', result_data['request'])
            return None


if __name__ == "__main__":
    init_time = datetime.now()
    # Use the function
    token = solve_recaptcha(API_KEY, SITE_KEY, URL)

    if token:
        print('Use this token in your request:', token)
    final_time = datetime.now()
    Total_time = final_time-init_time
    print(Total_time)