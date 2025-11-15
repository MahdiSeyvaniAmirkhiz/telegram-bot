from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

# ---------------------------
#  توکن ربات
# ---------------------------
TOKEN = "8363399737:AAERyUC0hTNQrVJoTwdAvACCO2Uc_uzRg-M"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# ---------------------------
#  منوی اصلی / دکمه‌های شیشه‌ای
# ---------------------------
@dp.message_handler(commands=['start'])
async def start(message: types.Message):

    keyboard = InlineKeyboardMarkup()

    keyboard.add(
        InlineKeyboardButton("استخراج از وب", callback_data="scrape")
    )
    keyboard.add(
        InlineKeyboardButton("انتشار پست", callback_data="publish")
    )
    keyboard.add(
        InlineKeyboardButton("استخراج محصول", callback_data="scrapeproduct")
    )
    keyboard.add(
        InlineKeyboardButton("استخراج شماره بیزینس‌ها", callback_data="scrapenumber")
    )

    await message.answer(
        "سلام! 👋\nاز منوی شیشه‌ای زیر یکی از گزینه‌ها را انتخاب کن:",
        reply_markup=keyboard
    )


# ---------------------------
#  هندلرهای مربوط به دکمه‌ها
# ---------------------------
@dp.callback_query_handler(lambda c: True)
async def callback_handler(call: types.CallbackQuery):

    if call.data == "scrape":
        await call.answer("استخراج از وب انتخاب شد ✔️", show_alert=False)

    elif call.data == "publish":
        await call.answer("انتشار پست انتخاب شد ✔️", show_alert=False)

    elif call.data == "scrapeproduct":
        await call.answer("استخراج محصول انتخاب شد ✔️", show_alert=False)

    elif call.data == "scrapenumber":
        await call.answer("استخراج شماره بیزینس‌ها انتخاب شد ✔️", show_alert=False)

    else:
        await call.answer("گزینه نامعتبر!", show_alert=False)


# ---------------------------
#  اجرای ربات
# ---------------------------
executor.start_polling(dp, skip_updates=True)
