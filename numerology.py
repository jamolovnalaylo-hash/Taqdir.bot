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

def get_arcana_description(n, lang, mode="short"):
    data = {
        1:{"uz":"Lider, kashfiyotchi","ru":"Лидер, первооткрыватель","en":"Leader, pioneer","task_uz":"Manaviy rivojlanish va intuitsiyani oshirish","task_ru":"Духовное развитие и интуиция","task_en":"Spiritual development and intuition","money_uz":"Pul manaviy rivojlanish orqali keladi","money_ru":"Деньги через духовное развитие","money_en":"Money through spiritual growth","love_uz":"Munosabatlarda lider, erkinlikni sevadi","love_ru":"Лидер в отношениях, любит свободу","love_en":"Leader in relationships, loves freedom"},
        2:{"uz":"Tenglik, hamohanglik","ru":"Равновесие, гармония","en":"Balance, harmony","task_uz":"Munosabatlarda muvozanat saqlash","task_ru":"Поддержание баланса","task_en":"Maintaining balance","money_uz":"Sheriklik orqali muvaffaqiyat","money_ru":"Успех через партнёрство","money_en":"Success through partnership","love_uz":"Uygunlik qidiradi","love_ru":"Ищет гармонию","love_en":"Seeks harmony"},
        3:{"uz":"Ijodkorlik, so'z kuchi","ru":"Творчество, сила слова","en":"Creativity, power of words","task_uz":"Ijodiy qobiliyatlarni rivojlantirish","task_ru":"Развитие творческих способностей","task_en":"Developing creative talents","money_uz":"Pul ijod orqali keladi","money_ru":"Деньги через творчество","money_en":"Money through creativity","love_uz":"Romantika va ifodalilik","love_ru":"Романтика и выразительность","love_en":"Romance and expressiveness"},
        4:{"uz":"Tartib, barqarorlik","ru":"Порядок, стабильность","en":"Order, stability","task_uz":"Mustahkam asos yaratish","task_ru":"Создание прочной основы","task_en":"Creating solid foundation","money_uz":"Barqaror mehnat orqali","money_ru":"Через стабильный труд","money_en":"Through stable work","love_uz":"Ishonchlilik va barqarorlik","love_ru":"Надёжность и стабильность","love_en":"Reliability and stability"},
        5:{"uz":"Bilim, ustoz","ru":"Знание, учитель","en":"Knowledge, teacher","task_uz":"Bilimni ulashish","task_ru":"Передача знаний","task_en":"Sharing knowledge","money_uz":"Ta'lim orqali daromad","money_ru":"Доход через обучение","money_en":"Income through education","love_uz":"Ustoz va shogird elementi","love_ru":"Элемент учителя","love_en":"Teacher element"},
        6:{"uz":"Sevgi, tanlov","ru":"Любовь, выбор","en":"Love, choice","task_uz":"To'g'ri tanlov va sevgi","task_ru":"Правильный выбор и любовь","task_en":"Right choice and love","money_uz":"Munosabatlar orqali pul","money_ru":"Деньги через отношения","money_en":"Money through relationships","love_uz":"Muhabbat asosiy energiya","love_ru":"Любовь — главная энергия","love_en":"Love is core energy"},
        7:{"uz":"G'alaba, intizom","ru":"Победа, дисциплина","en":"Victory, discipline","task_uz":"Maqsad sari harakat","task_ru":"Движение к цели","task_en":"Moving toward goals","money_uz":"Intizom orqali boylik","money_ru":"Богатство через дисциплину","money_en":"Wealth through discipline","love_uz":"Sevgi uchun kurashadi","love_ru":"Борется за любовь","love_en":"Fights for love"},
        8:{"uz":"Ichki kuch, sabr","ru":"Внутренняя сила, терпение","en":"Inner strength, patience","task_uz":"Ichki kuchni topish","task_ru":"Найти внутреннюю силу","task_en":"Find inner strength","money_uz":"Sabr — muvaffaqiyat kaliti","money_ru":"Терпение — ключ к успеху","money_en":"Patience is key to success","love_uz":"Kuchli va ilhomlantiruvchi","love_ru":"Сильный и вдохновляющий","love_en":"Strong and inspiring"},
        9:{"uz":"Donolik, yolg'izlik","ru":"Мудрость, одиночество","en":"Wisdom, solitude","task_uz":"Ichki donishmandlikni topish","task_ru":"Найти внутреннюю мудрость","task_en":"Find inner wisdom","money_uz":"Tajriba orqali daromad","money_ru":"Доход через опыт","money_en":"Income through experience","love_uz":"Chuqurlik va ma'nolilik","love_ru":"Глубина и смысл","love_en":"Depth and meaning"},
        10:{"uz":"O'zgarish, omad","ru":"Перемены, удача","en":"Change, fortune","task_uz":"O'zgarishlarga moslashish","task_ru":"Адаптация к переменам","task_en":"Adapting to changes","money_uz":"Tsiklik moliyaviy holat","money_ru":"Цикличное финансовое положение","money_en":"Cyclical financial situation","love_uz":"Munosabatlarda o'zgarishlar","love_ru":"Перемены в отношениях","love_en":"Changes in relationships"},
        11:{"uz":"Adolat, haqiqat","ru":"Справедливость, истина","en":"Justice, truth","task_uz":"Adolatli bo'lish","task_ru":"Быть справедливым","task_en":"Being fair","money_uz":"Adolatli mehnat orqali","money_ru":"Через справедливый труд","money_en":"Through fair work","love_uz":"Tenglik va adolat","love_ru":"Равенство и справедливость","love_en":"Equality and fairness"},
        12:{"uz":"Qurbon, ko'rinish","ru":"Жертва, видение","en":"Sacrifice, vision","task_uz":"Eski qarashlardan voz kechish","task_ru":"Отпустить старые взгляды","task_en":"Release old views","money_uz":"Eski e'tiqodlarni o'zgartirish","money_ru":"Изменить старые убеждения","money_en":"Change old beliefs","love_uz":"O'zini qurbon qilmaslik","love_ru":"Не жертвовать собой","love_en":"Don't sacrifice yourself"},
        13:{"uz":"O'zgarish, yangilanish","ru":"Трансформация, обновление","en":"Transformation, renewal","task_uz":"Eski narsalardan voz kechish","task_ru":"Отпустить старое","task_en":"Release the old","money_uz":"Yangi daromad manbalari","money_ru":"Новые источники дохода","money_en":"New income sources","love_uz":"Munosabatlarda transformatsiya","love_ru":"Трансформация в отношениях","love_en":"Transformation in relationships"},
        14:{"uz":"Muvozanat, me'yor","ru":"Баланс, умеренность","en":"Balance, moderation","task_uz":"Me'yorni saqlash","task_ru":"Сохранять меру","task_en":"Keep moderation","money_uz":"Me'yorli yondashuv kerak","money_ru":"Нужен умеренный подход","money_en":"Moderate approach needed","love_uz":"Sabr va muvozanat","love_ru":"Терпение и баланс","love_en":"Patience and balance"},
        15:{"uz":"Bog'liqlik, vasvas","ru":"Зависимость, соблазн","en":"Dependency, temptation","task_uz":"Bog'liqliklardan ozod bo'lish","task_ru":"Освободиться от зависимостей","task_en":"Free from dependencies","money_uz":"Qo'rquv va vasvaslardan qutilish","money_ru":"Избавиться от страхов","money_en":"Get rid of fears","love_uz":"Sog'lom munosabatni tanlash","love_ru":"Выбрать здоровые отношения","love_en":"Choose healthy relationships"},
        16:{"uz":"Inqilob, o'zgarish","ru":"Революция, перемены","en":"Revolution, change","task_uz":"Eski tuzilmalarni buzish","task_ru":"Разрушить старые структуры","task_en":"Break old structures","money_uz":"Inqirozdan keyin imkoniyat","money_ru":"Возможности после кризиса","money_en":"Opportunities after crisis","love_uz":"Keskin o'zgarishlar","love_ru":"Резкие перемены","love_en":"Sharp changes"},
        17:{"uz":"Umid, ilhom","ru":"Надежда, вдохновение","en":"Hope, inspiration","task_uz":"Umidni saqlash, ilhom berish","task_ru":"Сохранять надежду","task_en":"Keep hope, inspire","money_uz":"Ilhom orqali daromad","money_ru":"Доход через вдохновение","money_en":"Income through inspiration","love_uz":"Shifo beruvchi muhabbat","love_ru":"Целительная любовь","love_en":"Healing love"},
        18:{"uz":"Intuitsiya, sir","ru":"Интуиция, тайна","en":"Intuition, mystery","task_uz":"Intuitsiyani rivojlantirish","task_ru":"Развить интуицию","task_en":"Develop intuition","money_uz":"Intuitsiyaga ishoning","money_ru":"Доверяйте интуиции","money_en":"Trust your intuition","love_uz":"Hissiyot va haqiqat","love_ru":"Чувства и реальность","love_en":"Feelings and reality"},
        19:{"uz":"Muvaffaqiyat, quvonch","ru":"Успех, радость","en":"Success, joy","task_uz":"Quvonch va muvaffaqiyat","task_ru":"Радость и успех","task_en":"Joy and success","money_uz":"Boylik tabiiy keladi","money_ru":"Богатство приходит естественно","money_en":"Wealth comes naturally","love_uz":"Quvonch va yorqinlik","love_ru":"Радость и яркость","love_en":"Joy and brightness"},
        20:{"uz":"Uyg'onish, yangilanish","ru":"Пробуждение, обновление","en":"Awakening, renewal","task_uz":"O'tmish saboqlarini qabul qilish","task_ru":"Принять уроки прошлого","task_en":"Accept past lessons","money_uz":"O'tmish xatolardan saboq","money_ru":"Уроки прошлых ошибок","money_en":"Learn from past mistakes","love_uz":"O'tmish yaralarini davolash","love_ru":"Исцелить раны прошлого","love_en":"Heal past wounds"},
        21:{"uz":"Mukammallik, dunyo","ru":"Совершенство, мир","en":"Perfection, world","task_uz":"To'liqlik va mukammallikni his qilish","task_ru":"Ощутить полноту жизни","task_en":"Feel life's fullness","money_uz":"Barcha sohalarda muvaffaqiyat","money_ru":"Успех во всех сферах","money_en":"Success in all areas","love_uz":"To'liqlik va mukammallik","love_ru":"Полнота и совершенство","love_en":"Fullness and perfection"},
        22:{"uz":"Erkin ruh, yangi boshlanish","ru":"Свободный дух, новое начало","en":"Free spirit, new beginning","task_uz":"Yangi sarguzashtlarga dadillik","task_ru":"Смело в новые приключения","task_en":"Boldly into new adventures","money_uz":"Noan'anaviy daromad manbalari","money_ru":"Нетрадиционные источники дохода","money_en":"Non-traditional income sources","love_uz":"Erkinlik va yangilik","love_ru":"Свобода и новизна","love_en":"Freedom and novelty"},
    }
    d = data.get(n, data[1])
    lang = lang if lang in ["uz","ru","en"] else "uz"
    if mode == "short": return d.get(lang, d["uz"])
    if mode == "task": return d.get(f"task_{lang}", d["task_uz"])
    if mode == "money": return d.get(f"money_{lang}", d["money_uz"])
    if mode == "love": return d.get(f"love_{lang}", d["love_uz"])
    return d.get(lang, d["uz"])

