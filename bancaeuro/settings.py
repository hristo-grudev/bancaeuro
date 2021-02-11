BOT_NAME = 'bancaeuro'

SPIDER_MODULES = ['bancaeuro.spiders']
NEWSPIDER_MODULE = 'bancaeuro.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'bancaeuro.pipelines.BancaeuroPipeline': 100,

}