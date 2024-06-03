# API Endpoints
- `/` - test
- `/api/user/` - получить информацию о пользователе с *sessionKey* cookie (GET)
- `/api/user/login` - отправить json вида `{login: "login", password: "password"}`, установить *sessionKey* cookie при успешном запросе (POST)
- `/api/card/create` - отправить поля карточки для добавления БД с *sessionKey* cookie (PUT) 
- `/api/cards` - получить список карточек с *sessionKey* cookie (GET)
- `/api/overview` - получить общую информацию (?) с *sessionKey* cookie (GET)
- `/api/card?id={id}` - получить карточку по id с *sessionKey* cookie (GET)
- `/api/card/update` - обновить карточку (отложить, отметить как выполненное...), с *sessionKey* cookie (PUT)
