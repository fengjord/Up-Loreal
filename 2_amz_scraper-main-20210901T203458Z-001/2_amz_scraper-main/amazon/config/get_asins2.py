from requests_html import HTMLSession
import urllib.parse
import pandas as pd 


s = HTMLSession()

search_term = 'vichy'

base_url = "https://www.amazon.ca/s?k="


url = base_url + "vichy&rh=n%3A6205124011%2Cp_89%3AVichy&dc&qid=1630534966&rnid=7590290011&ref=sr_nr_p_89_1"


r = s.get(url)
r.html.render(sleep=1)
    
next_page = r.html.xpath('//li[@class="a-last"]/a/@href', first=True)
if next_page:
    url = urllib.parse.urljoin("https://www.amazon.ca",next_page)

products = r.html.find('div[data-asin]')

asins_list = []


for product in products: 
    if product.attrs['data-asin'] != '':
        asins_list.append(product.attrs['data-asin'])
    


asinsdf = pd.DataFrame(asins_list)
asinsdf.to_csv('asins.csv', index=False)