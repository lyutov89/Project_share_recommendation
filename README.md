# Pet-project
## Рекомендательная система по покупке ценных бумаг на основе признаков пользователей и признаков самих ценных бумаг

Вдохновение запилить pet-project по такой теме пришла от любви к рекомендательным системам и инвестициям в ценные бумаги. 
Автор этого репозитория давно увлекается инвестициями в ценные бумаги и изучает ML.

❓ Откуда взять данные для датасетов ❓

* `Датасет из пользователей.` Отправной точкой стала [статья Tinkoff](https://www.tinkoff.ru/invest/news/616676/) про портрет инвестора. Исходя из этой статьи
был создан [датасет](https://github.com/lyutov89/project_share_recommendation/blob/master/users/Data_collection_for_pet_project.ipynb) с синтетическими данными 

* `Датасет из ценных бумаг.` На этом этапе было изучено несколько скринеров. Встроенная питоновская библиотека yahoo finance ограничивает в доступе к некоторым фундаментальным показателям бумаг, поэтому выбор пал не finviz/trading view. Trading view можно спарсить исключительно через Selenium, а мне хотелось попробовать через фреймворк Scrapy. К тому же, [finviz](https://finviz.com/) парсится проще и закрытые данные из библиотеки yahoo finance тут уже доступны. [Паук](https://github.com/lyutov89/project_share_recommendation/tree/master/shares_parsing/finviz_parsing) собирает данные в базу данных Mongo DB.
    - [X] После собранные данные в Mongo DB были [обработаны отдельно](https://github.com/lyutov89/project_share_recommendation/blob/master/items_shares/items_treatment.ipynb) 
    - [X] Сделал [разведочный анализ данных](https://github.com/lyutov89/project_share_recommendation/blob/master/items_shares/finviz_shares_short_eda.ipynb) на обработанных данных

* `Список покупок ценных бумаг пользователями.` Наши юзеры должны совершать свои сделки. Недавно СПБ биржа сформировала индекс [spb100](https://spbexchange.ru/ru/stocks/index/SPB100/) из самых популярных акций среди российских клиентов. Состав этого индекса хорошо согласуется с статьей, которую я приводил в начале, но она охватывает весь рынок брокеров, а не только Тинькофф, поэтому было решено [собрать данные индекса](https://github.com/lyutov89/project_share_recommendation/tree/master/shares_parsing/spb_shares) при помощи Selenium.

* `Датасет взаимодействий user-item.` Собранные популярные бумаги СПБ биржи были синтетическим образом распределены по юзерам. О том, как это было сделано, можно прочесть в самом [ноутбуке.](https://github.com/lyutov89/project_share_recommendation/blob/master/interactions/interactions.ipynb)

* `Бейзлайны`. Метрика для бизнеса и ML-метрика precision_at_5. Выполнены следующие [одноуровневые модели](https://github.com/lyutov89/Project_share_recommendation/blob/dev-base/baselines/baselines.ipynb): 
    - [X] ItemItem Recommender, CosineRecommender, TfidfRecommender   
    - [X] ALS with/without bm25, BPR with bm25 
    - [X]
    - [X]
   
* `LightFM и двухуровневая рекомендательная система.`

Файл с предложениями по фичам для [датасета акций.](https://github.com/lyutov89/Project_share_recommendation/tree/two-step-system/2_step_recsys)


   В дальнейших планах (до конца февраля 2022 г.):
* `Гибридная модель на основе LightFm`   
* `Двухуровневая рекомендательная модель`
* `Настройка предфильтрации/постфильтрации`

