#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "public"

NAV = [
    ("catalog/", "Каталог"),
    ("projects-design/", "Работы"),
    ("#etaps", "Как заказать"),
    ("#contacts", "Контакты"),
]

PROJECTS = [
    {
        "src": "images/works/kitchen-white-gold.jpg",
        "title": "Кухня белая с золотом",
        "caption": "Рифлёные фасады МДФ и золотая фурнитура",
        "tag": "Кухни",
    },
    {
        "src": "images/works/kitchen-grey-oak.jpg",
        "title": "Кухня графит + дуб",
        "caption": "Матовые фасады, столешница под дерево",
        "tag": "Кухни",
    },
    {
        "src": "images/works/kitchen-gloss-white.jpg",
        "title": "Белая глянцевая кухня",
        "caption": "Глянец без ручек",
        "tag": "Кухни",
    },
    {
        "src": "images/works/kitchen-display-glass.jpg",
        "title": "Витрина с подсветкой",
        "caption": "Витрина и встройка техники",
        "tag": "Кухни",
    },
    {
        "src": "images/works/hallway-grey-wood.jpg",
        "title": "Прихожая с рейками",
        "caption": "В потолок, сиденье и рейки",
        "tag": "Прихожие",
    },
    {
        "src": "images/works/hallway-greige.jpg",
        "title": "Прихожая под потолок",
        "caption": "Ниша, антресоли, ящики",
        "tag": "Прихожие",
    },
    {
        "src": "images/works/wardrobe-walkin.jpg",
        "title": "Гардеробная белая",
        "caption": "Трековый свет и зона для обуви",
        "tag": "Шкафы",
    },
    {
        "src": "images/works/wardrobe-laundry.jpg",
        "title": "Шкаф с постирочной",
        "caption": "Стиральная машина внутри шкафа",
        "tag": "Шкафы",
    },
    {
        "src": "images/works/living-tv-slats.jpg",
        "title": "ТВ-зона с рейками",
        "caption": "Рейки, тумба и полки",
        "tag": "Гостиная",
    },
    {
        "src": "images/works/living-sideboard.jpg",
        "title": "Комод на золотых ножках",
        "caption": "Тумба под ТВ",
        "tag": "Тумбы",
    },
    {
        "src": "images/works/wardrobe-white-mirror.jpg",
        "title": "Встроенный шкаф с зеркалом",
        "caption": "В потолок, с зеркалом",
        "tag": "Шкафы",
    },
    {
        "src": "images/works/vanity-white-gold.jpg",
        "title": "Туалетный столик",
        "caption": "Белый с золотом",
        "tag": "Корпусная",
    },
]

