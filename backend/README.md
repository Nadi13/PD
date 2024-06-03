# API Endpoints

|Endpoint   |Input  |Output |Type   |Description    |
|-----------|-------|-------|-------|---------------|
|`/`        |       |test   |GET    |Просто тест    |
|`/api/user`|sessionKey|surname, name, patronymic, role|GET|Получить информацию о пользователе по ключу сессии|
|`/api/user/register`|username, password, info: {surname, name, patronymic, role}||POST|Регистрация пользователя|
|`/api/user/login`|username, password|sessionKey|POST|Вход в учетную запись|
|`/api/card/create`|?||POST|Создать новую карточку|
|`/api/cards`|sessionKey, type (опционально)|?|GET|Получить список карточек (лаб)|
|`/api/overview`|sessionKey|?|GET   |*?*            |
|`/api/card`|id, sessionKey|?|GET   |Получить карточку по его id|
|`/api/card/update`|id, sessionKey, updated||PUT|Послать обновлённые поля карточки (отметить как выполненное или отложенное, например)|
