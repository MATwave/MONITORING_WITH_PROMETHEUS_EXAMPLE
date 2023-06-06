# MONITORING_WITH_PROMETHEUS_EXAMPLE

Проект представляет собой веб-сервер на Flask, который обрабатывает запросы на корневом URL и маршруте "/metrics", 
собирает метрики о количестве запросов и их длительности, и предоставляет эти метрики в формате, понятном Prometheus. 
Это позволяет мониторить и анализировать производительность Python-кода с помощью инструментов Prometheus и Grafana.

![изображение](https://github.com/MATwave/MONITORING_WITH_PROMETHEUS_EXAMPLE/assets/44034959/8f31ce6a-ab08-4b5f-8b80-a53aca3fd324)

преднастроенные графики для grafanа в папке grafana-data (автоматически подгружаются при запуске)

запуск:
```commandline
docker compose up -d --build
```
  - flask-сервер доступен по [ссылке](http://localhost:81/) и [ссылке](http://localhost:81/metrics)
  - grafana доступна по [ссылке](http://localhost:3000/)

