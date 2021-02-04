BOT_NAME = 'turkishbank'
SPIDER_MODULES = ['turkishbank.spiders']
NEWSPIDER_MODULE = 'turkishbank.spiders'
LOG_LEVEL = 'WARNING'
ROBOTSTXT_OBEY = True
ITEM_PIPELINES = {
   'turkishbank.pipelines.DatabasePipeline': 300,
}