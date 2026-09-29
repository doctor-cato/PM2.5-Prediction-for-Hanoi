# Phát Biểu Bài Toán & Khung Mô Hình Hóa Toán Học

> **Đề tài:** Dự báo nồng độ bụi mịn $\text{PM}_{2.5}$ tại Hà Nội bằng Trí tuệ Nhân tạo  
> **Khoảng thời gian dự báo (Horizon):** $t + 24\text{ giờ}$ (Dự báo hồi quy đơn bước đa biến)  
> **Độ phân giải thời gian:** Chuỗi thời gian liên tục theo từng giờ ($\Delta t = 1\text{ giờ}$)

---

## 1. Phát Biểu Bài Toán

Bụi mịn $\text{PM}_{2.5}$ tại Hà Nội có đặc tính biến động phi tuyến mạnh mẽ theo mùa và theo giờ trong ngày, chịu ảnh hưởng đồng thời bởi các nguồn phát thải nội tại (giao thông, xây dựng, công nghiệp) và các điều kiện khí tượng khí quyển (nghịch nhiệt bề mặt, gió mùa Đông Bắc, độ ẩm cao).

Chúng tôi định nghĩa bài toán dưới dạng **bài toán hồi quy có giám sát trên chuỗi thời gian đa biến**:  
Tại mốc thời gian hiện tại $t$, dựa trên toàn bộ thông tin lịch sử về nồng độ ô nhiễm và các yếu tố khí tượng bề mặt thu thập được tính đến thời điểm $t$, mô hình cần dự báo chính xác nồng độ $\text{PM}_{2.5}$ tại thời điểm $t + 24\text{ giờ}$ trong tương lai.

Biểu diễn toán học:

$$\hat{y}_{t+24} = f\left(\mathbf{X}_{t}\right)$$

Trong đó:
- $\hat{y}_{t+24}$ là nồng độ khối lượng $\text{PM}_{2.5}$ ước lượng (đơn vị $\mu\text{g/m}^3$) tại thời điểm $t + 24\text{h}$.
- $\mathbf{X}_{t}$ là vectơ đặc trưng tổng hợp được xây dựng hoàn toàn từ các quan sát tại thời điểm $t' \le t$.

---

## 2. Tập Đặc Trưng Đầu Vào & Cơ Chế Nhân Quả

Để đảm bảo tính nhân quả và loại bỏ rò rỉ dữ liệu, toàn bộ các đặc trưng phải được trích xuất nghiêm ngặt từ quá khứ:

### 2.1. Nhóm đặc trưng trễ của PM2.5 (Historical Lags)
Đại diện cho quán tính khí quyển và hiện tượng tự tương quan chuỗi thời gian:
- $\text{pm25\_lag\_1}$: Nồng độ tại $t - 1\text{h}$ (quán tính tức thời).
- $\text{pm25\_lag\_3}$: Nồng độ tại $t - 3\text{h}$.
- $\text{pm25\_lag\_6}$: Nồng độ tại $t - 6\text{h}$ (chu kỳ buổi sáng/chiều).
- $\text{pm25\_lag\_12}$: Nồng độ tại $t - 12\text{h}$ (chu kỳ nửa ngày).
- $\text{pm25\_lag\_24}$: Nồng độ tại $t - 24\text{h}$ (chu kỳ lặp lại theo ngày).

### 2.2. Nhóm đặc trưng thống kê trượt (Rolling Statistics)
Đại diện cho xu hướng tích lũy và độ bất ổn định khí quyển ngắn hạn (áp dụng `shift(1)` để không rò rỉ điểm hiện tại):
- $\text{pm25\_rolling\_mean\_6}$, $\text{pm25\_rolling\_mean\_12}$, $\text{pm25\_rolling\_mean\_24}$: Giá trị trung bình trượt của $\text{PM}_{2.5}$ trong các cửa sổ 6h, 12h và 24h vừa qua.
- $\text{pm25\_rolling\_std\_24}$: Độ lệch chuẩn trượt 24h (đo lường độ biến thiên và xáo trộn khí quyển).

