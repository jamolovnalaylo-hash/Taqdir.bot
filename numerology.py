def reduce_to_arcana(n):
    if n == 0:
        return 22
    while n > 22:
        n = sum(int(d) for d in str(n))
    return n

def calculate_matrix(day, month, year):
    A = reduce_to_arcana(day)
    B = reduce_to_arcana(month)
    C = reduce_to_arcana(sum(int(d) for d in str(year)))
    D = reduce_to_arcana(A + B + C)
    E = reduce_to_arcana(A + B + C + D)
    M = reduce_to_arcana(D + E)
    N = reduce_to_arcana(M + D)
    L = reduce_to_arcana(E + C)
    R = reduce_to_arcana(M + L)
    R1 = reduce_to_arcana(R + M)
    R2 = reduce_to_arcana(R + L)
    K = reduce_to_arcana(B + E)
    F = reduce_to_arcana(A + B)
    G = reduce_to_arcana(B + C)
    F2 = reduce_to_arcana(F + L)
    G2 = reduce_to_arcana(G + L)
    O = reduce_to_arcana(A + E)
    P = reduce_to_arcana(B + E)
    Q = reduce_to_arcana(C + E)
    H = reduce_to_arcana(C + D)
    I = reduce_to_arcana(A + D)
    chakras = {
        "sahasrara": reduce_to_arcana(A + B),
        "ajna": reduce_to_arcana(O + P),
        "vishudha": reduce_to_arcana(A + E),
        "anahata": reduce_to_arcana(D + E),
        "manipura": E,
        "muladhara": reduce_to_arcana(C + D),
        "svadhisthana": reduce_to_arcana(M + N),
    }
    return {
        "A":A,"B":B,"C":C,"D":D,"E":E,
        "M":M,"N":N,"L":L,"R":R,"R1":R1,"R2":R2,
        "K":K,"F":F,"G":G,"F2":F2,"G2":G2,
        "O":O,"P":P,"J":O,"Q":Q,"H":H,"I":I,
        "chakras":chakras,
        "raw":{"day":day,"month":month,"year":year}
    }

