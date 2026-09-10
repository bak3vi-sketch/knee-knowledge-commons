# Chính sách quyền riêng tư và dữ liệu bệnh nhân

> Bản tiếng Việt dành cho chủ dự án và cộng đồng Việt Nam. Bản canonical: [`PRIVACY.md`](PRIVACY.md).

Privacy là ràng buộc thiết kế cốt lõi của Knee Knowledge Commons.

## Tuyệt đối không đưa dữ liệu sức khỏe có thể nhận dạng vào Git

Không được đưa vào repo công khai:
- tên bệnh nhân;
- email, số điện thoại, địa chỉ;
- mã hồ sơ/mã tài khoản;
- hồ sơ bệnh án;
- đơn thuốc, giấy hẹn, tài liệu khám chữa;
- MRI/DICOM thô;
- hoặc tổ hợp ngày tháng/địa điểm/chi tiết đủ làm tăng nguy cơ nhận dạng lại một người.

Lịch sử Git được thiết kế để lưu lâu dài. Xóa file khỏi nhánh hiện tại không có nghĩa dữ liệu đã biến mất khỏi lịch sử. Vì vậy GitHub không phải nơi phù hợp để lưu submission sức khỏe riêng tư.

## Dữ liệu bệnh nhân trong tương lai nên lưu ở đâu?

Submission riêng tư/bán riêng tư phải nằm trong database có:
- consent rõ ràng;
- chỉ thu dữ liệu tối thiểu;
- kiểm soát quyền truy cập;
- trạng thái moderation;
- cơ chế rút lại/xóa;
- audit phù hợp;
- tách thông tin tài khoản/nhận dạng khỏi dữ liệu trải nghiệm sức khỏe khi có thể.

## Những gì có thể đưa vào repo công khai?

- kết quả tổng hợp từ dữ liệu cộng đồng đã review;
- bản tóm tắt được cố ý công khai và khử định danh khi governance cho phép;
- schema, phương pháp, prompt và code phân tích không làm lộ dữ liệu riêng tư.

Khử định danh chỉ làm giảm rủi ro, **không bảo đảm ẩn danh tuyệt đối**.

## Thu thập tối thiểu

Nếu một trường dữ liệu không phục vụ use case hoặc mục tiêu nghiên cứu rõ ràng thì không thu “để sau này có thể cần”. Ưu tiên khoảng tuổi và mốc thời gian tương đối thay vì ngày sinh/ngày sự kiện chính xác khi không cần thiết.

## Gửi dữ liệu cho nhà cung cấp AI bên ngoài

Trước khi gửi nội dung sức khỏe riêng tư cho Gemini, OpenAI hoặc nhà cung cấp khác, phải xác định rõ:
- dữ liệu gì được gửi;
- tại sao cần gửi;
- thiết lập lưu trữ/training nếu có;
- yêu cầu pháp lý/hợp đồng theo địa phương;
- consent của người dùng;
- có phương án không dùng AI hay không.

Việc tích hợp một AI provider không được âm thầm mở rộng mục đích sử dụng dữ liệu.
