"""
Setup script for Project Analytics
"""

from setuptools import setup, find_packages
from pathlib import Path

# Читаем README для long_description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8') if (this_directory / "README.md").exists() else ""

setup(
    name="project-analytics",
    version="1.0.0",
    author="Ваше Имя",
    author_email="ваш.email@example.com",
    description="Система аналитики проектов с поддержкой Яндекс.Метрики и Яндекс.Директ",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ВАШ_USERNAME/project-analytics",
    project_urls={
        "Bug Reports": "https://github.com/ВАШ_USERNAME/project-analytics/issues",
        "Source": "https://github.com/ВАШ_USERNAME/project-analytics",
        "Documentation": "https://github.com/ВАШ_USERNAME/project-analytics/tree/main/docs",
    },
    packages=find_packages(where="src") if Path("src").exists() else [],
    package_dir={"": "src"} if Path("src").exists() else {"": "."},
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering :: Information Analysis",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "pandas>=2.0.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "numpy>=1.24.0",
        "openpyxl>=3.1.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
            "black>=23.0.0",
            "flake8>=6.0.0",
            "mypy>=1.0.0",
            "jupyter>=1.0.0",
        ],
        "test": [
            "pytest>=7.0.0",
            "pytest-cov>=4.0.0",
        ],
    },
    keywords="analytics, yandex-metrica, yandex-direct, sqlite, data-analysis, reporting",
    zip_safe=False,
)