ARCANA_INFO = {
    1: {
        "plus_uz": "Kuchli liderlik, yangi yo'llarni kashf etish, dadillik",
        "minus_uz": "Haddan ortiq o'ziga ishonch, boshqalarni tinglamas",
        "tavsiya_uz": "Intuitsiyangizga ishoning, lekin jamoada ishlashni o'rganing",
        "plus_ru": "Сильное лидерство, открытие новых путей, смелость",
        "minus_ru": "Чрезмерная самоуверенность, не слушает других",
        "tavsiya_ru": "Доверяйте интуиции, но учитесь работать в команде",
        "plus_en": "Strong leadership, discovering new paths, boldness",
        "minus_en": "Overconfidence, doesn't listen to others",
        "tavsiya_en": "Trust your intuition but learn to work in a team",
    },
    2: {
        "plus_uz": "Nozik his-tuyg'u, murosaga kelish qobiliyati, tinchlik yaratish",
        "minus_uz": "Qaror qabul qilishda qiyinchilik, o'zini ikkinchi o'ringa qo'yish",
        "tavsiya_uz": "O'z fikringizni bayon qiling, rozi bo'lishdan qo'rqmang",
        "plus_ru": "Тонкая чувствительность, умение идти на компромисс",
        "minus_ru": "Трудности с принятием решений, ставит себя на второй план",
        "tavsiya_ru": "Выражайте своё мнение, не бойтесь не соглашаться",
        "plus_en": "Fine sensitivity, ability to compromise, peacemaking",
        "minus_en": "Difficulty making decisions, puts self second",
        "tavsiya_en": "Express your opinion, don't be afraid to disagree",
    },
    3: {
        "plus_uz": "Kuchli ijodkorlik, so'z ustasi, odamlarni ilhomlantirish",
        "minus_uz": "Tarqoqlik, ko'p boshlab tugata olmaslik, ortiqcha gapirish",
        "tavsiya_uz": "Ijodingizni tizimga soling, bitta loyihaga e'tibor qarating",
        "plus_ru": "Мощное творчество, мастерство слова, вдохновение людей",
        "minus_ru": "Рассеянность, начинает много но не заканчивает",
        "tavsiya_ru": "Систематизируйте творчество, сосредоточьтесь на одном проекте",
        "plus_en": "Strong creativity, mastery of words, inspiring people",
        "minus_en": "Scattered energy, starts many things but doesn't finish",
        "tavsiya_en": "Systematize your creativity, focus on one project",
    },
    4: {
        "plus_uz": "Ishonchlilik, barqarorlik, tizimli fikrlash, mehnatsevarlik",
        "minus_uz": "Qattiqlik, o'zgarishlardan qo'rquv, ortiqcha nazorat",
        "tavsiya_uz": "Ba'zan qoidalarni buzing, moslashuvchan bo'lishni o'rganing",
        "plus_ru": "Надёжность, стабильность, системное мышление, трудолюбие",
        "minus_ru": "Жёсткость, страх перемен, чрезмерный контроль",
        "tavsiya_ru": "Иногда нарушайте правила, учитесь быть гибким",
        "plus_en": "Reliability, stability, systematic thinking, hard work",
        "minus_en": "Rigidity, fear of change, excessive control",
        "tavsiya_en": "Sometimes break the rules, learn to be flexible",
    },
    5: {
        "plus_uz": "Chuqur bilim, ma'naviy yo'nalish, o'qitish qobiliyati",
        "minus_uz": "Dogmatizm, o'z fikrdan chekinmaslik, ustoz rolini suiste'mol qilish",
        "tavsiya_uz": "Yangi g'oyalarga ochiq bo'ling, shogirdlaringizdan ham o'rganing",
        "plus_ru": "Глубокие знания, духовное наставничество, способность обучать",
        "minus_ru": "Догматизм, негибкость во взглядах",
        "tavsiya_ru": "Будьте открыты к новым идеям, учитесь у своих учеников",
        "plus_en": "Deep knowledge, spiritual guidance, teaching ability",
        "minus_en": "Dogmatism, inflexibility in views",
        "tavsiya_en": "Be open to new ideas, learn from your students too",
    },
    6: {
        "plus_uz": "Chuqur muhabbat, uyg'unlik yaratish, go'zallikni his qilish",
        "minus_uz": "Qaramlik, sevgisiz yashay olmaslik, noto'g'ri tanlov",
        "tavsiya_uz": "O'zingizni seving, munosabatda tenglikni saqlang",
        "plus_ru": "Глубокая любовь, создание гармонии, чувство красоты",
        "minus_ru": "Зависимость, не может жить без любви, неправильный выбор",
        "tavsiya_ru": "Любите себя, сохраняйте равенство в отношениях",
        "plus_en": "Deep love, creating harmony, feeling beauty",
        "minus_en": "Dependency, can't live without love, wrong choices",
        "tavsiya_en": "Love yourself, maintain equality in relationships",
    },
    7: {
        "plus_uz": "G'alaba qozonish kuchi, maqsadga intilish, intizom",
        "minus_uz": "Haddan ortiq raqobat, mag'lubiyatni qabul qila olmaslik",
        "tavsiya_uz": "Natijaga emas, jarayonga ham e'tibor bering",
        "plus_ru": "Сила победы, целеустремлённость, дисциплина",
        "minus_ru": "Чрезмерная конкуренция, не принимает поражение",
        "tavsiya_ru": "Обращайте внимание не только на результат, но и на процесс",
        "plus_en": "Power of victory, goal-orientation, discipline",
        "minus_en": "Excessive competition, can't accept defeat",
        "tavsiya_en": "Pay attention to the process, not just the result",
    },
    8: {
        "plus_uz": "Buyuk ichki kuch, sabr, qiyinchiliklarni yengish qobiliyati",
        "minus_uz": "O'z kuchini bilmaslik, haddan ortiq o'zini cheklash",
        "tavsiya_uz": "O'z kuchingizga ishoning, qo'rquvga emas kuchga tayanib yashang",
        "plus_ru": "Великая внутренняя сила, терпение, способность преодолевать трудности",
        "minus_ru": "Не знает своей силы, чрезмерно ограничивает себя",
        "tavsiya_ru": "Верьте в свою силу, живите опираясь на силу, а не на страх",
        "plus_en": "Great inner strength, patience, ability to overcome difficulties",
        "minus_en": "Doesn't know own strength, excessively limits self",
        "tavsiya_en": "Believe in your strength, live based on power not fear",
    },
    9: {
        "plus_uz": "Chuqur donolik, ichki dunyo boyligi, ma'naviy qidiruv",
        "minus_uz": "Yolg'izlikka moyillik, odamlardan uzoqlashish, sirlilik",
        "tavsiya_uz": "Bilimingizni ulashing, yolg'izlikni tanlasa ham aloqani uzmang",
        "plus_ru": "Глубокая мудрость, богатство внутреннего мира, духовный поиск",
        "minus_ru": "Склонность к одиночеству, отдаление от людей",
        "tavsiya_ru": "Делитесь знаниями, даже выбирая одиночество не теряйте связей",
        "plus_en": "Deep wisdom, rich inner world, spiritual seeking",
        "minus_en": "Tendency to solitude, distancing from people",
        "tavsiya_en": "Share your wisdom, even in solitude don't lose connections",
    },
    10: {
        "plus_uz": "O'zgarishlarga moslashish, omadni jalb qilish, tsiklik fikrlash",
        "minus_uz": "Beqarorlik, tashqi sharoitlarga haddan ortiq bog'liqlik",
        "tavsiya_uz": "O'zgarishlarni dushman emas, do'st deb qabul qiling",
        "plus_ru": "Адаптация к переменам, притяжение удачи, цикличное мышление",
        "minus_ru": "Нестабильность, чрезмерная зависимость от внешних условий",
        "tavsiya_ru": "Принимайте перемены как друга, а не врага",
        "plus_en": "Adapting to changes, attracting luck, cyclical thinking",
        "minus_en": "Instability, over-dependence on external conditions",
        "tavsiya_en": "Accept changes as a friend, not an enemy",
    },
    11: {
        "plus_uz": "Adolat, haqiqatni ko'rish, muvozanat saqlash qobiliyati",
        "minus_uz": "Haddan ortiq tanqidchilik, hamma narsani o'lchab tortish",
        "tavsiya_uz": "Yurak bilan ham qaror qiling, nafaqat aql bilan",
        "plus_ru": "Справедливость, видение истины, способность соблюдать баланс",
        "minus_ru": "Чрезмерная критичность, взвешивает всё слишком тщательно",
        "tavsiya_ru": "Принимайте решения и сердцем, не только умом",
        "plus_en": "Justice, seeing truth, ability to maintain balance",
        "minus_en": "Excessive criticism, weighs everything too carefully",
        "tavsiya_en": "Make decisions with your heart too, not just your mind",
    },
    12: {
        "plus_uz": "Boshqacha nuqtai nazar, sabr, chuqur tushunish",
        "minus_uz": "O'zini qurbon qilish, passivlik, vaziyatni o'zgartira olmaslik",
        "tavsiya_uz": "O'zingizni qurbon qilmang, faol pozitsiya oling",
        "plus_ru": "Иной взгляд на вещи, терпение, глубокое понимание",
        "minus_ru": "Самопожертвование, пассивность, неспособность изменить ситуацию",
        "tavsiya_ru": "Не жертвуйте собой, занимайте активную позицию",
        "plus_en": "Different perspective, patience, deep understanding",
        "minus_en": "Self-sacrifice, passivity, inability to change situations",
        "tavsiya_en": "Don't sacrifice yourself, take an active position",
    },
    13: {
        "plus_uz": "Transformatsiya kuchi, yangilanish, eski narsalarni qoldira olish",
        "minus_uz": "O'zgarishlardan qo'rquv, o'tib ketgan narsalarga yopishib qolish",
        "tavsiya_uz": "Eski narsalarni qo'yib yuboring — yangi hayot boshlanadi",
        "plus_ru": "Сила трансформации, обновление, способность отпускать старое",
        "minus_ru": "Страх перемен, цепляние за прошлое",
        "tavsiya_ru": "Отпустите старое — начнётся новая жизнь",
        "plus_en": "Power of transformation, renewal, ability to let go",
        "minus_en": "Fear of change, clinging to the past",
        "tavsiya_en": "Let go of the old — new life will begin",
    },
    14: {
        "plus_uz": "Muvozanat, sabr, ikki dunyoni birlashtira olish",
        "minus_uz": "Haddan ortiq ehtiyotkorlik, tavakkal qila olmaslik",
        "tavsiya_uz": "Ba'zan tavakkal qiling — hayot muvozanatsiz ham go'zal",
        "plus_ru": "Баланс, терпение, умение соединять два мира",
        "minus_ru": "Чрезмерная осторожность, неспособность рисковать",
        "tavsiya_ru": "Иногда рискуйте — жизнь прекрасна и без баланса",
        "plus_en": "Balance, patience, ability to unite two worlds",
        "minus_en": "Excessive caution, inability to take risks",
        "tavsiya_en": "Sometimes take risks — life is beautiful even without balance",
    },
    15: {
        "plus_uz": "Moddiy dunyo bilan ishlash kuchi, energiya jalb qilish",
        "minus_uz": "Bog'liqlik, vasvasga berilish, moddiyatga ko'milish",
        "tavsiya_uz": "Moddiy ne'matlardan foydalaning, lekin ular sizni boshqarmasin",
        "plus_ru": "Сила работы с материальным миром, притяжение энергии",
        "minus_ru": "Зависимость, поддаётся соблазнам, погружение в материализм",
        "tavsiya_ru": "Пользуйтесь материальными благами, но не давайте им управлять вами",
        "plus_en": "Power to work with material world, attracting energy",
        "minus_en": "Dependency, succumbing to temptation, materialism",
        "tavsiya_en": "Use material blessings but don't let them control you",
    },
    16: {
        "plus_uz": "Eski tuzilmalarni buzib yangi qurish, inqilobiy fikrlash",
        "minus_uz": "Kutilmagan inqirozlar, barqarorlik yo'qligi",
        "tavsiya_uz": "Inqirozlarni imkoniyat sifatida ko'ring — ular sizni kuchaytiradi",
        "plus_ru": "Разрушение старого и строительство нового, революционное мышление",
        "minus_ru": "Неожиданные кризисы, отсутствие стабильности",
        "tavsiya_ru": "Видьте в кризисах возможность — они вас усиливают",
        "plus_en": "Breaking old and building new, revolutionary thinking",
        "minus_en": "Unexpected crises, lack of stability",
        "tavsiya_en": "See crises as opportunities — they make you stronger",
    },
    17: {
        "plus_uz": "Umid, shifo energiyasi, boshqalarga ilhom berish",
        "minus_uz": "Haqiqatdan qochish, ortiqcha xayolparastlik",
        "tavsiya_uz": "Orzularingizni yerga tushiring — ularni amalga oshirish vaqti keldi",
        "plus_ru": "Надежда, целительная энергия, вдохновение других",
        "minus_ru": "Бегство от реальности, чрезмерная мечтательность",
        "tavsiya_ru": "Опустите мечты на землю — пришло время их реализовать",
        "plus_en": "Hope, healing energy, inspiring others",
        "minus_en": "Escaping reality, excessive daydreaming",
        "tavsiya_en": "Ground your dreams — it's time to make them real",
    },
    18: {
        "plus_uz": "Kuchli intuitsiya, sirli dunyo bilan aloqa, chuqur his",
        "minus_uz": "Qo'rquv, illuziyalar, haqiqatni ko'ra olmaslik",
        "tavsiya_uz": "Intuitsiyangizga ishoning, lekin haqiqatni ham ko'zing bilan ko'ring",
        "plus_ru": "Сильная интуиция, связь с тайным миром, глубокое чувство",
        "minus_ru": "Страх, иллюзии, неспособность видеть реальность",
        "tavsiya_ru": "Доверяйте интуиции, но и смотрите на реальность открытыми глазами",
        "plus_en": "Strong intuition, connection with hidden world, deep feelings",
        "minus_en": "Fear, illusions, inability to see reality",
        "tavsiya_en": "Trust intuition but also see reality with open eyes",
    },
    19: {
        "plus_uz": "Muvaffaqiyat, quvonch, yorqin energiya, odamlarni isitish",
        "minus_uz": "Egoizm, faqat o'zini ko'rish, ortiqcha optimizm",
        "tavsiya_uz": "Yorqinligingizni boshqalar bilan ulashing — bu sizni yanada kuchaytiradi",
        "plus_ru": "Успех, радость, яркая энергия, согревание людей",
        "minus_ru": "Эгоизм, видит только себя, чрезмерный оптимизм",
        "tavsiya_ru": "Делитесь своей яркостью — это сделает вас ещё сильнее",
        "plus_en": "Success, joy, bright energy, warming people",
        "minus_en": "Egoism, only sees self, excessive optimism",
        "tavsiya_en": "Share your brightness — it will make you even stronger",
    },
    20: {
        "plus_uz": "O'tmishdan saboq olish, yangilanish, ikkinchi imkoniyat",
        "minus_uz": "O'tmishga yopishib qolish, o'zini kechira olmaslik",
        "tavsiya_uz": "O'zingizni kechiring — o'tmish sizni o'qitdi, endi oldinga!",
        "plus_ru": "Извлечение уроков из прошлого, обновление, второй шанс",
        "minus_ru": "Застревание в прошлом, неспособность простить себя",
        "tavsiya_ru": "Простите себя — прошлое вас обучило, теперь вперёд!",
        "plus_en": "Learning from the past, renewal, second chances",
        "minus_en": "Stuck in the past, inability to forgive self",
        "tavsiya_en": "Forgive yourself — the past taught you, now move forward!",
    },
    21: {
        "plus_uz": "To'liqlik, mukammallik, hamma sohalarda muvaffaqiyat imkoni",
        "minus_uz": "Perfeksionizm, hech narsa yetarli emas degan his",
        "tavsiya_uz": "Mukammal bo'lishga intiling, lekin bugungi yutuqlaringizni ham qadrlang",
        "plus_ru": "Полнота, совершенство, возможность успеха во всех сферах",
        "minus_ru": "Перфекционизм, ощущение что ничего не достаточно",
        "tavsiya_ru": "Стремитесь к совершенству, но цените и сегодняшние достижения",
        "plus_en": "Fullness, perfection, possibility of success in all areas",
        "minus_en": "Perfectionism, feeling that nothing is enough",
        "tavsiya_en": "Strive for perfection but also value today's achievements",
    },
    22: {
        "plus_uz": "Cheksiz erkinlik, yangi boshlanishlar, sof imkoniyat",
        "minus_uz": "Mas'uliyatsizlik, yo'nalishsizlik, har narsaga boshlab hech narsani tugata olmaslik",
        "tavsiya_uz": "Erkinligingizni yo'nalishga aylantiring — katta ishlarga qodirsiz",
        "plus_ru": "Безграничная свобода, новые начинания, чистая возможность",
        "minus_ru": "Безответственность, отсутствие направления",
        "tavsiya_ru": "Превратите свою свободу в направление — вы способны на великое",
        "plus_en": "Boundless freedom, new beginnings, pure possibility",
        "minus_en": "Irresponsibility, lack of direction",
        "tavsiya_en": "Turn your freedom into direction — you're capable of great things",
    },
}

