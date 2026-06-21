import logging
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import (
    Application, CommandHandler, MessageHandler,
    CallbackQueryHandler, ConversationHandler, filters, ContextTypes
)
from numerology import calculate_matrix, get_arcana_description, get_topic_analysis
from texts import get_text

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

LANG, NAME, BIRTHDATE, TOPIC, QUESTION = range(5)

BOT_TOKEN = os.environ.get("BOT_TOKEN", "YOUR_BOT_TOKEN_HERE")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton("🇺🇿 O'zbek", callback_data="lang_uz"),
            InlineKeyboardButton("🇷🇺 Русский", callback_data="lang_ru"),
            InlineKeyboardButton("🇬🇧 English", callback_data="lang_en"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(
        "🌟 Taqdir Matritsasi | Матрица Судьбы | Destiny Matrix\n\nTilni tanlang / Выберите язык / Choose language:",
        reply_markup=reply_markup
    )
    return LANG


async def set_language(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = query.data.split("_")[1]
    context.user_data["lang"] = lang
    await query.edit_message_text(get_text("welcome", lang))
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
    import re
    match = re.match(r"(\d{1,2})[.\-/](\d{1,2})[.\-/](\d{4})", text)
    if not match:
        await update.message.reply_text(get_text("invalid_date", lang))
        return BIRTHDATE
    day, month, year = int(match.group(1)), int(match.group(2)), int(match.group(3))
    if not (1 <= day <= 31 and 1 <= month <= 12 and 1900 <= year <= 2015):
        await update.message.reply_text(get_text("invalid_date", lang))
        return BIRTHDATE
    context.user_data["birthdate"] = (day, month, year)
    matrix = calculate_matrix(day, month, year)
    context.user_data["matrix"] = matrix
    name = context.user_data.get("name", "")
    loading_msg = await update.message.reply_text(get_text("calculating", lang))
    analysis = build_general_analysis(matrix, name, lang)
    await loading_msg.delete()
    await update.message.reply_text(analysis, parse_mode="HTML")
    keyboard = [
        [InlineKeyboardButton(get_text("btn_money", lang), callback_data="topic_money")],
        [InlineKeyboardButton(get_text("btn_love", lang), callback_data="topic_love")],
        [InlineKeyboardButton(get_text("btn_health", lang), callback_data="topic_health")],
        [InlineKeyboardButton(get_text("btn_purpose", lang), callback_data="topic_purpose")],
        [InlineKeyboardButton(get_text("btn_karma", lang), callback_data="topic_karma")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text(get_text("ask_topic", lang), reply_markup=reply_markup, parse_mode="HTML")
    return TOPIC


def build_general_analysis(matrix, name, lang):
    A, B, C, E = matrix["A"], matrix["B"], matrix["C"], matrix["E"]
    a_desc = get_arcana_description(A, lang, "short")
    b_desc = get_arcana_description(B, lang, "short")
    c_desc = get_arcana_description(C, lang, "short")
    e_desc = get_arcana_description(E, lang, "short")
    if lang == "uz":
        return (f"✨ <b>{name} uchun Taqdir Matritsasi</b>\n\n"
                f"🔴 <b>A={A}</b> — {a_desc}\n"
                f"🔵 <b>B={B}</b> — {b_desc}\n"
                f"🟡 <b>C={C}</b> — {c_desc}\n"
                f"🟢 <b>E={E} (Markaziy)</b> — {e_desc}\n\n"
                f"📌 <b>40 yoshgacha vazifa (C={C}):</b> {get_arcana_description(C, lang, 'task')}")
    elif lang == "ru":
        return (f"✨ <b>Матрица Судьбы для {name}</b>\n\n"
                f"🔴 <b>A={A}</b> — {a_desc}\n"
                f"🔵 <b>B={B}</b> — {b_desc}\n"
                f"🟡 <b>C={C}</b> — {c_desc}\n"
                f"🟢 <b>E={E} (Центральная)</b> — {e_desc}\n\n"
                f"📌 <b>Задача до 40 лет (C={C}):</b> {get_arcana_description(C, lang, 'task')}")
    else:
        return (f"✨ <b>Destiny Matrix for {name}</b>\n\n"
                f"🔴 <b>A={A}</b> — {a_desc}\n"
                f"🔵 <b>B={B}</b> — {b_desc}\n"
                f"🟡 <b>C={C}</b> — {c_desc}\n"
                f"🟢 <b>E={E} (Central)</b> — {e_desc}\n\n"
                f"📌 <b>Task until 40 (C={C}):</b> {get_arcana_description(C, lang, 'task')}")


async def handle_topic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "uz")
    topic = query.data.split("_")[1]
    matrix = context.user_data.get("matrix", {})
    name = context.user_data.get("name", "")
    analysis = get_topic_analysis(topic, matrix, name, lang)
    await query.edit_message_text(analysis, parse_mode="HTML")
    await show_diagnostic_offer(query.message, lang)
    return TOPIC


async def show_diagnostic_offer(message, lang):
    if lang == "uz":
        text = ("🔮 <b>Chuqurroq bilishni xohlaysizmi?</b>\n\n"
                "✅ Pul bloklaringizni aniq bilib olasiz\n"
                "✅ Munosabatlaringizdagi karmani tushunasiz\n"
                "✅ Hayotingiz maqsadini aniq ko'rasiz\n\n"
                "💯 <b>100% kafolat beriladi!</b>")
    elif lang == "ru":
        text = ("🔮 <b>Хотите узнать глубже?</b>\n\n"
                "✅ Точно узнаете свои денежные блоки\n"
                "✅ Поймёте карму в отношениях\n"
                "✅ Ясно увидите цель своей жизни\n\n"
                "💯 <b>100% гарантия!</b>")
    else:
        text = ("🔮 <b>Want to go deeper?</b>\n\n"
                "✅ Identify your money blocks\n"
                "✅ Understand relationship karma\n"
                "✅ See your life purpose clearly\n\n"
                "💯 <b>100% guaranteed!</b>")
    keyboard = [
        [InlineKeyboardButton("💎 " + ("Diagnostika olish" if lang=="uz" else "Получить диагностику" if lang=="ru" else "Get Diagnostic"), callback_data="get_diagnostic")],
        [InlineKeyboardButton("💰 " + ("Narxlar" if lang=="uz" else "Цены" if lang=="ru" else "Prices"), callback_data="show_prices")],
        [InlineKeyboardButton("🔙 " + ("Boshqa mavzu" if lang=="uz" else "Другая тема" if lang=="ru" else "Other topic"), callback_data="back_topics")],
    ]
    await message.reply_text(text, reply_markup=InlineKeyboardMarkup(keyboard), parse_mode="HTML")


async def handle_diagnostic(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    lang = context.user_data.get("lang", "uz")
    if query.data == "get_diagnostic":
        msgs = {"uz": "📩 Diagnostika uchun: @YOUR_USERNAME", "ru": "📩 Для диагностики: @YOUR_USERNAME", "en": "📩 For diagnostic: @YOUR_USERNAME"}
        await query.edit_message_text(msgs.get(lang, msgs["uz"]))
    elif query.data == "show_prices":
        msgs = {"uz": "💰 <b>Narxlar tez kunda!</b>\n@YOUR_USERNAME ga yozing", "ru": "💰 <b>Цены скоро!</b>\nПишите @YOUR_USERNAME", "en": "💰 <b>Prices coming soon!</b>\nContact @YOUR_USERNAME"}
        await query.edit_message_text(msgs.get(lang, msgs["uz"]), parse_mode="HTML")
    elif query.data == "back_topics":
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
    lang = context.user_data.get("lang", "uz")
    msgs = {"uz": "Bot to'xtatildi. /start bilan qayta boshlang.", "ru": "Бот остановлен. Начните с /start.", "en": "Bot stopped. Start with /start."}
    await update.message.reply_text(msgs.get(lang, msgs["uz"]))
    return ConversationHandler.END


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CommandHandler("start", start)],
        states={
            LANG: [CallbackQueryHandler(set_language, pattern="^lang_")],
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            BIRTHDATE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_birthdate)],
            TOPIC: [
                CallbackQueryHandler(handle_topic, pattern="^topic_"),
                CallbackQueryHandler(handle_diagnostic, pattern="^(get_diagnostic|show_prices|back_topics)$"),
            ],
        },
        fallbacks=[CommandHandler("cancel", cancel)],
        allow_reentry=True,
    )
    app.add_handler(conv_handler)
    logger.info("Bot ishga tushdi...")
    app.run_polling(drop_pending_updates=True)


if __name__ == "__main__":
    main()
