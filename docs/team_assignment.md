# Ma Trận Phân Công Nhiệm Vụ Nhóm 5 Thành Viên

> **Môn học:** Đồ án Cuối kỳ Trí tuệ Nhân tạo (*Artificial Intelligence Final Project*)  
> **Quy mô nhóm:** 5 Sinh viên (Phân định chuyên môn hóa kỹ thuật + Trách nhiệm học thuật chung)  
> **Ánh xạ thang điểm:** Tiêu chí 1.1 trong Biểu điểm đánh giá (*Mô tả chi tiết chức năng và phân công nhiệm vụ nhóm*)

---

## 1. Bảng Phân Công Vai Trò Kỹ Thuật & Trách Nhiệm Học Thuật

| Thành viên | Vai trò Kỹ thuật Chính | Module & Issues Phụ trách | Phần Báo cáo PDF Đảm nhiệm | Slide Thuyết trình Phụ trách | Trọng tâm Vấn đáp Độc lập (Viva) |
|---|---|---|---|---|---|
| **Thành viên 1** | **Trưởng nhóm Kỹ thuật Dữ liệu** (*Data Engineering Lead*) | • `src/data/fetch_openaq.py`<br>• `src/data/fetch_weather.py`<br>• `src/data/clean_data.py`<br>• Issues #01, #03, #04, #16 | • Mục 4: Tập Dữ liệu & Xuất xứ<br>• Mục 5: Tiền xử lý & Kiểm toán Dữ liệu<br>• Đóng gói Tệp ZIP Nộp bài | • Slide 4: Quy trình Thu thập & Vệ sinh Dữ liệu | Quy trình nạp dữ liệu, cơ chế xử lý dữ liệu khuyết, kiểm toán logic vật lý, căn chỉnh lưới giờ liên tục |
| **Thành viên 2** | **Trưởng nhóm Kỹ nghệ Đặc trưng & Baseline** (*Feature & Baseline Lead*) | • `src/features/build_features.py`<br>• `src/features/split_data.py`<br>• `src/models/baseline.py`<br>• Issues #02, #05, #06, #14 | • Mục 2: Phát biểu Bài toán & Khung Toán học<br>• Mục 6: Kỹ nghệ Đặc trưng Chuỗi thời gian<br>• Mục 7: Phương pháp AI Đề xuất<br>• **Chủ biên Báo cáo PDF Cuối kỳ** | • Slide 3: Định nghĩa Bài toán<br>• Slide 5: Kỹ nghệ Đặc trưng Nhân quả | Kỹ thuật chống rò rỉ dữ liệu (*Data Leakage*), phân chia chuỗi thời gian tuyến tính, căn cứ chọn cửa sổ trễ, ý nghĩa mô hình Persistence |
| **Thành viên 3** | **Trưởng nhóm Học máy Cổ điển & SHAP** (*Classical ML & Explainability Lead*) | • `src/models/train_classical.py`<br>• `src/evaluation/explain.py`<br>• Issues #07, #10, #15 | • Mục 8: Phân tích Thuật toán Học máy<br>• Mục 9: Lựa chọn Siêu tham số Mô hình<br>• Mục 14: Giải thích Mô hình bằng Tree SHAP<br>• **Trưởng nhóm Thiết kế Slide Deck** | • Slide 6: Các Mô hình Học máy Đề xuất<br>• Slide 10: Minh bạch hóa Dự báo bằng SHAP | Bản chất toán học của thuật toán GBDT/Random Forest, căn cứ tinh chỉnh siêu tham số, phân tích vật lý khí tượng qua SHAP |
| **Thành viên 4** | **Trưởng nhóm Học sâu & Đánh giá Hiệu năng** (*Deep Learning & Evaluation Lead*) | • `src/models/train_lstm.py`<br>• `src/evaluation/metrics.py`<br>• Issues #08, #09 | • Mục 11: Thiết kế & Bố trí Thực nghiệm<br>• Mục 12: Bảng Kết quả Thực nghiệm<br>• Mục 13: So sánh Đối chứng & Phân tích Phần dư | • Slide 8: Kết quả Thực nghiệm & Đối sánh<br>• Slide 9: Phân tích Sai số Đợt Ô nhiễm Cao | Kiến trúc mạng nơ-ron hồi quy LSTM, hàm mất mát và tối ưu hóa AdamW, cơ chế Early Stopping, lý giải nguyên nhân lệch ở các đỉnh ô nhiễm |
| **Thành viên 5** | **Trưởng nhóm Đóng gói Ứng dụng & Triển khai** (*Application & Deployment Lead*) | • `src/inference/predict.py`<br>• `api/main.py` & `schemas.py`<br>• `app/streamlit_app.py`<br>• Issues #11, #12, #13 | • Mục 10: Sơ đồ Kiến trúc Hệ thống Tổng thể<br>• Mục 15: Ứng dụng Thực tế & Giao diện Demo<br>• Mục 16: Giới hạn Hệ thống & Khía cạnh Đạo đức | • Slide 7: Kiến trúc Hệ thống Tổng thể<br>• Slide 11: Demo Sản phẩm Tương tác | Kiến trúc phần mềm phân tầng, độ trễ suy luận thời gian thực, thiết kế API RESTful bằng FastAPI, xử lý ngoại lệ khi thiếu dữ liệu đầu vào |

