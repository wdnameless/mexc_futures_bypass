#!/usr/bin/env python3
"""
MEXC Futures Bypass - Demo Launcher

Простой скрипт для запуска демонстрации возможностей.
Показывает основные функции без полного доступа к коду.

Для полного доступа к коду свяжитесь: @shitmane
"""

import sys
import subprocess
import os
from pathlib import Path

def check_python_version():
    """Проверка версии Python"""
    if sys.version_info < (3, 8):
        print("❌ Требуется Python 3.8 или выше")
        print(f"   Текущая версия: {sys.version}")
        return False
    return True

def check_dependencies():
    """Проверка зависимостей"""
    try:
        import asyncio
        import time
        print("✅ Основные зависимости найдены")
        return True
    except ImportError as e:
        print(f"❌ Ошибка импорта: {e}")
        return False

def install_dependencies():
    """Установка зависимостей"""
    print("📦 Установка зависимостей...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
        print("✅ Зависимости установлены")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка установки: {e}")
        return False

def run_demo():
    """Запуск демо"""
    print("🚀 Запуск демонстрации...")
    try:
        subprocess.check_call([sys.executable, "demo.py"])
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Ошибка запуска демо: {e}")
        return False

def main():
    """Главная функция"""
    print("🎯 MEXC Futures Bypass - Demo Launcher")
    print("=" * 50)
    
    # Проверка Python версии
    if not check_python_version():
        sys.exit(1)
    
    # Проверка зависимостей
    if not check_dependencies():
        print("📦 Попытка установки зависимостей...")
        if not install_dependencies():
            print("❌ Не удалось установить зависимости")
            print("   Попробуйте: pip install -r requirements.txt")
            sys.exit(1)
    
    # Запуск демо
    if not run_demo():
        print("❌ Не удалось запустить демо")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    print("🎉 Демонстрация завершена!")
    print("\n💡 Для получения полного доступа:")
    print("   📞 Telegram: @shitmane")
    print("   💰 Стоимость: $100")
    print("   🚀 Начните зарабатывать уже сегодня!")

if __name__ == "__main__":
    main()
