import pandas as pd
import matplotlib.pyplot as plt
from tkinter import Tk, Label, Entry, Button

# Bước 1: Đọc dữ liệu từ file diemPython.csv
def doc_du_lieu(file_path):
    df = pd.read_csv(file_path)
    return df

# Bước 2: Thực hiện các yêu cầu
def thuc_hien_yeu_cau(df):
    # Tổng số sinh viên
    tong_sv = df['So SV'].sum()

    # Tổng số sinh viên đạt điểm A
    tong_sv_dat_A = df['Loại A'].sum()

    # Tỉ lệ phần trăm sinh viên đạt điểm A
    ti_le_dat_A = (tong_sv_dat_A / tong_sv) * 100

    # Tìm lớp có số sinh viên đạt điểm A cao nhất
    lop_max_A = df[df['Loại A'] == df['Loại A'].max()]['Mã lớp'].values[0]

    # Tìm trung bình số sinh viên đạt của các lớp qua môn
    trung_binh_sv_dat = df.groupby('Mã lớp')[['Loại A', 'Loại B+', 'Loại B', 'Loại C+', 'Loại C', 'Loại D+', 'Loại D', 'Loại F']].sum()

    # Tổng số sinh viên đạt của tất cả các lớp
    tong_sv_dat_cua_tat_ca_lop = trung_binh_sv_dat.sum()

    # Tính trung bình số sinh viên đạt điểm A của tất cả các lớp
    trung_binh_sv_dat_A_cua_tat_ca_lop = trung_binh_sv_dat['Loại A'].mean()

    return tong_sv, tong_sv_dat_A, ti_le_dat_A, lop_max_A, trung_binh_sv_dat, tong_sv_dat_cua_tat_ca_lop, trung_binh_sv_dat_A_cua_tat_ca_lop
           

# Bước 3: Vẽ biểu đồ phân bố điểm
def ve_bieu_do(diem_counts):
    labels = diem_counts.index
    values = diem_counts.values

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    ax.set_xlabel('Loại điểm')
    ax.set_ylabel('Số lượng sinh viên')
    ax.set_title('Phân bố điểm')

    plt.show()

# Xử lý sự kiện khi người dùng nhấn nút "Thực hiện"
def thuc_hien():
    # Lấy đường dẫn từ người dùng
    file_path = duong_dan_entry.get()

    if file_path:
        try:
            # Đọc dữ liệu từ file CSV
            df = doc_du_lieu(file_path)

            # Thực hiện các yêu cầu
            tong_sv, tong_sv_dat_A, ti_le_dat_A, lop_max_A, trung_binh_sv_dat, tong_sv_dat_cua_tat_ca_lop, trung_binh_sv_dat_A_cua_tat_ca_lop = thuc_hien_yeu_cau(df)

            # Hiển thị kết quả
            ket_qua_label.config(text=f"Tổng số sinh viên: {tong_sv}\nTổng số sinh viên đạt điểm A: {tong_sv_dat_A}\nTỉ lệ sinh viên đạt điểm A: {ti_le_dat_A:.2f}%\n"
                                      f"Lớp có số sinh viên đạt điểm A cao nhất: {lop_max_A}\n"
                                      f"Phân loại điểm của tất cả các lớp:\n{tong_sv_dat_cua_tat_ca_lop.to_string()}\n"
                                      f"Trung bình số sinh viên đạt điểm A của tất cả các lớp: {trung_binh_sv_dat_A_cua_tat_ca_lop:.2f}\n")

            # Vẽ biểu đồ phân bố điểm
            ve_bieu_do(df[['Loại A', 'Loại B+', 'Loại B', 'Loại C+', 'Loại C', 'Loại D+', 'Loại D', 'Loại F']].sum())

        except Exception as e:
            ket_qua_label.config(text=f"Đã xảy ra lỗi: {e}")
    else:
        ket_qua_label.config(text="Vui lòng nhập đường dẫn.")


# Tạo giao diện Tkinter
root = Tk()
root.geometry("800x600")
root.title("Thống kê điểm")

# Nhãn và ô nhập đường dẫn
duong_dan_label = Label(root, text="Nhập đường dẫn của file 'diemPython.csv':")
duong_dan_label.pack(pady=(10,0))

duong_dan_entry = Entry(root, width=50)
duong_dan_entry.pack(pady=(0,10))

# Nút "Thực hiện"
thuc_hien_button = Button(root, text="Thực hiện", command=thuc_hien)
thuc_hien_button.pack()

# Kết quả
ket_qua_label = Label(root, text="")
ket_qua_label.pack(pady=(10,0))

# Chạy giao diện
root.mainloop()
