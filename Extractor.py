from selenium import webdriver
from selenium.webdriver.common.by import By
import time

main_driver = webdriver.Chrome()

main_driver.get("https://monasebat.anhar.ir/")

# text file name
FileName = "Extracted.txt"
file = open(FileName, "w", encoding="utf-8")


# Lists
a_td_list = []
url_list = []

# td
td_element = main_driver.find_elements(By.TAG_NAME, "td")
for td in td_element:
    try:
        a_element = td.find_elements(By.TAG_NAME, "a")
        href_element = a_element[0].get_attribute("href")
        url_list.append(href_element)
    except:
        print(".")

print("urls: ", len(url_list))

for getData in url_list:
    # for i in range(2):
    # driver = webdriver.Chrome()
    main_driver.get(getData)
    # driver.get(getData)

    file.write("_" * 80 + "\n")
    # Write Title Of DayPage
    h1_element = main_driver.find_element(By.TAG_NAME, "h1")
    file.write(h1_element.text + "\n")

    # Find event links from every day
    article1 = main_driver.find_element(By.CLASS_NAME, "article")

    article1_links = [
        element
        for element in article1.find_elements(By.TAG_NAME, "a")
        if element.text != None and element.text != ""
    ]

    print("Len Link1 " + str(len(article1_links)))
    for link in article1_links:
        events_driver = webdriver.Chrome()
        # mylink = link
        mylink_href = link.get_attribute("href")
        print("Next Page")
        events_driver.get(mylink_href)

        file.write("-" * 40 + "\n")

        # Write Titles Of EventPage
        Title = events_driver.find_element(By.TAG_NAME, "h1")
        file.write(Title.text + "\n")

        # Find Descirption content of every event
        article2 = events_driver.find_element(By.CLASS_NAME, "article")

        article2_spans = [
            span_element
            for span_element in article2.find_elements(By.TAG_NAME, "span")
            if span_element.text != None and span_element.text != ""
        ]

        existing_contents = []

        article2_span_contents = []

        # Distinct content
        for span in article2_spans:
            if span.text in existing_contents:
                continue
            else:
                article2_span_contents.append(span)
                existing_contents.append(span.text)

        # article2_span_contents = [
        #     span_element
        #     for span_element in article2.find_elements(By.TAG_NAME, "span")
        #     if span_element.text != None and span_element.text != ""
        # ]

        for element in article2_span_contents:
            file.write(element.text + "\n")
        file.write("-" * 40 + "\n")

    file.write("_" * 80 + "\n")


print("Extracting Finished!")

file.write("Finished" + "\n")

file.close()
