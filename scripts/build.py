#!/usr/bin/env python3
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / "public"

NAV = [
    ("catalog/", "Каталог"),
    ("#etaps", "Этапы работы"),
    ("#advantages", "Преимущества"),
    ("delivery/", "Доставка"),
    ("oplata/", "Оплата"),
    ("projects-design/", "Наши работы"),
    ("#contacts", "Контакты"),
]

CATEGORIES = [
    {
        "slug": "bollards/",
        "title": "Тумбы",
        "short": "Комоды, тумбы ТВ и прикроватные тумбы",
        "image": "images/cat-tumby.jpg",
        "wide": False,
        "text": "Тумбы и комоды под размер помещения: под телевизор, в прихожую, в спальню. Подберём цвет, ручки и внутреннее наполнение.",
        "gallery": ["images/cat-tumby.jpg", "images/proj-5.jpg"],
    },
    {
        "slug": "commercial/",
        "title": "Торговая и офисная мебель",
        "short": "Ресепшен, витрины, стеллажи, кабинеты",
        "image": "images/cat-commercial.jpg",
        "wide": True,
        "text": "Мебель для магазинов, аптек, офисов и общественных пространств: ресепшен, витрины, стеллажи, рабочие зоны. Делаем по вашему проекту или предложим свой.",
        "gallery": ["images/cat-commercial.jpg", "images/cat-projects.jpg", "images/proj-3.jpg"],
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
        "slug": "kitchens/",
        "title": "Кухни",
        "short": "Кухни под ключ от производителя в Барнауле",
        "image": "images/cat-kitchens.jpg",
        "wide": False,
        "text": "Кухни под заказ от производителя в Барнауле. Считаем ваш проект, помогаем с дизайном, изготавливаем за 7–60 дней и при необходимости устанавливаем.",
        "gallery": [
            "images/cat-kitchens.jpg",
            "images/proj-1.jpg",
            "images/proj-4.jpg",
            "images/proj-7.jpg",
            "images/form-kitchen.png",
            "images/hero-kitchen.png",
        ],
    },
    {
        "slug": "losets/",
        "title": "Шкафы и зоны хранения",
        "short": "Встроенные шкафы, гардеробные, ниши",
        "image": "images/cat-closets.jpg",
        "wide": False,
        "text": "Шкафы и гардеробные в проём: распашные и системы хранения с нишами. Фасады, наполнение и подсветку подбираем под интерьер.",
        "gallery": ["images/cat-closets.jpg", "images/proj-2.jpg"],
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
        "slug": "projects-design/",
        "title": "Реализованные дизайн-проекты",
        "short": "Готовые интерьеры и комплекты мебели",
        "image": "images/cat-projects.jpg",
        "wide": True,
        "text": "Примеры реализованных объектов: кухни, детские, зоны хранения, торговая и офисная мебель. Пришлите свой проект — просчитаем и предложим варианты.",
        "gallery": [
            "images/cat-projects.jpg",
            "images/proj-1.jpg",
            "images/proj-2.jpg",
            "images/proj-3.jpg",
            "images/proj-4.jpg",
            "images/proj-5.jpg",
            "images/proj-6.jpg",
            "images/proj-7.jpg",
        ],
    },
]

PROJECTS = [
    "images/proj-1.jpg",
    "images/proj-2.jpg",
    "images/proj-3.jpg",
    "images/proj-4.jpg",
    "images/proj-5.jpg",
    "images/proj-6.jpg",
    "images/proj-7.jpg",
]

