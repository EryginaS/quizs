# Quizs API
API Система опросов

### ТЗ
#### Функционал для администратора системы:
- авторизация в системе (без регистрации)
- добавление/изменение/удаление опросов. Атрибуты опроса: название, дата старта, дата окончания, описание. После создания поле "дата старта" у опроса менять нельзя
- добавление/изменение/удаление вопросов в опросе. Атрибуты вопросов: текст вопроса, тип вопроса (ответ текстом, ответ с выбором одного варианта, ответ с выбором нескольких вариантов)

#### Функционал для пользователей системы:
- получение списка активных опросов
- прохождение опроса: опросы можно проходить анонимно, в качестве идентификатора пользователя в API передаётся числовой ID, по которому сохраняются ответы пользователя на вопросы; один пользователь может участвовать в любом количестве опросов
- получение пройденных пользователем опросов с детализацией по ответам (что выбрано) по ID уникальному пользователя

#### Установка:
1. Данный репозиторий склонируйте
2. Любым удобным способом создайте виртуальное окружение
3. Установите зависимости:
    - `pip install -r requirements.txt`
4. Создайте миграции
    - `python manage.py makemigrations`
    - `python manage.py migrate`
5. Создайте суперпользователя
    - `python manage.py createsuperuser`
6. Запустите сервер django
    - `python manage.py runserver`
    
### Документация API
   
##### Авторизация
1. Пользователь отправляет (POST) запрос с параметрами `username` и `password` на `api-token-auth/`, в ответе на запрос возвращается `token`.
2. При отправке запроса передавайте токен в заголовке Authorization: token `your_token`
(Для включения авторизации по JWT токену раскомментируйте раздел REST_FRAMEWORK в settings.py)

###### Получение всех опросов (GET)
- Права доступа: `Администратор`
- URL: `/api/quizs`
###### Получение данных о конкретном опросе (GET)
- Права доступа: `Администратор`
- URL: `/api/quizs/<int:pk>`
##### Добавление опросов (POST)
- Права доступа: `Администратор`
- URL: `/api/quizs/create/`
- QUERY PARAMETERS: `name`, `description`, `start_date`, `end_date`
###### Изменение/обновление опросов (PUT, PATCH)
- Права доступа: `Администратор`
- URL: `/api/quizs/update/<int:pk>/`
###### Удаление опросов (DELETE)
- Права доступа: `Администратор`
- URL: `/api/quizs/delete/<int:pk>/`


###### Получение всех вопросов (GET)
- Права доступа: `Администратор`
- URL: `/api/quizs/<int:quiz_pk>/questions`
###### Получение данных о конкретном вопросе (GET)
- Права доступа: `Администратор`
- URL: `/api/quizs/<int:quiz_pk>/questions/<int:pk>`
##### Добавление вопросов к опросу (POST)
- Права доступа: `Администратор`
- URL: `/api/quizs/<int:quiz_pk>/questions/`
- QUERY PARAMETERS: `question_text`, `question_type`(0,1,2), `quiz`
###### Изменение/обновление вопросов (PUT, PATCH)
- Права доступа: `Администратор`
- URL: `/api/quizs/<int:quiz_pk>/questions/<int:pk>/update/`
###### Удаление вопросов (DELETE)
- Права доступа: `Администратор`
- URL: `/api/quizs/<int:quiz_pk>/questions/<int:pk>/delete/`


##### Просмотр вариантов ответа к вопросу (GET)
- Права доступа: `Администратор`
- URL: `/api/quizs/<int:quiz_pk>/questions/<int:question_pk>/radio`
##### Добавление вариантов ответа к вопросу (POST)
- Права доступа: `Администратор`
- URL: `/api/quizs/<int:quiz_pk>/questions/<int:question_pk>/radio/create/`
- QUERY PARAMETERS: `radio_text`


##### Получение списка активных опросов (GET)
- Права доступа: `Любой пользователь`
- URL: `/api/active_quiz`

##### Прохождение опроса (POST)
- Права доступа: `Авторизованный пользователь`
- URL: `'/api/quizs/<int:id>/questions/<int:question_pk>/answers/`

##### Получение пройденных пользователем опросов (GET)
- Права доступа: `Авторизованный пользователь`
- URL: `/api/my_quizs`

## Технологии
djangorestframework
django
