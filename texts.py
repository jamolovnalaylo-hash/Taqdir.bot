"""
Ko'p tilli matnlar moduli
"""

TEXTS = {
    "welcome": {
        "uz": (
            "🌟 <b>Taqdir Matritsasi Botiga Xush Kelibsiz!</b>\n\n"
            "Bu bot Aziz Numerolog metodikasi asosida sizning:\n"
            "✨ Markaziy energiyangizni\n"
            "💰 Pul kanalingizni\n"
            "❤️ Munosabat karmangizni\n"
            "🎯 Hayot maqsadingizni\n"
            "🌿 Sog'liq chakralaringizni\n\n"
            "hisoblaydi va tahlil qiladi.\n\n"
            "Davom etamiz! 👇"
        ),
        "ru": (
            "🌟 <b>Добро пожаловать в бот Матрицы Судьбы!</b>\n\n"
            "Этот бот на основе методики Aziz Numerolog рассчитает и проанализирует вашу:\n"
            "✨ Центральную энергию\n"
            "💰 Денежный канал\n"
            "❤️ Карму отношений\n"
            "🎯 Жизненную цель\n"
            "🌿 Чакры здоровья\n\n"
            "Продолжаем! 👇"
        ),
        "en": (
            "🌟 <b>Welcome to the Destiny Matrix Bot!</b>\n\n"
            "This bot based on Aziz Numerolog methodology will calculate and analyze your:\n"
            "✨ Central energy\n"
            "💰 Money channel\n"
            "❤️ Relationship karma\n"
            "🎯 Life purpose\n"
            "🌿 Health chakras\n\n"
            "Let's continue! 👇"
        ),
    },
    "ask_name": {
        "uz": "👤 Ismingizni kiriting (faqat ism):",
        "ru": "👤 Введите ваше имя (только имя):",
        "en": "👤 Enter your name (first name only):",
    },
    "ask_birthdate": {
        "uz": "📅 Tug'ilgan sanangizni kiriting:\n\nFormat: <b>KK.OO.YYYY</b>\nMasalan: <b>15.03.1990</b>",
        "ru": "📅 Введите дату рождения:\n\nФормат: <b>ДД.ММ.ГГГГ</b>\nНапример: <b>15.03.1990</b>",
        "en": "📅 Enter your date of birth:\n\nFormat: <b>DD.MM.YYYY</b>\nExample: <b>15.03.1990</b>",
    },
    "invalid_name": {
        "uz": "❌ Iltimos, to'g'ri ism kiriting (kamida 2 harf).",
        "ru": "❌ Пожалуйста, введите правильное имя (минимум 2 буквы).",
        "en": "❌ Please enter a valid name (at least 2 letters).",
    },
    "invalid_date": {
        "uz": "❌ Sana noto'g'ri kiritildi. Iltimos, KK.OO.YYYY formatida kiriting.\nMasalan: 15.03.1990",
        "ru": "❌ Дата введена неверно. Пожалуйста, введите в формате ДД.ММ.ГГГГ.\nНапример: 15.03.1990",
        "en": "❌ Date entered incorrectly. Please enter in DD.MM.YYYY format.\nExample: 15.03.1990",
    },
    "calculating": {
        "uz": "🔮 Matritsangiz hisoblanmoqda...",
        "ru": "🔮 Вычисляем вашу матрицу...",
        "en": "🔮 Calculating your matrix...",
    },
    "ask_topic": {
        "uz": "📌 <b>Qaysi soha haqida bilmoqchisiz?</b>\n\nQuyidagi mavzulardan birini tanlang:",
        "ru": "📌 <b>О какой сфере хотите узнать?</b>\n\nВыберите одну из тем:",
        "en": "📌 <b>What area do you want to learn about?</b>\n\nChoose one of the topics:",
    },
    "btn_money": {
        "uz": "💰 Pul va Moliya",
        "ru": "💰 Деньги и Финансы",
        "en": "💰 Money & Finance",
    },
    "btn_love": {
        "uz": "❤️ Munosabatlar va Sevgi",
        "ru": "❤️ Отношения и Любовь",
        "en": "❤️ Relationships & Love",
    },
    "btn_health": {
        "uz": "🌿 Sog'liq va Chakralar",
        "ru": "🌿 Здоровье и Чакры",
        "en": "🌿 Health & Chakras",
    },
    "btn_purpose": {
        "uz": "🎯 Maqsad va Qobiliyatlar",
        "ru": "🎯 Цель и Способности",
        "en": "🎯 Purpose & Abilities",
    },
    "btn_karma": {
        "uz": "🔮 Karma va Ajdodlar",
        "ru": "🔮 Карма и Предки",
        "en": "🔮 Karma & Ancestors",
    },
}


def get_text(key: str, lang: str) -> str:
    lang = lang if lang in ["uz", "ru", "en"] else "uz"
    return TEXTS.get(key, {}).get(lang, TEXTS.get(key, {}).get("uz", ""))
