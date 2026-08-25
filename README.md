# Алтай Мебель Про

Восстановленный сайт [altaymebel.pro](https://altaymebel.pro): кухни и мебель на заказ в Барнауле.

Оригинал стоял на Tilda и сейчас отдаёт **402 Please renew your subscription**. Тексты, телефоны, адрес и фото собраны из архива Wayback Machine и с Tilda CDN.

## Локальный просмотр

```bash
python3 -m http.server 4173 --directory public
```

Локально: http://127.0.0.1:4173

Страницы совпадают со старыми адресами Tilda: `/kitchens/`, `/catalog/`, `/oplata/` и остальные.

## DNS в Рег.ру для GitHub Pages

Домены → `altaymebel.pro` → **Управление зоной**. Удалите старые A/AAAA/CNAME у `@` и `www`.

| Тип | Subdomain | Значение |
|---|---|---|
| A | `@` | `185.199.108.153` |
| A | `@` | `185.199.109.153` |
| A | `@` | `185.199.110.153` |
| A | `@` | `185.199.111.153` |
| AAAA | `@` | `2606:50c0:8000::153` |
| AAAA | `@` | `2606:50c0:8001::153` |
| AAAA | `@` | `2606:50c0:8002::153` |
| AAAA | `@` | `2606:50c0:8003::153` |
| CNAME | `www` | `Elenavsemogu.github.io` |

DNS-серверы домена: `ns1.reg.ru` и `ns2.reg.ru`, не Tilda. TTL 3600.

Заявки уходят в WhatsApp `+7 964 603-41-43`. Почта: `Papin.am@mail.ru`.
