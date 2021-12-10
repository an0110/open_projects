from seleniumwire import webdriver  # Import from seleniumwire

# Create a new instance of the Firefox driver
driver = webdriver.Firefox()

# Go to the Google home page
driver.get('https://chaturbate.com/lola_jd/')

# print (help(driver))
#
#
# exit()


# Access requests via the `requests` attribute
for request in driver.requests:
    if request.response:
        print(             request.url)
        print ("*"*10)
        print(    request.response.status_code)
        print("-" * 10)
        print(    request.response.headers['Content-Type'])