# API Endpoints

|Endpoint   |Input  |Output |Type   |Description    |
|-----------|-------|-------|-------|---------------|
|`/`        |       |test   |GET    |Просто тест    |
|`/api/user`|sessionKey|surname, name, patronymic, role|GET|Получить информацию о пользователе по ключу сессии|
|`/api/user/register`|username, password, surname, name, patronymic, role, info: {group (для студентов)}||POST|Регистрация пользователя|
|`/api/user/login`|username, password|sessionKey|POST|Вход в учетную запись|
|`/api/card/create`|id: Number, studentid: String, labid: Number, content: String, comments: String, lecturerid: String, variant: Number \| null (опционально), info: object||POST|Создать новую карточку|
|`/api/cards`|sessionKey, type (опционально)|[id: int, studentid: str, labid: int, content: str, comments: str, lecturerid: str, variant: int | None, info: dict[str, Any], status: str ("Accepted", "Declined", "Postponed", "Pending"), creationdate: str]|GET|Получить список карточек (лаб)|
|`/api/overview`|sessionKey|?|GET   |*?*            |
|`/api/card`|id, sessionKey|...|GET   |Получить карточку по его id|
|`/api/card/update`|id, sessionKey, updated||PUT|Послать обновлённые поля карточки (отметить как выполненное или отложенное, например)|
