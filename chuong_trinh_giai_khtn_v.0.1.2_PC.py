# import các thư viện quan trọng
import msvcrt
from colorama import Fore, Style, init
init(autoreset=True)


# Hàm giới thiệu chương trình

def gioithieu_ct():
    print(Fore.YELLOW + "=======================================")
    print(Fore.CYAN + "CHƯƠNG TRÌNH GIẢI CÁC CÔNG THỨC HÓA HỌC")
    print(Fore.YELLOW + "=======================================")
    print(Fore.LIGHTRED_EX + "LƯU Ý: NẾU TRONG QUÁ TRÌNH SỬ DỤNG CÓ XẢY RA LỖI, SỰ CỐ. HÃY CHỤP ẢNH MÀN HÌNH VÀ GỬI QUA EMAIL CHO TUI :lt.thu280879@gmail.com HAY LÀ TOP TOP: l_WoTBhehe ĐỂ TUI CÒN SỬA NHA :3")
    msvcrt.getch()
    print(Fore.GREEN + "version 0.1.1")
    msvcrt.getch()
    print(Fore.MAGENTA + "by Trung Nghĩa" + Style.RESET_ALL)


gioithieu_ct()

# Hàm khởi động và báo lỗi nhập liệu
msvcrt.getch()


def khoidong_ct():
    while True:
        khoidong = input(Fore.CYAN + "Nhập tt để tiếp tục:")
        if khoidong == "tt":
            break
        else:
            print(Fore.RED + "NHẬP SAI RỒI, 'tt' MỚI ĐÚNG")


khoidong_ct()

# Hàm menu, tính toán, change log và out chương trình


def menu_va_tinhtoan():
    while True:
        try:
            print(Fore.CYAN + "CHỌN TÌM SỐ MOL NHẤN: MOL / CHỌN TÌM KHỐI LƯỢNG MOL NHẤN: KL/M / CHANGE LOG: upd in4")
            print(Fore.CYAN + "THOÁT CHƯƠNG TRÌNH: exit")
            chonchucnang = input(": ")
# Tính toán
            if chonchucnang == "MOL":
                print(Fore.CYAN + "Hãy nhập m(khối lượng nguyên tử hoặc phân tử):")
                m = float(input(": "))
                print(Fore.CYAN + "Hãy nhập M(khối lượng mol của chất):")
                M = float(input(": "))
                n = m / M
                print(Fore.GREEN + "Số mol là:", n, "mol")
            elif chonchucnang == "KL/M":
                print(Fore.CYAN + "Hãy nhập m(khối lượng nguyên tử hoặc phân tử):")
                m = float(input(": "))
                print(Fore.CYAN + "Hãy nhập n(số mol):")
                n = float(input(": "))
                M = m / n
                print(Fore.GREEN + "Khối lượng mol là:", n, "mol/gam")
            elif chonchucnang == "KL.NT/PT":
                print(Fore.CYAN + "Hãy nhập n(số mol):")
                n = float(input(":"))
                print(Fore.CYAN + "Hãy nhập M(khối lượng mol):")
                M = float(input(":"))
                m = n * M
                print(Fore.GREEN + "Khối lượng nguyên tử/phân tử là:", m, "gam")

# Change log
            elif chonchucnang == "upd in4":
                print(Fore.YELLOW + "=========== CHANGE LOG ===========")
                print(Fore.CYAN + "Thông tin phiên bản: v0.1.1")
                print(Fore.WHITE + "Tác giả: Trung Nghĩa")
                print(Fore.MAGENTA + "Ngày phát hành: 6/10/2025")
                print(Fore.GREEN + "Sửa đổi: Lặp chương trình, fix bug,")
                print(
                    Fore.GREEN + "- Sửa lỗi nhập liệu (thông báo khi nhập sai), sử dụng hàm def, và thêm màu sắc ")
                print(Fore.GREEN + "- Menu hoạt động liên tục, không cần khởi động lại")
                print(Fore.BLUE + "Tính năng: tính số mol và khối lượng mol")
                print(Fore.WHITE + "Sứ mệnh của chưng trình là giúp những bạn học sinh cấp 2/3 sử dụng trong các mục đích về học tập và nghiên cứu")
                print(
                    Fore.MAGENTA + "Bản mobile ở github nha chừng nào có link tui bỏ vô đây:    ")
                print(Fore.CYAN + "Nhấn bất kỳ phím nào để trở lại màn hình chính")
                msvcrt.getch()
                continue
# Out
            elif chonchucnang == "exit":
                print(Fore.YELLOW + "===========")
                print(Fore.CYAN + "Bái bai :D")
                print(Fore.MAGENTA + "TY 4 using")
                print(Fore.YELLOW + "===========")
                break
# Báo lỗi
            else:
                print(Fore.RED + "Chức năng không tồn tại")
        except:
            print(Fore.RED + "KHÔNG ĐƯỢC NHẬP CHỮ")


menu_va_tinhtoan()