CATEGORIES = [
    {
        "slug": "kitchens/",
        "title": "Кухни",
        "short": "Под размер из ЛДСП и МДФ",
        "image": "images/works/kitchen-white-gold.jpg",
        "wide": True,
        "text": "Кухни под заказ от производителя в Барнауле. Считаем ваш проект, помогаем с дизайном, изготавливаем за 7–60 дней и при необходимости устанавливаем. Фасады ЛДСП и МДФ, столешницы Скиф или искусственный камень.",
        "gallery": [
            "images/works/kitchen-white-gold.jpg",
            "images/works/kitchen-white-gold-2.jpg",
            "images/works/kitchen-grey-oak.jpg",
            "images/works/kitchen-gloss-white.jpg",
            "images/works/kitchen-display-glass.jpg",
            "images/works/kitchen-detail-gold.jpg",
        ],
    },
    {
        "slug": "losets/",
        "title": "Шкафы и зоны хранения",
        "short": "Купе, гардеробные, ниши",
        "image": "images/works/hallway-grey-wood.jpg",
        "wide": False,
        "text": "Шкафы и гардеробные в проём: распашные, купе и системы хранения с нишами. Фасады, наполнение и подсветку подбираем под интерьер.",
        "gallery": [
            "images/works/hallway-grey-wood.jpg",
            "images/works/hallway-greige.jpg",
            "images/works/hallway-niche.jpg",
            "images/works/wardrobe-walkin.jpg",
            "images/works/wardrobe-laundry.jpg",
            "images/works/wardrobe-white-mirror.jpg",
            "images/works/hallway-sonya-2.jpg",
        ],
    },
    {
        "slug": "bollards/",
        "title": "Тумбы",
        "short": "ТВ-зоны, комоды",
        "image": "images/works/living-sideboard.jpg",
        "wide": False,
        "text": "Тумбы и комоды под размер помещения: под телевизор, в прихожую, в спальню. Подберём цвет, ручки и внутреннее наполнение.",
        "gallery": [
            "images/works/living-sideboard.jpg",
            "images/works/living-tv-slats.jpg",
            "images/works/living-tv-night.jpg",
            "images/works/vanity-white-gold.jpg",
        ],
    },
    {
        "slug": "children/",
        "title": "Детские",
        "short": "Кровати, столы, шкафы и системы хранения",
        "image": "images/cat-children.jpg",
        "wide": False,
        "text": "Детские гарнитуры на заказ: стол у окна, комод, кровать и шкаф в одной цветовой гамме. Безопасные кромки и удобная фурнитура.",
        "gallery": ["images/cat-children.jpg", "images/proj-6.jpg"],
    },
    {
        "slug": "bathroom/",
        "title": "Мебель в ванную и туалет",
        "short": "Тумбы под раковину, пеналы, зеркала",
        "image": "images/cat-bathroom.jpg",
        "wide": False,
        "text": "Влагостойкая мебель в ванную и туалет: тумбы под раковину, открытые полки, пеналы. Считаем по вашим размерам.",
        "gallery": ["images/cat-bathroom.jpg"],
    },
    {
        "slug": "commercial/",
        "title": "Торговая и офисная мебель",
        "short": "Ресепшен, витрины, стеллажи, кабинеты",
        "image": "images/cat-commercial.jpg",
        "wide": False,
        "text": "Мебель для магазинов, аптек, офисов и общественных пространств: ресепшен, витрины, стеллажи, рабочие зоны. Делаем по вашему проекту или предложим свой.",
        "gallery": ["images/cat-commercial.jpg", "images/cat-projects.jpg"],
    },
    {
        "slug": "projects-design/",
        "title": "Реализованные дизайн-проекты",
        "short": "Фото готовых объектов",
        "image": "images/works/kitchen-white-gold.jpg",
        "wide": True,
        "text": "Реальные объекты в Барнауле: кухни, прихожие, шкафы и корпусная мебель. Пришлите свой проект — просчитаем и предложим варианты.",
        "gallery": [],  # rendered by projects_page()
        "portfolio": True,
    },
]

DECORS = [
    ("Дуб вотан", "Тёплый ЛДСП"),
    ("Дуб сонома", "Классика"),
    ("Крафт золотой", "С белым"),
    ("Кашемир", "Бежево-серый"),
    ("Графит", "Матовый"),
    ("МДФ", "Эмаль и плёнка"),
]

STEPS = [
    (
        "Замер и проект",
        "Бесплатный замер в Барнауле или расчёт по вашим размерам. Подберём материалы и фасады.",
    ),
    (
        "Договор",
        "Фиксируем смету и сроки в договоре. Оплата наличными, безналом или в рассрочку.",
    ),
    (
        "Изготовление",
        "Делаем на своём производстве — обычно от 2 недель, сложные проекты до 60 дней.",
    ),
    (
        "Доставка и монтаж",
        "Привезём и установим. Гарантия на изделия — 3 года.",
    ),
]


def href(path):
    if path.startswith("#"):
        return "/" + path
    if path.startswith("http") or path.startswith("tel:") or path.startswith("mailto:"):
        return path
    return "/" + path.lstrip("/")


def nav_html(active=""):
    links = []
    for path, title in NAV:
        cls = ' class="is-active"' if path.rstrip("/") == active.rstrip("/") else ""
        links.append(f'<a href="{href(path)}"{cls}>{title}</a>')
    return "\n          ".join(links)


def lead_form(lead="Хочу рассчитать мебель", extra_field=False, button="Рассчитать проект"):
    extra = (
        """
          <textarea name="message" placeholder="Что нужно: кухня, шкаф, размеры или ссылка на проект"></textarea>"""
        if extra_field
        else ""
    )
    return f"""
        <form class="form" data-lead="{lead}">
          <div class="form-row">
            <input name="name" type="text" placeholder="Ваше имя" required>
            <input name="phone" type="tel" placeholder="Телефон" required>
            {extra}
          </div>
          <button class="btn btn--pine" type="submit">{button}</button>
          <p class="note">Ответ в WhatsApp. Согласие на обработку персональных данных.</p>
        </form>"""


