from bs4 import BeautifulSoup
import requests
import csv
url = "https://www.amazon.in/s?k=bags&crid=2M096C61O4MLT&qid=1653308124&sprefix=ba%2Caps%2C283&ref=sr_pg_7"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0) Gecko/20100101 Firefox/110.0"
}
html_page = requests.get(url, headers=headers)
soup = BeautifulSoup(html_page.content, "html.parser")
with open("bags.csv","a") as csv_file:
    try:
        csv_writer=csv.writer(csv_file)
        # csv_writer.writerow(['URL','Name','Price','Rating','No_of_reviews','Asin'])
        bags = soup.find_all(
            "div", class_="s-card-container s-overflow-hidden aok-relative puis-include-content-margin puis s-latency-cf-section s-card-border")[1::]
        # print(len(bags))
        for i in bags:
            # print(i.find("div",class_="a-section aok-relative s-image-fixed-height").get_text())

            title_div = i.find(
                "div", class_="sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 sg-col-12-of-24 s-list-col-right")

            title_head = title_div.find(
                "div", class_="a-section a-spacing-none puis-padding-right-small s-title-instructions-style")

            url = title_head.find(
                "a", class_="a-link-normal s-underline-text s-underline-link-text s-link-style a-text-normal")

            main_url = "amazon.in"+str(url.get("href"))
            print(main_url)  # !got

            title = url.find(
                "span", class_="a-size-medium a-color-base a-text-normal").get_text()
            print(title)  # !got

            rating = title_div.find("span", class_="a-size-base").get_text()
            print(rating)  # !got

            reviews = title_div.find("div", class_="a-section a-spacing-none a-spacing-top-micro").find("div", class_="a-row a-size-small").find(
                'a', class_="a-link-normal s-underline-text s-underline-link-text s-link-style").find("span", class_="a-size-base s-underline-text").get_text()
            print(reviews)  # !got
            reviews=str(reviews)
            reviews=reviews[1:-1]
            
            price = title_div.find("span", class_="a-price-whole").get_text()
            print(price)  # !got
            
            asin=main_url.find("dp/")
            asin=main_url[asin+3:asin+13:]#!got
            if(asin[0]=='a'):
                asin="none"
            print(asin)
            
            row = [main_url, title, price, rating, reviews, asin]
            csv_writer.writerow(row)
    except Exception:
        pass
