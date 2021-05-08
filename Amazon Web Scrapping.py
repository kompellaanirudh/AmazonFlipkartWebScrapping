from autoscraper import AutoScraper

amazon_url = "https://www.amazon.in/s?k=alexa"

wanted_list = ["₹5,999",
               "Echo Dot (3rd Gen), Certified Refurbished, Grey – Improved smart speaker with Alexa – Like new, backed with 1-year warranty"]
scraper = AutoScraper()
result = scraper.build(amazon_url, wanted_list)
print(result)
scraper.get_result_similar(amazon_url, grouped=True)

scraper.set_rule_aliases({'rule_gt34': 'Price', 'rule_ly4h': 'Title'})
scraper.keep_rules(['rule_ly4h', 'rule_gt34'])
scraper.save('amazon-search')
