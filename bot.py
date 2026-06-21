import logging
import os
import re
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, MessageHandler, CallbackQueryHandler, ConversationHandler, filters, ContextTypes
from numerology import calculate_matrix, get_arcana_description, get_topic_analysis
from texts import get_text

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LANG, NAME, BIRTHDATE, TOPIC = range(4)
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[
        InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uz"),
        InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
        InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
    ]]
    await update.message.reply_text(
        "🌟 Taqdir Matritsasi | Матрица Судьбы | Destiny Matrix\n\nTilni tanlang:",
        reply_markup=InlineKeyboardMarkup(keyboard)
    )
    return LANG

async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = query.data.split("_")[1]
    context.user_data["lang"] = lang
    await query.edit_message_text(get_text("welcome", lang), parse_mode="HTML")
    await query.message.reply_text(get_text("ask_name", lang))
    return NAME

async def get_name(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "uz")
    name = update.message.text.strip()
    if len(name) < 2:
        await update.message.reply_text(get_text("invalid_name", lang))
        return NAME
    context.user_data["name"] = name
    await update.message.reply_text(get_text("ask_birthdate", lang), parse_mode="HTML")
    return BIRTHDATE

async def get_birthdate(update: Update, context: ContextTypes.DEFAULT_TYPE):
    lang = context.user_data.get("lang", "uz")
    text = update.message.text.strip()
    match = re.match(r"(\d{1,2})[.\-/](\d{1,2})[.\-/](\d{4})", text)
    if not match:
        await update.message.reply_text(get_text("invalid_date", lang))
        return BIRTHDATE
    day, month, year = int(match.group(1)), int(match.group(2)), int(match.group(3))
    if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2015):
        await update.message.reply_text(get_text("invalid_date", lang))
        return BIRTHDATE
    matrix = calculate_matrix(day, month, year)
    context.user_data["matrix"] = matrix
    name = context.user_data.get("name", "")
    A,B,C,E = matrix["A"],matrix["B"],matrix["C"],matrix["E"]
    if lang == "uz":
        text2 = (f"✨ <b>{name} uchun Taqdir Matritsasi</b>\n\n"
                f"🔴 A={A} — {get_arcana_description(A,lang)}\n"
                f"🔵 B={B} — {get_arcana_description(B,lang)}\n"
                f"🟡 C={C} — {get_arcana_description(C,lang)}\n"
                f"🟢 E={E} (Markaziy) — {get_arcana_description(E,lang)}\n\n"
                f"📌 40 yoshgacha vazifa: {get_arcana_description(C,lang,'task')}")
    elif lang == "ru":
        text2 = (f"✨ <b>Матрица Судьбы для {name}</b>\n\n"
                f"🔴 A={A} — {get_arcana_description(A,lang)}\n"
                f"🔵 B={B} — {get_arcana_description(B,lang)}\n"
                f"🟡 C={C} — {get_arcana_description(C,lang)}\n"
                f"🟢 E={E} (Центральная) — {get_arcana_description(E,lang)}\n\n"
                f"📌 Задача до 40 лет: {get_arcana_description(C,lang,'task')}")
    else:
        text2 = (f"✨ <b>Destiny Matrix for {name}</b>\n\n"
                f"🔴 A={A} — {get_arcana_description(A,lang)}\n"
                f"🔵 B={B} — {get_arcana_description(B,lang)}\n"
                f"🟡 C={C} — {get_arcana_description(C,lang)}\n"
                f"🟢 E={E} (Central) — {get_arcana_description(E,lang)}\n\n"
                f"📌 Task until 40: {get_arcana_description(C,lang,'task')}")
    await update.message.reply_text(text2, parse_mode="HTML")
    keyboard = [
        [InlineKeyboardButton(get_text("btn_money", lang), callback_data="topic_money")],
        [InlineKeyboardButton(get_text("btn_love", lang), callback_data="topic_love")],
        [InlineKeyboardButton(get_text("btn_health", lang), callback_data="topic_health")],
        [InlineKeyboardButton(get_text("btn_purpose", lang), callback_data="topic_purpose")],
        [InlineKeyboardButton(get_text("btn_karma", lang), callback_data="topic_karma")],
    ]
    await update.message.reply_text(get_text("ask_topic", lang), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")
    return TOPIC

async def handle_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "uz")
    topic = query.data.split("_")[1]
    matrix = context.user_data.get("matrix", {})
    name = context.user_data.get("name", "")
    analysis = get_topic_analysis(topic, matrix, name, lang)
    await query.edit_message_text(analysis, parse_mode="HTML")
    if lang == "uz":
        txt = "🔮 <b>Chuqurroq bilishni xohlaysizmi?</b>\n\n✅ Pul bloklaringizni aniqlash\n✅ Munosabat karmangiz\n✅ Hayot maqsadingiz\n\n💯 <b>100% kafolat!</b>"
    elif lang == "ru":
        txt = "🔮 <b>Хотите узнать глубже?</b>\n\n✅ Денежные блоки\n✅ Карма отношений\n✅ Цель жизни\n\n💯 <b>100% гарантия!</b>"
    else:
        txt = "🔮 <b>Want to go deeper?</b>\n\n✅ Money blocks\n✅ Relationship karma\n✅ Life purpose\n\n💯 <b>100% guaranteed!</b>"
    keyboard = [
        [InlineKeyboardButton("💎 " + ("Diagnostika" if lang=="uz" else "Диагностика" if lang=="ru" else "Diagnostic"), callback_data="diag")],
        [InlineKeyboardButton("💰 " + ("Narxlar" if lang=="uz" else "Цены" if lang=="ru" else "Prices"), callback_data="price")],
        [InlineKeyboardButton("🔙 " + ("Boshqa mavzu" if lang=="uz" else "Другая тема" if lang=="ru" else "Other topic"), callback_data="back")],
    ]
    await query.message.reply_text(txt, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")
    return TOPIC

async def handle_buttons(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "uz")
    if query.data == "diag":
        msgs = {"uz":"📩 Diagnostika uchun: @YOUR_USERNAME","ru":"📩 Для диагностики: @YOUR_USERNAME","en":"📩 Contact: @YOUR_USERNAME"}
        await query.edit_message_text(msgs.get(lang, msgs["uz"]))
    elif query.data == "price":
        msgs = {"uz":"💰 <b>Narxlar tez kunda!</b>","ru":"💰 <b>Цены скоро!</b>","en":"💰 <b>Prices coming soon!</b>"}
        await query.edit_message_text(msgs.get(lang, msgs["uz"]), parse_mode="HTML")
    elif query.data == "back":
        keyboard = [
            [InlineKeyboardButton(get_text("btn_money", lang), callback_data="topic_money")],
            [InlineKeyboardButton(get_text("btn_love", lang), callback_data="topic_love")],
            [InlineKeyboardButton(get_text("btn_health", lang), callback_data="topic_health")],
            [InlineKeyboardButton(get_text("btn_purpose", lang), callback_data="topic_purpose")],
            [InlineKeyboardButton(get_text("btn_karma", lang), callback_data="topic_karma")],
        ]
        await query.edit_message_text(get_text("ask_topic", lang), reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")
    return TOPIC

async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Bot to'xtatildi. /start bilan qayta boshlang.")
    return ConversationHandler.END

def main():
    app = Application.builder().token(BOT_TOKEN).build()
    conv = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            LANG: [CallbackQueryHandler(set_language, pattern="^lang_")],
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            BIRTHDATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_birthdate)],
            TOPIC: [
                CallbackQueryHandler(handle_topic, pattern="^topic_"),
                CallbackQueryHandler(handle_buttons, pattern="^(diag|price|back)$"),
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True,
    )
    app.add_handler(conv)
    logger.info("Bot ishga tushdi!")
    app.run_polling(drop_pending_updates=True)

if __name__ == "__main__":
    main()