HEADER = """    <header class="header">
      <div class="wrap header__inner">
        <a class="logo" href="/" aria-label="Алтай Мебель Про">
          <img src="/images/logo.png" alt="Алтай Мебель Про">
        </a>
        <nav class="nav">
          {nav}
        </nav>
        <div class="header__cta">
          <a class="phone" href="tel:+79646034143">+7 964 603-41-43</a>
          <a class="btn btn--gold" href="#" data-open="modal-call">Рассчитать</a>
          <button class="burger" id="burger" type="button" aria-label="Меню">☰</button>
        </div>
      </div>
    </header>"""

FOOTER = """    <footer class="footer">
      <div class="wrap footer__grid">
        <div>
          <a class="logo" href="/"><img src="/images/logo.png" alt="Алтай Мебель Про"></a>
          <p>Кухни и корпусная мебель на заказ. Барнаул, Матросова 9И.</p>
        </div>
        <div>
          <p><a href="tel:+79646034143">+7 964 603-41-43</a></p>
          <p><a href="mailto:Papin.am@mail.ru">Papin.am@mail.ru</a></p>
          <p>Пн–Вс, 10:00–18:00</p>
        </div>
        <div>
          <p><a href="/catalog/">Каталог</a></p>
          <p><a href="/projects-design/">Работы</a></p>
          <p><a href="/oplata/">Оплата и рассрочка</a></p>
          <p><a href="/delivery/">Доставка</a></p>
        </div>
      </div>
      <div class="wrap"><small>© Алтай Мебель Про</small></div>
    </footer>
    <a class="float-wa" href="https://wa.me/79646034143?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5.%20%D0%A5%D0%BE%D1%87%D1%83%20%D1%80%D0%B0%D1%81%D1%81%D1%87%D0%B8%D1%82%D0%B0%D1%82%D1%8C%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82." target="_blank" rel="noopener" aria-label="WhatsApp">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 3.5A11 11 0 0 0 2.1 16.7L1 23l6.5-1.1A11 11 0 0 0 20.5 3.5zm-8.5 17a9 9 0 0 1-4.6-1.3l-.3-.2-3.8.6.6-3.7-.2-.3A9 9 0 1 1 12 20.5zm5-6.7c-.3-.1-1.6-.8-1.8-.9s-.4-.1-.6.1-.7.9-.8 1-.3.2-.6.1a7.4 7.4 0 0 1-2.2-1.4 8.2 8.2 0 0 1-1.5-1.9c-.2-.3 0-.4.1-.6l.4-.4.1-.3c0-.1 0-.3 0-.4s-.6-1.5-.8-2-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3a2.1 2.1 0 0 0-.7 1.6 3.6 3.6 0 0 0 .8 1.9 8.3 8.3 0 0 0 3.2 2.9 10.7 10.7 0 0 0 3.2 1.1c.4.1.8.1 1.1.1a2.3 2.3 0 0 0 1.5-.7 1.9 1.9 0 0 0 .4-1.3c0-.1 0-.2-.2-.3z"/></svg>
    </a>
    <div class="modal" id="modal-call">
      <div class="modal__box">
        <button class="modal__close" type="button" data-close="modal-call" aria-label="Закрыть">×</button>
        <h3>Рассчитать проект</h3>
        <p>Ориентир по цене или запись на бесплатный замер.</p>
        """ + lead_form("Хочу рассчитать проект / замер", extra_field=True, button="Отправить в WhatsApp") + """
      </div>
    </div>"""


def page(title, description, body, active="", og="images/works/kitchen-white-gold.jpg"):
    return f"""<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{title}</title>
  <meta name="description" content="{description}">
  <meta property="og:title" content="{title}">
  <meta property="og:description" content="{description}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="https://altaimebel.pro">
  <meta property="og:image" content="{og}">
  <link rel="icon" href="/favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Manrope:wght@400;500;600;700;800&family=Unbounded:wght@500;600;700&display=swap">
  <link rel="stylesheet" href="/css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Алтай Мебель Про",
    "url": "https://altaimebel.pro",
    "telephone": "+79646034143",
    "email": "Papin.am@mail.ru",
    "address": {{
      "@type": "PostalAddress",
      "streetAddress": "ул. Матросова, 9И",
      "addressLocality": "Барнаул",
      "addressCountry": "RU"
    }},
    "areaServed": "Барнаул"
  }}
  </script>
</head>
<body>
  <a class="skip" href="#main">К содержанию</a>
{HEADER.format(nav=nav_html(active))}
  <main id="main">
{body}
  </main>
{FOOTER}
  <script src="/js/main.js"></script>
</body>
</html>
"""


