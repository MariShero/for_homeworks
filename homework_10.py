import requests
def get_data(URL):
    response = requests.get(URL)
    if response.status_code == 200:
        print(response.text)
    else:
        print("ვერ მოხერხდა მოცემულ საიტთან კონტაქტის დამყარება")

get_data("https://api.github.com/")
get_data("https://api.hi.com/")
get_data("https://api.aleqsichaiqolos.com/") #ამაზე არ მოქმედებს რატომღაც