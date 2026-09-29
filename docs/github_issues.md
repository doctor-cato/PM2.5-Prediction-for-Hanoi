# Danh Mục 16 GitHub Issues Chi Tiết

> **Đề tài:** Dự báo nồng độ bụi mịn $\text{PM}_{2.5}$ tại Hà Nội bằng Trí tuệ Nhân tạo  
> **Quy mô:** 16 Issues kỹ thuật chuẩn mực (#01 – #16) bao quát toàn bộ vòng đời 5–6 tuần  
> **Quy ước đặt tên:** Tuân thủ chuẩn Conventional Commits (`feat`, `chore`, `docs`, `fix`)

---

### Issue #01
- **Tiêu đề:** `chore(setup): khởi tạo cấu trúc dự án, môi trường thực thi và quy ước nhóm`
- **Mục tiêu:** Thiết lập khung thư mục chuẩn, cố định phiên bản thư viện và thống nhất quy ước làm việc của nhóm 5 thành viên.
- **Bối cảnh:** Đảm bảo toàn bộ 5 thành viên đều có môi trường thực thi đồng nhất, không phát sinh xung đột phiên bản trên Windows/Linux.
- **Nhiệm vụ cụ thể:**
  - Khởi tạo cây thư mục chuẩn theo đặc tả kiến trúc.
  - Cố định tệp `requirements.txt` tương thích Python 3.10+ (`pandas`, `pyarrow`, `scikit-learn`, `lightgbm`, `torch`, `fastapi`, `streamlit`, `shap`).
  - Viết tệp kiểm thử môi trường để tự động kiểm tra I/O và nạp các package cốt lõi.
  - Soạn thảo quy ước nhóm và biên bản cam kết liêm chính học thuật.
- **Tiêu chí nghiệm thu (Acceptance Criteria):**
  - Chạy `pip install -r requirements.txt` thành công không có lỗi biên dịch C++.
  - Lệnh kiểm tra `import torch, lightgbm, fastapi, streamlit` thực thi trơn tru với mã thoát `0`.
- **Phụ thuộc (Dependencies):** Không
- **Kết quả đầu ra:** Repository được cấu hình, tệp `requirements.txt`, script kiểm tra môi trường.
- **Người phụ trách đề xuất:** Thành viên 1 | **Mức độ ưu tiên:** Blocker (P0)

---

### Issue #02
- **Tiêu đề:** `docs(spec): đặc tả bài toán toán học, hàm mục tiêu và quy chuẩn chống rò rỉ dữ liệu`
- **Mục tiêu:** Xác lập định dạng bài toán hồi quy có giám sát, xác định các độ đo chuẩn và đóng băng quy chuẩn chống rò rỉ dữ liệu.
- **Bối cảnh:** Đáp ứng tiêu chí 1.1–1.3 trong thang điểm chấm (Phân tích và đề xuất giải pháp).
- **Nhiệm vụ cụ thể:**
  - Định nghĩa chính xác biến mục tiêu: $y(t) = PM_{2.5}(t + 24\text{h})$.
  - Xác lập các độ đo đánh giá: $MAE$, $RMSE$, $R^2$, và sai số trong đợt ô nhiễm cao ($PM_{2.5} > 100\,\mu\text{g/m}^3$).
  - Soạn thảo bộ quy tắc chống rò rỉ dữ liệu (*Data Leakage Checklist*) trong `docs/problem_definition.md`.
- **Tiêu chí nghiệm thu:** Tài liệu được toàn bộ 5 thành viên thẩm định và ký duyệt; định nghĩa rõ ràng điều kiện nhân quả của đặc trưng.
- **Phụ thuộc:** #01
- **Kết quả đầu ra:** `docs/problem_definition.md` hoàn chỉnh.
- **Người phụ trách đề xuất:** Thành viên 2 | **Mức độ ưu tiên:** Cao (P1)

---

### Issue #03
- **Tiêu đề:** `feat(data): xây dựng pipeline thu thập dữ liệu tự động đa nguồn (OpenAQ + Open-Meteo)`
- **Mục tiêu:** Tự động thu thập dữ liệu chuỗi thời gian nồng độ bụi mịn và các yếu tố thời tiết bề mặt tại Hà Nội giai đoạn 2022–2024.
- **Bối cảnh:** Dữ liệu thô upstream chưa có sẵn trên đĩa; AI project cần một bộ tải dữ liệu độc lập, có tính tái lập để lấy dữ liệu thực tế.
- **Nhiệm vụ cụ thể:**
  - Viết module `src/data/fetch_openaq.py` thu thập dữ liệu trạm Đại sứ quán Hoa Kỳ tại Hà Nội ($PM_{2.5}, PM_{10}$).
  - Viết module `src/data/fetch_weather.py` thu thập dữ liệu Open-Meteo ERA5 (nhiệt độ, độ ẩm, tốc độ/hướng gió, áp suất, lượng mưa).
  - Lưu các tệp thô bất biến vào `data/raw/` dưới định dạng Parquet kèm siêu dữ liệu nguồn.
- **Tiêu chí nghiệm thu:** Tập dữ liệu thô thu thập được $\ge 15.000$ dòng quan trắc theo giờ; mã nguồn có cơ chế tự động thử lại khi mất mạng.
- **Phụ thuộc:** #01, #02
- **Kết quả đầu ra:** Các module nạp dữ liệu tại `src/data/` và tệp thô trong `data/raw/`.
- **Người phụ trách đề xuất:** Thành viên 1 | **Mức độ ưu tiên:** Blocker (P0)

---

### Issue #04
- **Tiêu đề:** `feat(data): làm sạch tất định, kiểm tra tính hợp lý vật lý và căn chỉnh lưới thời gian`
- **Mục tiêu:** Chuyển đổi dữ liệu thô thành tập dữ liệu sạch, đảm bảo tính liên tục theo giờ và không chứa các giá trị vi phạm vật lý.
- **Bối cảnh:** Dữ liệu cảm biến môi trường thường xuyên gặp lỗi truyền tín hiệu, mất điện hoặc kẹt kim đo.
- **Nhiệm vụ cụ thể:**
  - Chuẩn hóa múi giờ đồng nhất về `Asia/Ho_Chi_Minh` (UTC+7).
  - Áp dụng kiểm tra vật lý: $PM_{2.5} \le PM_{10} + 1.0$; $RH \in [0, 100\%]$; phát hiện và bóc trần các mã lỗi ngụy trang (`-999`).
  - Reindex chuỗi thời gian về lưới giờ liên tục 1h; áp dụng điền tiến (*forward-fill*) cho các khoảng khuyết ngắn $\le 2\text{h}$; giữ nguyên `NaN` với khoảng khuyết dài.
  - Ghép nối dữ liệu ô nhiễm và thời tiết theo trục thời gian; xuất ra `data/interim/canonical_cleaned.parquet`.
- **Tiêu chí nghiệm thu:** Trục thời gian liên tục 100% không bị nhảy bước giờ; không có dòng trùng lặp thời gian; có nhật ký làm sạch (*Cleaning Log*).
- **Phụ thuộc:** #03
- **Kết quả đầu ra:** `src/data/clean_data.py`, `notebooks/01_data_audit_and_prep.ipynb`.
- **Người phụ trách đề xuất:** Thành viên 1 | **Mức độ ưu tiên:** Blocker (P0)

---

### Issue #05
- **Tiêu đề:** `feat(features): kỹ nghệ đặc trưng nhân quả và phân chia tập dữ liệu theo thời gian`
- **Mục tiêu:** Sinh ma trận đặc trưng từ quá khứ, tạo cột mục tiêu dự báo $t+24\text{h}$, và phân chia Train/Val/Test chống rò rỉ.
- **Bối cảnh:** Đây là chốt chặn quan trọng nhất để đảm bảo mô hình không học lén tương lai.
- **Nhiệm vụ cụ thể:**
  - Sinh các đặc trưng trễ: $PM_{2.5}(t-1), PM_{2.5}(t-3), PM_{2.5}(t-6), PM_{2.5}(t-12), PM_{2.5}(t-24)$.
  - Sinh đặc trưng thống kê trượt: Trung bình và độ lệch chuẩn trượt trên các cửa sổ 6h, 12h, 24h (dùng `shift(1)`).
  - Mã hóa chu kỳ lượng giác $\sin/\cos$ cho giờ trong ngày và tháng trong năm.
  - Căn chỉnh biến mục tiêu $target = PM_{2.5}(t + 24\text{h})$.
  - Phân chia tuyến tính: Train (70%), Validation (15%), Test (15%). Huấn luyện `StandardScaler` duy nhất trên Train và lưu ra đĩa.
  - Xuất dữ liệu đã sẵn sàng huấn luyện vào `data/processed/`.
- **Tiêu chí nghiệm thu:** Không có bất kỳ giá trị khuyết `NaN` nào trong ma trận huấn luyện; kiểm toán khẳng định hàng $k$ không chứa thông tin tại $k+24$.
- **Phụ thuộc:** #04
- **Kết quả đầu ra:** `src/features/build_features.py`, `src/features/split_data.py`, `notebooks/02_feature_engineering.ipynb`.
- **Người phụ trách đề xuất:** Thành viên 2 | **Mức độ ưu tiên:** Blocker (P0)

---

### Issue #06
- **Tiêu đề:** `feat(models): xây dựng mô hình cơ sở Persistence và hồi quy tuyến tính Ridge`
- **Mục tiêu:** Thiết lập các ngưỡng hiệu năng sàn tối thiểu mà bất kỳ mô hình AI phức tạp nào cũng bắt buộc phải vượt qua.
- **Bối cảnh:** Trong học máy, một mô hình chỉ có giá trị khi chứng minh được nó đánh bại được phương pháp suy đoán ngây thơ.
- **Nhiệm vụ cụ thể:**
  - Xây dựng mô hình Naive Persistence: $\hat{y}(t+24) = y(t)$.
  - Xây dựng mô hình 24-Hour Seasonal Persistence: $\hat{y}(t+24) = y(t-24)$.
  - Huấn luyện mô hình hồi quy Ridge và Lasso với việc tinh chỉnh tham số điều hòa $\alpha$ trên tập Validation.
  - Ghi nhận MAE, RMSE, $R^2$ của các baseline trên tập Validation và Test vào bảng thực nghiệm.
- **Tiêu chí nghiệm thu:** Có mã nguồn thực thi độc lập cho baseline; các giá trị độ đo làm mốc đối chứng được ghi nhận đầy đủ.
- **Phụ thuộc:** #05
- **Kết quả đầu ra:** `src/models/baseline.py`, `notebooks/03_baseline_and_classical.ipynb`.
- **Người phụ trách đề xuất:** Thành viên 2 | **Mức độ ưu tiên:** Cao (P1)

---

### Issue #07
- **Tiêu đề:** `feat(models): huấn luyện và tinh chỉnh mô hình học máy dạng cây (Random Forest & LightGBM)`
- **Mục tiêu:** Xây dựng, tối ưu hóa siêu tham số và đánh giá các mô hình Ensemble Trees trên dữ liệu bảng chuỗi thời gian.
- **Bối cảnh:** Cây quyết định tăng cường gradient (GBDT) thường là phương pháp đạt hiệu quả cao nhất trên dữ liệu dạng bảng có tương tác khí tượng.
- **Nhiệm vụ cụ thể:**
  - Xây dựng module `src/models/train_classical.py` hỗ trợ Random Forest và LightGBM Regressor.
  - Tinh chỉnh siêu tham số trên tập Validation (`n_estimators`, `max_depth`, `learning_rate`, `num_leaves`, `subsample`).
  - Thực hiện thực nghiệm triệt tiêu đặc trưng (*Feature Ablation*): Chỉ dùng lags $PM_{2.5}$ vs. Kết hợp lags + biến thời tiết vs. Toàn bộ đặc trưng.
  - Đo lường thời gian huấn luyện và độ trễ suy luận trên 1.000 mẫu quan sát.
- **Tiêu chí nghiệm thu:** LightGBM đạt MAE và RMSE thấp hơn có ý nghĩa so với mô hình Persistence trên tập Validation.
- **Phụ thuộc:** #05, #06
- **Kết quả đầu ra:** Mô hình đã lưu tại `models/`, tệp nhật ký thực nghiệm tại `docs/experiments.md`.
- **Người phụ trách đề xuất:** Thành viên 3 | **Mức độ ưu tiên:** Cao (P1)

---

### Issue #08
- **Tiêu đề:** `feat(models): phát triển mô hình chuỗi sâu PyTorch LSTM`
- **Mục tiêu:** Xây dựng và huấn luyện mạng nơ-ron hồi quy chuỗi sâu (LSTM) để nắm bắt động lực thời gian đa bước.
- **Bối cảnh:** Thử nghiệm học sâu để đánh giá xem trạng thái ẩn hồi quy có vượt qua được các đặc trưng trễ thủ công của mô hình cây hay không.
- **Nhiệm vụ cụ thể:**
  - Xây dựng lớp PyTorch `Dataset` và `DataLoader` tạo tensor cửa sổ trượt 3D `(batch_size, 24, n_features)`.
  - Thiết kế kiến trúc mạng 2 tầng LSTM có Dropout và lớp Linear kết xuất giá trị dự báo điểm.
  - Viết vòng lặp huấn luyện với AdamW, hàm mất mát MSE, bộ lập lịch learning rate và cơ chế dừng sớm *EarlyStopping* theo dõi loss tập Validation.
  - Ghi chép căn cứ chọn siêu tham số: chiều dài chuỗi (24h), hidden size (64), dropout (0.2), batch size (64), epochs (50).
- **Tiêu chí nghiệm thu:** Đồ thị mất mát hội tụ rõ ràng, không xuất hiện hiện tượng quá khớp cực đoan; lưu trọng số tốt nhất vào `models/lstm_best.pt`.
- **Phụ thuộc:** #05, #06
- **Kết quả đầu ra:** `src/models/train_lstm.py`, `notebooks/04_deep_learning_lstm.ipynb`.
- **Người phụ trách đề xuất:** Thành viên 4 | **Mức độ ưu tiên:** Cao (P1)

---

### Issue #09
- **Tiêu đề:** `feat(eval): đối sánh toàn diện các mô hình, phân tích phần dư và kiểm toán sai số đợt đỉnh ô nhiễm`
- **Mục tiêu:** Đánh giá chuẩn hóa toàn bộ các mô hình trên tập Test độc lập, phân tích chuyên sâu các trường hợp mô hình thất bại.
- **Bối cảnh:** Tiêu chí đánh giá của giảng viên yêu cầu phân tích rõ: cái gì hoạt động, cái gì không, tại sao, và hạn chế là gì.
- **Nhiệm vụ cụ thể:**
  - Điền đầy đủ bảng so sánh đa chỉ số: MAE, RMSE, $R^2$, sMAPE, Thời gian huấn luyện, Tốc độ suy luận.
  - Vẽ biểu đồ đường Thực tế vs. Dự báo trên các khoảng thời gian kiểm tra tiêu biểu (mùa đông nghịch nhiệt vs. mùa hè thông thoáng).
  - Phân tích phần dư: phân phối sai số, sai số theo mức độ ô nhiễm, sai số trong đợt bụi cực đoan ($PM_{2.5} > 100\,\mu\text{g/m}^3$).
  - Lý giải nguyên nhân vì sao mô hình cây hoặc LSTM có ưu/nhược thế trong từng trường hợp khí tượng.
- **Tiêu chí nghiệm thu:** Bảng kết quả hoàn chỉnh không ngụy tạo số liệu; các biểu đồ chất lượng cao được lưu vào `figures/`.
- **Phụ thuộc:** #06, #07, #08
- **Kết quả đầu ra:** `src/evaluation/metrics.py`, `notebooks/05_evaluation_and_shap.ipynb`, `figures/model_comparison.png`.
- **Người phụ trách đề xuất:** Thành viên 4 | **Mức độ ưu tiên:** Cao (P1)

---

### Issue #10
- **Tiêu đề:** `feat(eval): giải thích mô hình và định lượng đóng góp của các yếu tố khí tượng bằng SHAP`
- **Mục tiêu:** Sử dụng giá trị SHAP để minh bạch hóa mô hình hộp đen, tìm hiểu xem các yếu tố nào chi phối dự báo nhiều nhất.
- **Bối cảnh:** Yêu cầu giải thích mô hình AI (Explainable AI) phục vụ trả lời phản biện và chứng minh hiểu biết bản chất vật lý.
- **Nhiệm vụ cụ thể:**
  - Áp dụng `shap.TreeExplainer` lên mô hình LightGBM tốt nhất.
  - Xuất biểu đồ ong vò vẽ (SHAP Beeswarm Plot) và biểu đồ cột mức độ quan trọng đặc trưng (Feature Importance).
  - Đối chiếu với lý thuyết khí tượng: phân tích tác động dấu âm/dương của tốc độ gió, độ ẩm, áp suất lên nồng độ bụi tích lũy.
  - Phân tích giới hạn giải thích của mạng nơ-ron LSTM.
- **Tiêu chí nghiệm thu:** Biểu đồ SHAP được tạo và giải thích cặn kẽ trong báo cáo; diễn giải được ý nghĩa vật lý của ít nhất 5 đặc trưng hàng đầu.
- **Phụ thuộc:** #07, #09
- **Kết quả đầu ra:** `src/evaluation/explain.py`, `figures/shap_summary.png`.
- **Người phụ trách đề xuất:** Thành viên 3 | **Mức độ ưu tiên:** Trung bình (P2)

---

### Issue #11
- **Tiêu đề:** `feat(inference): đóng gói engine suy luận độc lập và lưu trữ mô hình quán quân`
- **Mục tiêu:** Đóng gói toàn bộ chuỗi tiền xử lý, scaler và mô hình tốt nhất thành một module suy luận gọi bằng 1 dòng lệnh.
- **Bối cảnh:** Phân tách hoàn toàn môi trường huấn luyện thử nghiệm khỏi môi trường triển khai thực tế.
- **Nhiệm vụ cụ thể:**
  - Xây dựng lớp `PM25Forecaster` trong `src/inference/predict.py`.
  - Tiếp nhận đầu vào là DataFrame quan trắc 24h gần nhất hoặc chuỗi JSON.
  - Tự động áp dụng cơ chế điền thiếu an toàn, tạo đặc trưng, chuẩn hóa và dự báo điểm $t+24\text{h}$ kèm khoảng tin cậy.
  - Viết Unit Test kiểm thử chức năng suy luận với cả dữ liệu giả lập và dữ liệu thực tế gần nhất.
- **Tiêu chí nghiệm thu:** Phương thức `forecaster.predict(recent_data)` trả về giá trị số thực hợp lệ trong thời gian $< 50\text{ ms}$.
- **Phụ thuộc:** #09, #10
- **Kết quả đầu ra:** `src/inference/predict.py`, tệp gói mô hình hoàn chỉnh trong `models/`.
- **Người phụ trách đề xuất:** Thành viên 5 | **Mức độ ưu tiên:** Blocker (P0)

---

### Issue #12
- **Tiêu đề:** `feat(api): xây dựng dịch vụ REST API bằng FastAPI phục vụ dự báo thời gian thực`
- **Mục tiêu:** Mở cổng giao tiếp chuẩn hóa cho hệ thống AI thông qua dịch vụ web API nhẹ, có tài liệu tự động.
- **Bối cảnh:** Giảng viên đánh giá rất cao khả năng ứng dụng thực tiễn và tính module hóa của giải pháp phần mềm.
- **Nhiệm vụ cụ thể:**
  - Viết `api/main.py` sử dụng framework FastAPI.
  - Thiết lập các endpoint: `GET /health`, `GET /model-info`, `POST /predict`.
  - Định nghĩa lược đồ xác thực dữ liệu vào/ra bằng Pydantic trong `api/schemas.py` có kiểm tra khoảng giá trị vật lý.
  - Bổ sung ghi log thời gian xử lý và xử lý ngoại lệ thân thiện khi dữ liệu gửi lên bị thiếu trường.
- **Tiêu chí nghiệm thu:** Giao diện Swagger UI (`/docs`) hoạt động hoàn hảo; gọi `POST /predict` trả về mã HTTP 200 kèm kết quả dự báo chính xác.
- **Phụ thuộc:** #11
- **Kết quả đầu ra:** `api/main.py`, `api/schemas.py`, script gửi request kiểm thử.
- **Người phụ trách đề xuất:** Thành viên 5 | **Mức độ ưu tiên:** Cao (P1)

---

### Issue #13
- **Tiêu đề:** `feat(app): phát triển giao diện Web Dashboard tương tác bằng Streamlit`
- **Mục tiêu:** Cung cấp giao diện trực quan, sinh động cho người dùng và hội đồng chấm thi trải nghiệm dự báo nồng độ bụi.
- **Bối cảnh:** Trực quan hóa sản phẩm đầu cuối phục vụ buổi bảo vệ đồ án và minh họa giá trị thực tế.
- **Nhiệm vụ cụ thể:**
  - Xây dựng `app/streamlit_app.py`.
  - Thành phần 1: Thẻ thông tin thời gian thực (nồng độ $\text{PM}_{2.5}$ hiện tại, xếp loại mức độ ô nhiễm, thời tiết hiện tại).
  - Thành phần 2: Biểu đồ đường dự báo 24 giờ tới kèm dải độ lệch tin cậy.
  - Thành phần 3: Bộ mô phỏng kịch bản thời tiết (*What-if Slider*: Điều gì xảy ra nếu tốc độ gió tăng gấp đôi hoặc độ ẩm tăng vọt?).
  - Thành phần 4: Tab minh bạch thuật toán hiển thị bảng chỉ số thực nghiệm, đồ thị SHAP và biểu ngữ khuyến cáo đạo đức.
- **Tiêu chí nghiệm thu:** Ứng dụng chạy mượt mà qua lệnh `streamlit run app/streamlit_app.py`; giao diện trực quan, hiển thị rõ ràng câu từ khuyến cáo học thuật.
- **Phụ thuộc:** #11, #12
- **Kết quả đầu ra:** `app/streamlit_app.py`, ảnh chụp màn hình ứng dụng tại `figures/app_demo.png`.
- **Người phụ trách đề xuất:** Thành viên 5 | **Mức độ ưu tiên:** Cao (P1)

---

### Issue #14
- **Tiêu đề:** `docs(report): biên soạn báo cáo học thuật cuối kỳ hoàn chỉnh (PDF 15–20 trang)`
- **Mục tiêu:** Viết báo cáo khoa học chi tiết, bám sát từng mục trong biểu điểm đánh giá của giảng viên.
- **Bối cảnh:** Chiếm tới 8/10 điểm tổng kết của toàn bộ môn học.
- **Nhiệm vụ cụ thể:**
  - Viết Mục 1–5: Mở đầu, Bài toán, Giá trị thực tiễn, Dữ liệu & Xuất xứ, Tiền xử lý (Thành viên 1 & 2).
  - Viết Mục 6–10: Kỹ nghệ đặc trưng, Phương pháp AI, Phân tích siêu tham số, Kiến trúc hệ thống, Bố trí thực nghiệm (Thành viên 2 & 3).
  - Viết Mục 11–15: Bảng kết quả thực nghiệm, So sánh mô hình, Phân tích sai số phần dư, Giải thích mô hình SHAP, Ứng dụng demo (Thành viên 4 & 5).
  - Viết Mục 16–20: Giới hạn hệ thống, Vấn đề đạo đức, Bảng phân công đóng góp cá nhân, Kết luận, Tài liệu tham khảo (Cả 5 thành viên).
  - Biên dịch và xuất bản tệp PDF chuẩn mực.
- **Tiêu chí nghiệm thu:** Báo cáo PDF đầy đủ 20 mục; có bảng phân công nhiệm vụ chi tiết; số liệu thống kê khớp 100% với mã nguồn chạy thực tế.
- **Phụ thuộc:** #09, #10, #13
- **Kết quả đầu ra:** `reports/AI_PM25_Forecasting_Final_Report.pdf`.
- **Người phụ trách đề xuất:** Cả 5 thành viên (Chủ biên: Thành viên 2) | **Mức độ ưu tiên:** Blocker (P0)

---

### Issue #15
- **Tiêu đề:** `docs(presentation): thiết kế bộ slide thuyết trình bảo vệ đồ án (10–12 slides)`
- **Mục tiêu:** Thiết kế slide thuyết trình cô đọng, chuyên nghiệp phục vụ 10–12 phút báo cáo trước hội đồng.
- **Bối cảnh:** Quyết định điểm thuyết trình và ấn tượng ban đầu của hội đồng đánh giá.
- **Nhiệm vụ cụ thể:**
  - Slide 1: Tiêu đề đề tài, Giảng viên hướng dẫn, Danh sách nhóm 5 thành viên.
  - Slide 2: Tính cấp thiết và Bối cảnh ô nhiễm không khí tại Hà Nội.
  - Slide 3: Định nghĩa bài toán & Mục tiêu dự báo 24 giờ.
  - Slide 4: Quy trình xử lý dữ liệu & Phân chia chuỗi thời gian chống rò rỉ.
  - Slide 5: Kỹ nghệ đặc trưng (Lags, Rolling Means, Cyclical Encodings).
  - Slide 6: Tiến trình mô hình hóa (Persistence $\rightarrow$ LightGBM $\rightarrow$ PyTorch LSTM).
  - Slide 7: Sơ đồ kiến trúc giải pháp tổng thể.
  - Slide 8: Bảng kết quả thực nghiệm và so sánh hiệu năng.
  - Slide 9: Phân tích sai số: Tại sao mô hình gặp khó khăn ở các đỉnh ô nhiễm?
  - Slide 10: Minh bạch hóa mô hình bằng Tree SHAP (Tác động của gió và độ ẩm).
  - Slide 11: Demo sản phẩm ứng dụng (REST API + Streamlit Dashboard).
  - Slide 12: Đạo đức, Giới hạn đề tài & Hướng phát triển tương lai.
- **Tiêu chí nghiệm thu:** Bộ slide đúng 12 trang; có ghi chú phân công người nói cho từng slide; khớp thời lượng 10–12 phút.
- **Phụ thuộc:** #14
- **Kết quả đầu ra:** `reports/AI_PM25_Defense_Slides.pptx` hoặc `PDF`.
- **Người phụ trách đề xuất:** Cả 5 thành viên (Trưởng thiết kế: Thành viên 3) | **Mức độ ưu tiên:** Cao (P1)

---

### Issue #16
- **Tiêu đề:** `chore(audit): kiểm toán tái lập trên môi trường sạch, đóng gói tệp nộp bài và luyện tập vấn đáp Viva`
- **Mục tiêu:** Xác nhận mã nguồn chạy trơn tru từ đầu đến cuối trên máy tính mới, đóng gói tệp ZIP và luyện tập trả lời phản biện.
- **Bối cảnh:** Tránh rủi ro "chạy được trên máy em nhưng lỗi trên máy thầy cô"; chuẩn bị cho phần vấn đáp cá nhân 2 điểm.
- **Nhiệm vụ cụ thể:**
  - Thực hiện bài test môi trường sạch (*Clean-slate test*): clone repo vào thư mục tạm, tạo venv mới, chạy toàn bộ pipeline từ tải dữ liệu đến suy luận.
  - Đóng gói toàn bộ mã nguồn, dữ liệu mẫu và tài liệu thành tệp nộp bài nén `PM25_Prediction_Hanoi_TeamSubmission.zip`.
  - Tổ chức buổi vấn đáp thử nghiệm giữa 5 thành viên xoay quanh 15 câu hỏi trọng tâm (chống rò rỉ, trade-off độ đo, giải thích thuật toán).
- **Tiêu chí nghiệm thu:** Pipeline chạy tự động 100% không cần can thiệp thủ công; tệp ZIP nộp bài hoàn thiện; cả 5 thành viên nắm chắc phần việc của mình.
- **Phụ thuộc:** #14, #15
- **Kết quả đầu ra:** Tệp ZIP nộp bài, tài liệu hướng dẫn vấn đáp `docs/defense_preparation.md`.
- **Người phụ trách đề xuất:** Cả 5 thành viên (Điều phối: Thành viên 1) | **Mức độ ưu tiên:** Blocker (P0)
