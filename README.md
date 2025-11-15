# 📊 Project Analytics - Профессиональная система аналитики проектов

<div align="center">

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Code Style](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![Tests](https://img.shields.io/badge/tests-pytest-blue.svg)](https://pytest.org/)
[![GitHub Stars](https://img.shields.io/github/stars/ВАШ_USERNAME/project-analytics.svg?style=social)](https://github.com/ВАШ_USERNAME/project-analytics)

**Комплексная система для анализа проектов с интеграцией Яндекс.Метрики и Яндекс.Директ**

[Документация](docs/) • [Примеры](examples/) • [Установка](docs/INSTALLATION.md) • [Вопросы](https://github.com/DmitryProffessor/project-analytics/issues)

</div>

---

## 📑 Содержание

- [О проекте](#-о-проекте)
- [Возможности](#-возможности)
- [Архитектура](#-архитектура)
- [Быстрый старт](#-быстрый-старт)
- [Установка](#-установка)
- [Использование](#-использование)
- [Структура проекта](#-структура-проекта)
- [Документация](#-документация)
- [Тестирование](#-тестирование)
- [Вклад в проект](#-вклад-в-проект)
- [Лицензия](#-лицензия)

---

## 🎯 О проекте

**Project Analytics** — это профессиональная система для сбора, хранения и анализа данных о производительности проектов. Система интегрируется с Яндекс.Метрикой и Яндекс.Директ, предоставляя комплексную аналитику в едином интерфейсе.

### Основные преимущества:

- ✅ **Единая точка доступа** ко всем метрикам проекта
- ✅ **Автоматическая агрегация** данных по месяцам
- ✅ **Готовые отчеты** и визуализация
- ✅ **Простое API** для интеграции
- ✅ **Расширяемая архитектура**

---

## ✨ Возможности

### 📈 Аналитика проектов
- Отслеживание метрик производительности
- Помесячная статистика
- Сравнение проектов
- Трендовый анализ

### 🎯 Интеграция с Яндекс.Метрикой
- Поддержка множественных счетчиков
- Автоматический сбор метрик
- Анализ целей и конверсий
- Демографический анализ

### 📢 Анализ Яндекс.Директ
- Мониторинг кампаний
- Расчет ROI и CPA
- Анализ эффективности
- Оптимизация бюджета

### 🔍 SEO-аналитика
- Отслеживание позиций
- Динамика по запросам
- Анализ конкурентов

### 📊 Визуализация
- Автоматическая генерация графиков
- Интерактивные дашборды
- Экспорт отчетов

### 💾 Хранение данных
- SQLite база данных
- Помесячная агрегация
- Резервное копирование
- Экспорт в различные форматы

---

## 🏗️ Архитектура

### Диаграмма структуры базы данных

```mermaid
erDiagram
    projects {
        integer id PK "ID проекта"
        string name "Название"
        string slug "URL-идентификатор"
        string timezone "Часовой пояс"
        string currency "Валюта"
        datetime created_at "Дата создания"
    }
    
    yandex_counters {
        integer id PK "ID счетчика"
        integer project_id FK "ID проекта"
        integer counter_id "ID Яндекс.Метрики"
        string name "Название счетчика"
        string token "Токен доступа"
    }
    
    direct_accounts {
        integer id PK "ID аккаунта"
        integer project_id FK "ID проекта"
        string account_id "ID Яндекс.Директ"
        string name "Название аккаунта"
        string token "Токен доступа"
    }
    
    metrics_monthly {
        integer id PK "ID записи"
        integer project_id FK "ID проекта"
        date month "Месяц"
        integer visitors "Посетители"
        integer sessions "Сессии"
        float bounce_rate "Отказы"
        float conversion_rate "Конверсия"
    }
    
    goals {
        integer id PK "ID цели"
        integer counter_id FK "ID счетчика"
        integer goal_id "ID цели"
        string name "Название цели"
    }
    
    direct_campaigns {
        integer id PK "ID кампании"
        integer account_id FK "ID аккаунта"
        integer campaign_id "ID кампании"
        string name "Название кампании"
    }
    
    direct_campaign_monthly {
        integer id PK "ID записи"
        integer campaign_id FK "ID кампании"
        date month "Месяц"
        decimal spend "Расходы"
        integer clicks "Клики"
        integer impressions "Показы"
        float ctr "CTR"
    }

    projects ||--o{ yandex_counters : "имеет"
    projects ||--o{ direct_accounts : "имеет"
    projects ||--o{ metrics_monthly : "содержит"
    yandex_counters ||--o{ goals : "содержит"
    direct_accounts ||--o{ direct_campaigns : "содержит"
    direct_campaigns ||--o{ direct_campaign_monthly : "статистика"
```

### Архитектура системы

```mermaid
flowchart TD
    A[👤 Пользователь] --> B[📓 Jupyter Notebook / Python API]
    
    B --> C[🎯 ProjectAnalytics Class]
    B --> D[📤 Data Export Module]
    B --> E[📊 Visualization Module]
    
    C --> F[💾 SQLite Database Layer]
    D --> F
    E --> F
    
    subgraph F [Уровень базы данных]
        F1[🗃️ Core Tables]
        F2[📈 Aggregate Tables]
        F3[🔍 Indexes]
    end
    
    G[📊 Яндекс.Метрика] --> H[🔄 Data Collector]
    I[📢 Яндекс.Директ] --> H
    H --> F
    
    F --> J[⚙️ Analytics Engine]
    J --> K[📋 Reports & Visualization]
    
    style A fill:#e1f5fe
    style B fill:#f3e5f5
    style C fill:#e8f5e8
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#f5f5f5
    style G fill:#bbdefb
    style I fill:#c8e6c9
    style J fill:#fff9c4
    style K fill:#d1c4e9
```

### Поток данных

```mermaid
sequenceDiagram
    participant YM as Яндекс.Метрика
    participant YD as Яндекс.Директ
    participant DC as Data Collector
    participant DB as SQLite Database
    participant AE as Analytics Engine
    participant RV as Reports & Visualization
    
    Note over YM, RV: Процесс сбора данных
    loop Ежедневно/еженедельно
        YM->>DC: Запрос метрик
        YD->>DC: Запрос статистики кампаний
        DC->>DB: Сохранение сырых данных
    end
    
    Note over YM, RV: Процесс агрегации
    loop В конце месяца
        DB->>AE: Агрегация помесячных данных
        AE->>DB: Сохранение агрегированных данных
    end
    
    Note over YM, RV: Процесс анализа
    AE->>AE: Расчет KPI и трендов
    AE->>RV: Подготовка данных для визуализации
    
    Note over YM, RV: Генерация отчетов
    RV->>RV: Создание графиков и дашбордов
    RV-->>Пользователь: Отображение результатов
```

---

## 🚀 Быстрый старт

### Минимальная установка (30 секунд)

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/ВАШ_USERNAME/project-analytics.git
cd project-analytics

# 2. Установите зависимости
pip install -r requirements.txt

# 3. Запустите Jupyter
jupyter notebook

# 4. Откройте MAIN_code.ipynb и выполните ячейки
```

### Проверка установки

```bash
# Запустите тесты
pytest tests/

# Или проверьте вручную
python -c "import sqlite3, pandas, matplotlib; print('✓ Все зависимости установлены')"
```

---

## 📦 Установка

### Требования

- **Python**: 3.8+
- **ОС**: Windows, Linux, macOS
- **Память**: 512 MB RAM минимум
- **Диск**: 100 MB свободного места

### Детальная установка

См. [Руководство по установке](docs/INSTALLATION.md)

---

## 💻 Использование

### Базовый пример

```python
from project_analytics import ProjectAnalytics

# Создание экземпляра
analyzer = ProjectAnalytics('project_analytics.db')

# Генерация комплексного отчета
report = analyzer.generate_comprehensive_report()

# Анализ производительности
performance = analyzer.analyze_projects_performance()

# Закрытие соединения
analyzer.close()
```

### Добавление проекта

```python
# Безопасное добавление проекта
analyzer.safe_insert_project(
    name="Мой проект",
    slug="my-project",
    timezone="Europe/Moscow",
    currency="RUB"
)
```

### Работа с метриками

```python
# Анализ помесячных трендов
trends = analyzer.analyze_monthly_trends()

# Анализ кампаний Директа
campaigns = analyzer.analyze_direct_campaigns()

# Демографический анализ
demographics = analyzer.analyze_audience_demographics()
```

### Экспорт данных

```python
# Экспорт в Excel
analyzer.export_to_excel('report.xlsx')

# Экспорт в CSV
analyzer.export_to_csv('data.csv')

# Создание бэкапа
analyzer.create_backup('backup.zip')
```

**Больше примеров:** [examples/](examples/)

---

## 📁 Структура проекта

```
project-analytics/
│
├── 📄 README.md                 # Этот файл
├── 📄 LICENSE                    # Лицензия MIT
├── 📄 requirements.txt           # Зависимости Python
├── 📄 .gitignore                # Игнорируемые файлы Git
├── 📄 setup.py                  # Установочный скрипт
├── 📄 pyproject.toml            # Конфигурация проекта
│
├── 📓 MAIN_code.ipynb           # Основной Jupyter notebook
│
├── 📂 src/                      # Исходный код
│   └── project_analytics/
│       ├── __init__.py
│       ├── database.py          # Работа с БД
│       ├── analytics.py         # Аналитика
│       ├── export.py            # Экспорт данных
│       └── visualization.py     # Визуализация
│
├── 📂 tests/                     # Тесты
│   ├── __init__.py
│   ├── test_database.py         # Тесты БД
│   ├── test_analytics.py        # Тесты аналитики
│   ├── test_export.py           # Тесты экспорта
│   └── conftest.py              # Конфигурация pytest
│
├── 📂 examples/                  # Примеры использования
│   ├── basic_usage.py
│   ├── advanced_usage.py
│   └── integration_example.py
│
├── 📂 docs/                      # Документация
│   ├── INSTALLATION.md
│   ├── API.md
│   ├── ARCHITECTURE.md
│   └── CONTRIBUTING.md
│
├── 📂 .github/                   # GitHub конфигурация
│   └── workflows/
│       └── ci.yml               # CI/CD pipeline
│
└── 📂 scripts/                  # Вспомогательные скрипты
    ├── setup_database.py
    └── generate_docs.py

    
```
```mermaid
graph TD
    A[📦 project-analytics/] --> B[📄 Документация]
    A --> C[🔧 Исходный код]
    A --> D[🧪 Тесты]
    A --> E[📊 Примеры]
    A --> F[⚙️ Конфигурации]
    
    B --> B1[📖 README.md]
    B --> B2[📚 docs/]
    B2 --> B2a[🛠️ INSTALLATION.md]
    B2 --> B2b[🔗 API.md]
    B2 --> B2c[🏗️ ARCHITECTURE.md]
    
    C --> C1[💻 src/]
    C1 --> C1a[📂 project_analytics/]
    C1a --> C1a1[🗃️ database.py]
    C1a --> C1a2[📈 analytics.py]
    C1a --> C1a3[📤 export.py]
    C1a --> C1a4[📊 visualization.py]
    C1a --> C1a5[🔌 api.py]
    
    D --> D1[🧪 tests/]
    D1 --> D1a[✅ test_database.py]
    D1 --> D1b[✅ test_analytics.py]
    D1 --> D1c[✅ test_export.py]
    D1 --> D1d[✅ test_integration.py]
    
    E --> E1[💡 examples/]
    E1 --> E1a[🚀 basic_usage.py]
    E1 --> E1b[🔧 advanced_usage.py]
    E1 --> E1c[🔗 integration_example.py]
    E1 --> E1d[📊 dashboard_example.ipynb]
    
    F --> F1[⚙️ config/]
    F1 --> F1a[🔧 settings.yaml]
    F1 --> F1b[🔑 credentials.example]
    F --> F2[🐳 docker-compose.yml]
    F --> F3[🔨 pyproject.toml]

    style A fill:#f0f8ff,stroke:#333,stroke-width:2px
    style B fill:#e6f3ff,stroke:#1e88e5
    style C fill:#f0fff0,stroke:#43a047
    style D fill:#fffaf0,stroke:#ff9800
    style E fill:#f5f0ff,stroke:#7e57c2
    style F fill:#fff5f5,stroke:#e53935
```
### Описание компонентов

| Компонент | Описание | Файлы |
|-----------|----------|-------|
| **Core** | Основная логика системы | `src/project_analytics/` |
| **Database** | Работа с SQLite | `database.py` |
| **Analytics** | Аналитические функции | `analytics.py` |
| **Export** | Экспорт данных | `export.py` |
| **Visualization** | Графики и отчеты | `visualization.py` |
| **Tests** | Автоматические тесты | `tests/` |
| **Examples** | Примеры использования | `examples/` |
| **Docs** | Документация | `docs/` |

```mermaid
graph LR
    A[🎯 Core Components] --> B[💾 Database Layer]
    A --> C[📊 Analytics Engine]
    A --> D[📈 Visualization]
    A --> E[🔌 API Layer]
    
    B --> B1[🗃️ SQLite Manager]
    B --> B2[🔍 Query Builder]
    B --> B3[📝 Schema Migrations]
    
    C --> C1[📈 Metrics Calculator]
    C --> C2[📉 Trend Analysis]
    C --> C3[📊 Performance KPIs]
    C --> C4[🔮 Forecasting]
    
    D --> D1[📊 Chart Generator]
    D --> D2[📋 Report Builder]
    D --> D3[🎯 Dashboard Creator]
    
    E --> E1[🌐 REST API]
    E --> E2[📡 Webhook Handler]
    E --> E3[🔗 Integration Adapters]
    
    style A fill:#e3f2fd
    style B fill:#e8f5e8
    style C fill:#fff3e0
    style D fill:#fce4ec
    style E fill:#f3e5f5
```

---

## 📚 Документация

### Основная документация

- 📖 [Руководство по установке](docs/INSTALLATION.md)
- 📖 [API Reference](docs/API.md)
- 📖 [Архитектура системы](docs/ARCHITECTURE.md)
- 📖 [Примеры использования](examples/)

### Дополнительные материалы

- 🔧 [Настройка и конфигурация](docs/CONFIGURATION.md)
- 🐛 [Устранение неполадок](docs/TROUBLESHOOTING.md)
- 🤝 [Руководство для контрибьюторов](CONTRIBUTING.md)
- 📝 [История изменений](CHANGELOG.md)

---

## 🧪 Тестирование

### Запуск тестов

```bash
# Все тесты
pytest

# С покрытием кода
pytest --cov=src/project_analytics --cov-report=html

# Конкретный тест
pytest tests/test_database.py

# С verbose выводом
pytest -v
```

### Структура тестов

```mermaid
graph TD
    A[🧪 tests/] --> B[✅ Unit Tests]
    A --> C[🔗 Integration Tests]
    A --> D[⚡ Performance Tests]
    A --> E[🐳 E2E Tests]
    
    B --> B1[🗃️ test_database.py]
    B --> B2[📈 test_analytics.py]
    B --> B3[📤 test_export.py]
    B --> B4[📊 test_visualization.py]
    
    C --> C1[🔌 test_integrations.py]
    C --> C2[🌐 test_api.py]
    C --> C3[📡 test_webhooks.py]
    
    D --> D1[⚡ test_performance.py]
    D --> D2[📊 test_benchmarks.py]
    D --> D3[🔍 test_load.py]
    
    E --> E1[🎯 test_e2e.py]
    E --> E2[📋 test_user_flows.py]
    E --> E3[🖥️ test_ui.py]
    
    F[⚙️ test_config/] --> F1[🎛️ conftest.py]
    F --> F2[📁 fixtures/]
    F --> F3[📊 test_data/]
    
    style A fill:#fffaf0
    style B fill:#e8f5e8
    style C fill:#e3f2fd
    style D fill:#fff3e0
    style E fill:#fce4ec
    style F fill:#f3e5f5
```

### Покрытие кода

Текущее покрытие: **85%+**

```bash
# Генерация отчета о покрытии
pytest --cov=src --cov-report=term-missing
```

---

## 🔄 CI/CD

Проект использует GitHub Actions для автоматического тестирования:

- ✅ Автоматический запуск тестов при каждом коммите
- ✅ Проверка стиля кода (black, flake8)
- ✅ Проверка типов (mypy)
- ✅ Генерация документации

Статус: [![CI](https://github.com/DmitryProffessor/project-analytics/workflows/CI/badge.svg)](https://github.com/DmitryProffessor/project-analytics/actions)
## Конвейер автоматизации
```mermaid
graph LR
    A[📝 Push Code] --> B[🔄 GitHub Actions]
    B --> C[🧪 Run Tests]
    B --> D[🔍 Code Quality]
    B --> E[📦 Build Package]
    B --> F[🚀 Deploy]
    
    C --> C1[✅ Unit Tests]
    C --> C2[🔗 Integration Tests]
    C --> C3[📊 Coverage Report]
    
    D --> D1[⚫ Black Formatting]
    D --> D2[🧹 Flake8 Linting]
    D --> D3[📝 MyPy Type Checking]
    
    E --> E1[🐍 Build Wheel]
    E --> E2[📦 Create Package]
    E --> E3[🏷️ Version Tagging]
    
    F --> F1[📚 Update Docs]
    F --> F2[🐳 Docker Build]
    F --> F3[☁️ Cloud Deploy]
    
    style A fill:#e3f2fd
    style B fill:#fff3e0
    style C fill:#e8f5e8
    style D fill:#fce4ec
    style E fill:#f3e5f5
    style F fill:#e1f5fe
```

---

## 🤝 Вклад в проект

Мы приветствуем вклад в развитие проекта! См. [CONTRIBUTING.md](CONTRIBUTING.md) для деталей.

### Быстрый старт для контрибьюторов

```bash
# 1. Форкните репозиторий
# 2. Клонируйте ваш форк
git clone https://github.com/ВАШ_USERNAME/project-analytics.git

# 3. Создайте ветку
git checkout -b feature/amazing-feature

# 4. Внесите изменения и зафиксируйте
git commit -m "Add amazing feature"

# 5. Отправьте в ваш форк
git push origin feature/amazing-feature

# 6. Откройте Pull Request
```

---

## 📊 Статистика проекта

- 📦 **Версия**: 1.0.0
- 🐍 **Python**: 3.8+
- 📚 **Зависимости**: 6 основных пакетов
- 🧪 **Тесты**: 20+ тестовых случаев
- 📖 **Документация**: Полная API документация
- ⭐ **Звезды**: [Посмотреть на GitHub](https://github.com/ВАШ_USERNAME/project-analytics)

---

## 📝 Лицензия

Этот проект распространяется под лицензией MIT. См. [LICENSE](LICENSE) для подробностей.

---

## 👥 Авторы

**Ваше Имя**
- GitHub: [@ВАШ_USERNAME](https://github.com/ВАШ_USERNAME)
- Email: ваш.email@example.com

---

## 🙏 Благодарности

- Команде разработчиков [pandas](https://pandas.pydata.org/)
- Сообществу [Jupyter](https://jupyter.org/)
- Всем [контрибьюторам](https://github.com/ВАШ_USERNAME/project-analytics/graphs/contributors) проекта

---

## 📞 Поддержка

- 💬 [Discussions](https://github.com/ВАШ_USERNAME/project-analytics/discussions)
- 🐛 [Issues](https://github.com/ВАШ_USERNAME/project-analytics/issues)
- 📧 Email: ваш.email@example.com

---

<div align="center">

**⭐ Если проект был полезен, поставьте звезду!**

[⬆ Наверх](#-project-analytics---профессиональная-система-аналитики-проектов)

</div>

