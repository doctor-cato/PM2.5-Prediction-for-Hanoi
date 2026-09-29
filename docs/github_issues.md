# Danh Mục 22 GitHub Issues Chi Tiết

> **Đề tài:** Dự báo nồng độ bụi mịn $\text{PM}_{2.5}$ tại Hà Nội bằng Trí tuệ Nhân tạo  
> **Quy mô:** 22 Issues kỹ thuật chuẩn mực (#01 – #22) phân bổ trên 7 Milestones chuẩn (M0 – M6)  
> **Quy ước đặt tên:** Tuân thủ chuẩn Conventional Commits (`feat`, `chore`, `docs`, `fix`)

---

## Milestone 0: Project Foundation (Tuần 1)

### Issue #01
- **Tiêu đề:** `chore(setup): rà soát yêu cầu môn học, cấu hình môi trường và kiểm toán repo`
- **Mục tiêu:** Thiết lập khung thư mục chuẩn, cố định phiên bản thư viện và cấu hình Git ban đầu.
- **Phạm vi:** Thư mục, `.gitignore`, `requirements.txt`, script kiểm tra nạp thư viện.
- **Nhiệm vụ:**
  - [ ] Khởi tạo khung thư mục module hóa chuẩn (`src/`, `data/`, `notebooks/`, `models/`, `api/`, `app/`, `docs/`, `reports/`).
  - [ ] Cố định phiên bản thư viện trong `requirements.txt` tương thích Python 3.10+.
  - [ ] Viết script kiểm thử môi trường xác nhận nạp thành công toàn bộ thư viện trên Windows/Linux.
- **Sản phẩm đầu ra:** Thư mục hoàn chỉnh, `requirements.txt`, script kiểm thử môi trường.
- **Phụ thuộc:** Không
- **Tiêu chí nghiệm thu:**
  - [ ] Lệnh `pip install -r requirements.txt` cài đặt thành công không lỗi.
  - [ ] Script kiểm thử môi trường chạy với mã thoát `0`.
- **Người phụ trách:** Huy (@doctor-cato) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 0 | **Labels:** `planning`, `high-priority`

---

### Issue #02
- **Tiêu đề:** `docs(spec): đặc tả toán học bài toán dự báo và quy chuẩn chống rò rỉ dữ liệu`
- **Mục tiêu:** Xác lập định dạng toán học bài toán dự báo $t+24\text{h}$, danh mục đặc trưng nhân quả và chốt chặn chống rò rỉ dữ liệu.
- **Phạm vi:** Tài liệu `docs/problem_definition.md`.
- **Nhiệm vụ:**
  - [ ] Định nghĩa biến mục tiêu: $y(t) = PM_{2.5}(t + 24\text{h})$.
  - [ ] Quy định các biến đầu vào: Lags ($t-1$ đến $t-24$), thống kê trượt, biến khí tượng, $\sin/\cos$ thời gian.
  - [ ] Xây dựng checklist 3 nguyên tắc chống rò rỉ dữ liệu (chia tập theo thời gian, fit scaler duy nhất trên Train, không dùng tương lai).
- **Sản phẩm đầu ra:** `docs/problem_definition.md` đã phê duyệt.
- **Phụ thuộc:** #01
- **Tiêu chí nghiệm thu:**
  - [ ] Cả 5 thành viên thẩm định và thống nhất công thức toán học.
  - [ ] Quy tắc rò rỉ dữ liệu được đặc tả rõ ràng, không có ngoại lệ.
- **Người phụ trách:** Khương (@lekhuong123456798-cpu) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 0 | **Labels:** `planning`, `documentation`

---

### Issue #03
- **Tiêu đề:** `docs(arch): hoàn thiện sơ đồ kiến trúc hệ thống và ma trận phân công nhóm 5 thành viên`
- **Mục tiêu:** Xây dựng sơ đồ kiến trúc hệ thống phân tầng và phân định trách nhiệm cân bằng cho 5 thành viên.
- **Phạm vi:** `docs/architecture.md`, `docs/team_assignment.md`, `README.md`.
- **Nhiệm vụ:**
  - [ ] Vẽ sơ đồ luồng dữ liệu kiến trúc Mermaid từ dữ liệu thô đến API và Dashboard.
  - [ ] Lập bảng ma trận phân công 5 thành viên: mỗi người nắm 1 module code + 1 phần báo cáo/slide + 1 chuyên đề vấn đáp Viva.
  - [ ] Thêm ghi chú giải trình gửi hội đồng về quy mô nhóm 5 sinh viên.
- **Sản phẩm đầu ra:** `docs/architecture.md`, `docs/team_assignment.md`.
- **Phụ thuộc:** #01, #02
- **Tiêu chí nghiệm thu:**
  - [ ] Không có thành viên nào chỉ làm tài liệu mà không viết code.
  - [ ] Sơ đồ kiến trúc thể hiện rõ ràng các tầng giao tiếp.
- **Người phụ trách:** Huy (@doctor-cato) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 0 | **Labels:** `planning`, `documentation`

---

## Milestone 1: Problem Definition & Data Foundation (Tuần 1)

### Issue #04
- **Tiêu đề:** `docs(data): xác lập khế ước dữ liệu với dự án Khoa học Dữ liệu upstream`
- **Mục tiêu:** Định nghĩa chính xác cấu trúc dữ liệu mà dự án AI kỳ vọng tiếp nhận từ dự án Data Science tiền đề.
- **Phạm vi:** Đặc tả giao diện dữ liệu trung lập (Canonical Schema).
- **Nhiệm vụ:**
  - [ ] Khớp nối 11 trường canonical từ upstream (`timestamp`, `station_id`, `pm25`, `pm10`, 6 biến thời tiết, `location`).
  - [ ] Xác lập múi giờ chuẩn bắt buộc `Asia/Ho_Chi_Minh` (UTC+7).
  - [ ] Khóa các quy ước về dữ liệu khuyết (không điền 0 bừa bãi, bóc trần `-999`).
- **Sản phẩm đầu ra:** Phần đặc tả khế ước dữ liệu trong `docs/data_dictionary.md`.
- **Phụ thuộc:** #02
- **Tiêu chí nghiệm thu:**
  - [ ] Tên cột, kiểu dữ liệu, đơn vị đo chuẩn khớp 100% với Canonical Schema của upstream repo.
- **Người phụ trách:** Huy (@doctor-cato) | **Độ ưu tiên:** P1 | **Milestone:** Milestone 1 | **Labels:** `data`, `documentation`

---

### Issue #05
- **Tiêu đề:** `feat(data): xây dựng pipeline thu thập dữ liệu tự động (OpenAQ + Open-Meteo)`
- **Mục tiêu:** Thu thập dữ liệu lịch sử quan trắc bụi mịn và thời tiết bề mặt giai đoạn 2022–2024 tại Hà Nội.
- **Phạm vi:** `src/data/fetch_openaq.py`, `src/data/fetch_weather.py`.
- **Nhiệm vụ:**
  - [ ] Viết adapter gọi OpenAQ REST API lấy dữ liệu trạm Đại sứ quán Hoa Kỳ tại Hà Nội.
  - [ ] Viết adapter gọi Open-Meteo Historical Weather API lấy dữ liệu tái phân tích ERA5.
  - [ ] Lưu trữ các tệp thô bất biến vào `data/raw/` dưới định dạng Snappy Parquet.
- **Sản phẩm đầu ra:** Các module nạp dữ liệu và tệp `data/raw/*.parquet`.
- **Phụ thuộc:** #04
- **Tiêu chí nghiệm thu:**
  - [ ] Tải về thành công $\ge 15.000$ dòng quan trắc theo giờ.
  - [ ] Script có tính tiền định và cơ chế tự động thử lại khi mất mạng.
- **Người phụ trách:** Huy (@doctor-cato) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 1 | **Labels:** `data`, `high-priority`

---

### Issue #06
- **Tiêu đề:** `feat(data): kiểm toán chất lượng dữ liệu và căn chỉnh chuỗi thời gian liên tục 1 giờ`
- **Mục tiêu:** Phát hiện bất thường cảm biến, lọc logic vật lý và tạo chuỗi thời gian liên tục không đứt gãy.
- **Phạm vi:** `src/data/clean_data.py`, `notebooks/01_data_audit_and_prep.ipynb`.
- **Nhiệm vụ:**
  - [ ] Kiểm tra ràng buộc vật lý: $PM_{2.5} \le PM_{10} + 1.0$; $RH \in [0, 100\%]$; áp suất $\in [900, 1100]\text{ hPa}$.
  - [ ] Chuyển đổi mã lỗi cảm biến (`-999`, `-9999`) thành `np.nan`.
  - [ ] Reindex chuỗi thời gian về lưới giờ liên tục (`freq='1h'`). Điền tiến (*forward-fill*) cho các khoảng khuyết vi mô $\le 2\text{h}$; giữ nguyên `NaN` với khoảng khuyết lớn.
  - [ ] Xuất dữ liệu sạch tích hợp sang `data/interim/canonical_cleaned.parquet`.
- **Sản phẩm đầu ra:** Module làm sạch, notebook kiểm toán chất lượng và tệp interim parquet.
- **Phụ thuộc:** #05
- **Tiêu chí nghiệm thu:**
  - [ ] Trục thời gian liên tục 100%, không trùng lặp timestamp.
  - [ ] Có Cleaning Log ghi nhận số lượng bản ghi bị xử lý.
- **Người phụ trách:** Huy (@doctor-cato) | **Độ ưu tiên:** P1 | **Milestone:** Milestone 1 | **Labels:** `data`

---

## Milestone 2: Data Preparation & Feature Engineering (Tuần 2)

### Issue #07
- **Tiêu đề:** `feat(features): xây dựng biến mục tiêu dự báo PM2.5 trước 24 giờ (t + 24h)`
- **Mục tiêu:** Tạo cột mục tiêu hồi quy giám sát cho bước dự báo 24 giờ tiếp theo.
- **Phạm vi:** `src/features/build_features.py`.
- **Nhiệm vụ:**
  - [ ] Tạo cột mục tiêu: `target = pm25.shift(-24)`.
  - [ ] Loại bỏ các dòng cuối chuỗi không có nhãn tương lai do vượt quá biên dữ liệu.
  - [ ] Kiểm toán đảm bảo không có sự xô lệch mốc thời gian giữa biến giải thích và biến mục tiêu.
- **Sản phẩm đầu ra:** Hàm tạo mục tiêu trong `src/features/build_features.py`.
- **Phụ thuộc:** #06
- **Tiêu chí nghiệm thu:**
  - [ ] Dòng $t$ chứa giá trị mục tiêu chính xác bằng nồng độ $PM_{2.5}$ thực tế tại dòng $t+24\text{h}$.
- **Người phụ trách:** Khương (@lekhuong123456798-cpu) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 2 | **Labels:** `feature-engineering`, `high-priority`

---

### Issue #08
- **Tiêu đề:** `feat(features): xây dựng pipeline kỹ nghệ đặc trưng nhân quả (Lags, Rolling, Sin/Cos)`
- **Mục tiêu:** Sinh toàn bộ các đặc trưng dự báo dựa hoàn toàn vào dữ liệu quá khứ.
- **Phạm vi:** `src/features/build_features.py`, `notebooks/02_feature_engineering.ipynb`.
- **Nhiệm vụ:**
  - [ ] Tạo các đặc trưng trễ: $PM_{2.5}(t-1), PM_{2.5}(t-3), PM_{2.5}(t-6), PM_{2.5}(t-12), PM_{2.5}(t-24)$.
  - [ ] Tạo các thống kê trượt: Trung bình và độ lệch chuẩn trượt trên cửa sổ 6h, 12h, 24h (dùng `shift(1)`).
  - [ ] Mã hóa chu kỳ lượng giác: $\sin/\cos$ của giờ trong ngày và tháng trong năm.
  - [ ] Phân rã hướng gió thành thành phần $\sin(WD)$ và $\cos(WD)$.
- **Sản phẩm đầu ra:** Pipeline tạo đặc trưng hoàn chỉnh trong `src/features/build_features.py`.
- **Phụ thuộc:** #07
- **Tiêu chí nghiệm thu:**
  - [ ] Toàn bộ đặc trưng tại thời điểm $t$ chỉ phụ thuộc vào quan sát $\le t$.
  - [ ] Không sinh ra lỗi vô tận hoặc chia cho 0.
- **Người phụ trách:** Khương (@lekhuong123456798-cpu) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 2 | **Labels:** `feature-engineering`, `high-priority`

---

### Issue #09
- **Tiêu đề:** `feat(features): phân chia tập Train/Val/Test theo thời gian và cô lập bộ chuẩn hóa`
- **Mục tiêu:** Phân chia ma trận dữ liệu theo trật tự thời gian tuyến tính và đóng gói bộ chuẩn hóa không rò rỉ.
- **Phạm vi:** `src/features/split_data.py`.
- **Nhiệm vụ:**
  - [ ] Phân chia chuỗi thời gian: 70% Train (quá khứ) $\rightarrow$ 15% Validation $\rightarrow$ 15% Test (tương lai độc lập).
  - [ ] Huấn luyện `StandardScaler` duy nhất trên tập Train; áp dụng `.transform()` lên Validation và Test.
  - [ ] Lưu các mảng dữ liệu đã chuẩn hóa vào `data/processed/` và lưu `models/scaler.pkl`.
- **Sản phẩm đầu ra:** `src/features/split_data.py`, các tệp processed parquet và `scaler.pkl`.
- **Phụ thuộc:** #08
- **Tiêu chí nghiệm thu:**
  - [ ] Tập Test hoàn toàn nằm sau tập Validation và Train theo thời gian.
  - [ ] Tham số $\mu, \sigma$ của Scaler không chứa bất kỳ thông tin nào từ tập Validation hay Test.
- **Người phụ trách:** Khương (@lekhuong123456798-cpu) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 2 | **Labels:** `feature-engineering`, `high-priority`

---

### Issue #10
- **Tiêu đề:** `chore(audit): kiểm toán độc lập triệt tiêu rò rỉ dữ liệu và tính tiền định (Seed 42)`
- **Mục tiêu:** Chạy kịch bản kiểm tra tự động phát hiện rò rỉ dữ liệu và kiểm chứng tính tái lập.
- **Phạm vi:** Tài liệu phương pháp luận và kiểm toán `docs/methodology.md`.
- **Nhiệm vụ:**
  - [ ] Kiểm toán ngẫu nhiên 100 dòng: xác nhận đặc trưng tại dòng $k$ không biến thiên khi giá trị nhãn tại $k+24$ bị thay đổi.
  - [ ] Cố định `random_state=42` xuyên suốt toàn bộ các phép biến đổi ngẫu nhiên.
  - [ ] Lập biên bản kiểm toán rò rỉ dữ liệu lưu vào `docs/methodology.md`.
- **Sản phẩm đầu ra:** Báo cáo kiểm toán rò rỉ dữ liệu trong tài liệu phương pháp luận.
- **Phụ thuộc:** #09
- **Tiêu chí nghiệm thu:**
  - [ ] 0% dấu hiệu rò rỉ dữ liệu từ tương lai vào quá khứ.
  - [ ] Chạy lại notebook cho ra kết quả trùng khớp từng chữ số thập phân.
- **Người phụ trách:** Khánh (@nguyenphanminhkhanh9a-netizen) | **Độ ưu tiên:** P1 | **Milestone:** Milestone 2 | **Labels:** `evaluation`, `feature-engineering`

---

## Milestone 3: Baseline & Classical Machine Learning (Tuần 3)

### Issue #11
- **Tiêu đề:** `feat(models): xây dựng mô hình cơ sở Persistence và hồi quy tuyến tính Ridge`
- **Mục tiêu:** Thiết lập các mốc hiệu năng sàn mà mọi mô hình học máy phức tạp phải vượt qua.
- **Phạm vi:** `src/models/baseline.py`, `notebooks/03_baseline_and_classical.ipynb`.
- **Nhiệm vụ:**
  - [ ] Xây dựng mô hình Naive Persistence Baseline: $\hat{y}(t+24) = y(t)$.
  - [ ] Xây dựng mô hình 24-Hour Seasonal Persistence: $\hat{y}(t+24) = y(t-24)$.
  - [ ] Huấn luyện mô hình hồi quy tuyến tính điều hòa Ridge Regression với tham số $\alpha$ tinh chỉnh trên Validation.
  - [ ] Ghi nhận MAE, RMSE, $R^2$ trên tập Validation và Test vào bảng thực nghiệm.
- **Sản phẩm đầu ra:** `src/models/baseline.py`, kết quả đối chứng cơ sở.
- **Phụ thuộc:** #09
- **Tiêu chí nghiệm thu:**
  - [ ] Baseline chạy độc lập, cho kết quả benchmark ổn định để làm căn cứ so sánh.
- **Người phụ trách:** Khương (@lekhuong123456798-cpu) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 3 | **Labels:** `baseline`, `high-priority`

---

### Issue #12
- **Tiêu đề:** `feat(models): triển khai mô hình học máy dạng cây (Random Forest & LightGBM)`
- **Mục tiêu:** Xây dựng và huấn luyện các mô hình cây quyết định tăng cường gradient trên ma trận đặc trưng.
- **Phạm vi:** `src/models/train_classical.py`.
- **Nhiệm vụ:**
  - [ ] Xây dựng pipeline huấn luyện cho Random Forest Regressor và LightGBM Regressor.
  - [ ] Thiết lập không gian siêu tham số có giải thích vật lý (`n_estimators`, `max_depth`, `learning_rate`, `num_leaves`).
  - [ ] Lưu các trọng số mô hình tốt nhất vào `models/champion_classical.joblib`.
- **Sản phẩm đầu ra:** Module huấn luyện cây và tệp mô hình đã lưu.
- **Phụ thuộc:** #11
- **Tiêu chí nghiệm thu:**
  - [ ] Mô hình LightGBM đánh bại rõ rệt mô hình Persistence Baseline trên tập Validation.
- **Người phụ trách:** Khánh (@nguyenphanminhkhanh9a-netizen) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 3 | **Labels:** `machine-learning`, `high-priority`

---

### Issue #13
- **Tiêu đề:** `feat(models): thực nghiệm triệt tiêu đặc trưng và tối ưu hóa siêu tham số trên Validation`
- **Mục tiêu:** Định lượng giá trị đóng góp của từng nhóm đặc trưng và lựa chọn siêu tham số tối ưu hoàn toàn trên Train/Val.
- **Phạm vi:** `notebooks/03_baseline_and_classical.ipynb`, `docs/experiments.md`.
- **Nhiệm vụ:**
  - [ ] Chạy thực nghiệm Feature Ablation: (1) Chỉ dùng Lags $PM_{2.5}$ vs. (2) Lags + Khí tượng vs. (3) Toàn bộ đặc trưng.
  - [ ] Tối ưu hóa siêu tham số bằng Validation Search (tuyệt đối không đụng vào tập Test).
  - [ ] Ghi lại thời gian huấn luyện và độ trễ suy luận trên 1.000 mẫu.
- **Sản phẩm đầu ra:** Nhật ký thực nghiệm hoàn chỉnh tại `docs/experiments.md`.
- **Phụ thuộc:** #12
- **Tiêu chí nghiệm thu:**
  - [ ] Chứng minh bằng số liệu thực nghiệm: Thêm biến thời tiết giúp cải thiện MAE so với chỉ dùng nồng độ bụi quá khứ.
- **Người phụ trách:** Khánh (@nguyenphanminhkhanh9a-netizen) | **Độ ưu tiên:** P1 | **Milestone:** Milestone 3 | **Labels:** `machine-learning`, `evaluation`

---

## Milestone 4: Deep Learning & Model Evaluation (Tuần 4)

### Issue #14
- **Tiêu đề:** `feat(models): phát triển mô hình chuỗi sâu PyTorch LSTM và Early Stopping`
- **Mục tiêu:** Xây dựng mạng nơ-ron hồi quy chuỗi sâu (LSTM) với cửa sổ trượt 24 giờ để nắm bắt động lực thời gian.
- **Phạm vi:** `src/models/train_lstm.py`, `notebooks/04_deep_learning_lstm.ipynb`.
- **Nhiệm vụ:**
  - [ ] Xây dựng lớp PyTorch `Dataset` và `DataLoader` tạo tensor trượt 3D `(batch_size, 24, n_features)`.
  - [ ] Thiết kế kiến trúc 2 tầng LSTM có Dropout (0.2) và lớp Linear xuất ra dự báo điểm $t+24\text{h}$.
  - [ ] Viết vòng lặp huấn luyện với AdamW, MSE Loss, Cosine Annealing scheduler và Early Stopping theo dõi validation loss.
  - [ ] Lưu checkpoint trọng số tốt nhất vào `models/lstm_best.pt`.
- **Sản phẩm đầu ra:** `src/models/train_lstm.py`, notebook huấn luyện và tệp checkpoint PyTorch.
- **Phụ thuộc:** #09
- **Tiêu chí nghiệm thu:**
  - [ ] Đồ thị mất mát hội tụ ổn định, Early Stopping kích hoạt thành công khi validation loss ngừng cải thiện.
- **Người phụ trách:** Hưng (@ViolaPeracia) | **Độ ưu tiên:** P1 | **Milestone:** Milestone 4 | **Labels:** `deep-learning`

---

### Issue #15
- **Tiêu đề:** `feat(eval): đánh giá đối sánh toàn diện trên tập Test và phân tích sai số đỉnh ô nhiễm`
- **Mục tiêu:** Mở niêm phong tập Test độc lập, đo đạc chuẩn mực toàn bộ mô hình và kiểm toán sai số các đợt nghịch nhiệt.
- **Phạm vi:** `src/evaluation/metrics.py`, `notebooks/05_evaluation_and_shap.ipynb`.
- **Nhiệm vụ:**
  - [ ] Tính toán bộ ba độ đo chuẩn: MAE, RMSE, $R^2$, sMAPE trên tập Test cho toàn bộ 5 mô hình: Persistence, Ridge, Random Forest, LightGBM, LSTM.
  - [ ] Vẽ biểu đồ đường Thực tế vs. Dự báo trên chuỗi thời gian thử nghiệm.
  - [ ] Kiểm toán sai số chuyên sâu trong các đợt bùng phát ô nhiễm ($PM_{2.5} > 100\,\mu\text{g/m}^3$) và giải thích nguyên nhân khí tượng.
- **Sản phẩm đầu ra:** Bảng tổng hợp đối sánh độ đo, đồ thị so sánh lưu tại `figures/model_comparison.png`.
- **Phụ thuộc:** #11, #13, #14
- **Tiêu chí nghiệm thu:**
  - [ ] Bảng số liệu trung thực 100%, không bịa đặt kết quả; có phân tích nguyên nhân tại sao mô hình lệch ở đỉnh ô nhiễm.
- **Người phụ trách:** Hưng (@ViolaPeracia) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 4 | **Labels:** `evaluation`, `high-priority`

---

### Issue #16
- **Tiêu đề:** `feat(eval): minh bạch hóa mô hình và giải thích đóng góp khí tượng bằng Tree SHAP`
- **Mục tiêu:** Định lượng mức độ đóng góp của từng yếu tố thời tiết và lịch sử bụi mịn vào kết quả dự báo của LightGBM.
- **Phạm vi:** `src/evaluation/explain.py`, `notebooks/05_evaluation_and_shap.ipynb`.
- **Nhiệm vụ:**
  - [ ] Áp dụng `shap.TreeExplainer` lên mô hình LightGBM tốt nhất.
  - [ ] Xuất biểu đồ ong vò vẽ SHAP Summary Beeswarm Plot và biểu đồ Feature Importance Bar Plot.
  - [ ] Giải thích ý nghĩa vật lý: Tại sao tốc độ gió cao làm giảm dự báo nồng độ bụi? Độ ẩm cao tác động thế nào?
- **Sản phẩm đầu ra:** `src/evaluation/explain.py`, biểu đồ `figures/shap_summary.png`.
- **Phụ thuộc:** #13, #15
- **Tiêu chí nghiệm thu:**
  - [ ] Diễn giải rõ ràng tác động của ít nhất 5 đặc trưng quan trọng nhất; không tuyên bố quá mức rằng SHAP chứng minh quan hệ nhân quả tuyệt đối.
- **Người phụ trách:** Khánh (@nguyenphanminhkhanh9a-netizen) | **Độ ưu tiên:** P2 | **Milestone:** Milestone 4 | **Labels:** `evaluation`

---

## Milestone 5: Inference, API & Demo (Tuần 5)

### Issue #17
- **Tiêu đề:** `feat(inference): đóng gói engine suy luận PM25Forecaster độc lập`
- **Mục tiêu:** Tạo một module suy luận đóng gói duy nhất, có khả năng nhận dữ liệu thô gần nhất và trả về dự báo sau 24h.
- **Phạm vi:** `src/inference/predict.py`.
- **Nhiệm vụ:**
  - [ ] Xây dựng lớp `PM25Forecaster` nạp mô hình quán quân và `scaler.pkl`.
  - [ ] Tích hợp kiểm tra tính hợp lệ dữ liệu vào, tự động xử lý thiếu trường và tạo đặc trưng tức thời.
  - [ ] Trả về kết quả dự báo điểm kèm khoảng tin cậy ước tính ($\pm 1.96 \cdot \text{RMSE}$).
- **Sản phẩm đầu ra:** `src/inference/predict.py`.
- **Phụ thuộc:** #15
- **Tiêu chí nghiệm thu:**
  - [ ] Một lệnh gọi `forecaster.predict(df_recent)` thực thi trong thời gian $< 50\text{ ms}$.
- **Người phụ trách:** Hùng (@Izuki-1780N) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 5 | **Labels:** `deployment`, `high-priority`

---

### Issue #18
- **Tiêu đề:** `feat(api): xây dựng dịch vụ REST API bằng FastAPI (POST /predict)`
- **Mục tiêu:** Cung cấp giao diện dịch vụ web chuẩn mực, phục vụ tích hợp thời gian thực.
- **Phạm vi:** `api/main.py`, `api/schemas.py`.
- **Nhiệm vụ:**
  - [ ] Viết API bằng FastAPI với các endpoint: `GET /health`, `GET /model-info`, `POST /predict`.
  - [ ] Định nghĩa Pydantic Schemas kiểm tra chặt chẽ kiểu dữ liệu và giới hạn vật lý của thông số khí tượng.
  - [ ] Thiết lập tài liệu Swagger UI tự động tại `/docs`.
- **Sản phẩm đầu ra:** Dịch vụ API hoàn chỉnh tại `api/`.
- **Phụ thuộc:** #17
- **Tiêu chí nghiệm thu:**
  - [ ] Endpoint `/predict` phản hồi mã HTTP 200 kèm JSON kết quả khi payload hợp lệ; trả về HTTP 422 khi dữ liệu sai định dạng.
- **Người phụ trách:** Hùng (@Izuki-1780N) | **Độ ưu tiên:** P1 | **Milestone:** Milestone 5 | **Labels:** `deployment`

---

### Issue #19
- **Tiêu đề:** `feat(app): phát triển Web Dashboard tương tác bằng Streamlit`
- **Mục tiêu:** Cung cấp giao diện trực quan sinh động cho người dùng và hội đồng chấm thi trải nghiệm mô hình.
- **Phạm vi:** `app/streamlit_app.py`.
- **Nhiệm vụ:**
  - [ ] Thiết kế thẻ thông số hiện tại (nồng độ $\text{PM}_{2.5}$, phân loại mức độ ô nhiễm, nhiệt độ, tốc độ gió).
  - [ ] Vẽ biểu đồ đường dự báo chuỗi 24 giờ tiếp theo.
  - [ ] Tạo thanh trượt mô phỏng kịch bản thời tiết (*What-if Scenario Slider*).
  - [ ] Đặt biểu ngữ tuyên bố miễn trừ trách nhiệm pháp lý và thông tin giải thích mô hình.
- **Sản phẩm đầu ra:** Ứng dụng `app/streamlit_app.py`, ảnh chụp màn hình tại `figures/app_demo.png`.
- **Phụ thuộc:** #17, #18
- **Tiêu chí nghiệm thu:**
  - [ ] Khởi chạy mượt mà bằng lệnh `streamlit run app/streamlit_app.py` không gặp lỗi; giao diện tương tác tức thời.
- **Người phụ trách:** Hùng (@Izuki-1780N) | **Độ ưu tiên:** P1 | **Milestone:** Milestone 5 | **Labels:** `deployment`

---

## Milestone 6: Final Deliverables & Defense (Tuần 6)

### Issue #20
- **Tiêu đề:** `docs(report): biên soạn Báo cáo Học thuật Cuối kỳ hoàn chỉnh (PDF 15–20 trang)`
- **Mục tiêu:** Soạn thảo báo cáo học thuật đầy đủ, bám sát từng mục trong biểu điểm chấm thi của giảng viên.
- **Phạm vi:** `reports/AI_PM25_Forecasting_Final_Report.pdf`.
- **Nhiệm vụ:**
  - [ ] Tổng hợp Mục 1–5: Mở đầu, Bài toán, Giá trị thực tiễn, Dữ liệu & Xuất xứ, Tiền xử lý (Huy & Khương).
  - [ ] Tổng hợp Mục 6–10: Kỹ nghệ đặc trưng, Phương pháp AI, Siêu tham số, Kiến trúc, Bố trí thực nghiệm (Khương & Khánh).
  - [ ] Tổng hợp Mục 11–15: Bảng kết quả thực nghiệm, So sánh đối chứng, Phân tích phần dư, Giải thích SHAP, Ứng dụng Demo (Hưng & Hùng).
  - [ ] Tổng hợp Mục 16–20: Giới hạn hệ thống, Vấn đề đạo đức, Bảng phân công đóng góp cá nhân, Kết luận, Tài liệu tham khảo (Cả 5 thành viên).
  - [ ] Biên dịch xuất bản tệp PDF hoàn chỉnh.
- **Sản phẩm đầu ra:** Báo cáo PDF hoàn chỉnh tại `reports/`.
- **Phụ thuộc:** #15, #16, #19
- **Tiêu chí nghiệm thu:**
  - [ ] Đầy đủ 20 mục nội dung; có bảng phân công nhiệm vụ chi tiết; số liệu thực nghiệm khớp 100% với code.
- **Người phụ trách:** Cả 5 thành viên (Chủ biên: Khương @lekhuong123456798-cpu) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 6 | **Labels:** `documentation`, `high-priority`

---

### Issue #21
- **Tiêu đề:** `docs(presentation): thiết kế bộ slide thuyết trình bảo vệ đồ án (10–12 slides)`
- **Mục tiêu:** Thiết kế slide thuyết trình cô đọng, chuyên nghiệp phục vụ 10–12 phút báo cáo trước hội đồng.
- **Phạm vi:** `reports/AI_PM25_Defense_Slides.pptx` hoặc `PDF`.
- **Nhiệm vụ:**
  - [ ] Slide 1: Trang bìa, giảng viên, nhóm 5 thành viên.
  - [ ] Slide 2: Tính cấp thiết & Bối cảnh ô nhiễm Hà Nội.
  - [ ] Slide 3: Phát biểu bài toán dự báo $t+24\text{h}$.
  - [ ] Slide 4: Pipeline dữ liệu & Chống rò rỉ thời gian.
  - [ ] Slide 5: Kỹ nghệ đặc trưng (Lags, Rolling, Sin/Cos).
  - [ ] Slide 6: Tiến trình mô hình hóa (Persistence $\rightarrow$ LightGBM $\rightarrow$ LSTM).
  - [ ] Slide 7: Sơ đồ kiến trúc giải pháp tổng thể.
  - [ ] Slide 8: Bảng kết quả thực nghiệm và so sánh.
  - [ ] Slide 9: Phân tích sai số tại các đỉnh ô nhiễm.
  - [ ] Slide 10: Minh bạch hóa khí tượng bằng Tree SHAP.
  - [ ] Slide 11: Demo ứng dụng (FastAPI + Streamlit).
  - [ ] Slide 12: Đạo đức, Giới hạn & Hướng phát triển.
- **Sản phẩm đầu ra:** Bộ slide chuẩn đúng 12 trang tại `reports/`.
- **Phụ thuộc:** #20
- **Tiêu chí nghiệm thu:**
  - [ ] Đúng 12 slides; có ghi chú phân công người thuyết trình cho từng slide; khớp thời lượng 10–12 phút.
- **Người phụ trách:** Cả 5 thành viên (Trưởng thiết kế: Khánh @nguyenphanminhkhanh9a-netizen) | **Độ ưu tiên:** P1 | **Milestone:** Milestone 6 | **Labels:** `documentation`

---

### Issue #22
- **Tiêu đề:** `chore(audit): kiểm toán tái lập môi trường sạch, đóng gói tệp nộp bài và luyện tập vấn đáp Viva`
- **Mục tiêu:** Đảm bảo mã nguồn chạy trơn tru từ đầu đến cuối trên máy tính của giảng viên, đóng gói tệp nộp bài và luyện tập vấn đáp cá nhân.
- **Phạm vi:** `docs/defense_preparation.md`, script đóng gói tệp ZIP.
- **Nhiệm vụ:**
  - [ ] Chạy kiểm chứng độc lập trên môi trường ảo sạch: clone repo, chạy pipeline từ nạp dữ liệu đến suy luận.
  - [ ] Đóng gói toàn bộ mã nguồn, dữ liệu mẫu và tài liệu thành tệp nén `PM25_Prediction_Hanoi_TeamSubmission.zip`.
  - [ ] Tổ chức buổi vấn đáp thử nghiệm giữa 5 thành viên xoay quanh 15 câu hỏi trọng tâm trong cẩm nang Viva.
- **Sản phẩm đầu ra:** Tệp ZIP nộp bài, biên bản diễn tập bảo vệ thử.
- **Phụ thuộc:** #20, #21
- **Tiêu chí nghiệm thu:**
  - [ ] Pipeline chạy tự động 100% không lỗi; cả 5 thành viên tự tin trả lời cặn kẽ mọi câu hỏi về phần việc của mình và kiến trúc chung.
- **Người phụ trách:** Cả 5 thành viên (Điều phối: Huy @doctor-cato) | **Độ ưu tiên:** P0 | **Milestone:** Milestone 6 | **Labels:** `planning`, `high-priority`