def homepage():
    cards = []
    for cat in CATEGORIES:
        wide = " card--wide" if cat["wide"] else ""
        cards.append(
            f"""        <a class="card{wide}" href="{href(cat['slug'])}">
          <img src="{href(cat['image'])}" alt="{cat['title']}">
          <div class="card__body">
            <h3>{cat['title']}</h3>
            <span>{cat['short']}</span>
          </div>
        </a>"""
        )
    slides = "\n".join(
        f"""          <figure class="slide">
            <img src="{href(p['src'])}" alt="{p['title']}">
            <figcaption>
              <span class="slide__tag">{p['tag']}</span>
              <strong>{p['title']}</strong>
              <em>{p['caption']}</em>
            </figcaption>
          </figure>"""
        for p in PROJECTS
    )
    steps = "\n".join(
        f"""        <article class="step">
          <b>{i}</b>
          <div>
            <h3>{title}</h3>
            <p>{text}</p>
          </div>
        </article>"""
        for i, (title, text) in enumerate(STEPS, 1)
    )
    decors = "\n".join(
        f"""          <li class="decor">
            <strong>{name}</strong>
            <span>{hint}</span>
          </li>"""
        for name, hint in DECORS
    )
    # Homepage shows main categories only — less clutter
    home_cards = [c for c in cards if "/children/" not in c and "/bathroom/" not in c and "/commercial/" not in c]
    body = f"""
    <section class="hero">
      <div class="wrap hero__layout">
        <div class="hero__copy">
          <p class="hero__brand">Алтай Мебель Про</p>
          <h1>Кухни и мебель на заказ в Барнауле</h1>
          <p>Свой цех. Делаем под ваши размеры из ЛДСП и МДФ — с замером, договором и гарантией 3 года.</p>
          <div class="hero__actions">
            <a class="btn btn--gold" href="#project">Рассчитать проект</a>
            <a class="btn btn--ghost" href="#" data-open="modal-call">Бесплатный замер</a>
          </div>
        </div>
        <ul class="hero__trust">
          <li><b>Бесплатный замер</b><span>по Барнаулу</span></li>
          <li><b>От 2 недель</b><span>изготовление</span></li>
          <li><b>Рассрочка</b><span>Тинькофф 3–12 мес.</span></li>
        </ul>
      </div>
    </section>

    <section class="section" id="catalog">
      <div class="wrap">
        <div class="section__head">
          <h2>Что делаем</h2>
          <a href="/catalog/">Весь каталог</a>
        </div>
        <div class="grid">
{chr(10).join(home_cards)}
        </div>
      </div>
    </section>

    <section class="section section--paper" id="works">
      <div class="wrap">
        <div class="section__head">
          <h2>Работы</h2>
          <a href="/projects-design/">Смотреть все</a>
        </div>
        <div class="slider">
          <div class="slider__track">
{slides}
          </div>
          <div class="slider__nav">
            <button class="icon-btn" type="button" data-slide="prev" aria-label="Назад">←</button>
            <button class="icon-btn" type="button" data-slide="next" aria-label="Вперёд">→</button>
          </div>
        </div>
      </div>
    </section>

    <section class="section section--soft" id="decors">
      <div class="wrap">
        <div class="section__head">
          <h2>Декоры и материалы</h2>
        </div>
        <ul class="decors">
{decors}
        </ul>
        <p class="decors__note">Образцы в цехе на Матросова, 9И — привезём на замер.</p>
      </div>
    </section>

    <section class="section" id="project">
      <div class="wrap contacts">
        <div>
          <h2>Рассчитать проект</h2>
          <p class="lead">Пришлите размеры или фото — ответим с ориентиром по цене.</p>
          <div class="cta-stack">
            <a class="btn btn--dark" href="https://wa.me/79646034143?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5.%20%D0%A5%D0%BE%D1%87%D1%83%20%D1%80%D0%B0%D1%81%D1%81%D1%87%D0%B8%D1%82%D0%B0%D1%82%D1%8C%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82.">WhatsApp</a>
            <a class="btn btn--ghost-dark" href="tel:+79646034143">Позвонить</a>
          </div>
        </div>
        {lead_form("Прошу рассчитать проект мебели", extra_field=True, button="Рассчитать")}
      </div>
    </section>

    <section class="section section--paper" id="etaps">
      <div class="wrap">
        <div class="section__head"><h2>Как заказать</h2></div>
        <div class="steps">
{steps}
        </div>
      </div>
    </section>

    <section class="section credit" id="credit">
      <div class="wrap credit__box">
        <div>
          <h2>Рассрочка 3–12 месяцев</h2>
          <p>Через Тинькофф. Сначала смета — потом решение.</p>
          <a class="btn btn--gold" href="/oplata/">Условия</a>
        </div>
        <img src="/images/tinkoff.png" alt="Тинькофф Банк">
      </div>
    </section>

    <section class="section" id="contacts">
      <div class="wrap contacts">
        <div class="info-card">
          <h2>Контакты</h2>
          <p><a class="phone" href="tel:+79646034143">+7 964 603-41-43</a></p>
          <p><a href="mailto:Papin.am@mail.ru">Papin.am@mail.ru</a></p>
          <p>Барнаул, ул. Матросова, 9И</p>
          <iframe class="map" title="Карта" src="https://yandex.ru/map-widget/v1/?text=%D0%91%D0%B0%D1%80%D0%BD%D0%B0%D1%83%D0%BB%20%D0%9C%D0%B0%D1%82%D1%80%D0%BE%D1%81%D0%BE%D0%B2%D0%B0%209%D0%98"></iframe>
        </div>
        <div>
          <h2>Написать нам</h2>
          {lead_form("Вопрос с сайта", button="Отправить")}
        </div>
      </div>
    </section>
"""
    return page(
        "Кухни и мебель на заказ в Барнауле — Алтай Мебель Про",
        "Кухни, шкафы и корпусная мебель на заказ в Барнауле от производителя. ЛДСП и МДФ, бесплатный замер, гарантия 3 года, рассрочка.",
        body,
        "/",
    )


