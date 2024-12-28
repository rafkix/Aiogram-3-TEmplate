Mana, `README.md` faylining to'liq nusxasi, uzbek tilida yozilgan:

```markdown
# Bot Loyihasi

Ushbu loyiha Telegram boti bo'lib, [Aiogram](https://github.com/aiogram/aiogram) kutubxonasi yordamida yozilgan. Bu zamonaviy va samarali Telegram botlarini yaratish uchun ishlatiladi. Botda bir nechta funksiyalar mavjud: admin paneli, foydalanuvchi bilan o'zaro aloqalar, va maxsus filtrlar.

## Xususiyatlar

- **Admin Paneli:** Administratorlar botni boshqarish va o'zaro aloqada bo'lish uchun komandalar orqali foydalanishi mumkin.
- **Filtrlar:** Foydalanuvchi adminmi yoki xabar guruhdan/kaneldanmi ekanligini tekshirish uchun maxsus filtrlar.
- **Bot Komandalari:** Foydalanuvchilar uchun oson aloqada bo'lish uchun maxsus komandalar.

## Talablar

- Python 3.8 va yuqoriroq versiya
- Talab qilingan kutubxonalarni o'rnatish uchun quyidagi komandani ishlating:

  ```bash
  pip install -r requirements.txt
```

## Sozlash

1. Loyihani o'z kompyuteringizga yuklab oling:

    ```bash
    git clone https://github.com/yourusername/your-bot-project.git
    cd your-bot-project
    ```

2. Loyihangizning ildiz papkasida `.env` faylini yaratib, bot tokeni va admin ID-ni qo'shing:

    ```env
    BOT_TOKEN=your_bot_token
    ADMIN_ID=your_admin_id
    ```

3. Kerakli kutubxonalarni o'rnatish:

    ```bash
    pip install -r requirements.txt
    ```

4. Botni ishga tushurish:

    ```bash
    python bot.py
    ```

## Foydalanish

- `/start` komandasini ishlatib, botni ishga tushuring.
- Administratorlar `/admin` yoki `/panel` komandasini yozib admin paneliga kirishlari mumkin.

## Litsenziya

Ushbu loyiha MIT Litsenziyasi asosida litsenziyalangan - batafsil ma'lumotni [LICENSE](LICENSE) faylida topishingiz mumkin.
```

### Qanday o'zgartirish mumkin:
- `yourusername` va `your-bot-project` ni GitHub foydalanuvchi nomingiz va repository nomingiz bilan almashtiring.
- `.env` faylida `your_bot_token` va `your_admin_id` joylariga haqiqiy bot tokeni va admin ID-ni kiriting.

Bu faqat boshlang'ich namunadir, va siz uni o'zingizning loyihangizning funksiyalari, ko'rsatmalar va boshqa tafsilotlarga moslab o'zgartirishingiz mumkin.

Agar qo'shimcha yordam kerak bo'lsa, ayting!