ARCANA_SHORT = {
    1:"Lider, kashfiyotchi", 2:"Tenglik, hamohanglik", 3:"Ijodkorlik, so'z kuchi",
    4:"Tartib, barqarorlik", 5:"Bilim, ustoz", 6:"Sevgi, tanlov",
    7:"G'alaba, intizom", 8:"Ichki kuch, sabr", 9:"Donolik, yolg'izlik",
    10:"O'zgarish, omad", 11:"Adolat, haqiqat", 12:"Qurbon, ko'rinish",
    13:"Transformatsiya", 14:"Muvozanat, me'yor", 15:"Bog'liqlik, moddiyat",
    16:"Inqilob, o'zgarish", 17:"Umid, ilhom", 18:"Intuitsiya, sir",
    19:"Muvaffaqiyat, quvonch", 20:"Uyg'onish, yangilanish", 21:"Mukammallik, dunyo",
    22:"Erkin ruh, yangi boshlanish"
}

ARCANA_SHORT_RU = {
    1:"Лидер, первооткрыватель", 2:"Равновесие, гармония", 3:"Творчество, сила слова",
    4:"Порядок, стабильность", 5:"Знание, учитель", 6:"Любовь, выбор",
    7:"Победа, дисциплина", 8:"Внутренняя сила, терпение", 9:"Мудрость, одиночество",
    10:"Перемены, удача", 11:"Справедливость, истина", 12:"Жертва, видение",
    13:"Трансформация", 14:"Баланс, умеренность", 15:"Зависимость, материализм",
    16:"Революция, перемены", 17:"Надежда, вдохновение", 18:"Интуиция, тайна",
    19:"Успех, радость", 20:"Пробуждение, обновление", 21:"Совершенство, мир",
    22:"Свободный дух, новое начало"
}

