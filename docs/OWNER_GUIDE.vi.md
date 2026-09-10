# Hướng dẫn dành cho chủ dự án

Đây là **điểm bắt đầu ngắn gọn dành cho chủ dự án**. File này không phải bản dịch của toàn bộ repo và không cố lặp lại mọi policy. Các tài liệu canonical có thể đọc bằng chức năng dịch của trình duyệt hoặc nhờ AI giải thích khi cần.

## Dự án đang ở đâu?

Trạng thái sống của dự án được lưu tại [`CONTINUITY.md`](../CONTINUITY.md). Nếu thông tin ở đây và `CONTINUITY.md` khác nhau, **ưu tiên `CONTINUITY.md`** và cập nhật file này khi sự khác biệt ảnh hưởng tới định hướng dành cho chủ dự án.

Hiện tại:
- Foundation v0.1: **đã hoàn thành**.
- Chiến lược: **Việt Nam trước, sẵn sàng mở rộng toàn cầu**.
- Việc quan trọng tiếp theo: **Pilot 0002 — người vừa được chẩn đoán ACL ± sụn chêm**.
- Chưa nên xây website lớn, AI chẩn đoán hoặc kho kiến thức ACL toàn diện trước khi pilot chứng minh pipeline đầu–cuối.

## Bạn nên đọc gì?

### Thường xuyên
- [`CONTINUITY.md`](../CONTINUITY.md) — dự án đang làm gì, đã quyết gì, bước tiếp theo là gì.
- [`../plans/0002-acl-meniscus-knowledge-pilot.md`](../plans/0002-acl-meniscus-knowledge-pilot.md) — phạm vi và tiêu chí hoàn thành của pilot đang active.
- [`../README.vi.md`](../README.vi.md) — cửa giới thiệu tiếng Việt cho cộng đồng.

### Khi cần ra quyết định
- [`../ROADMAP.md`](../ROADMAP.md) — thứ tự phát triển dài hạn.
- [`PRODUCT_VISION.md`](PRODUCT_VISION.md) — sản phẩm cuối cùng hướng tới điều gì.
- [`../MEDICAL_SAFETY.md`](../MEDICAL_SAFETY.md) — ranh giới an toàn y khoa.
- [`../PRIVACY.md`](../PRIVACY.md) — dữ liệu bệnh nhân được/không được lưu ở đâu.
- [`../GOVERNANCE.md`](../GOVERNANCE.md) — ai được duyệt loại thay đổi nào.
- [`AI_POLICY.md`](AI_POLICY.md) — AI được phép làm gì và không được tự quyết gì.
- [`ARCHITECTURE.md`](ARCHITECTURE.md) — hệ thống và source-of-truth được tổ chức ra sao.

Bạn có thể dùng dịch tự động của trình duyệt cho các file tiếng Anh. Khi một quyết định cần bạn duyệt, agent phải giải thích lại bằng **tiếng Việt dễ hiểu**, thay vì bắt bạn tự giải mã tài liệu kỹ thuật.

## Vai trò của bạn

Bạn không cần trở thành bác sĩ, researcher hay developer. Vai trò quan trọng nhất là:
1. Giữ sứ mệnh: giúp người bệnh có thông tin tốt hơn và tránh sai lầm do thiếu thông tin.
2. Xác định nỗi đau và câu hỏi thật của bệnh nhân Việt Nam.
3. Quyết định thứ tự ưu tiên hành trình người dùng.
4. Đánh giá nội dung/giao diện có dễ hiểu và thực sự hữu ích không.
5. Xây mạng lưới reviewer/đối tác phù hợp theo thời gian.
6. Quyết định khi nào dự án đủ trưởng thành để mở rộng tính năng hoặc quốc gia.
7. Không để tốc độ, số lượng nội dung hay tính năng AI làm suy yếu safety, privacy và evidence integrity.

## Agent phải báo cho bạn như thế nào?

Với thay đổi không nhỏ, agent phải giải thích bằng tiếng Việt:
- **Vấn đề:** đang giải quyết chuyện gì?
- **Vì sao làm bây giờ:** có thực sự cần không?
- **Lợi ích:** dự án/người dùng được gì?
- **Rủi ro/đánh đổi:** có thể hỏng ở đâu?
- **Bạn cần quyết định gì:** nếu có.
- **Xong khi nào:** tiêu chí hoàn thành cụ thể.

Nếu agent chỉ đưa code, schema hoặc thuật ngữ nghiên cứu mà không giải thích tác động sản phẩm thì phần báo cáo cho chủ dự án chưa đạt yêu cầu.

## Hệ thống “trí nhớ” của repo

- `AGENTS.md` — agent phải làm việc như thế nào.
- `CONTINUITY.md` — dự án hiện đang ở đâu.
- `ROADMAP.md` — dự án sẽ đi đâu.
- `plans/` — giai đoạn hiện tại phải làm gì và khi nào được coi là xong.
- `docs/ARCHITECTURE.md` — source-of-truth, boundary và critical path.
- `docs/adr/` — tại sao các quyết định kiến trúc lâu dài đã được chọn.
- `docs/CHANGE_MAP.md` — thay đổi loại X thì phải kiểm tra tài liệu Y nào.
- `CHANGELOG.md` — những thay đổi đáng chú ý đã xảy ra.
- Git history / Issue / PR — bằng chứng chi tiết về việc đã thực hiện.

Mục tiêu là để một agent mới có thể tiếp tục dự án **từ repo**, không cần phụ thuộc vào lịch sử chat trước đó.

## Quy tắc ngôn ngữ

- Tài liệu nội bộ: ưu tiên một bản canonical; dùng browser/AI translation khi cần.
- `OWNER_GUIDE.vi.md`: giữ tiếng Việt vì đây là bản định hướng được viết riêng cho vai trò chủ dự án, không phải bản mirror.
- `README.vi.md`: giữ làm cửa vào cho cộng đồng Việt Nam trong giai đoạn đầu.
- Nội dung y khoa dành cho bệnh nhân Việt Nam: phải có tiếng Việt được xây/review như sản phẩm thật, không chỉ dựa mù quáng vào dịch tự động.
- Không tạo hai hệ thống evidence độc lập Việt/Anh.
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