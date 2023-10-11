import requests
from lxml import html
def parser(name,quarter,year,url):

  response = requests.get(url)

  if response.status_code == 200:
    tree = html.fromstring(response.text)

    transcript_element = tree.xpath("/html/body/div[1]/div/div/main/section[2]/div[1]/div/div[3]/div")

    if transcript_element:
        # Extract the text content from the element
        transcript_text = transcript_element[0].text_content()
        filename = f"{name}_{quarter}_{year}.txt"
        
        with open(filename, "w", encoding="utf-8") as file:
            file.write(transcript_text)
        
        print("Text content has been saved to 'earnings_call_transcript.txt'")
    else:
        print("Transcript element not found on the page.")
  else:
    print("Failed to fetch the page. Status code:", response.status_code)
