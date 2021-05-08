from autoscraper import AutoScraper

flipkart_url = "https://www.flipkart.com/search?q=iphones&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"

wanted_list = ["₹32,999", "Apple iPhone SE (White, 64 GB) (Includes EarPods, Power..."]
scraper = AutoScraper()
result = scraper.build(flipkart_url, wanted_list)
print(result)
scraper.get_result_similar(flipkart_url, grouped=True)

scraper.set_rule_aliases({'rule_o8x0': 'Price', 'rule_4gn6': 'Title'})
scraper.keep_rules(['rule_4gn6', 'rule_o8x0'])
scraper.save('flipkart-search')