ARCANA_SHORT_EN = {
    1:"Leader, pioneer", 2:"Balance, harmony", 3:"Creativity, power of words",
    4:"Order, stability", 5:"Knowledge, teacher", 6:"Love, choice",
    7:"Victory, discipline", 8:"Inner strength, patience", 9:"Wisdom, solitude",
    10:"Change, fortune", 11:"Justice, truth", 12:"Sacrifice, vision",
    13:"Transformation", 14:"Balance, moderation", 15:"Dependency, materialism",
    16:"Revolution, change", 17:"Hope, inspiration", 18:"Intuition, mystery",
    19:"Success, joy", 20:"Awakening, renewal", 21:"Perfection, world",
    22:"Free spirit, new beginning"
}

def get_arcana_description(n, lang, mode="short"):
    n = max(1, min(22, n))
    info = ARCANA_INFO.get(n, ARCANA_INFO[1])
    if mode == "short":
        if lang == "ru": return ARCANA_SHORT_RU.get(n, "")
        if lang == "en": return ARCANA_SHORT_EN.get(n, "")
        return ARCANA_SHORT.get(n, "")
    if mode == "task":
        if lang == "ru": return info.get("tavsiya_ru", "")
        if lang == "en": return info.get("tavsiya_en", "")
        return info.get("tavsiya_uz", "")
    if mode == "plus":
        if lang == "ru": return info.get("plus_ru", "")
        if lang == "en": return info.get("plus_en", "")
        return info.get("plus_uz", "")
    if mode == "minus":
        if lang == "ru": return info.get("minus_ru", "")
        if lang == "en": return info.get("minus_en", "")
        return info.get("minus_uz", "")
    if mode == "tavsiya":
        if lang == "ru": return info.get("tavsiya_ru", "")
        if lang == "en": return info.get("tavsiya_en", "")
        return info.get("tavsiya_uz", "")
    return ARCANA_SHORT.get(n, "")

