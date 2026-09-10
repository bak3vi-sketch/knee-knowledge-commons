# Hướng dẫn dành cho chủ dự án

Tài liệu này là **điểm bắt đầu dành cho chủ dự án**. Bạn không cần đọc toàn bộ file kỹ thuật trong repo để điều hành Knee Knowledge Commons.

## Dự án đang ở đâu?

- Foundation v0.1: **đã hoàn thành**.
- Chiến lược: **Việt Nam trước, sẵn sàng mở rộng toàn cầu**.
- Việc quan trọng tiếp theo: **Pilot 0002 — người vừa được chẩn đoán ACL ± sụn chêm**.
- Chưa nên xây website lớn, AI chẩn đoán hoặc kho kiến thức ACL toàn diện trước khi pilot chứng minh pipeline đầu–cuối.

## Bạn nên đọc những gì?

### Cần đọc / hiểu ở mức chủ dự án
- [`README.vi.md`](../README.vi.md) — dự án là gì và đang đi đâu.
- [`ROADMAP.vi.md`](../ROADMAP.vi.md) — thứ tự phát triển.
- [`PRODUCT_VISION.vi.md`](PRODUCT_VISION.vi.md) — sản phẩm dài hạn trông như thế nào.
- [`../plans/0002-acl-meniscus-knowledge-pilot.vi.md`](../plans/0002-acl-meniscus-knowledge-pilot.vi.md) — việc đang làm tiếp theo.
- [`../MEDICAL_SAFETY.vi.md`](../MEDICAL_SAFETY.vi.md) — ranh giới an toàn y khoa.
- [`../PRIVACY.vi.md`](../PRIVACY.vi.md) — dữ liệu bệnh nhân được/không được lưu ở đâu.
- [`../GOVERNANCE.vi.md`](../GOVERNANCE.vi.md) — ai được duyệt loại thay đổi nào.
- [`AI_POLICY.vi.md`](AI_POLICY.vi.md) — AI được phép làm gì và không được tự quyết gì.

### Không cần đọc thường xuyên
Các file như schema JSON, chi tiết architecture, agent prompt, implementation và code chủ yếu phục vụ agent/developer/reviewer. Khi chúng tạo ra một quyết định ảnh hưởng tới sản phẩm, agent phải giải thích lại cho bạn bằng tiếng Việt dễ hiểu.

## Vai trò của bạn

Bạn không cần trở thành bác sĩ, researcher hay developer. Vai trò quan trọng nhất của chủ dự án là:
1. Giữ sứ mệnh: giúp người bệnh có thông tin tốt hơn và tránh sai lầm do thiếu thông tin.
2. Xác định nỗi đau và câu hỏi thật của bệnh nhân Việt Nam.
3. Quyết định thứ tự ưu tiên hành trình người dùng.
4. Đánh giá nội dung/giao diện có dễ hiểu và thực sự hữu ích không.
5. Xây mạng lưới reviewer/đối tác phù hợp theo thời gian.
6. Quyết định khi nào dự án đủ trưởng thành để mở rộng tính năng hoặc quốc gia.
7. Không cho tốc độ, tính năng AI hoặc số lượng nội dung làm suy yếu safety, privacy và evidence integrity.

## Agent phải báo cho bạn như thế nào?

Với thay đổi không nhỏ, agent phải giải thích bằng tiếng Việt:
- **Vấn đề:** đang giải quyết chuyện gì?
- **Vì sao làm bây giờ:** có thực sự cần không?
- **Lợi ích:** dự án/người dùng được gì?
- **Rủi ro/đánh đổi:** có thể hỏng ở đâu?
- **Bạn cần quyết định gì:** nếu có.
- **Xong khi nào:** tiêu chí hoàn thành cụ thể.

Nếu agent chỉ đưa code hoặc thuật ngữ kỹ thuật mà không giải thích tác động sản phẩm, tài liệu chưa đạt yêu cầu owner-facing.

## Quy tắc ngôn ngữ

- Nội dung dành cho bệnh nhân Việt Nam: ưu tiên tiếng Việt.
- Tài liệu cần chủ dự án quyết định: phải có bản/tóm tắt tiếng Việt.
- Schema, ID, technical docs và nguồn nghiên cứu: có thể dùng tiếng Anh để dễ cộng tác quốc tế.
- Không tạo hai hệ thống evidence độc lập Việt/Anh; hai ngôn ngữ phải dùng cùng nguồn tri thức cốt lõi.
- Thông tin riêng Việt Nam phải gắn là local context, không biến thành khuyến cáo toàn cầu.

## Quyết định hiện tại

Chưa cần quyết định công nghệ website hay chọn Gemini/OpenAI làm AI chính.

Ưu tiên hiện tại là chứng minh được:

`câu hỏi thật`
→ `nguồn`
→ `evidence record`
→ `kiểm tra phạm vi/citation`
→ `human review`
→ `nội dung tiếng Việt`
→ `AI hỏi–đáp có nguồn`.

Khi chuỗi này chạy tốt, quyết định công nghệ phía trước sẽ dễ và ít rủi ro hơn rất nhiều.
