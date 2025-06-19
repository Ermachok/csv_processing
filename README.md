## CSV Processor

### Запуск
```bash
  pip install -r requirements.txt
```
---

### Использование
```bash
  python -m csv_processor.main --file <путь_к_файлу.csv> [--where "условие"] [--aggregate колонка операция]
```
### Примеры запуска

Фильтрация по цене больше 500:
```bash
  python -m csv_processor.main --file products.csv --where "price>500"
```
![Картинка](screens/price.png)

Агрегация: среднее значение цены
```bash
  python -m csv_processor.main --file products.csv --aggregate price avg
```
![Картинка](screens/aggregation_price.png)

---

### Тестирование

Запуск тестов с покрытием:
```bash
  PYTHONPATH=. pytest --cov=csv_processor tests/
```
![Картинка](screens/tests_coverage.png)

---