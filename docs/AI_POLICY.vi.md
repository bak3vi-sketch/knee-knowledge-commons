# Chính sách sử dụng AI

> Bản tiếng Việt dành cho chủ dự án và cộng đồng Việt Nam. Bản canonical: [`AI_POLICY.md`](AI_POLICY.md).

AI là **công cụ tăng tốc và lớp giao tiếp**, không phải cơ quan có thẩm quyền y khoa.

## AI nên làm gì?

AI phù hợp để:
- tìm và sàng lọc tài liệu;
- trích xuất dữ liệu có cấu trúc từ nguồn;
- kiểm tra citation và tính nhất quán;
- soạn bản dễ hiểu;
- tạo bản dịch nháp;
- phát hiện nội dung trùng hoặc cũ;
- tổng hợp dữ liệu cộng đồng đã được review;
- chuẩn bị PR và gói thông tin cho reviewer;
- hỏi–đáp dựa trên knowledge đã duyệt.

## Con người chịu trách nhiệm ở đâu?

Bất kỳ output AI nào làm thay đổi:
- ý nghĩa y khoa;
- hành vi an toàn;
- privacy;
- hoặc cách công chúng hiểu một vấn đề quan trọng

đều phải qua loại review tương ứng trong `GOVERNANCE.md`.

## AI hỏi–đáp cho bệnh nhân

Assistant phải tìm từ **approved knowledge** của dự án trước và tách rõ:
1. câu trả lời ngắn;
2. evidence đã review nói gì;
3. trải nghiệm cộng đồng liên quan nếu có;
4. điều còn chưa chắc chắn/mâu thuẫn;
5. câu hỏi hữu ích nên trao đổi với chuyên gia;
6. nguồn.

Nếu kho tri thức chưa đủ để trả lời, AI phải nói rõ **chưa đủ dữ liệu** thay vì dùng sự tự tin của model để lấp chỗ trống.

## Chọn nhà cung cấp AI

Dự án dùng một lớp trung gian mỏng để không bị phụ thuộc Gemini, OpenAI hay bất kỳ hãng nào khác.

Có thể chọn model theo từng việc dựa trên:
- chất lượng;
- chi phí;
- privacy;
- độ sẵn sàng;
- khả năng dùng công cụ/tìm nguồn.

Người dùng bình thường không cần phải chọn model nếu không có lý do thực sự cần thiết.

Gemini Notebook/NotebookLM có thể dùng làm **research workspace** cho reviewer/maintainer, nhưng không phải nơi lưu canonical knowledge và không được dùng để bỏ qua review của repo.

## Tách knowledge đã duyệt và bản nháp

AI production dành cho bệnh nhân chỉ được index nguồn đã duyệt. Công cụ dành cho reviewer có thể truy cập draft/unreviewed material nhưng phải hiển thị trạng thái thật rõ.

## Phải test trước khi phát hành

Bộ test cần có các trường hợp:
- người dùng yêu cầu quyết định điều trị cá nhân;
- citation không khớp claim;
- các nguồn mâu thuẫn;
- evidence và giai thoại bị trộn;
- thiếu thông tin;
- lỗi dịch làm đổi ý nghĩa;
- dữ liệu nhạy cảm;
- tình huống cần hướng người dùng tới chăm sóc phù hợp.

Trong giai đoạn Vietnam-first phải có **evaluation set tiếng Việt** trước khi mở rộng ngôn ngữ.

Đổi model AI cũng được xem là một thay đổi sản phẩm: phải chạy lại evaluation trước khi triển khai rộng.
