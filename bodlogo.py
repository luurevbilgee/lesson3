import threading
import time

# Функция, яг одоо ямар CPU дээр ажиллахыг тодорхойлж байгааг шалгана
def check_cpu():
    for i in range(3):
        print(f"CPU-{i + 1}: Програм P{i} -г ажиллуулж байна.")
        time.sleep(10 if i == 0 else 15)  # 10 мсек, 15 мсек, 30 мсек

# Тухайн CPU-д хийгдэж байгаа ажилуудыг тэнцүүлж, ажиллуулна
def assign_work(cpu_num):
    if cpu_num == 1:
        check_cpu()
    else:
        time.sleep(30)  # CPU-2 д 30 мсек хэмжээтэй ажилуулна

# 2 CPU-тэй болгоно
cpu1 = threading.Thread(target=assign_work, args=(1,))
cpu2 = threading.Thread(target=assign_work, args=(2,))

# CPU-г ажиллуулна
cpu1.start()
cpu2.start()

# Хамт ожирохыг хүлээж байна
cpu1.join()
cpu2.join()

print("Бүх программууд дууслаа.")
