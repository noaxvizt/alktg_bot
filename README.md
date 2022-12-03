# alktg_bot
Телеграм бот, с помошбю которого удобно отправлять дз по алктг. Прорешивая задания и сфотографировав их, мы присылаем фото боту, который из них образует пдф файл. Далее бот может отослать этот пдф файл на указанную почту
как установить проект

git clone https://github.com/noaxvizt/alktg_bot.git
cd alktg_bot
git checkout dev
python3 -m pip install --user --upgrade pip pip install -r requirements.txt
python3 main.py

python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
python3 -m pip install -r requirements.txt


Бота можно завести через ботфазер
Почта используется яндекс. При небольших изменениях можно и поменять ее на другую. Чтобы настроить почтовый аккаунт, нужно зайти в янекс почту, нажать на шестеренку, перейти в настройки, почтовые программы и поставить галочки на: 
<br>С сервера imap.yandex.ru по протоколу IMAP
<br>Пароли приложений и OAuth-токены
<br>Портальный пароль