STEPS = [
    (
        "Выбор дизайна",
        "Посмотрите наши модели, выберите понравившуюся и закажите. Или принесите свой чертёж и идеи — мы их реализуем. Если нет времени разбираться в материалах, поможем с дизайном и предложим лучшие варианты.",
    ),
    (
        "Замер помещения",
        "Можете замерить помещение самостоятельно и прислать размеры — подберём варианты. При замере кухни учитывайте разводку коммуникаций и углы.",
    ),
    (
        "Договор и оплата",
        "После согласования утверждается дизайн-проект, составляется и подписывается договор. Оплата наличными или безналичным переводом. Есть рассрочка и кредит.",
    ),
    (
        "Изготовление мебели",
        "Срок изготовления — от 7 до 60 дней в зависимости от объёма и сложности. Можем собрать конструктор с инструкцией или готовые базы.",
    ),
    (
        "Доставка и установка",
        "Забрать мебель можно самостоятельно или воспользоваться доставкой. Установить можно самим — если есть вопросы, поможем. Можем установить сами.",
    ),
    (
        "Гарантия",
        "Гарантийный срок изделий — 3 года.",
    ),
    (
        "Самостоятельная сборка",
        "Если выбрали самостоятельную сборку, каждый блок едет в отдельной упаковке. К нему прилагается инструкция, а мы можем приехать помочь или проконсультировать.",
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


def lead_form(lead="Хочу рассчитать мебель", extra_field=False):
    extra = (
        """
          <textarea name="message" placeholder="Размеры, пожелания или ссылка на проект"></textarea>"""
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
          <button class="btn btn--teal" type="submit">Отправить заявку</button>
          <p class="note">Заявка откроется в WhatsApp. Нажимая кнопку, вы соглашаетесь на обработку персональных данных.</p>
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
          <a class="btn btn--teal" href="#" data-open="modal-call">Заказать звонок</a>
          <button class="burger" id="burger" type="button" aria-label="Меню">☰</button>
        </div>
      </div>
    </header>"""

FOOTER = """    <footer class="footer">
      <div class="wrap footer__grid">
        <div>
          <img src="/images/logo.png" alt="Алтай Мебель Про" width="220">
          <p>Кухни и мебель под заказ от производителя в Барнауле.</p>
        </div>
        <div>
          <p><a href="tel:+79646034143">+7 964 603-41-43</a></p>
          <p><a href="mailto:Papin.am@mail.ru">Papin.am@mail.ru</a></p>
          <p>г. Барнаул, ул. Матросова, 9И</p>
        </div>
        <div>
          <p><a href="/catalog/">Каталог</a></p>
          <p><a href="/delivery/">Доставка</a></p>
          <p><a href="/oplata/">Оплата</a></p>
          <p><a href="https://wa.me/79646034143?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5.%20%D0%A5%D0%BE%D1%87%D1%83%20%D0%BF%D1%80%D0%B8%D1%81%D0%BB%D0%B0%D1%82%D1%8C%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%20%D0%BA%D1%83%D1%85%D0%BD%D0%B8.">Свой проект кухни? Пришлите — просчитаем</a></p>
        </div>
      </div>
      <div class="wrap"><small>© Алтай Мебель Про</small></div>
    </footer>
    <a class="float-wa" href="https://wa.me/79646034143" target="_blank" rel="noopener" aria-label="WhatsApp">
      <svg viewBox="0 0 24 24" aria-hidden="true"><path d="M20.5 3.5A11 11 0 0 0 2.1 16.7L1 23l6.5-1.1A11 11 0 0 0 20.5 3.5zm-8.5 17a9 9 0 0 1-4.6-1.3l-.3-.2-3.8.6.6-3.7-.2-.3A9 9 0 1 1 12 20.5zm5-6.7c-.3-.1-1.6-.8-1.8-.9s-.4-.1-.6.1-.7.9-.8 1-.3.2-.6.1a7.4 7.4 0 0 1-2.2-1.4 8.2 8.2 0 0 1-1.5-1.9c-.2-.3 0-.4.1-.6l.4-.4.1-.3c0-.1 0-.3 0-.4s-.6-1.5-.8-2-.4-.4-.6-.4h-.5c-.2 0-.4.1-.6.3a2.1 2.1 0 0 0-.7 1.6 3.6 3.6 0 0 0 .8 1.9 8.3 8.3 0 0 0 3.2 2.9 10.7 10.7 0 0 0 3.2 1.1c.4.1.8.1 1.1.1a2.3 2.3 0 0 0 1.5-.7 1.9 1.9 0 0 0 .4-1.3c0-.1 0-.2-.2-.3z"/></svg>
    </a>
    <div class="modal" id="modal-call">
      <div class="modal__box">
        <button class="modal__close" type="button" data-close="modal-call" aria-label="Закрыть">×</button>
        <h3>Заказать звонок</h3>
        <p>Оставьте имя и телефон — перезвоним.</p>
        """ + lead_form("Прошу перезвонить") + """
      </div>
    </div>"""


def page(title, description, body, active="", og="images/proj-7.jpg"):
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
  <meta property="og:url" content="https://altaymebel.pro">
  <meta property="og:image" content="{og}">
  <link rel="icon" href="/favicon.ico">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Montserrat:wght@400;500;600;700&display=swap">
  <link rel="stylesheet" href="/css/style.css">
  <script type="application/ld+json">
  {{
    "@context": "https://schema.org",
    "@type": "LocalBusiness",
    "name": "Алтай Мебель Про",
    "url": "https://altaymebel.pro",
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
        f'          <figure class="slide"><img src="{href(src)}" alt="Выполненный проект"></figure>'
        for src in PROJECTS
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
    body = f"""
    <section class="hero">
      <div class="wrap">
        <p class="hero__kicker">от производителя в Барнауле</p>
        <h1>мебель под заказ</h1>
        <p>Кухни, шкафы, детские, тумбы, ванные и торговая мебель. Считаем ваш проект, изготавливаем и при необходимости устанавливаем.</p>
        <div class="hero__actions">
          <a class="btn btn--gold" href="/catalog/">Смотреть каталог</a>
          <a class="btn btn--ghost" href="#" data-open="modal-call">Заказать звонок</a>
        </div>
      </div>
    </section>

    <section class="section" id="catalog">
      <div class="wrap">
        <div class="section__head">
          <h2>Каталог</h2>
          <a href="/catalog/">Все разделы</a>
        </div>
        <div class="grid">
{chr(10).join(cards)}
        </div>
      </div>
    </section>

    <section class="section section--paper" id="works">
      <div class="wrap">
        <div class="section__head">
          <h2>Наши выполненные проекты</h2>
          <a href="/projects-design/">Посмотреть все</a>
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

    <section class="section stats" id="advantages">
      <div class="wrap stats-grid">
        <div class="stat"><b>5</b><span>лет безупречной репутации</span></div>
        <div class="facts">
          <h3>Цифры и факты</h3>
          <div class="facts-row">
            <div class="stat"><b>36</b><span>месяцев гарантия</span></div>
            <div class="stat"><b>790</b><span>клиентов пришли по рекомендации</span></div>
            <div class="stat"><b>15</b><span>лет средний срок службы кухни</span></div>
          </div>
        </div>
        <div>
          <div class="stat"><b>2</b><span>недели средний срок изготовления</span></div>
          <div class="stat" style="margin-top:24px"><b>814</b><span>довольных клиентов</span></div>
        </div>
      </div>
    </section>

    <section class="section" id="project">
      <div class="wrap contacts">
        <div>
          <h2>Свой проект кухни?</h2>
          <p class="lead">Пришлите проект — просчитаем и быстро ответим. Можно написать в WhatsApp или оставить заявку.</p>
          <p><a class="btn btn--dark" href="https://wa.me/79646034143?text=%D0%97%D0%B4%D1%80%D0%B0%D0%B2%D1%81%D1%82%D0%B2%D1%83%D0%B9%D1%82%D0%B5.%20%D0%A5%D0%BE%D1%87%D1%83%20%D0%BF%D1%80%D0%B8%D1%81%D0%BB%D0%B0%D1%82%D1%8C%20%D0%BF%D1%80%D0%BE%D0%B5%D0%BA%D1%82%20%D0%BA%D1%83%D1%85%D0%BD%D0%B8.">Прислать проект</a></p>
        </div>
        {lead_form("Прошу просчитать проект кухни", extra_field=True)}
      </div>
    </section>

    <section class="section section--paper" id="etaps">
      <div class="wrap">
        <div class="section__head"><h2>Порядок работы</h2></div>
        <div class="steps">
{steps}
        </div>
      </div>
    </section>

    <section class="section credit" id="credit">
      <div class="wrap credit__box">
        <div>
          <h2>Берите кухню сегодня, а платите потом</h2>
          <p>Кредит или рассрочка от Тинькофф Банка. Срок — 3, 6, 10 или 12 месяцев.</p>
          <a class="btn btn--gold" href="/oplata/">Узнать подробнее</a>
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
          <p>г. Барнаул, ул. Матросова, 9И</p>
          <iframe class="map" title="Карта" src="https://yandex.ru/map-widget/v1/?text=%D0%91%D0%B0%D1%80%D0%BD%D0%B0%D1%83%D0%BB%20%D0%9C%D0%B0%D1%82%D1%80%D0%BE%D1%81%D0%BE%D0%B2%D0%B0%209%D0%98"></iframe>
        </div>
        <div>
          <h2>Остались вопросы? Задайте нам их</h2>
          {lead_form("Вопрос с сайта")}
        </div>
      </div>
    </section>
"""
    return page(
        "Кухни от производителя под ключ — Алтай Мебель Про",
        "Кухни от производителя под ключ в Барнауле. Мебель на заказ: кухни, шкафы, детские, тумбы, ванные и торговая мебель.",
        body,
        "/",
    )


def catalog_page():
    cards = []
    for cat in CATEGORIES:
        cards.append(
            f"""        <a class="card" href="{href(cat['slug'])}">
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
        <p>Мебель под заказ от производителя в Барнауле. Выберите раздел или пришлите свой проект.</p>
      </div>
    </section>
    <section class="section">
      <div class="wrap grid">
{chr(10).join(cards)}
      </div>
    </section>
"""
    return page("Каталог — Алтай Мебель Про", "Каталог мебели на заказ: кухни, шкафы, детские, тумбы, ванные, торговая мебель.", body, "catalog")


def category_page(cat):
    gallery = "\n".join(f'        <img src="{href(src)}" alt="{cat["title"]}">' for src in cat["gallery"])
    body = f"""
    <section class="page-hero">
      <div class="wrap">
        <p class="crumbs"><a href="/">Главная</a> / <a href="/catalog/">Каталог</a> / {cat['title']}</p>
        <h1>{cat['title']}</h1>
        <p>{cat['text']}</p>
        <p><a class="btn btn--gold" href="#" data-open="modal-call">Заказать расчёт</a></p>
      </div>
    </section>
    <section class="section">
      <div class="wrap gallery">
{gallery}
      </div>
    </section>
"""
    return page(f"{cat['title']} на заказ в Барнауле — Алтай Мебель Про", cat["text"], body, "catalog", href(cat["image"]))


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
        pages[f"{cat['slug'].strip('/')}/index.html"] = category_page(cat)

    for name, html in pages.items():
        write_page(name, html)

    (ROOT / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: https://altaymebel.pro/sitemap.xml\n", encoding="utf-8")
    urls = [""] + [name.replace("index.html", "") for name in pages if name != "index.html"]
    sitemap = "\n".join(f"  <url><loc>https://altaymebel.pro/{u}</loc></url>" for u in urls)
    (ROOT / "sitemap.xml").write_text(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
        + sitemap
        + "\n</urlset>\n",
        encoding="utf-8",
    )
    print("done")


if __name__ == "__main__":
    main()
