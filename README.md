# FilesUploaderAPI


API для загрузки файлов на сервер.


## Развертывание и тестирование
* Запустить докер контейнеры приложения 
```shell script
make build
```
* Перейти на вкладку с http://localhost:8000/docs

![Снимок экрана 2023-09-17 в 19.28.35.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fmw%2Fhjjbg4pd41766zc64fg6np700000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_DFCA00%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-09-17%20%D0%B2%2019.28.35.png) приложения

* Попробовать отправлять запросы на ендпониты приложения

## Make команды:
* Запустить докер контейнеры приложения 
```shell script
make build
```

* Запуск тестов
```shell script
make test
```


## Описание url:
* / - стартовая страница с информацией о состоянии приложения
* /docs - страница с списком API endpoints (swager)
* GET /api/files - api endpint для запроса существующих файлов на сарвере
* POST /api/files - api endpint для создания файла в папке на сервере
* GET /api/files/{guid} - api endpint для скачивания файла с сервера



## Работа с API:
### API endpoint: /api/files
* метод: POST
* Decription:
Ендпоинт нужен, чтобы создавать файлы на сервере
* Для создания файла, необходимо в форму ввести будущий GUID файла, по которому его можно будет потом найти.

    * Cгенерировать GUID можно на сайте https://www.guidgenerator.com/online-guid-generator.aspx 
или взять из файла data_for_test/guids.txt.

    * Так же необходимо выбрать файл, можно взять любой ваш на выбор или взять файл data_for_test/test_file.pdf.

* BODY request:
```shell script
    guid
    file
```
* JSON response:
```shell script
{
  "guid": "string",
  "name": "string"
}
```
![Снимок экрана 2023-09-17 в 19.44.17.png](..%2F..%2F..%2FDesktop%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-09-17%20%D0%B2%2019.44.17.png)

### API endpoint: /api/files
* метод: GET
* Decription: Ендпоинт нужен, запросить информацию о существующших файлах на сервере
* JSON request:
```shell script
{}
```
* JSON response:
```shell script
[
  {
    "guid": "string",
    "name": "string"
  }
]

```
![Снимок экрана 2023-09-17 в 19.46.18.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fmw%2Fhjjbg4pd41766zc64fg6np700000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_gzpvJm%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-09-17%20%D0%B2%2019.46.18.png)
### API endpoint: /api/files/{guid}
* метод: GET
* Decription: Ендпоинт нужен, скачать файл с сервера по его guid.
В ответ возвращается данные о файле, которые можно сохранить.
* JSON request:
```shell script
{}
```
* JSON response:
```shell script
{}
```
![Снимок экрана 2023-09-17 в 19.46.56.png](..%2F..%2F..%2F..%2F..%2Fvar%2Ffolders%2Fmw%2Fhjjbg4pd41766zc64fg6np700000gn%2FT%2FTemporaryItems%2FNSIRD_screencaptureui_L9SuAQ%2F%D0%A1%D0%BD%D0%B8%D0%BC%D0%BE%D0%BA%20%D1%8D%D0%BA%D1%80%D0%B0%D0%BD%D0%B0%202023-09-17%20%D0%B2%2019.46.56.png)

## Authors and acknowledgment
Victor Pyatakov
