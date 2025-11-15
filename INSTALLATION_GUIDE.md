# 📦 Руководство по установке

## Системные требования

- **Python**: 3.8 или выше
- **ОС**: Windows, Linux, macOS
- **Память**: Минимум 512 MB свободной RAM
- **Дисковое пространство**: ~100 MB для установки

## Способ 1: Установка из репозитория (рекомендуется)

### Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/ВАШ_USERNAME/project-analytics.git
cd project-analytics
```

### Шаг 2: Создание виртуального окружения (рекомендуется)

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/macOS:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Шаг 3: Установка зависимостей

```bash
pip install -r requirements.txt
```

### Шаг 4: Запуск

```bash
jupyter notebook
```

Затем откройте `MAIN_code.ipynb`

---

## Способ 2: Установка через pip (если опубликовано в PyPI)

```bash
pip install project-analytics
```

---

## Способ 3: Установка в режиме разработки

```bash
git clone https://github.com/ВАШ_USERNAME/project-analytics.git
cd project-analytics
pip install -e .
```

---

## Проверка установки

Создайте тестовый скрипт `test_installation.py`:

```python
import sys

try:
    import pandas
    import matplotlib
    import seaborn
    import numpy
    import sqlite3
    print("✓ Все зависимости установлены успешно!")
    print(f"Python версия: {sys.version}")
except ImportError as e:
    print(f"✗ Ошибка: {e}")
    print("Установите зависимости: pip install -r requirements.txt")
```

Запустите:
```bash
python test_installation.py
```

---

## Устранение проблем

### Проблема: "pip не найден"

**Решение:**
```bash
# Windows
python -m pip install --upgrade pip

# Linux/macOS
python3 -m pip install --upgrade pip
```

### Проблема: "Permission denied"

**Решение:**
```bash
# Используйте флаг --user
pip install --user -r requirements.txt
```

### Проблема: Ошибки при установке matplotlib

**Решение:**
```bash
# Windows - установите Visual C++ Redistributable
# Linux
sudo apt-get install python3-tk

# macOS
brew install python-tk
```

### Проблема: Jupyter не запускается

**Решение:**
```bash
# Переустановите Jupyter
pip uninstall jupyter
pip install jupyter
```

---

## Дополнительная настройка

### Настройка Jupyter

Создайте конфигурационный файл:
```bash
jupyter notebook --generate-config
```

### Настройка Git (для разработчиков)

```bash
git config --global user.name "Ваше Имя"
git config --global user.email "ваш.email@example.com"
```

---

## Следующие шаги

После установки:

1. Откройте `MAIN_code.ipynb` в Jupyter
2. Выполните ячейки по порядку
3. Изучите примеры в папке `examples/`
4. Прочитайте документацию в `docs/`

---

## Получение помощи

Если возникли проблемы:
- Откройте [Issue](https://github.com/ВАШ_USERNAME/project-analytics/issues)
- Проверьте [FAQ](docs/FAQ.md)
- Напишите на email: ваш.email@example.com