def get_topic_analysis(topic, matrix, name, lang):
    E=matrix.get("E",1); A=matrix.get("A",1); M=matrix.get("M",1)
    L=matrix.get("L",1); R=matrix.get("R",1); R2=matrix.get("R2",1)
    R1=matrix.get("R1",1); C=matrix.get("C",1); D=matrix.get("D",1)
    K=matrix.get("K",1); F2=matrix.get("F2",1); G2=matrix.get("G2",1)
    N=matrix.get("N",1)

    if topic == "money":
        e_m = get_arcana_description(E, lang, "money")
        l_d = get_arcana_description(L, lang, "short")
        r_d = get_arcana_description(R, lang, "short")
        if lang=="uz":
            return (f"💰 <b>{name} uchun Pul Tahlili</b>\n\n🔑 <b>E={E}:</b> {e_m}\n\n📊 <b>L={L} (Moliya kanali):</b> {l_d}\n\n💫 <b>R={R} (Pul oqimi):</b> {r_d}\n\n✅ <b>Tavsiya:</b> Manaviy rivojlanish pul oqimini ochadi. R2={R2} energiyasini faollashtiring.")
        elif lang=="ru":
            return (f"💰 <b>Денежный анализ для {name}</b>\n\n🔑 <b>E={E}:</b> {e_m}\n\n📊 <b>L={L} (Канал денег):</b> {l_d}\n\n💫 <b>R={R} (Поток денег):</b> {r_d}\n\n✅ <b>Рекомендация:</b> Духовное развитие открывает денежный поток. Активируйте энергию R2={R2}.")
        else:
            return (f"💰 <b>Money Analysis for {name}</b>\n\n🔑 <b>E={E}:</b> {e_m}\n\n📊 <b>L={L} (Money channel):</b> {l_d}\n\n💫 <b>R={R} (Money flow):</b> {r_d}\n\n✅ <b>Tip:</b> Spiritual growth opens money flow. Activate R2={R2} energy.")

    elif topic == "love":
        e_l = get_arcana_description(E, lang, "love")
        m_d = get_arcana_description(M, lang, "short")
        r1_d = get_arcana_description(R1, lang, "short")
        if lang=="uz":
            return (f"❤️ <b>{name} uchun Munosabatlar Tahlili</b>\n\n🔑 <b>E={E}:</b> {e_l}\n\n💑 <b>M={M} (Munosabat energiyasi):</b> {m_d}\n\n🌸 <b>R1={R1} (Munosabat tabiati):</b> {r1_d}\n\n✅ <b>Tavsiya:</b> Avvalo o'zingizni sevishni o'rganing.")
        elif lang=="ru":
            return (f"❤️ <b>Анализ отношений для {name}</b>\n\n🔑 <b>E={E}:</b> {e_l}\n\n💑 <b>M={M} (Энергия отношений):</b> {m_d}\n\n🌸 <b>R1={R1} (Природа отношений):</b> {r1_d}\n\n✅ <b>Совет:</b> Сначала научитесь любить себя.")
        else:
            return (f"❤️ <b>Relationship Analysis for {name}</b>\n\n🔑 <b>E={E}:</b> {e_l}\n\n💑 <b>M={M} (Relationship energy):</b> {m_d}\n\n🌸 <b>R1={R1} (Relationship nature):</b> {r1_d}\n\n✅ <b>Tip:</b> Learn to love yourself first.")

    elif topic == "health":
        ch = matrix.get("chakras", {})
        if lang=="uz":
            return (f"🌿 <b>{name} uchun Sog'liq Tahlili</b>\n\n👑 Sahasrara={ch.get('sahasrara','?')}\n👁 Ajna={ch.get('ajna','?')}\n🗣 Vishudha={ch.get('vishudha','?')}\n💚 Anahata={ch.get('anahata','?')}\n🔥 Manipura={E}\n🌊 Svadhisthana={ch.get('svadhisthana','?')}\n🌍 Muladhara={ch.get('muladhara','?')}\n\n⚠️ Sog'liq masalalarida shifokorga murojaat qiling!")
        elif lang=="ru":
            return (f"🌿 <b>Анализ здоровья для {name}</b>\n\n👑 Сахасрара={ch.get('sahasrara','?')}\n👁 Аджна={ch.get('ajna','?')}\n🗣 Вишудха={ch.get('vishudha','?')}\n💚 Анахата={ch.get('anahata','?')}\n🔥 Манипура={E}\n🌊 Свадхистхана={ch.get('svadhisthana','?')}\n🌍 Муладхара={ch.get('muladhara','?')}\n\n⚠️ По вопросам здоровья обратитесь к врачу!")
        else:
            return (f"🌿 <b>Health Analysis for {name}</b>\n\n👑 Sahasrara={ch.get('sahasrara','?')}\n👁 Ajna={ch.get('ajna','?')}\n🗣 Vishudha={ch.get('vishudha','?')}\n💚 Anahata={ch.get('anahata','?')}\n🔥 Manipura={E}\n🌊 Svadhisthana={ch.get('svadhisthana','?')}\n🌍 Muladhara={ch.get('muladhara','?')}\n\n⚠️ For health issues consult a doctor!")

    elif topic == "purpose":
        c_d = get_arcana_description(C, lang, "task")
        e_d = get_arcana_description(E, lang, "short")
        k_d = get_arcana_description(K, lang, "short")
        if lang=="uz":
            return (f"🎯 <b>{name} uchun Maqsad Tahlili</b>\n\n🌟 <b>C={C} (Ruh vazifasi):</b> {c_d}\n\n💚 <b>E={E} (Komfort zona):</b> {e_d}\n\n✨ <b>K={K} (Iste'dod):</b> {k_d}\n👨 Ota iste'dodi F2={F2}\n👩 Ona iste'dodi G2={G2}\n\n✅ {K}-arkan iste'dodingizni kasbga aylantiring!")
        elif lang=="ru":
            return (f"🎯 <b>Анализ цели для {name}</b>\n\n🌟 <b>C={C} (Задача души):</b> {c_d}\n\n💚 <b>E={E} (Зона комфорта):</b> {e_d}\n\n✨ <b>K={K} (Талант):</b> {k_d}\n👨 Талант отца F2={F2}\n👩 Талант матери G2={G2}\n\n✅ Превратите талант {K}-аркана в профессию!")
        else:
            return (f"🎯 <b>Purpose Analysis for {name}</b>\n\n🌟 <b>C={C} (Soul task):</b> {c_d}\n\n💚 <b>E={E} (Comfort zone):</b> {e_d}\n\n✨ <b>K={K} (Talent):</b> {k_d}\n👨 Father talent F2={F2}\n👩 Mother talent G2={G2}\n\n✅ Turn your {K}-arcana talent into a profession!")

    elif topic == "karma":
        m_d = get_arcana_description(M, lang, "short")
        n_d = get_arcana_description(N, lang, "short")
        d_d = get_arcana_description(D, lang, "short")
        if lang=="uz":
            return (f"🔮 <b>{name} uchun Karma Tahlili</b>\n\n⛓ <b>Karmik quyruq:</b>\nM={M}: {m_d}\nN={N}: {n_d}\nD={D}: {d_d}\n\n✅ <b>Karmani yengillashtirish:</b>\n• O'tmishni kechiring\n• Boshqalarga yordam bering\n• Manaviy amaliyotlarni davom ettiring")
        elif lang=="ru":
            return (f"🔮 <b>Кармический анализ для {name}</b>\n\n⛓ <b>Кармический хвост:</b>\nM={M}: {m_d}\nN={N}: {n_d}\nD={D}: {d_d}\n\n✅ <b>Облегчить карму:</b>\n• Простите прошлое\n• Помогайте другим\n• Продолжайте духовные практики")
        else:
            return (f"🔮 <b>Karma Analysis for {name}</b>\n\n⛓ <b>Karmic tail:</b>\nM={M}: {m_d}\nN={N}: {n_d}\nD={D}: {d_d}\n\n✅ <b>Ease karma:</b>\n• Forgive the past\n• Help others\n• Continue spiritual practices")

    return "Tahlil topilmadi"
