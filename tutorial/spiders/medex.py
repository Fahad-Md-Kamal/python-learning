import scrapy


class MedexSpider(scrapy.Spider):
    name = 'medex'
    allowed_domains = ['medex.com.bd']
    start_urls = ['http://medex.com.bd/brands/']

    def parse(self, response):
        brand_pages = response.css('ul.pagination li:nth-child(15) a.page-link::attr(href)').get()
        yield from response.follow_all(brand_pages, self.parse)

        products = response.css('a.hoverable-block::attr(href)').getall()
        yield from response.follow_all(products, self.parse_product)

        # brand_urls = response.css('li#nav-menu-drugs a::attr(href)')
        # yield from response.follow_all(brand_urls, self.brand_parse)



    def parse_product(self, response):

        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'medecin': extract_with_css('h1 span:nth-child(2)::text'),
            'generic-name': extract_with_css('div.brand-header div:nth-child(2) a::text'),
            'strength': extract_with_css('div.brand-header div:nth-child(3)::text'),
            'manufactured-by': extract_with_css('div.brand-header div:nth-child(4) a::text'),
        }

        #  response.css('li#nav-menu-drugs a::attr(href)').getall()
