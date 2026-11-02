#!/usr/bin/env python3
"""Build the public Timary information site. Python standard library only."""
from datetime import date
from html import escape
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent
BASE = "https://lakkiant.github.io/timary-support"
EMAIL = "anton.andreev.general@gmail.com"
CONTACT = f'<a href="mailto:{EMAIL}">{EMAIL}</a>'

COPY = {
    "en": {
        "tagline": "A little more order. A little more time.",
        "intro": "Timary brings your appointments, clients and services together, so you can focus on the people you work with.",
        "home": "Home", "privacy": "Privacy policy", "support": "Support",
        "skip": "Skip to content", "nav": "Main navigation", "language": "Українська",
        "date": "Effective and last updated: November 2, 2026",
        "footer": "An organizer for independent service professionals.",
        "privacy_intro": "A clear explanation of what stays on your device, what is shared with service providers, and the choices you have.",
        "support_intro": "Have a question, found a problem, or need help with your data? Get in touch with the developer of Timary.",
        "contact_label": "Contact the developer",
        "privacy_card": "Understand how Timary handles your information, iCloud sync, analytics and backups.",
        "support_card": "Find help with appointments, notifications, iCloud and transferring your data.",
        "contents": "On this page",
        "sections": [
            ("about", "Who is responsible", [
                f"This policy applies to the Timary iPhone and iPad app and this information website. The developer of Timary is responsible for the app's data practices. Contact the developer at {CONTACT} for privacy questions or requests.",
                "Timary does not require a separate Timary account. You decide what client and appointment information to enter. If you use Timary for your work, you are responsible for having an appropriate basis to store and share your clients' information."
            ]),
            ("records", "Client and appointment information", [
                "Timary stores the information you enter: client names, phone numbers, social contact handles and notes; services, prices and durations; appointments, visit history, payments recorded by you and tips; working hours, days off, preferences and message templates. Payment amounts are bookkeeping entries, not payment-card details.",
                "These records are stored on your device and used to provide scheduling, client management, reminders, statistics and data transfer. We do not operate a separate server that receives your client database. We do not sell client information or use the contents of your records for advertising.",
                "Timary's defined analytics events do not include client names, phone numbers, message or note text, appointment details, prices, service names or client identifiers. Analytics and crash reporting are described separately below."
            ]),
            ("icloud", "Optional iCloud sync", [
                "iCloud sync is off until you enable it. When enabled, Timary uses Apple's CloudKit private database associated with your Apple Account to sync records and supported settings across your devices. This includes clients, services, appointments, days off, preferences and message templates. System contact links and device permissions stay on the device.",
                "Apple processes the synced data under its service terms and privacy policy. The developer does not have a support interface for browsing your private iCloud records. Turning sync off does not delete data already stored in iCloud. Changes to the sync setting take effect after you fully close and reopen Timary."
            ]),
            ("permissions", "Contacts, photos and notifications", [
                "If you choose a person through Apple's contact picker, Timary imports the name and selected phone number you choose and keeps a local link to that contact. Timary does not upload your address book to a developer-operated server.",
                "If you choose to save an image of your available hours, Timary requests permission to add it to Photos. This feature does not require access to read your photo library.",
                "Appointment reminders are local notifications for you. You can change notification permissions in your device settings. Reminders are not automatic messages to your clients; their contents may appear on the lock screen according to your notification settings."
            ]),
            ("sharing", "Messages, sharing and backups", [
                "When you choose to call a client, open Telegram, Instagram or Viber, or share an image or file, the relevant phone number, handle, prepared message or selected content is passed to the destination you choose. Timary does not send client messages automatically. The receiving app or service handles this information under its own privacy policy.",
                "A Timary backup contains client, service and appointment records, notes, preferences and message templates. The exported file is not encrypted by Timary. Store and share it carefully. Copies saved to Files, iCloud Drive, another storage provider or another person remain there until you remove them separately. Device backups managed by Apple are separate from Timary's optional sync."
            ]),
            ("diagnostics", "Usage analytics and crash reports", [
                "Timary uses Google Analytics for Firebase and Firebase Crashlytics to measure app usage and stability. Collection is enabled by default and can be disabled in Settings → Privacy. Defined analytics events exclude client names, contact details and appointment contents. The app does not collect IDFA or use cross-app advertising tracking. Data practices are disclosed in the privacy policy.",
                "These services can process app-instance or installation identifiers, device and operating-system information, app versions, event times, usage events and crash traces. Crash reports may include technical application state and recent action breadcrumbs. Google Analytics can derive approximate geography from network information. The app uses FirebaseAnalyticsCore without IDFA collection and does not display third-party ads.",
                "This data is processed by Google/Firebase; it is separate from your locally stored client database. You can turn both services on or off under Settings → Privacy → Analytics and diagnostics; previous opt-outs remain effective. Turning this off stops future sharing and clears pending crash reports and local Analytics data; it does not delete data already received by Google. Crash reports from a previous session are sent only while sharing is enabled. Contact us about data questions, objections or deletion requests. Where data is associated only with a generated installation identifier, we may need additional information to identify it, and we may not be able to link it to your email address."
            ]),
            ("retention", "How long information is kept", [
                "Client and appointment records remain in your app storage until you edit or delete them, app cleanup rules apply, or the app's local data is removed. Removing a client profile does not necessarily remove the historical information saved in appointments; review and delete those records separately if needed.",
                "Synced data remains in your private iCloud storage until deleted through the app or Apple's available storage controls. Exported files and device backups remain under your control and the relevant storage provider's retention rules. Uninstalling Timary or turning sync off does not by itself remove those copies.",
                "Event-level analytics retention follows the retention setting for the Google Analytics property; aggregate reports can have different retention rules. Contact us for the current setting or a deletion request. Firebase states that Crashlytics retains crash traces and associated identifiers for 90 days before beginning removal from live and backup systems.",
                "If you email support, we use your address, message and any attachments to handle your request. We keep that correspondence while it is needed to resolve and follow up on the issue, or to meet applicable obligations. You can ask us to delete it."
            ]),
            ("choices", "Your choices and requests", [
                "You can edit or delete records in Timary, export your data, leave iCloud sync off, and manage notification and photo permissions in device settings. A deletion made while iCloud sync is active can propagate to your other connected devices.",
                f"To ask about access, correction, deletion, restriction or objection to processing, or to withdraw consent you have given, email {CONTACT}. Your rights depend on applicable law. We may need to verify a request and identify the relevant data. Withdrawing consent does not affect prior lawful processing.",
                "The developer cannot remotely retrieve or erase data held only on your device or in your private iCloud database. We can guide you through the controls available to you. To remove all copies, also consider synced devices, exported files and backups. Please do not email your client database or other people's personal information unless it is necessary and we have agreed a suitable way to share it."
            ]),
            ("providers", "Service providers and security", [
                "Apple provides iCloud and system services; Google/Firebase provides analytics and crash reporting. Messages and files go to external services only when you choose the relevant action. Providers may process information in countries other than yours under their applicable privacy and data-protection terms. We do not promise that information is stored in a specific country.",
                'Read <a href="https://www.apple.com/legal/privacy/">Apple’s privacy policy</a>, <a href="https://firebase.google.com/support/privacy">Firebase’s privacy and security information</a>, and <a href="https://policies.google.com/privacy">Google’s privacy policy</a> for provider details. We use these services under their applicable data-protection terms and expect providers processing data on our behalf to protect it accordingly.',
                "We rely on device security and the protections of the selected service providers. No storage or transmission method is completely secure. Protect your device and Apple Account, and take particular care with exported files."
            ]),
            ("website", "This website", [
                'This static website is hosted on GitHub Pages. We do not add analytics scripts, advertising, forms or cookies to this site. GitHub records visitors’ IP addresses for security purposes. See the <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">GitHub privacy statement</a>. If you email us, your email provider also processes that communication.'
            ]),
            ("children", "Children", [
                "Timary is intended for people managing professional appointments and is not designed specifically for children. We do not knowingly request personal information directly from children. Contact us if you believe a child has sent personal information to the developer."
            ]),
            ("changes", "Changes to this policy", [
                "We will update this page when the app's data practices change and revise the date at the top. Where required, we will provide an additional notice or seek consent before a relevant change takes effect."
            ])
        ],
        "help": [
            ("When you write", "Include your Timary version, iOS or iPadOS version, device model and the steps that led to the issue. You can find the app version at the bottom of Settings. Please redact client names, contact details and notes from screenshots."),
            ("Reminders", "Check that notifications are allowed for Timary in device settings, then review the reminder settings in the app. Reminders notify you; Timary does not automatically send messages to clients."),
            ("iCloud sync", "Use the same Apple Account on your devices and enable sync in Timary on each one. Fully close and reopen the app after changing the setting. Turning sync off does not delete your iCloud data."),
            ("Backups and moving devices", "Open Settings → Timary Data to export a backup or restore a file. Restoring replaces the current app data. Keep an extra copy before restoring and protect backup files because they contain client information."),
            ("Privacy requests", "Use the same contact email for questions about data, access or deletion. The developer cannot directly browse records held only on your device or in your private iCloud storage. We can help you find the appropriate controls.")
        ]
    },
    "uk": {
        "tagline": "Більше порядку. Більше часу для себе.",
        "intro": "Timary об’єднує записи, клієнтів і послуги, щоб ви могли зосередитися на людях, з якими працюєте.",
        "home": "Головна", "privacy": "Політика приватності", "support": "Підтримка",
        "skip": "Перейти до вмісту", "nav": "Основна навігація", "language": "English",
        "date": "Чинна з 2 листопада 2026 року · Оновлено 2 листопада 2026 року",
        "footer": "Органайзер для фахівців, які працюють за записом.",
        "privacy_intro": "Що залишається на вашому пристрої, які дані отримують постачальники сервісів і чим ви можете керувати.",
        "support_intro": "Маєте запитання, помітили проблему чи потрібна допомога з даними? Напишіть розробнику Timary.",
        "contact_label": "Написати розробнику",
        "privacy_card": "Дізнайтеся про зберігання даних, синхронізацію iCloud, аналітику та резервні копії.",
        "support_card": "Допомога із записами, сповіщеннями, iCloud і перенесенням даних.",
        "contents": "На цій сторінці",
        "sections": [
            ("about", "Хто відповідає за дані", [
                f"Ця політика стосується застосунку Timary для iPhone та iPad і цього інформаційного сайту. За роботу застосунку з даними відповідає розробник Timary. З питань приватності та запитів щодо даних пишіть на {CONTACT}.",
                "Для роботи в Timary не потрібен окремий обліковий запис Timary. Ви самі обираєте, яку інформацію про клієнтів і записи вносити. Якщо ви використовуєте Timary для роботи, ви відповідаєте за належні підстави для зберігання та поширення даних своїх клієнтів."
            ]),
            ("records", "Інформація про клієнтів і записи", [
                "Timary зберігає внесені вами дані: імена клієнтів, телефони, контакти в соцмережах і нотатки; послуги, ціни та тривалість; записи, історію візитів, зазначені вами оплати й чайові; робочі години, вихідні, налаштування та шаблони повідомлень. Суми оплат — це облікові записи, а не реквізити платіжних карток.",
                "Ці дані зберігаються на вашому пристрої та використовуються для розкладу, роботи з клієнтами, нагадувань, статистики й перенесення даних. Ми не маємо окремого сервера, який отримує вашу базу клієнтів. Ми не продаємо дані клієнтів і не використовуємо вміст ваших записів для реклами.",
                "Визначені в Timary події аналітики не містять імен клієнтів, телефонів, текстів повідомлень і нотаток, деталей візитів, цін, назв послуг чи ідентифікаторів клієнтів. Аналітику й звіти про збої описано окремо нижче."
            ]),
            ("icloud", "Необов’язкова синхронізація iCloud", [
                "Синхронізація iCloud вимкнена, доки ви її не ввімкнете. Після ввімкнення Timary використовує приватну базу Apple CloudKit, пов’язану з вашим обліковим записом Apple, для обміну даними між вашими пристроями. Передаються клієнти, послуги, записи, вихідні, налаштування та шаблони повідомлень. Зв’язки із системними контактами й дозволи залишаються на пристрої.",
                "Apple обробляє синхронізовані дані відповідно до своїх умов і політики приватності. Розробник не має інтерфейсу підтримки для перегляду ваших приватних записів iCloud. Вимкнення синхронізації не видаляє дані, вже збережені в iCloud. Зміна режиму застосовується після повного закриття й повторного відкриття Timary."
            ]),
            ("permissions", "Контакти, фото та сповіщення", [
                "Коли ви обираєте людину через системний вибір контактів Apple, Timary імпортує вибрані ім’я та номер телефону й зберігає локальний зв’язок із контактом. Timary не завантажує вашу адресну книгу на сервер розробника.",
                "Якщо ви обираєте збереження зображення вільних годин, Timary запитує дозвіл на додавання до «Фото». Для цієї функції не потрібен доступ до читання вашої фототеки.",
                "Нагадування про візити — локальні сповіщення для вас. Дозволами можна керувати в налаштуваннях пристрою. Це не автоматичні повідомлення клієнтам; вміст нагадувань може з’являтися на заблокованому екрані відповідно до ваших налаштувань сповіщень."
            ]),
            ("sharing", "Повідомлення, поширення та копії", [
                "Коли ви обираєте дзвінок клієнту, відкриття Telegram, Instagram або Viber чи поширення зображення або файлу, відповідний телефон, ім’я користувача, підготовлений текст або вибраний вміст передається до обраного вами застосунку. Timary не надсилає повідомлення клієнтам автоматично. Подальша обробка відбувається за політикою відповідного сервісу.",
                "Резервна копія Timary містить клієнтів, послуги, записи, нотатки, налаштування та шаблони повідомлень. Timary не шифрує експортований файл. Обережно обирайте місце зберігання та одержувачів. Копії у «Файлах», iCloud Drive, іншому сховищі або в іншої людини залишаються там, доки ви не видалите їх окремо. Резервні копії пристрою, якими керує Apple, відокремлені від синхронізації Timary."
            ]),
            ("diagnostics", "Аналітика та звіти про збої", [
                "Timary використовує Google Analytics for Firebase і Firebase Crashlytics для оцінювання використання та стабільності застосунку. Надсилання ввімкнене за замовчуванням; його можна вимкнути в розділі «Налаштування → Приватність». Визначені події аналітики не містять імен клієнтів, контактних даних і вмісту записів. Застосунок не збирає IDFA й не використовує рекламне відстеження між застосунками.",
                "Ці сервіси можуть обробляти ідентифікатори встановлення або екземпляра застосунку, відомості про пристрій і систему, версію застосунку, час подій, дії та технічні звіти про збої. Звіти можуть містити технічний стан застосунку й послідовність попередніх дій. Google Analytics може визначати приблизний регіон за мережевою інформацією. Застосунок використовує FirebaseAnalyticsCore без збору IDFA й не показує сторонню рекламу.",
                "Дані обробляє Google/Firebase; вони відокремлені від локальної бази ваших клієнтів. Увімкнути або вимкнути надсилання для обох сервісів можна в розділі «Налаштування → Приватність → Аналітика й діагностика»; попередні відмови залишаються чинними. Вимкнення зупиняє подальше надсилання й очищає відкладені звіти про збої та локальні дані Analytics, але не видаляє дані, які Google вже отримав. Звіти про збої попереднього сеансу надсилаються лише за ввімкненого надсилання. Звертайтеся до нас із запитаннями, запереченнями або запитами на видалення. Якщо дані пов’язані лише зі згенерованим ідентифікатором встановлення, для їх пошуку може знадобитися додаткова інформація; пов’язати їх із вашою email-адресою може бути неможливо."
            ]),
            ("retention", "Строки зберігання", [
                "Клієнти й записи залишаються у сховищі застосунку, доки ви їх не зміните або не видалите, не спрацюють правила очищення застосунку чи не буде видалено його локальні дані. Видалення профілю клієнта не обов’язково прибирає історичну інформацію у візитах; за потреби перевірте й видаліть такі записи окремо.",
                "Синхронізовані дані залишаються у приватному сховищі iCloud до видалення через застосунок або доступні засоби Apple. Експортовані файли й резервні копії пристрою зберігаються під вашим контролем і за правилами відповідного сховища. Видалення Timary чи вимкнення синхронізації саме по собі не прибирає ці копії.",
                "Строк зберігання окремих подій аналітики визначається налаштуванням ресурсу Google Analytics; для зведених звітів можуть діяти інші правила. Щоб дізнатися поточне налаштування або подати запит на видалення, напишіть нам. За документацією Firebase, Crashlytics зберігає звіти та пов’язані ідентифікатори 90 днів, після чого починає видаляти їх із робочих і резервних систем.",
                "Якщо ви пишете до підтримки, ми використовуємо вашу адресу, повідомлення й вкладення для відповіді. Листування зберігається, поки воно потрібне для вирішення питання, подальшого супроводу чи виконання застосовних обов’язків. Ви можете попросити його видалити."
            ]),
            ("choices", "Ваші налаштування та запити", [
                "Ви можете редагувати й видаляти записи, експортувати дані, не вмикати iCloud та керувати дозволами на сповіщення й фото в налаштуваннях пристрою. Видалення за активної синхронізації може поширитися на інші підключені пристрої.",
                f"Із запитами щодо доступу, виправлення, видалення, обмеження обробки, заперечення або відкликання наданої згоди пишіть на {CONTACT}. Обсяг прав залежить від застосовного законодавства. Для виконання запиту може знадобитися перевірка звернення й пошук відповідних даних. Відкликання згоди не впливає на попередню правомірну обробку.",
                "Розробник не може дистанційно отримати чи видалити дані, які є лише на вашому пристрої або у приватній базі iCloud. Ми можемо допомогти знайти доступні засоби керування. Для повного видалення враховуйте інші пристрої, експортовані файли й резервні копії. Не надсилайте базу клієнтів або персональні дані інших людей електронною поштою без потреби та попереднього узгодження відповідного способу передавання."
            ]),
            ("providers", "Постачальники сервісів і безпека", [
                "Apple надає iCloud і системні сервіси; Google/Firebase — аналітику та звіти про збої. Повідомлення й файли потрапляють до зовнішніх сервісів, коли ви обираєте відповідну дію. Постачальники можуть обробляти інформацію в інших країнах за своїми умовами захисту даних. Ми не обіцяємо зберігання в конкретній країні.",
                'Докладніше: <a href="https://www.apple.com/legal/privacy/">політика приватності Apple</a>, <a href="https://firebase.google.com/support/privacy">приватність і безпека Firebase</a> та <a href="https://policies.google.com/privacy">політика приватності Google</a>. Ми використовуємо сервіси відповідно до їхніх застосовних умов захисту даних і очікуємо належного захисту від постачальників, які обробляють інформацію від нашого імені.',
                "Для захисту даних використовуються засоби безпеки пристрою й обраних сервісів. Абсолютно безпечних способів зберігання чи передавання немає. Захищайте пристрій та обліковий запис Apple й особливо обережно поводьтеся з експортованими файлами."
            ]),
            ("website", "Цей сайт", [
                'Цей статичний сайт розміщено на GitHub Pages. Ми не додаємо сюди аналітичних скриптів, реклами, форм чи cookies. GitHub записує IP-адреси відвідувачів із міркувань безпеки. Докладніше — у <a href="https://docs.github.com/en/site-policy/privacy-policies/github-general-privacy-statement">політиці приватності GitHub</a>. Якщо ви надсилаєте нам email, поштовий провайдер також обробляє це листування.'
            ]),
            ("children", "Діти", [
                "Timary призначено для керування професійними записами, а не спеціально для дітей. Ми свідомо не запитуємо персональні дані безпосередньо в дітей. Напишіть нам, якщо вважаєте, що дитина передала персональні дані розробнику."
            ]),
            ("changes", "Зміни політики", [
                "Ми оновлюватимемо цю сторінку й дату на початку, коли змінюватиметься робота застосунку з даними. Коли це потрібно, перед відповідною зміною надамо додаткове повідомлення або отримаємо згоду."
            ])
        ],
        "help": [
            ("Що вказати у зверненні", "Напишіть версію Timary, версію iOS або iPadOS, модель пристрою та кроки, після яких виникла проблема. Версія застосунку є внизу налаштувань. На скриншотах приховайте імена, контакти й нотатки клієнтів."),
            ("Нагадування", "Перевірте дозвіл на сповіщення Timary в налаштуваннях пристрою та параметри нагадувань у застосунку. Нагадування сповіщають вас; Timary не надсилає повідомлення клієнтам автоматично."),
            ("Синхронізація iCloud", "Використовуйте той самий обліковий запис Apple та ввімкніть синхронізацію Timary на кожному пристрої. Після зміни режиму повністю закрийте й відкрийте застосунок. Вимкнення синхронізації не видаляє дані iCloud."),
            ("Копії та зміна пристрою", "У налаштуваннях відкрийте «Дані Timary», щоб експортувати копію або відновити файл. Відновлення замінює поточні дані. Перед цим збережіть додаткову копію; захищайте файли, адже вони містять інформацію про клієнтів."),
            ("Запити щодо приватності", "Із запитаннями про дані, доступ чи видалення пишіть на ту саму email-адресу. Розробник не може безпосередньо переглядати записи, що є лише на вашому пристрої або в приватному сховищі iCloud, але допоможе знайти відповідні засоби керування.")
        ]
    }
}