def get_topic_analysis(topic, matrix, name, lang):
    E=matrix.get("E",1); A=matrix.get("A",1); M=matrix.get("M",1)
    L=matrix.get("L",1); R=matrix.get("R",1); R1=matrix.get("R1",1)
    R2=matrix.get("R2",1); C=matrix.get("C",1); D=matrix.get("D",1)
    K=matrix.get("K",1); F2=matrix.get("F2",1); G2=matrix.get("G2",1)
    N=matrix.get("N",1)

    if topic == "money":
        if lang == "uz":
            return (
                f"💰 <b>{name}, sizning pul matritsangiz:</b>\n\n"
                f"🔑 <b>Pul kanalingizda {L}-arkan turibdi</b>\n"
                f"Bu — {get_arcana_description(L,'uz')} energiyasi.\n"
                f"✅ <b>Plus:</b> {get_arcana_description(L,'uz','plus')}\n"
                f"❌ <b>Minus:</b> {get_arcana_description(L,'uz','minus')}\n\n"
                f"💫 <b>Pul oqimingizda {R}-arkan turibdi</b>\n"
                f"Bu — {get_arcana_description(R,'uz')} energiyasi.\n"
                f"✅ <b>Plus:</b> {get_arcana_description(R,'uz','plus')}\n"
                f"❌ <b>Minus:</b> {get_arcana_description(R,'uz','minus')}\n\n"
                f"🎯 <b>Sizning markaziy {E}-arkan energiyangiz pul sohasida:</b>\n"
                f"{get_arcana_description(E,'uz','plus')}\n\n"
                f"📌 <b>Tavsiya:</b> {get_arcana_description(L,'uz','tavsiya')}\n\n"
                f"💡 <b>Pul bloklaringizni ochish uchun:</b>\n"
                f"• {R2}-arkan energiyasini faollashtiring\n"
                f"• Har kuni moliyaviy o'ylab ko'ring\n"
                f"• Pul haqida ijobiy fikr yuring"
            )
        elif lang == "ru":
            return (
                f"💰 <b>{name}, ваша денежная матрица:</b>\n\n"
                f"🔑 <b>В вашем денежном канале стоит {L}-аркан</b>\n"
                f"Это энергия — {get_arcana_description(L,'ru')}.\n"
                f"✅ <b>Плюс:</b> {get_arcana_description(L,'ru','plus')}\n"
                f"❌ <b>Минус:</b> {get_arcana_description(L,'ru','minus')}\n\n"
                f"💫 <b>В потоке денег стоит {R}-аркан</b>\n"
                f"Это энергия — {get_arcana_description(R,'ru')}.\n"
                f"✅ <b>Плюс:</b> {get_arcana_description(R,'ru','plus')}\n"
                f"❌ <b>Минус:</b> {get_arcana_description(R,'ru','minus')}\n\n"
                f"🎯 <b>Ваша центральная {E}-арканная энергия в сфере денег:</b>\n"
                f"{get_arcana_description(E,'ru','plus')}\n\n"
                f"📌 <b>Рекомендация:</b> {get_arcana_description(L,'ru','tavsiya')}\n\n"
                f"💡 <b>Чтобы открыть денежные блоки:</b>\n"
                f"• Активируйте энергию {R2}-аркана\n"
                f"• Ежедневно думайте о финансах позитивно\n"
                f"• Работайте с убеждениями о деньгах"
            )
        else:
            return (
                f"💰 <b>{name}, your money matrix:</b>\n\n"
                f"🔑 <b>Your money channel has {L}-arcana</b>\n"
                f"Energy: {get_arcana_description(L,'en')}.\n"
                f"✅ <b>Plus:</b> {get_arcana_description(L,'en','plus')}\n"
                f"❌ <b>Minus:</b> {get_arcana_description(L,'en','minus')}\n\n"
                f"💫 <b>Your money flow has {R}-arcana</b>\n"
                f"Energy: {get_arcana_description(R,'en')}.\n"
                f"✅ <b>Plus:</b> {get_arcana_description(R,'en','plus')}\n"
                f"❌ <b>Minus:</b> {get_arcana_description(R,'en','minus')}\n\n"
                f"🎯 <b>Your central {E}-arcana energy in money:</b>\n"
                f"{get_arcana_description(E,'en','plus')}\n\n"
                f"📌 <b>Tip:</b> {get_arcana_description(L,'en','tavsiya')}\n\n"
                f"💡 <b>To open money blocks:</b>\n"
                f"• Activate {R2}-arcana energy\n"
                f"• Think positively about finances daily\n"
                f"• Work on your money beliefs"
            )

    elif topic == "love":
        if lang == "uz":
            return (
                f"❤️ <b>{name}, sizning munosabatlar matritsangiz:</b>\n\n"
                f"💑 <b>Munosabat kanalingizda {M}-arkan turibdi</b>\n"
                f"Bu — {get_arcana_description(M,'uz')} energiyasi.\n"
                f"✅ <b>Plus:</b> {get_arcana_description(M,'uz','plus')}\n"
                f"❌ <b>Minus:</b> {get_arcana_description(M,'uz','minus')}\n\n"
                f"🌸 <b>Munosabat tabiatingizda {R1}-arkan turibdi</b>\n"
                f"Bu — {get_arcana_description(R1,'uz')} energiyasi.\n"
                f"✅ <b>Plus:</b> {get_arcana_description(R1,'uz','plus')}\n"
                f"❌ <b>Minus:</b> {get_arcana_description(R1,'uz','minus')}\n\n"
                f"💡 <b>Munosabatlaringizni yaxshilash uchun:</b>\n"
                f"📌 {get_arcana_description(M,'uz','tavsiya')}\n\n"
                f"🔑 <b>Esingizda bo'lsin:</b> Avvalo o'zingizni seving — shundagina boshqalarni chin dildan seva olasiz!"
            )
        elif lang == "ru":
            return (
                f"❤️ <b>{name}, ваша матрица отношений:</b>\n\n"
                f"💑 <b>В канале отношений стоит {M}-аркан</b>\n"
                f"Это энергия — {get_arcana_description(M,'ru')}.\n"
                f"✅ <b>Плюс:</b> {get_arcana_description(M,'ru','plus')}\n"
                f"❌ <b>Минус:</b> {get_arcana_description(M,'ru','minus')}\n\n"
                f"🌸 <b>В природе отношений стоит {R1}-аркан</b>\n"
                f"Это энергия — {get_arcana_description(R1,'ru')}.\n"
                f"✅ <b>Плюс:</b> {get_arcana_description(R1,'ru','plus')}\n"
                f"❌ <b>Минус:</b> {get_arcana_description(R1,'ru','minus')}\n\n"
                f"💡 <b>Для улучшения отношений:</b>\n"
                f"📌 {get_arcana_description(M,'ru','tavsiya')}\n\n"
                f"🔑 <b>Помните:</b> Сначала полюбите себя — тогда сможете по-настоящему любить других!"
            )
        else:
            return (
                f"❤️ <b>{name}, your relationship matrix:</b>\n\n"
                f"💑 <b>Your relationship channel has {M}-arcana</b>\n"
                f"Energy: {get_arcana_description(M,'en')}.\n"
                f"✅ <b>Plus:</b> {get_arcana_description(M,'en','plus')}\n"
                f"❌ <b>Minus:</b> {get_arcana_description(M,'en','minus')}\n\n"
                f"🌸 <b>Your relationship nature has {R1}-arcana</b>\n"
                f"Energy: {get_arcana_description(R1,'en')}.\n"
                f"✅ <b>Plus:</b> {get_arcana_description(R1,'en','plus')}\n"
                f"❌ <b>Minus:</b> {get_arcana_description(R1,'en','minus')}\n\n"
                f"💡 <b>To improve relationships:</b>\n"
                f"📌 {get_arcana_description(M,'en','tavsiya')}\n\n"
                f"🔑 <b>Remember:</b> First love yourself — then you can truly love others!"
            )

    elif topic == "health":
        ch = matrix.get("chakras", {})
        if lang == "uz":
            return (
                f"🌿 <b>{name}, sizning sog'liq matritsangiz:</b>\n\n"
                f"🔮 <b>Chakralaringiz holati:</b>\n\n"
                f"👑 <b>Sahasrara (bosh, miya)</b> = {ch.get('sahasrara','?')}-arkan\n"
                f"└ {get_arcana_description(ch.get('sahasrara',1),'uz','plus')}\n\n"
                f"👁 <b>Ajna (ko'z, intuitsiya)</b> = {ch.get('ajna','?')}-arkan\n"
                f"└ {get_arcana_description(ch.get('ajna',1),'uz','plus')}\n\n"
                f"🗣 <b>Vishudha (tomoq, o'pka)</b> = {ch.get('vishudha','?')}-arkan\n"
                f"└ {get_arcana_description(ch.get('vishudha',1),'uz','plus')}\n\n"
                f"💚 <b>Anahata (yurak)</b> = {ch.get('anahata','?')}-arkan\n"
                f"└ {get_arcana_description(ch.get('anahata',1),'uz','plus')}\n\n"
                f"🔥 <b>Manipura (qorin, jigar)</b> = {E}-arkan\n"
                f"└ {get_arcana_description(E,'uz','plus')}\n\n"
                f"🌊 <b>Muladhara (ildiz)</b> = {ch.get('muladhara','?')}-arkan\n"
                f"└ {get_arcana_description(ch.get('muladhara',1),'uz','plus')}\n\n"
                f"⚠️ <i>Bu ma'naviy tahlil. Sog'liq masalalarida albatta shifokorga murojaat qiling!</i>"
            )
        elif lang == "ru":
            return (
                f"🌿 <b>{name}, ваша матрица здоровья:</b>\n\n"
                f"🔮 <b>Состояние ваших чакр:</b>\n\n"
                f"👑 <b>Сахасрара (голова, мозг)</b> = {ch.get('sahasrara','?')}-аркан\n"
                f"└ {get_arcana_description(ch.get('sahasrara',1),'ru','plus')}\n\n"
                f"👁 <b>Аджна (глаза, интуиция)</b> = {ch.get('ajna','?')}-аркан\n"
                f"└ {get_arcana_description(ch.get('ajna',1),'ru','plus')}\n\n"
                f"🗣 <b>Вишудха (горло, лёгкие)</b> = {ch.get('vishudha','?')}-аркан\n"
                f"└ {get_arcana_description(ch.get('vishudha',1),'ru','plus')}\n\n"
                f"💚 <b>Анахата (сердце)</b> = {ch.get('anahata','?')}-аркан\n"
                f"└ {get_arcana_description(ch.get('anahata',1),'ru','plus')}\n\n"
                f"🔥 <b>Манипура (живот, печень)</b> = {E}-аркан\n"
                f"└ {get_arcana_description(E,'ru','plus')}\n\n"
                f"🌊 <b>Муладхара (корень)</b> = {ch.get('muladhara','?')}-аркан\n"
                f"└ {get_arcana_description(ch.get('muladhara',1),'ru','plus')}\n\n"
                f"⚠️ <i>Это духовный анализ. При проблемах со здоровьем обязательно обратитесь к врачу!</i>"
            )
        else:
            return (
                f"🌿 <b>{name}, your health matrix:</b>\n\n"
                f"🔮 <b>Your chakra status:</b>\n\n"
                f"👑 <b>Sahasrara (head, brain)</b> = {ch.get('sahasrara','?')}-arcana\n"
                f"└ {get_arcana_description(ch.get('sahasrara',1),'en','plus')}\n\n"
                f"👁 <b>Ajna (eyes, intuition)</b> = {ch.get('ajna','?')}-arcana\n"
                f"└ {get_arcana_description(ch.get('ajna',1),'en','plus')}\n\n"
                f"🗣 <b>Vishudha (throat, lungs)</b> = {ch.get('vishudha','?')}-arcana\n"
                f"└ {get_arcana_description(ch.get('vishudha',1),'en','plus')}\n\n"
                f"💚 <b>Anahata (heart)</b> = {ch.get('anahata','?')}-arcana\n"
                f"└ {get_arcana_description(ch.get('anahata',1),'en','plus')}\n\n"
                f"🔥 <b>Manipura (stomach, liver)</b> = {E}-arcana\n"
                f"└ {get_arcana_description(E,'en','plus')}\n\n"
                f"🌊 <b>Muladhara (root)</b> = {ch.get('muladhara','?')}-arcana\n"
                f"└ {get_arcana_description(ch.get('muladhara',1),'en','plus')}\n\n"
                f"⚠️ <i>This is a spiritual analysis. For health issues please consult a doctor!</i>"
            )

    elif topic == "purpose":
        if lang == "uz":
            return (
                f"🎯 <b>{name}, sizning maqsad va iste'dod matritsangiz:</b>\n\n"
                f"🌟 <b>40 yoshgacha ruh vazifangiz — {C}-arkan</b>\n"
                f"Bu — {get_arcana_description(C,'uz')} energiyasi.\n"
                f"✅ <b>Plus:</b> {get_arcana_description(C,'uz','plus')}\n"
                f"❌ <b>Minus:</b> {get_arcana_description(C,'uz','minus')}\n"
                f"📌 <b>Tavsiya:</b> {get_arcana_description(C,'uz','tavsiya')}\n\n"
                f"✨ <b>Tabiiy iste'dodingiz — {K}-arkan</b>\n"
                f"Bu — {get_arcana_description(K,'uz')} energiyasi.\n"
                f"{get_arcana_description(K,'uz','plus')}\n\n"
                f"👨 <b>Ota tomonidan kelgan iste'dod — {F2}-arkan</b>\n"
                f"{get_arcana_description(F2,'uz','plus')}\n\n"
                f"👩 <b>Ona tomonidan kelgan iste'dod — {G2}-arkan</b>\n"
                f"{get_arcana_description(G2,'uz','plus')}\n\n"
                f"💚 <b>Komfort zonangiz — {E}-arkan</b>\n"
                f"Siz {get_arcana_description(E,'uz')} energiyasida eng yaxshi ishlaysiz!\n\n"
                f"🚀 <b>Hayotiy maqsadingizga erishish uchun:</b>\n"
                f"{get_arcana_description(C,'uz','tavsiya')}"
            )
        elif lang == "ru":
            return (
                f"🎯 <b>{name}, ваша матрица цели и таланта:</b>\n\n"
                f"🌟 <b>Задача души до 40 лет — {C}-аркан</b>\n"
                f"Это энергия — {get_arcana_description(C,'ru')}.\n"
                f"✅ <b>Плюс:</b> {get_arcana_description(C,'ru','plus')}\n"
                f"❌ <b>Минус:</b> {get_arcana_description(C,'ru','minus')}\n"
                f"📌 <b>Рекомендация:</b> {get_arcana_description(C,'ru','tavsiya')}\n\n"
                f"✨ <b>Ваш природный талант — {K}-аркан</b>\n"
                f"Это энергия — {get_arcana_description(K,'ru')}.\n"
                f"{get_arcana_description(K,'ru','plus')}\n\n"
                f"👨 <b>Талант по линии отца — {F2}-аркан</b>\n"
                f"{get_arcana_description(F2,'ru','plus')}\n\n"
                f"👩 <b>Талант по линии матери — {G2}-аркан</b>\n"
                f"{get_arcana_description(G2,'ru','plus')}\n\n"
                f"💚 <b>Ваша зона комфорта — {E}-аркан</b>\n"
                f"Вы лучше всего работаете в энергии {get_arcana_description(E,'ru')}!\n\n"
                f"🚀 <b>Для достижения жизненной цели:</b>\n"
                f"{get_arcana_description(C,'ru','tavsiya')}"
            )
        else:
            return (
                f"🎯 <b>{name}, your purpose and talent matrix:</b>\n\n"
                f"🌟 <b>Soul task until 40 — {C}-arcana</b>\n"
                f"Energy: {get_arcana_description(C,'en')}.\n"
                f"✅ <b>Plus:</b> {get_arcana_description(C,'en','plus')}\n"
                f"❌ <b>Minus:</b> {get_arcana_description(C,'en','minus')}\n"
                f"📌 <b>Tip:</b> {get_arcana_description(C,'en','tavsiya')}\n\n"
                f"✨ <b>Your natural talent — {K}-arcana</b>\n"
                f"Energy: {get_arcana_description(K,'en')}.\n"
                f"{get_arcana_description(K,'en','plus')}\n\n"
                f"👨 <b>Father's talent — {F2}-arcana</b>\n"
                f"{get_arcana_description(F2,'en','plus')}\n\n"
                f"👩 <b>Mother's talent — {G2}-arcana</b>\n"
                f"{get_arcana_description(G2,'en','plus')}\n\n"
                f"💚 <b>Your comfort zone — {E}-arcana</b>\n"
                f"You work best in {get_arcana_description(E,'en')} energy!\n\n"
                f"🚀 <b>To achieve your life purpose:</b>\n"
                f"{get_arcana_description(C,'en','tavsiya')}"
            )

    elif topic == "karma":
        if lang == "uz":
            return (
                f"🔮 <b>{name}, sizning karma matritsangiz:</b>\n\n"
                f"⛓ <b>Karmik quyrug'ingizda {M}-arkan turibdi</b>\n"
                f"Bu — {get_arcana_description(M,'uz')} energiyasi.\n"
                f"✅ <b>Plus:</b> {get_arcana_description(M,'uz','plus')}\n"
                f"❌ <b>Minus (karmik vazifa):</b> {get_arcana_description(M,'uz','minus')}\n\n"
                f"🌀 <b>Karmik dasturda {N}-arkan turibdi</b>\n"
                f"Bu — {get_arcana_description(N,'uz')} energiyasi.\n"
                f"{get_arcana_description(N,'uz','plus')}\n\n"
                f"👨‍👩‍👧 <b>Oilaviy karmada {D}-arkan turibdi</b>\n"
                f"Bu — {get_arcana_description(D,'uz')} energiyasi.\n"
                f"{get_arcana_description(D,'uz','plus')}\n\n"
                f"💡 <b>Karmangizni yengillashtirish uchun:</b>\n"
                f"📌 {get_arcana_description(M,'uz','tavsiya')}\n\n"
                f"🙏 <b>Eng muhim tavsiyalar:</b>\n"
                f"• O'tmishdagi xatolarni kechiring\n"
                f"• Boshqalarga yordam bering\n"
                f"• O'zingizni ham kechiring"
            )
        elif lang == "ru":
            return (
                f"🔮 <b>{name}, ваша карматическая матрица:</b>\n\n"
                f"⛓ <b>В кармическом хвосте стоит {M}-аркан</b>\n"
                f"Это энергия — {get_arcana_description(M,'ru')}.\n"
                f"✅ <b>Плюс:</b> {get_arcana_description(M,'ru','plus')}\n"
                f"❌ <b>Минус (кармическая задача):</b> {get_arcana_description(M,'ru','minus')}\n\n"
                f"🌀 <b>В кармической программе стоит {N}-аркан</b>\n"
                f"Это энергия — {get_arcana_description(N,'ru')}.\n"
                f"{get_arcana_description(N,'ru','plus')}\n\n"
                f"👨‍👩‍👧 <b>В семейной карме стоит {D}-аркан</b>\n"
                f"Это энергия — {get_arcana_description(D,'ru')}.\n"
                f"{get_arcana_description(D,'ru','plus')}\n\n"
                f"💡 <b>Для облегчения кармы:</b>\n"
                f"📌 {get_arcana_description(M,'ru','tavsiya')}\n\n"
                f"🙏 <b>Главные рекомендации:</b>\n"
                f"• Простите ошибки прошлого\n"
                f"• Помогайте другим\n"
                f"• Простите и себя тоже"
            )
        else:
            return (
                f"🔮 <b>{name}, your karma matrix:</b>\n\n"
                f"⛓ <b>Your karmic tail has {M}-arcana</b>\n"
                f"Energy: {get_arcana_description(M,'en')}.\n"
                f"✅ <b>Plus:</b> {get_arcana_description(M,'en','plus')}\n"
                f"❌ <b>Minus (karmic task):</b> {get_arcana_description(M,'en','minus')}\n\n"
                f"🌀 <b>Your karmic program has {N}-arcana</b>\n"
                f"Energy: {get_arcana_description(N,'en')}.\n"
                f"{get_arcana_description(N,'en','plus')}\n\n"
                f"👨‍👩‍👧 <b>Your family karma has {D}-arcana</b>\n"
                f"Energy: {get_arcana_description(D,'en')}.\n"
                f"{get_arcana_description(D,'en','plus')}\n\n"
                f"💡 <b>To ease your karma:</b>\n"
                f"📌 {get_arcana_description(M,'en','tavsiya')}\n\n"
                f"🙏 <b>Key recommendations:</b>\n"
                f"• Forgive past mistakes\n"
                f"• Help others\n"
                f"• Forgive yourself too"
            )

    return "Tahlil topilmadi"
