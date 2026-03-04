import json
import os
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)  # Renkleri otomatik sıfırlar

TASKS_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r", encoding="utf-8") as f:
                return json.load(f)
        except:
            return []
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, ensure_ascii=False, indent=2)

def add_task(tasks):
    description = input("Yapılacak iş nedir? ").strip()
    if not description:
        print(f"{Fore.YELLOW}Boş görev eklenemez.{Style.RESET_ALL}")
        return
    
    task = {
        "description": description,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    print(f"{Fore.GREEN}✓ Eklendi: {description}{Style.RESET_ALL}")

def list_tasks(tasks):
    if not tasks:
        print(f"{Fore.YELLOW}Henüz görev yok.{Style.RESET_ALL}")
        return
    
    print(f"\n{Fore.CYAN}Görev Listesi:{Style.RESET_ALL}")
    for i, task in enumerate(tasks, 1):
        status = f"{Fore.GREEN}✓{Style.RESET_ALL}" if task["done"] else f"{Fore.RED}✗{Style.RESET_ALL}"
        print(f"{i}. [{status}] {task['description']}  ({task['created']})")

def complete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    
    try:
        num = int(input(f"\n{Fore.CYAN}Tamamlanan görevin numarası: {Style.RESET_ALL}"))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print(f"{Fore.GREEN}✓ Görev tamamlandı!{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Geçersiz numara.{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Lütfen sayı gir.{Style.RESET_ALL}")

def delete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    
    try:
        num = int(input(f"\n{Fore.CYAN}Silinecek görevin numarası: {Style.RESET_ALL}"))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"{Fore.RED}🗑 Silindi: {removed['description']}{Style.RESET_ALL}")
        else:
            print(f"{Fore.RED}Geçersiz numara.{Style.RESET_ALL}")
    except:
        print(f"{Fore.RED}Lütfen sayı gir.{Style.RESET_ALL}")

def main():
    tasks = load_tasks()
    
    while True:
        print(f"\n{Fore.CYAN}" + "="*40)
        print(f"{Fore.CYAN}  TO-DO UYGULAMASI")
        print(f"{Fore.CYAN}" + "="*40)
        print("1. Görev ekle")
        print("2. Görevleri listele")
        print("3. Görevi tamamla")
        print("4. Görev sil")
        print("5. Çıkış")
        
        choice = input(f"\n{Fore.YELLOW}Seçiminiz (1-5): {Style.RESET_ALL}").strip()
        
        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            list_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print(f"\n{Fore.GREEN}Görüşürüz! Görevleriniz kaydedildi.{Style.RESET_ALL}")
            break
        else:
            print(f"{Fore.RED}Geçersiz seçim, 1-5 arası bir sayı girin.{Style.RESET_ALL}")
        
        save_tasks(tasks)  # Her işlemden sonra kaydet

if __name__ == "__main__":
    main()
