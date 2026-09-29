# Cẩm Nang Chuẩn Bị Vấn Đáp Bảo Vệ Đồ Án (Oral Defense / Viva)

> **Môn học:** Đồ án Cuối kỳ Trí tuệ Nhân tạo (*Artificial Intelligence Final Project*)  
> **Trọng số điểm:** 2.0 Điểm (Thuyết trình nhóm và vấn đáp cá nhân độc lập)  
> **Mục tiêu:** Trang bị cho từng thành viên khả năng tự tin giải trình cặn kẽ mọi quyết định kỹ thuật trước Hội đồng Chấm thi.

---

## 1. Tiêu Chuẩn Nắm Vững Kiến Thức Của Từng Thành Viên

Mỗi thành viên trong nhóm, bất kể đảm nhiệm vị trí nào, đều bắt buộc phải nắm vững:
- [ ] Sơ đồ luồng dữ liệu tổng thể từ khâu tải dữ liệu thô đến khi hiển thị kết quả trên Web Dashboard.
- [ ] Định nghĩa bài toán: Tại sao lại chọn đích dự báo là $PM_{2.5}(t + 24\text{h})$ và tại sao mô hình ngây thơ Persistence là bắt buộc.
- [ ] Cơ chế loại bỏ rò rỉ dữ liệu (*Data Leakage*): Phân chia chuỗi thời gian như thế nào? Bộ chuẩn hóa được fit ở đâu?
- [ ] Phần đóng góp kỹ thuật trực tiếp của bản thân trong mã nguồn Git và báo cáo.
- [ ] Ý nghĩa toán học của các độ đo: MAE, RMSE, $R^2$, và tại sao không dùng Accuracy trong bài toán hồi quy.
- [ ] Nguyên nhân vật lý khiến mô hình thường dự báo thấp hơn thực tế ở các đỉnh ô nhiễm cực đoan ($PM_{2.5} > 100\,\mu\text{g/m}^3$).
- [ ] Sự khác biệt cốt lõi giữa kết quả dự báo của mô hình học máy và thông báo cảnh báo ô nhiễm chính thức từ cơ quan quản lý nhà nước.

---

## 2. Ngân Hàng 15 Câu Hỏi Vấn Đáp Trọng Tâm Kèm Đáp Án Chuẩn

### Nhóm A: Bản Chất Vấn Đề & Động Lực Nghiên Cứu
**Câu 1: Tại sao nhóm lại chọn dự báo nồng độ liên tục PM2.5 ($\mu\text{g/m}^3$) thay vì phân loại chỉ số chất lượng không khí (AQI)?**  
*Trả lời:* AQI là một hàm biến đổi phi tuyến từng đoạn (*piecewise linear transformation*) từ nồng độ bụi sang các thang điểm quy ước. Việc dự báo nồng độ khối lượng liên tục giúp bảo toàn các biến động vật lý vi mô của khí quyển, loại bỏ sai số lượng tử hóa (*quantization error*), đồng thời cho phép người dùng tùy biến quy đổi sang bất kỳ chuẩn AQI nào (như QCVN 05:2023 của Việt Nam hay US EPA của Mỹ).

**Câu 2: Tại sao nhóm lại chọn khoảng thời gian dự báo là 24 giờ tiếp theo (Horizon = 24h)?**  
*Trả lời:* Dự báo trước 1 giờ có độ chính xác rất cao nhờ quán tính khí quyển, nhưng không mang lại giá trị thực tiễn cho cộng đồng vì thời gian quá ngắn để các trường học hoặc cơ quan quản lý đưa ra khuyến cáo. Ngược lại, dự báo trước 7 ngày tích lũy sai số phi tuyến khổng lồ nếu không sử dụng các mô hình động lực học khí quyển số trị phức tạp (NWP). Khoảng thời gian 24 giờ là điểm cân bằng tối ưu: vừa đủ lead-time cho công tác chuẩn bị bảo vệ sức khỏe, vừa nằm trong chu kỳ biến động ngày đêm lặp lại của thời tiết địa phương.

---

### Nhóm B: Kỹ Thuật Dữ Liệu & Chống Rò Rỉ Thời Gian
**Câu 3: Nhóm đã thực hiện những biện pháp kỹ thuật cụ thể nào để triệt tiêu hiện tượng rò rỉ dữ liệu (Data Leakage)?**  
*Trả lời:* Nhóm tuân thủ quy tắc 3 bước nghiêm ngặt:
1. *Phân chia tập dữ liệu:* Tuyệt đối không dùng `train_test_split` ngẫu nhiên. Dữ liệu được chia tuyến tính theo trục thời gian (Train: 70% quá khứ, Validation: 15% tiếp theo, Test: 15% tương lai độc lập).
2. *Kỹ nghệ đặc trưng nhân quả:* Mọi đặc trưng trễ (*lags*) và thống kê trượt (*rolling*) tại mốc $t$ chỉ được tính từ các dòng quan sát tại thời điểm $\le t$ thông qua thao tác dịch chuyển `shift(1)`.
3. *Đóng băng bộ chuẩn hóa:* Các tham số trung bình $\mu$ và độ lệch chuẩn $\sigma$ của `StandardScaler` chỉ được học (*fit*) duy nhất trên tập Train, sau đó áp dụng cố định lên Validation và Test.