def location(lang, kind):
    prefix = "" if lang == "en" else "uk/"
    return prefix + ("" if kind == "home" else kind + "/")


def page(lang, kind, body):
    c = COPY[lang]
    current = location(lang, kind)
    depth = len([p for p in current.split("/") if p])
    root = "../" * depth or "./"
    title = "Timary" if kind == "home" else c[kind] + " · Timary"
    other = "uk" if lang == "en" else "en"
    canonical = BASE + "/" + current
    navigation = "".join(
        f'<a href="{root}{location(lang, target)}"' + (' aria-current="page"' if target == kind else '') + f'>{c[target]}</a>'
        for target in ("privacy", "support")
    )
    return f'''<!doctype html>
<html lang="{lang}">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <meta name="color-scheme" content="light dark">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(c['intro'] if kind == 'home' else c[kind + '_intro'], quote=True)}">
  <link rel="canonical" href="{canonical}">
  <link rel="alternate" hreflang="en" href="{BASE}/{location('en', kind)}">
  <link rel="alternate" hreflang="uk" href="{BASE}/{location('uk', kind)}">
  <link rel="alternate" hreflang="x-default" href="{BASE}/{location('en', kind)}">
  <link rel="icon" type="image/png" href="{root}assets/icon.png">
  <link rel="stylesheet" href="{root}assets/theme.css">
  <link rel="stylesheet" href="{root}assets/styles.css">
</head>
<body>
  <a class="skip" href="#main">{c['skip']}</a>
  <header class="site-header wrap">
    <a class="brand" href="{root}{location(lang, 'home')}" aria-label="Timary — {c['home']}"><img src="{root}assets/icon.png" width="42" height="42" alt="">Timary<span class="brand-dot" aria-hidden="true">.</span></a>
    <nav aria-label="{c['nav']}">{navigation}<a class="language" lang="{other}" hreflang="{other}" href="{root}{location(other, kind)}">{c['language']}</a></nav>
  </header>
  <main id="main" class="wrap">{body}</main>
  <footer class="site-footer wrap"><div><a class="footer-brand" href="{root}{location(lang, 'home')}">Timary</a><p>{c['footer']}</p></div><div><a href="mailto:{EMAIL}">{EMAIL}</a><p>© {date.today().year} Timary</p></div></footer>
</body>
</html>
'''


