import scrapy

class CountriesSpider(scrapy.Spider):
    name = "countries"
    allowed_domains = ["www.worldometers.info"]    # Here don't put slash at the end otherwise error can be occured
    start_urls = ["https://www.worldometers.info/world-population/population-by-country/"]

    def parse(self, response):
        
        # here because we are going to open the link also so we need the whole a element with text and href because we will customize the response we will not use getall() method here
        countries = response.xpath("//td/a")

        for country in countries:
            # the response object in countries will be stored all the selected path now individual selected path also have the xpath method where we select the elements by starting like this .// 
            # so to select the name
            name = country.xpath('.//text').get()
            link = country.xpath('.//@href').get()
    
            # yield {
            #     "country_name": name,
            #     "country_link": link
            # }


            # But here we are not only crawling one single page but also the corresponding countries content so we need to get request from each link and the content from it to do that:
            # yield scrapy.Request(url=link) # but the problem is the link doesn't contain the domain or type of protocols version but only the path
            #To fix this

            # absolute_url = f"https://www.worldometers.info{link}"
            # But still this isn't the best practice, so other way
            # absolute_url = response.urljoin(link)
            # yield scrapy.Request(absolute_url)

            # Also I can do like this at the same time in one command to successfully request each link
            yield response.follow(url=link)

            # but only sending the request and getting the response is not enough. we have to capture the request so we can scrape -- where we gonna catch the response? 

            # For that we need to create a method which can catch response

            