---

## 2. Tiến Độ Phối Hợp Tuần Tự (Lộ Trình 6 Tuần)

| Tuần | Cột mốc (Milestone) | Thành viên 1 | Thành viên 2 | Thành viên 3 | Thành viên 4 | Thành viên 5 |
|:---:|---|---|---|---|---|---|
| **T1** | **M0, M1, M2** | Thiết lập repo & viết script nạp OpenAQ (#01, #03) | Đặc tả toán học & quy tắc chống rò rỉ (#02) | Khảo sát tài liệu về mô hình GBDT cho chuỗi thời gian | Khảo sát tài liệu về kiến trúc mạng LSTM | Phác thảo cấu trúc schema API & luồng dữ liệu |
| **T2** | **M3, M4, M5** | Làm sạch tất định & reindex lưới giờ liên tục (#04) | Tạo lags, rolling stats & phân chia tập 70/15/15 (#05) | Kiểm tra tương quan đặc trưng & phân phối dữ liệu | Chuẩn bị bộ nạp dữ liệu tensor 3D cho PyTorch | Thiết kế giao diện khung (*Wireframe*) cho Streamlit |
| **T3** | **M5** | Kiểm tra tính ổn định của pipeline nạp dữ liệu | Huấn luyện mô hình cơ sở Persistence & Ridge (#06) | Huấn luyện & tinh chỉnh LightGBM, Random Forest (#07) | Thiết lập vòng lặp huấn luyện LSTM cơ bản | Xây dựng khung API FastAPI với dữ liệu giả lập |
| **T4** | **M6, M7** | Kiểm toán trôi dạt dữ liệu (*Data Drift*) theo mùa | Tài liệu hóa ma trận đặc trưng & độ đo | Tính toán giá trị Tree SHAP & xuất biểu đồ (#10) | Tối ưu hóa siêu tham số LSTM & lập bảng so sánh (#08, #09) | Kết nối API FastAPI với mô hình tạm thời |
| **T5** | **M8, M9** | Viết bản thảo Báo cáo Mục 4 & 5 | Viết bản thảo Báo cáo Mục 2, 6, 7 (Chủ biên) | Viết bản thảo Báo cáo Mục 8, 9, 14 | Viết bản thảo Báo cáo Mục 11, 12, 13 | Đóng gói `PM25Forecaster`, hoàn thiện API & Streamlit (#11, #12, #13) |
| **T6** | **M10, M11** | Kiểm toán môi trường sạch & đóng gói ZIP (#16) | Tổng hợp & rà soát toàn bộ Báo cáo PDF (#14) | Hoàn thiện bộ Slide thuyết trình 10–12 trang (#15) | Xuất các biểu đồ ấn phẩm & phân tích sai số đỉnh | Kiểm thử tải giao diện web & tổ chức buổi vấn đáp thử (#16) |

---

## 3. Giải Trình Về Quy Mô Nhóm 5 Thành Viên

> **Ghi chú gửi Hội đồng Đánh giá & Giảng viên Hướng dẫn:**  
> Trong khi đề cương chung khuyến nghị nhóm tối đa 3 sinh viên, nhóm đồ án này được thành lập với **5 thành viên** theo phân công thực tế của lớp học. Để đảm bảo tính công bằng và sự nghiêm ngặt trong đánh giá học thuật, khối lượng công việc của đề tài đã được mở rộng tương ứng trên 5 phân hệ kỹ thuật độc lập:
> 1. Kỹ thuật Dữ liệu, Kiểm toán Chất lượng & Làm sạch Chuỗi thời gian.
> 2. Kỹ nghệ Đặc trưng Causal, Toán học Mô hình & Baseline Đối chứng.
> 3. Mô hình Cây Tăng cường Gradient & Minh bạch hóa Khí quyển (SHAP).
> 4. Mô hình Học sâu Hồi quy Chuỗi Đa bước (PyTorch LSTM) & Đánh giá Phần dư.
> 5. Kiến trúc Đóng gói Độc lập, Dịch vụ REST API & Giao diện Dashboard Tương tác.
>
> Toàn bộ 5 thành viên đều có lịch sử commit Git rõ ràng trên kho lưu trữ, đồng thời chịu trách nhiệm trực tiếp cho một phân hệ mã nguồn và các chương tương ứng trong báo cáo, đảm bảo làm chủ 100% nội dung khi vấn đáp bảo vệ cá nhân độc lập.
