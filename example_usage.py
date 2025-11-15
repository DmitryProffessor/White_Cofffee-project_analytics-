"""
Пример использования Project Analytics System

Этот файл демонстрирует базовое использование системы аналитики проектов.
"""

import sqlite3
import sys
import os

# Добавляем путь к проекту (если нужно)
# sys.path.append(os.path.dirname(os.path.abspath(__file__)))

# Импортируем необходимые модули
# from project_analytics import ProjectAnalytics

def example_basic_usage():
    """Базовый пример использования"""
    print("=== Пример 1: Базовое использование ===\n")
    
    # Подключение к базе данных
    conn = sqlite3.connect('project_analytics.db')
    cursor = conn.cursor()
    
    # Проверка существования таблиц
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
    tables = cursor.fetchall()
    print(f"Найдено таблиц: {len(tables)}")
    for table in tables:
        print(f"  - {table[0]}")
    
    conn.close()
    print("\n✓ Базовое использование завершено\n")


def example_add_project():
    """Пример добавления проекта"""
    print("=== Пример 2: Добавление проекта ===\n")
    
    conn = sqlite3.connect('project_analytics.db')
    cursor = conn.cursor()
    
    try:
        # Добавляем проект
        cursor.execute("""
            INSERT OR IGNORE INTO projects (name, slug, timezone, currency, is_active)
            VALUES (?, ?, ?, ?, ?)
        """, ('Тестовый проект', 'test-project', 'Europe/Moscow', 'RUB', 1))
        
        conn.commit()
        print("✓ Проект успешно добавлен")
        
        # Получаем ID добавленного проекта
        cursor.execute("SELECT id FROM projects WHERE slug = 'test-project'")
        project_id = cursor.fetchone()[0]
        print(f"  ID проекта: {project_id}")
        
    except Exception as e:
        print(f"✗ Ошибка: {e}")
    
    conn.close()
    print("\n✓ Добавление проекта завершено\n")


def example_query_data():
    """Пример запроса данных"""
    print("=== Пример 3: Запрос данных ===\n")
    
    conn = sqlite3.connect('project_analytics.db')
    cursor = conn.cursor()
    
    try:
        # Получаем список всех проектов
        cursor.execute("SELECT id, name, slug, currency FROM projects")
        projects = cursor.fetchall()
        
        print("Список проектов:")
        for project in projects:
            print(f"  ID: {project[0]}, Название: {project[1]}, Slug: {project[2]}, Валюта: {project[3]}")
        
        # Получаем статистику по проектам
        cursor.execute("""
            SELECT 
                p.name,
                COUNT(DISTINCT yc.id) as counters_count,
                COUNT(DISTINCT dc.id) as campaigns_count
            FROM projects p
            LEFT JOIN yandex_counters yc ON p.id = yc.project_id
            LEFT JOIN direct_campaigns dc ON p.id = dc.direct_account_id
            GROUP BY p.id, p.name
        """)
        
        stats = cursor.fetchall()
        print("\nСтатистика по проектам:")
        for stat in stats:
            print(f"  {stat[0]}: {stat[1]} счетчиков, {stat[2]} кампаний")
        
    except Exception as e:
        print(f"✗ Ошибка: {e}")
    
    conn.close()
    print("\n✓ Запрос данных завершен\n")


def example_export_data():
    """Пример экспорта данных"""
    print("=== Пример 4: Экспорт данных ===\n")
    
    import pandas as pd
    
    conn = sqlite3.connect('project_analytics.db')
    
    try:
        # Экспортируем проекты в DataFrame
        df_projects = pd.read_sql_query("SELECT * FROM projects", conn)
        print(f"Экспортировано проектов: {len(df_projects)}")
        
        # Сохраняем в CSV
        df_projects.to_csv('projects_export.csv', index=False, encoding='utf-8')
        print("✓ Данные сохранены в projects_export.csv")
        
        # Экспортируем метрики
        df_metrics = pd.read_sql_query("SELECT * FROM metrics_monthly", conn)
        if len(df_metrics) > 0:
            print(f"Экспортировано метрик: {len(df_metrics)}")
            df_metrics.to_csv('metrics_export.csv', index=False, encoding='utf-8')
            print("✓ Метрики сохранены в metrics_export.csv")
        else:
            print("⚠ Метрики не найдены")
        
    except Exception as e:
        print(f"✗ Ошибка: {e}")
    
    conn.close()
    print("\n✓ Экспорт данных завершен\n")


def example_analysis():
    """Пример анализа данных"""
    print("=== Пример 5: Анализ данных ===\n")
    
    import pandas as pd
    
    conn = sqlite3.connect('project_analytics.db')
    
    try:
        # Анализ посещений по проектам
        query = """
            SELECT 
                p.name,
                SUM(mm.visits) as total_visits,
                SUM(mm.users) as total_users,
                SUM(mm.conversions) as total_conversions
            FROM projects p
            LEFT JOIN metrics_monthly mm ON p.id = mm.project_id
            GROUP BY p.id, p.name
            ORDER BY total_visits DESC
        """
        
        df = pd.read_sql_query(query, conn)
        
        if len(df) > 0:
            print("Анализ посещений:")
            print(df.to_string(index=False))
            
            # Расчет конверсионной ставки
            df['conversion_rate'] = (df['total_conversions'] / df['total_visits'] * 100).round(2)
            print("\nКонверсионная ставка:")
            print(df[['name', 'conversion_rate']].to_string(index=False))
        else:
            print("⚠ Данные для анализа не найдены")
        
    except Exception as e:
        print(f"✗ Ошибка: {e}")
    
    conn.close()
    print("\n✓ Анализ данных завершен\n")


if __name__ == "__main__":
    print("=" * 60)
    print("Примеры использования Project Analytics System")
    print("=" * 60)
    print()
    
    # Проверяем существование базы данных
    if not os.path.exists('project_analytics.db'):
        print("⚠ База данных не найдена!")
        print("  Сначала запустите MAIN_code.ipynb для создания базы данных")
        sys.exit(1)
    
    # Запускаем примеры
    try:
        example_basic_usage()
        example_add_project()
        example_query_data()
        example_export_data()
        example_analysis()
        
        print("=" * 60)
        print("✓ Все примеры выполнены успешно!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Ошибка при выполнении примеров: {e}")
        sys.exit(1)

