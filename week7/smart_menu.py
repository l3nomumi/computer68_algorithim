from typing import List, Dict, Optional


def main():
    items: List[Dict] = []

    while True:
            print("\n=== Smart Menu Analyzer ===")
            print("1) เพิ่มเมนู")
            print("2) ลบเมนู")
            print("3) แสดงรายการทั้งหมด")
            print("4) หาถูกสุด/แพงสุด")
            print("5) ยอดรวม/ค่าเฉลี่ย")
            print("6) นับเมนูที่ราคา > X")
            print("7) เรียงราคา (Bubble/Selection)")
            print("0) ออก")

            choice = input("เลือกเมนู : ").strip()

            if choice == "1":
                add_item(items)
            
            elif choice == "2":
                remove_item(items)
            elif choice == "3":
                show_items(items)
            elif choice == "4":
                find_min_max(items)
            elif choice == "5":
                total_and_average(items)   
            elif choice == "6":
                count_greater_than(items)  
            elif choice == "7":
                sort_menu(items)  

          
            elif choice == "0":
                print("👋 ออกจากโปรแกรม")
                break
            else:
                print("❌ กรุณาเลือกเมนูให้ถูกต้อง")


def add_item(items: List[Dict]) -> None:
    name = input("ชื่อเมนู: ").strip()
    if not name:
        print("❌ ชื่อเมนูห้ามว่าง")
        return
    price = input_float("ราคา: ")
    items.append({"name": name, "price": price})
    print("✅ เพิ่มเมนูเรียบร้อย")


def remove_item(items: List[Dict]) -> None:
    if not items:
        print("❌ ยังไม่มีเมนู")
        return
    show_items(items)
    idx = input_int("ใส่ลำดับเมนูที่จะลบ: ")
    if idx < 1 or idx > len(items):
        print("❌ ลำดับไม่ถูกต้อง")
        return
    removed = items.pop(idx - 1)
    print(f"✅ ลบเมนู: {removed['name']} ราคา {removed['price']:.2f} บาท")

def show_items(items: List[Dict]) -> None:
    if not items:
        print("❌ ยังไม่มีเมนู")
        return
    print("\n--- รายการเมนู ---")
    for i, it in enumerate(items, start=1):
        print(f"{i:>2}) {it['name']:<20} {it['price']:>8.2f} บาท")
    print("------------------\n")


def input_int(prompt: str) -> int:
    """รับ int แบบปลอดภัย"""
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            return v
        except ValueError:
            print("❌ กรุณากรอกเป็นจำนวนเต็ม")

def input_float(prompt: str) -> float:
    """รับ float แบบปลอดภัย"""
    while True:
        s = input(prompt).strip()
        try:
            v = float(s)
            if v < 0:
                print("❌ ราคา/จำนวนต้องไม่ติดลบ")
                continue
            return v
        except ValueError:
            print("❌ กรุณากรอกเป็นตัวเลข")

def find_min_max(items: List[Dict]) -> None:
    if not items:
        print("❌ ยังไม่มีเมนู")
        return
    min_item = min(items, key=lambda x: x["price"])
    max_item = max(items, key=lambda x: x["price"])
    print(f"💸 ถูกสุด: {min_item['name']} = {min_item['price']:.2f} บาท")
    print(f"💰 แพงสุด: {max_item['name']} = {max_item['price']:.2f} บาท")
    
def total_and_average(items: List[Dict]) -> None:
    if not items:
        print("❌ ยังไม่มีเมนู")
        return
    total = sum(item["price"] for item in items)
    avg = total / len(items)
    print(f"💵 ยอดรวม: {total:.2f} บาท")
    print(f"📊 ค่าเฉลี่ย: {avg:.2f} บาท")
    
def count_greater_than(items: List[Dict]) -> None:
    if not items:
        print("❌ ยังไม่มีเมนู")
        return
    x = input_float("ใส่ราคา X: ")
    count = 0
    for item in items:
        if item["price"] > x:
            count += 1
    print(f"🔢 มีเมนูที่ราคามากกว่า {x:.2f} บาท = {count} รายการ")
    
def sort_menu(items: List[Dict]) -> None:
    if not items:
        print("❌ ยังไม่มีเมนู")
        return

    print("\n--- เลือกการเรียง ---")
    print("1) ราคา น้อย → มาก (Bubble)")
    print("2) ราคา มาก → น้อย (Bubble)")
    print("3) ชื่อ A-Z (Selection)")
    print("4) ชื่อ Z-A (Selection)")
    choice = input("เลือก: ").strip()

    n = len(items)

    if choice == "1":  # Bubble sort ราคา น้อย -> มาก
        for i in range(n):
            for j in range(n - i - 1):
                if items[j]["price"] > items[j + 1]["price"]:
                    items[j], items[j + 1] = items[j + 1], items[j]

    elif choice == "2":  # Bubble sort ราคา มาก -> น้อย
        for i in range(n):
            for j in range(n - i - 1):
                if items[j]["price"] < items[j + 1]["price"]:
                    items[j], items[j + 1] = items[j + 1], items[j]

    elif choice == "3":  # Selection sort ชื่อ A-Z
        for i in range(n):
            min_idx = i
            for j in range(i + 1, n):
                if items[j]["name"].lower() < items[min_idx]["name"].lower():
                    min_idx = j
            items[i], items[min_idx] = items[min_idx], items[i]

    elif choice == "4":  # Selection sort ชื่อ Z-A
        for i in range(n):
            max_idx = i
            for j in range(i + 1, n):
                if items[j]["name"].lower() > items[max_idx]["name"].lower():
                    max_idx = j
            items[i], items[max_idx] = items[max_idx], items[i]

    else:
        print("❌ เลือกไม่ถูกต้อง")
        return

    print("✅ เรียงข้อมูลเรียบร้อย")
    show_items(items)



    
def test():
    print("Test")   

if __name__ == "__main__":
    main()