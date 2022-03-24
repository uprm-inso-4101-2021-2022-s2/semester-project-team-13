from autoscraper import AutoScraper
from .models import Mod


def nexus_scraper(url):

    base_url = 'https://www.nexusmods.com/stardewvalley/mods/11288'

    # We can add one or multiple candidates here.
    # You can also put urls here to retrieve urls.
    wanted_list = ["Aquarism - Immersive Fish Ponds", #mod_title
                   "DaLion", #mod_author
                   "Stardew Valley", #mod_game
                   "Makes Fish Ponds useful and immersive by preserving fish quality, scaling roe production with population, and spontaneously growing algae if left empty." #mod_description
                   ]

    scraper = AutoScraper()
    result = scraper.build(base_url, wanted_list)

    result = scraper.get_result_exact(url)
    newmod = Mod(mod_title=result[0], mod_author=result[1], mod_source=url, mod_game=result[3], mod_description=result[4])
    newmod.save()
    newmod.id

    return result


def nexus_scraper(url, start, end):

    base_url = 'https://www.nexusmods.com/stardewvalley/mods/11288'
    wanted_list = ["Aquarism - Immersive Fish Ponds", #mod_title
                   "DaLion", #mod_author
                   "Stardew Valley", #mod_game
                   "Makes Fish Ponds useful and immersive by preserving fish quality, scaling roe production with population, and spontaneously growing algae if left empty." #mod_description
                   ]
    scraper = AutoScraper()
    result = scraper.build(base_url, wanted_list)

    while(start<=end):
        iter_url = url + str(start)
        result = scraper.get_result_exact(iter_url)
        newmod = Mod(mod_title=result[0], mod_author=result[1], mod_source=iter_url, mod_game=result[3],
                     mod_description=result[4])
        newmod.save()
        newmod.id
        start = start + 1

    return result