**Câu 4: Tại sao không được phép điền số 0 hoặc giá trị trung bình vào các ô dữ liệu bị khuyết?**  
*Trả lời:* Trong khoa học môi trường, nồng độ $\text{PM}_{2.5} = 0\,\mu\text{g/m}^3$ đại diện cho môi trường chân không lý tưởng (hoàn toàn không thể xảy ra tại Hà Nội). Việc điền số 0 sẽ kéo tụt phân phối và làm sai lệch nghiêm trọng các trọng số hồi quy. Việc điền giá trị trung bình sẽ triệt tiêu phương sai và phá vỡ tính biến thiên chu kỳ ngày đêm. Nhóm chỉ áp dụng điền tiến (*forward-fill*) cho các khoảng khuyết vi mô $\le 2\text{ giờ}$ do trễ mạng cảm biến, và loại bỏ các cửa sổ chuỗi nếu gặp khoảng mất dữ liệu dài.

---

### Nhóm C: Thuật Toán AI & Tối Ưu Hóa Mô Hình
**Câu 5: Tại sao mô hình LightGBM lại cho kết quả cạnh tranh, thậm chí vượt trội hơn mạng học sâu LSTM trên tập dữ liệu này?**  
*Trả lời:* Đối với dữ liệu dạng bảng chuỗi thời gian kết hợp các biến khí tượng, việc kỹ nghệ đặc trưng tường minh (lags, rolling stats, cyclical encoding) đã cung cấp sẵn các mặt cắt phân chia phi tuyến tối ưu cho cây quyết định. Thuật toán Gradient Boosting tối ưu hóa trực tiếp trên các đặc trưng này rất nhanh và hiệu quả. Ngược lại, mạng nơ-ron LSTM đòi hỏi khối lượng dữ liệu khổng lồ để tự học các bộ lọc thời gian từ đầu, đồng thời rất dễ bị quá khớp (*overfitting*) trên tập dữ liệu môi trường quy mô vừa ($\approx 15.000$ dòng quan trắc).

**Câu 6: Tại sao mô hình Persistence Baseline lại bắt buộc phải có mặt trong báo cáo?**  
*Trả lời:* Nồng độ bụi mịn có tính tự tương quan rất cao với quá khứ gần ($r > 0.8$ tại lag 1h). Một mô hình học máy phức tạp có thể đạt hệ số xác định $R^2 = 0.65$ nhưng trên thực tế vẫn có thể dự báo kém hơn mô hình ngây thơ lấy giá trị hiện tại làm dự báo tương lai ($\hat{y}_{t+24} = y_t$). Mô hình Persistence đóng vai trò là "ngưỡng sàn khoa học", chứng minh rằng hệ thống AI thực sự học được mối quan hệ dự báo từ khí tượng chứ không chỉ đơn thuần khai thác quán tính số liệu.

**Câu 7: Nhóm đã tinh chỉnh siêu tham số như thế nào để tránh hiện tượng quá khớp (Overfitting)?**  
*Trả lời:* Không thực hiện tìm kiếm lưới khổng lồ bừa bãi. Nhóm thiết lập không gian tìm kiếm nhỏ, có giải thích vật lý và đánh giá hoàn toàn trên tập Validation (không đụng chạm vào tập Test). Đối với LightGBM, nhóm giới hạn độ sâu cây (`max_depth` từ 4 đến 8) và số lượng lá (`num_leaves` từ 15 đến 63) kết hợp với hệ số co (*shrinkage / learning_rate* $\approx 0.03 - 0.05$). Đối với LSTM, áp dụng kỹ thuật Dropout (0.2) và Early Stopping ngắt huấn luyện nếu validation loss không giảm sau 7 epochs.

---

### Nhóm D: Đánh Giá & Phân Tích Sai Số Phần Dư
**Câu 8: Tại sao nhóm lại sử dụng song song cả hai chỉ số MAE và RMSE?**  
*Trả lời:* MAE đo lường sai số tuyệt đối trung bình theo thang tuyến tính, phản ánh mức sai lệch điển hình mà người dùng cảm nhận hàng ngày ($\mu\text{g/m}^3$). Trong khi đó, RMSE bình phương các phần dư trước khi lấy căn bậc hai, do đó sẽ phạt rất nặng các điểm dự báo sai số lớn. Khi chênh lệch giữa RMSE và MAE càng cao, điều đó chứng tỏ mô hình đang gặp vấn đề với các điểm ngoại lai hoặc dự báo trượt rất xa trong những đợt ô nhiễm đột biến.

