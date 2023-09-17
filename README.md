# FilesUploaderAPI


API для загрузки файлов на сервер.


## Развертывание и тестирование
* Запустить докер контейнеры приложения 
```shell script
make build
```
* Перейти на вкладку с http://localhost:8000/docs

![1.png](img%2F1.png)

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
![2.png](img%2F2.png)
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
![3.png](img%2F3.png)
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
![4.png](img%2F4.png)
## Authors and acknowledgment
Victor Pyatakov
