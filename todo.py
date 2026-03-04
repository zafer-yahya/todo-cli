import json
import os
from datetime import datetime

# Dosya adı
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
        print("Boş görev eklenemez.")
        return
    
    task = {
        "description": description,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d %H:%M")
    }
    tasks.append(task)
    print(f"✓ Eklendi: {description}")

def list_tasks(tasks):
    if not tasks:
        print("Henüz görev yok.")
        return
    
    print("\nGörev Listesi:")
    for i, task in enumerate(tasks, 1):
        status = "✓" if task["done"] else " "
        print(f"{i}. [{status}] {task['description']}  ({task['created']})")

def complete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    
    try:
        num = int(input("\nTamamlanan görevin numarası: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("✓ Görev tamamlandı!")
        else:
            print("Geçersiz numara.")
    except:
        print("Lütfen sayı gir.")

def delete_task(tasks):
    list_tasks(tasks)
    if not tasks:
        return
    
    try:
        num = int(input("\nSilinecek görevin numarası: "))
        if 1 <= num <= len(tasks):
            removed = tasks.pop(num-1)
            print(f"🗑 Silindi: {removed['description']}")
        else:
            print("Geçersiz numara.")
    except:
        print("Lütfen sayı gir.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\n" + "="*40)
        print("  TO-DO UYGULAMASI")
        print("="*40)
        print("1. Görev ekle")
        print("2. Görevleri listele")
        print("3. Görevi tamamla")
        print("4. Görev sil")
        print("5. Çıkış")
        
        choice = input("\nSeçiminiz (1-5): ").strip()
        
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
            print("\nGörüşürüz! Görevleriniz kaydedildi.")
            break
        else:
            print("Geçersiz seçim, 1-5 arası bir sayı girin.")
        
        # Her işlemden sonra kaydet (güvenli olsun)
        save_tasks(tasks)

if __name__ == "__main__":
    main()
