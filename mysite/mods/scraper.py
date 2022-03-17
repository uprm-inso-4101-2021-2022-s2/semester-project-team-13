from autoscraper import AutoScraper
from .models import Mod


def nexus_scraper(url):

    base_url = 'https://www.nexusmods.com/skyrim/mods/3863?tab=description'

    # We can add one or multiple candidates here.
    # You can also put urls here to retrieve urls.
    wanted_list = ["SkyUI", #mod_title
                   "SkyUI Team", #mod_author
                   "Skyrim", #mod_game
                   "Elegant, PC-friendly interface mod with many advanced features. " #mod_description
                   ]

    scraper = AutoScraper()
    result = scraper.build(base_url, wanted_list)

    result = scraper.get_result_exact(url)
    newmod = Mod(mod_title=result[0], mod_author=result[1], mod_source=url, mod_game=result[2], mod_description=result [3])
    newmod.save()
    newmod.id
    # i = 3863
    #
    # while (i < 3867):
    #     url = 'https://www.nexusmods.com/skyrim/mods/' + str(i) + '?tab=description'
    #     i = i + 1
    #     result = scraper.get_result_exact(url)

    return result

