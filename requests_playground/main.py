# import requests
#
#
# def print_info(element):
#     return type(element)
#
# rez = requests.get("https://chaturbate.com/sophiekinky/")
#
# # print (help((rez.iter_content())))
#
# print (rez.content)
#
#
#
# #
# # for el in rez.iter_content():
# #     print(type(el))
# #     exit()
#
#
#
#
#
#


import PyChromeDevTools

chrome = PyChromeDevTools.ChromeInterface()
chrome.Network.enable()
chrome.Page.enable()
#
# chrome.Page.navigate(url="http://www.facebook.com")
# event,messages=chrome.wait_event("Page.frameStoppedLoading", timeout=60)
#
# for m in messages:
#     if "method" in m and m["method"] == "Network.responseReceived":
#         try:
#             url=m["params"]["response"]["url"]
#             print (url)
#         except:
#             pass











