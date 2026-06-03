import json
import os

locales_dir = "locales"

replacements = {
    "de.json": [
        ("Wir begleiten", "Ich begleite"),
        ("Wir helfen", "Ich helfe"),
        ("Was wir anbieten", "Was Sie bei mir bekommen"),
        ("Unsere Leistungen", "Meine Leistungen"),
        ("Schreiben Sie uns", "Schreiben Sie mir"),
        ("Warum wir", "Warum ich"),
        ("Wir antworten", "Ich antworte"),
        ("Was unsere Kunden", "Was meine Kunden"),
        ("stellen Sie uns", "stellen Sie mir"),
        ("wir antworten", "ich antworte"),
        ("Wir betreuen", "Ich betreue"),
        ("Kontaktieren Sie uns", "Kontaktieren Sie mich"),
        ("wir beraten", "ich berate"),
        ("Wer wir sind", "Wer ich bin"),
        ("das Team hinter", "den Berater hinter"),
        ("was uns antreibt", "was mich antreibt"),
        ("Mehr über uns", "Mehr über mich"),
        ("Unsere Geschichte", "Meine Geschichte"),
        ("wir verbinden", "ich verbinde"),
        ("sind bekannt", "bin bekannt"),
        ("Was uns ausmacht", "Was mich ausmacht"),
        ("Unsere Werte", "Meine Werte"),
        ("unsere Arbeit", "meine Arbeit"),
        ("erklären wir", "erkläre ich"),
        ("Wir arbeiten", "Ich arbeite"),
        ("Unsere Entwicklung", "Mein Werdegang"),
        ("wir unseren ersten", "ich meinen ersten"),
        ("Wir wachsen", "Ich wachse"),
        ("wir immer waren", "ich immer war"),
        ("wir melden uns", "ich melde mich"),
        ("Wir sind meist", "Ich bin meist"),
        ("versuchen wir", "versuche ich"),
        ("Über uns", "Über mich"),
        ("Erfahrene KFZ-Profis", "Erfahrener KFZ-Berater"),
        ("unser Team", "ich"),
        ("Unser Team", "Ich"),
        ("wir", "ich"),
        ("Wir", "Ich"),
        ("uns", "mich")
    ],
    "en.json": [
        ("About us", "About me"),
        ("About Us", "About Me"),
        ("We accompany", "I accompany"),
        ("What we offer", "What I offer"),
        ("Our Services", "My Services"),
        ("Our services", "My services"),
        ("We help", "I help"),
        ("Write to us", "Write to me"),
        ("Why us", "Why me"),
        ("We reply", "I reply"),
        ("We answer", "I answer"),
        ("What our customers", "What my customers"),
        ("ask us", "ask me"),
        ("We take care", "I take care"),
        ("Contact us", "Contact me"),
        ("we advise", "I advise"),
        ("Who we are", "Who I am"),
        ("the team behind", "the person behind"),
        ("drives us", "drives me"),
        ("More about us", "More about me"),
        ("Our history", "My history"),
        ("Our History", "My History"),
        ("Our values", "My values"),
        ("Our Values", "My Values"),
        ("our work", "my work"),
        ("we explain", "I explain"),
        ("We work", "I work"),
        ("Our development", "My background"),
        ("we grow", "I grow"),
        ("we always were", "I always was"),
        ("we will get back", "I will get back"),
        ("We are usually", "I am usually"),
        ("we try", "I try"),
        ("Experienced Car Professionals", "Experienced Car Consultant"),
        ("Our team", "I"),
        ("our team", "me")
    ],
    "ru.json": [
        ("О нас", "Обо мне"),
        ("Мы сопровождаем", "Я сопровождаю"),
        ("Что мы предлагаем", "Что я предлагаю"),
        ("Наши услуги", "Мои услуги"),
        ("Мы помогаем", "Я помогаю"),
        ("Напишите нам", "Напишите мне"),
        ("Почему мы", "Почему я"),
        ("Мы отвечаем", "Я отвечаю"),
        ("Что говорят наши клиенты", "Что говорят мои клиенты"),
        ("задайте нам", "задайте мне"),
        ("мы отвечаем", "я отвечаю"),
        ("Мы заботимся", "Я забочусь"),
        ("Свяжитесь с нами", "Свяжитесь со мной"),
        ("мы консультируем", "я консультирую"),
        ("Кто мы", "Кто я"),
        ("команде", "обо мне"),
        ("нас мотивирует", "меня мотивирует"),
        ("Больше о нас", "Больше обо мне"),
        ("Наша история", "Моя история"),
        ("Наши ценности", "Мои ценности"),
        ("нашу работу", "мою работу"),
        ("мы объясняем", "я объясняю"),
        ("Мы работаем", "Я работаю"),
        ("Наше развитие", "Мой путь"),
        ("Мы растем", "Я расту"),
        ("мы всегда были", "я всегда был"),
        ("мы свяжемся", "я свяжусь"),
        ("Мы обычно", "Я обычно"),
        ("мы стараемся", "я стараюсь"),
        ("Опытные автоспециалисты", "Опытный автоэксперт"),
        ("Наша команда", "Я"),
        ("наша команда", "я")
    ],
    "uk.json": [
        ("Про нас", "Про мене"),
        ("Ми супроводжуємо", "Я супроводжую"),
        ("Що ми пропонуємо", "Що я пропоную"),
        ("Наші послуги", "Мої послуги"),
        ("Ми допомагаємо", "Я допомагаю"),
        ("Напишіть нам", "Напишіть мені"),
        ("Чому ми", "Чому я"),
        ("Ми відповідаємо", "Я відповідаю"),
        ("Що кажуть наші клієнти", "Що кажуть мої клієнти"),
        ("задайте нам", "задайте мені"),
        ("ми відповідаємо", "я відповідаю"),
        ("Ми дбаємо", "Я дбаю"),
        ("Зв'яжіться з нами", "Зв'яжіться зі мною"),
        ("ми консультуємо", "я консультую"),
        ("Хто ми", "Хто я"),
        ("команду", "про мене"),
        ("нас мотивує", "мене мотивує"),
        ("Більше про нас", "Більше про мене"),
        ("Наша історія", "Моя історія"),
        ("Наші цінності", "Мої цінності"),
        ("нашу роботу", "мою роботу"),
        ("ми пояснюємо", "я пояснюю"),
        ("Ми працюємо", "Я працюю"),
        ("Наш розвиток", "Мій шлях"),
        ("Ми ростемо", "Я росту"),
        ("ми завжди були", "я завжди був"),
        ("ми зв'яжемося", "я зв'яжусь"),
        ("Ми зазвичай", "Я зазвичай"),
        ("ми намагаємося", "я намагаюся"),
        ("Досвідчені автоспеціалісти", "Досвідчений автоексперт"),
        ("Наша команда", "Я"),
        ("наша команда", "я")
    ]
}

for filename in os.listdir(locales_dir):
    if filename.endswith(".json") and not filename.startswith("._"):
        filepath = os.path.join(locales_dir, filename)
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            
        file_replacements = replacements.get(filename, [])
        
        for key, value in data.items():
            if isinstance(value, str):
                new_val = value
                for old_s, new_s in file_replacements:
                    new_val = new_val.replace(old_s, new_s)
                data[key] = new_val
                
        with open(filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

print("Locales updated.")