def catalog_page():
    cards = []
    for cat in CATEGORIES:
        wide = " card--wide" if cat.get("wide") else ""
        cards.append(
            f"""        <a class="card{wide}" href="{href(cat['slug'])}">
          <img src="{href(cat['image'])}" alt="{cat['title']}">
          <div class="card__body">
            <h3>{cat['title']}</h3>
            <span>{cat['short']}</span>
          </div>
        </a>"""
        )
    body = f"""
    <section class="page-hero">
      <div class="wrap">
        <p class="crumbs"><a href="/">Главная</a> / Каталог</p>
        <h1>Каталог</h1>
        <p>Кухни, шкафы и корпусная мебель на заказ в Барнауле.</p>
        <p><a class="btn btn--gold" href="#" data-open="modal-call">Рассчитать проект</a></p>
      </div>
    </section>
    <section class="section">
      <div class="wrap grid">
{chr(10).join(cards)}
      </div>
    </section>
"""
    return page(
        "Каталог мебели на заказ — Алтай Мебель Про",
        "Каталог: кухни, шкафы-купе, гардеробные, детские, тумбы, ванные и торговая мебель на заказ в Барнауле.",
        body,
        "catalog",
    )


def category_page(cat):
    gallery = "\n".join(f'        <img src="{href(src)}" alt="{cat["title"]}">' for src in cat["gallery"])
    wa = (
        "https://wa.me/79646034143?text="
        + __import__("urllib.parse").parse.quote(f"Здравствуйте. Интересует {cat['title']} на заказ.")
    )
    body = f"""
    <section class="page-hero">
      <div class="wrap">
        <p class="crumbs"><a href="/">Главная</a> / <a href="/catalog/">Каталог</a> / {cat['title']}</p>
        <h1>{cat['title']} на заказ</h1>
        <p>{cat['text']}</p>
        <div class="hero__actions">
          <a class="btn btn--gold" href="#" data-open="modal-call">Рассчитать проект</a>
          <a class="btn btn--ghost" href="{wa}">Написать в WhatsApp</a>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap gallery">
{gallery}
      </div>
    </section>
"""
    return page(
        f"{cat['title']} на заказ в Барнауле — Алтай Мебель Про",
        cat["text"],
        body,
        "catalog",
        href(cat["image"]),
    )


