from bing_image_downloader import downloader

downloader.download("people from drone view", limit=1000,  output_dir='images', adult_filter_off=False)

# First one is the query for search
# Second one is the limit of images to download
# Third one is the output directory
# Fourth one is the adult filter off (which is closed in this case)

# Additional notes: First pictures can be irrelevant but its will be okay let the program keep running.