from dgram import types
from dgram.async_dgram import Asyncdgram
from dgram.asyncio_filters import AdvancedCustomFilter
from dgram.callback_data import CallbackData, CallbackDataFilter

calendar_factory = CallbackData("year", "month", prefix="calendar")
calendar_zoom = CallbackData("year", prefix="calendar_zoom")


class CalendarCallbackFilter(AdvancedCustomFilter):
    key = 'calendar_config'

    async def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)


class CalendarZoomCallbackFilter(AdvancedCustomFilter):
    key = 'calendar_zoom_config'

    async def check(self, call: types.CallbackQuery, config: CallbackDataFilter):
        return config.check(query=call)


def bind_filters(bot: Asyncdgram):
    bot.add_custom_filter(CalendarCallbackFilter())
    bot.add_custom_filter(CalendarZoomCallbackFilter())
