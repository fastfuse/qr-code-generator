TEXT_TEMPLATE = "{text}"
URL_TEMPLATE = "{url}"
GEO_TEMPLATE = "geo:{latitude},{longitude};"
WIFI_TEMPLATE = "WIFI:S:{ssid};T:{encryption};P:{password};H:false;"
CALENDAR_TEMPLATE = ""

DATA_TEMPLATES = {
    'text': TEXT_TEMPLATE,
    'url': URL_TEMPLATE,
    'geo': GEO_TEMPLATE,
    'wifi': WIFI_TEMPLATE,
    'calendar': CALENDAR_TEMPLATE
}

IMG_PATH_TEMPLATE = '<img style="height:100%;width:100%;display:block;" src="static/img/{filename}" alt="">'