**Câu 9: Tại sao mô hình có xu hướng dự báo thấp hơn thực tế ở các đợt đỉnh ô nhiễm (Peak Episodes)?**  
*Trả lời:* Các đợt bùng phát ô nhiễm nghiêm trọng tại Hà Nội ($PM_{2.5} > 100\,\mu\text{g/m}^3$) thường do hiện tượng nghịch nhiệt bức xạ cực đoan vào ban đêm mùa đông kết hợp với lớp biên khí quyển bị nén chặt xuống dưới 200m. Các sự kiện này chỉ chiếm tỷ lệ rất nhỏ ($< 5\%$) trong tổng số mẫu quan sát. Hàm mất mát MSE có xu hướng tối ưu hóa cho đại đa số dữ liệu bình thường, kéo các dự báo về vùng trung bình của phân phối để giảm thiểu tổng sai số bình phương.

---

### Nhóm E: Triển Khai Thực Tế & Khía Cạnh Đạo Đức
**Câu 10: Dịch vụ FastAPI xử lý như thế nào nếu người dùng gửi yêu cầu dự báo nhưng thiếu dữ liệu thời tiết của vài giờ gần nhất?**  
*Trả lời:* Pipeline suy luận `PM25Forecaster` được lập trình với cơ chế phòng thủ đa tầng: nếu phát hiện thiếu dữ liệu khí tượng tức thời, module sẽ tự động kích hoạt chế độ dự phòng (*fallback*), sử dụng giá trị quan sát hợp lệ gần nhất hoặc giá trị thời tiết trung bình giờ đó theo lịch sử, đồng thời đính kèm trường cảnh báo `warning: meteorological fallback active` và mở rộng biên độ dải tin cậy trong payload JSON trả về.

**Câu 11: Sản phẩm này có thể dùng để thay thế trạm đo tiêu chuẩn của Nhà nước không?**  
*Trả lời:* Hoàn toàn không. Đây là hệ thống nghiên cứu học thuật phục vụ cảnh báo sớm mang tính tham khảo. Các trạm đo tiêu chuẩn quốc gia sử dụng phương pháp đo cân mẫu khối lượng trực tiếp (BAM / TEOM) được hiệu chuẩn vật lý nghiêm ngặt theo quy chuẩn QCVN. Mô hình AI dựa trên ước lượng thống kê và chỉ đóng vai trò công cụ hỗ trợ ra quyết định sớm.

---

### Nhóm F: Vấn Đáp Chuyên Sâu Từng Vị Trí Thành Viên
**Câu 12: (Hỏi Thành viên 1 - Data): Bạn đã xử lý vấn đề lệch múi giờ và căn chỉnh chuỗi quan trắc như thế nào?**  
*Trả lời:* Dữ liệu thô từ OpenAQ thường được đánh dấu theo chuẩn UTC (Z), trong khi dữ liệu thời tiết có thể ở giờ địa phương. Tôi đã dùng Pandas chuyển đổi tường minh toàn bộ về múi giờ chuẩn Việt Nam `Asia/Ho_Chi_Minh` (UTC+7). Sau đó, dùng `reindex(pd.date_range(..., freq='1h'))` để tạo một trục thời gian liên tục tuyệt đối, đảm bảo không bị nhảy cóc bước giờ nào.

**Câu 13: (Hỏi Thành viên 2 - Features): Tại sao bạn lại mã hóa giờ trong ngày bằng hàm sin và cos thay vì giữ nguyên số nguyên từ 0 đến 23?**  
*Trả lời:* Nếu để dạng số nguyên từ 0 đến 23, mô hình tuyến tính hoặc khoảng cách sẽ coi 23 giờ đêm và 0 giờ sáng là hai điểm cách xa nhau nhất (khoảng cách là 23). Tuy nhiên trong thực tế, 23h và 0h là hai mốc thời gian liền kề liên tục. Phép biến đổi lên đường tròn lượng giác 2 chiều $(\sin(2\pi h/24), \cos(2\pi h/24))$ giúp bảo toàn trọn vẹn tính liên tục chu kỳ này.

**Câu 14: (Hỏi Thành viên 3 - Classical ML): Biểu đồ SHAP Summary cho thấy tốc độ gió và độ ẩm ảnh hưởng thế nào đến nồng độ bụi?**  
*Trả lời:* Biểu đồ SHAP chỉ ra rằng tốc độ gió có giá trị SHAP âm mạnh khi đạt giá trị lớn ($> 3\text{ m/s}$), chứng minh gió lớn đóng vai trò xáo trộn và phát tán bụi tích tụ. Ngược lại, độ ẩm tương đối cao đi kèm với giá trị SHAP dương, phù hợp với nguyên lý vật lý: độ ẩm cao tạo điều kiện cho các hạt bụi hút ẩm trương nở và phản ứng hóa học thứ cấp hình thành sol khí ngưng tụ.

**Câu 15: (Hỏi Thành viên 4 & 5 - DL & Serving): Độ trễ suy luận (Inference Latency) của mô hình là bao nhiêu và có đáp ứng thời gian thực không?**  
*Trả lời:* Mô hình LightGBM thực hiện dự báo cho 1 mẫu chỉ mất khoảng $1.5\text{ ms}$, trong khi mô hình PyTorch LSTM mất khoảng $12\text{ ms}$ trên CPU thông thường. Cả hai đều vượt xa yêu cầu phản hồi thời gian thực ($< 100\text{ ms}$) của một dịch vụ web API tiêu chuẩn.