### 2.3. Nhóm biến khí tượng bề mặt tại thời điểm $t$
Thu thập từ nguồn ERA5 / Open-Meteo Historical Weather:
- **Nhiệt độ ($T$, $^\circ\text{C}$):** Ảnh hưởng đến sự đối lưu thẳng đứng và độ dày tầng biên khí quyển.
- **Độ ẩm tương đối ($RH$, $\%$):** Kích thích phản ứng ngưng tụ và tăng kích thước hạt ẩm hấp phụ.
- **Tốc độ gió ($WS$, $\text{m/s}$):** Động lực chính phát tán, vận chuyển và pha loãng chất ô nhiễm.
- **Hướng gió ($WD$, độ góc):** Chiều hướng vận chuyển khối khí; được phân rã thành hai thành phần liên tục $\sin(WD)$ và $\cos(WD)$.
- **Áp suất bề mặt ($P$, $\text{hPa}$):** Áp cao thường đi kèm tĩnh đọng khí quyển và sương mù gây tích tụ bụi.
- **Lượng mưa ($Precip$, $\text{mm}$):** Hiệu ứng rửa trôi (*Wet scavenging*) bụi mịn khỏi tầng không khí sát mặt đất.

### 2.4. Nhóm đặc trưng chu kỳ thời gian (Cyclical Temporal Features)
Đảm bảo tính liên tục của không gian thời gian (giờ 23 liền kề giờ 0):
$$\text{hour\_sin} = \sin\left(\frac{2\pi \cdot \text{hour}}{24}\right), \quad \text{hour\_cos} = \cos\left(\frac{2\pi \cdot \text{hour}}{24}\right)$$
$$\text{month\_sin} = \sin\left(\frac{2\pi \cdot \text{month}}{12}\right), \quad \text{month\_cos} = \cos\left(\frac{2\pi \cdot \text{month}}{12}\right)$$
$$\text{dow} = \text{Thứ trong tuần } [0-6] \text{ (Phân biệt ngày làm việc và cuối tuần)}$$

---

## 3. Quy Chuẩn Kỹ Thuật Ngăn Chặn Rò Rỉ Dữ Liệu (Anti-Leakage Protocol)

Rò rỉ dữ liệu (*Data Leakage*) là lỗi nghiêm trọng nhất trong dự báo chuỗi thời gian. Dự án áp dụng bộ quy tắc 3 lớp:

1. **Phân chia tập dữ liệu tuần tự theo thời gian (*Chronological Splitting*):**
   - **Tập Huấn luyện (Train):** 70% đầu tiên của chuỗi thời gian.
   - **Tập Thẩm định (Validation):** 15% tiếp theo (dùng cho tinh chỉnh siêu tham số và Early Stopping).
   - **Tập Kiểm tra (Test):** 15% thời gian tương lai độc lập (chỉ dùng cho đánh giá cuối cùng).
   - *Tuyệt đối cấm sử dụng `train_test_split` ngẫu nhiên.*
2. **Cô lập bộ chuẩn hóa (*Scaler Isolation*):**
   - Các phép biến đổi tỉ lệ (`StandardScaler`, `MinMaxScaler`) chỉ được thực hiện phương thức `.fit()` **duy nhất trên tập Train**.
   - Các tham số $(\mu, \sigma)$ đã học sẽ được đóng băng và áp dụng `.transform()` lên tập Validation và Test.
3. **Giới hạn thời gian trích xuất đặc trưng (*Causal Horizon Isolation*):**
   - Khi tính toán đặc trưng cho thời điểm $t$, không được phép sử dụng bất kỳ giá trị nào tại $t' > t$.
   - Trong mô hình cơ sở, không giả định trước dự báo thời tiết hoàn hảo của tương lai để tránh hiện tượng ảo tưởng độ chính xác.