def build():
    urls = []
    for lang, c in COPY.items():
        prefix = "" if lang == "en" else "uk/"
        arrow = '<span aria-hidden="true">↗</span>'
        home = f'''<section class="home-hero"><p class="eyebrow">Timary · iPhone &amp; iPad</p><h1>{c['tagline']}</h1><p class="lead">{c['intro']}</p></section>
<div class="destination-grid"><a class="destination" href="privacy/"><span class="number">01</span><h2>{c['privacy']} {arrow}</h2><p>{c['privacy_card']}</p></a><a class="destination" href="support/"><span class="number">02</span><h2>{c['support']} {arrow}</h2><p>{c['support_card']}</p></a></div>'''
        contents = "".join(f'<li><a href="#{sid}">{heading}</a></li>' for sid, heading, _ in c["sections"])
        sections = "".join(f'<section id="{sid}" class="policy-section"><h2>{heading}</h2>' + "".join(f'<p>{p}</p>' for p in paragraphs) + '</section>' for sid, heading, paragraphs in c["sections"])
        privacy = f'''<div class="page-intro"><p class="eyebrow">Timary</p><h1>{c['privacy']}</h1><p class="lead">{c['privacy_intro']}</p><p class="updated">{c['date']}</p></div>
<div class="policy-layout"><aside class="contents"><details open><summary>{c['contents']}</summary><ol>{contents}</ol></details></aside><article class="policy" aria-label="{c['privacy']}">{sections}<div class="contact-note"><h2>{c['contact_label']}</h2><p>{CONTACT}</p></div></article></div>'''
        help_content = "".join(f'<section><h2>{heading}</h2><p>{text}</p></section>' for heading, text in c["help"])
        support = f'''<div class="page-intro"><p class="eyebrow">Timary</p><h1>{c['support']}</h1><p class="lead">{c['support_intro']}</p></div><div class="support-layout"><aside class="contact-note"><h2>{c['contact_label']}</h2><a href="mailto:{EMAIL}">{EMAIL}</a></aside><div class="policy">{help_content}</div></div>'''
        for kind, body in (("home", home), ("privacy", privacy), ("support", support)):
            path = ROOT / location(lang, kind) / "index.html"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(page(lang, kind, body), encoding="utf-8")
            urls.append(BASE + "/" + location(lang, kind))
    (ROOT / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">' + ''.join(f'<url><loc>{u}</loc></url>' for u in urls) + '</urlset>\n', encoding="utf-8")
    print(json.dumps({"pages": len(urls), "urls": urls}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    build()