def projects_page():
    cards = "\n".join(
        f"""        <article class="work-card">
          <img src="{href(p['src'])}" alt="{p['title']}">
          <div class="work-card__body">
            <span class="slide__tag">{p['tag']}</span>
            <h3>{p['title']}</h3>
            <p>{p['caption']}</p>
          </div>
        </article>"""
        for p in PROJECTS
    )
    body = f"""
    <section class="page-hero">
      <div class="wrap">
        <p class="crumbs"><a href="/">Главная</a> / Наши работы</p>
        <h1>Наши работы</h1>
        <p>Кухни, прихожие и шкафы, сделанные под размер в Барнауле.</p>
        <div class="hero__actions">
          <a class="btn btn--gold" href="#" data-open="modal-call">Рассчитать похожий</a>
          <a class="btn btn--ghost" href="/kitchens/">Кухни</a>
        </div>
      </div>
    </section>
    <section class="section">
      <div class="wrap work-grid">
{cards}
      </div>
    </section>
"""
    return page(
        "Наши работы — кухни и мебель на заказ в Барнауле",
        "Портфолио Алтай Мебель Про: кухни, прихожие, шкафы и корпусная мебель на заказ в Барнауле.",
        body,
        "projects-design",
        href(PROJECTS[0]["src"]),
    )


def simple_page(slug, title, intro, content, active):
    body = f"""
    <section class="page-hero">
      <div class="wrap">
        <p class="crumbs"><a href="/">Главная</a> / {title}</p>
        <h1>{title}</h1>
        <p>{intro}</p>
      </div>
    </section>
    <section class="section">
      <div class="wrap">
        {content}
      </div>
    </section>
"""
    return page(f"{title} — Алтай Мебель Про", intro, body, active)


def write_page(path, html):
    dest = ROOT / path
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(html, encoding="utf-8")
    print("wrote", path)


def main():
    for old in ROOT.glob("*.html"):
        if old.name != "index.html":
            old.unlink()

    pages = {
        "index.html": homepage(),
        "catalog/index.html": catalog_page(),
        "delivery/index.html": simple_page(
            "delivery/",
            "Доставка и установка",
            "Забрать мебель можно самостоятельно или заказать доставку по Барнаулу.",
            """
        <div class="steps">
          <article class="step"><b>1</b><div><h3>Самовывоз</h3><p>Забираете готовый заказ сами. Каждый блок упакован отдельно.</p></div></article>
          <article class="step"><b>2</b><div><h3>Доставка</h3><p>Привезём на адрес. Срок и стоимость согласуем при заказе.</p></div></article>
          <article class="step"><b>3</b><div><h3>Установка</h3><p>Кухню можно собрать самостоятельно по инструкции или заказать монтаж у нас.</p></div></article>
        </div>
            """,
            "delivery",
        ),
        "oplata/index.html": simple_page(
            "oplata/",
            "Оплата",
            "Наличные, безнал, рассрочка и кредит от Тинькофф Банка.",
            """
        <div class="steps">
          <article class="step"><b>1</b><div><h3>Договор</h3><p>После согласования дизайн-проекта подписываем договор.</p></div></article>
          <article class="step"><b>2</b><div><h3>Оплата</h3><p>Наличными или безналичным переводом.</p></div></article>
          <article class="step"><b>3</b><div><h3>Рассрочка и кредит</h3><p>Тинькофф Банк: 3, 6, 10 или 12 месяцев. Условия уточняйте при заказе.</p></div></article>
        </div>
        <p style="margin-top:28px"><img src="/images/tinkoff.png" alt="Тинькофф Банк" width="240"></p>
            """,
            "oplata",
        ),
    }
    for cat in CATEGORIES:
        if cat.get("portfolio"):
            pages[f"{cat['slug'].strip('/')}/index.html"] = projects_page()
        else:
            pages[f"{cat['slug'].strip('/')}/index.html"] = category_page(cat)

    for name, html in pages.items():
        write_page(name, html)

    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://altaimebel.pro/sitemap.xml\n", encoding="utf-8")
    urls = [""] + [name.replace("index.html", "") for name in pages if name != "index.html"]
    sitemap = "\n".join(f"  <url><loc>https://altaimebel.pro/{u}</loc></url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + sitemap
        + "\n</urlset>\n",
        encoding="utf-8",
    )
    print("done")


if __name__ == "__main__":
    main()
