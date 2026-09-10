# Knee Knowledge Commons

**Kho tri thức mở, có nguồn và có kiểm chứng dành cho người gặp chấn thương khớp gối — được xây dựng cùng bệnh nhân, bác sĩ, nhà nghiên cứu và AI.**

Knee Knowledge Commons là dự án cộng đồng nhằm giúp người gặp chấn thương khớp gối tránh những sai lầm do thiếu thông tin, hiểu rõ hơn tình trạng và các lựa chọn của mình, chuẩn bị câu hỏi tốt hơn, và tham gia hiệu quả hơn vào quá trình ra quyết định cùng chuyên gia y tế phù hợp.

Trọng tâm ban đầu là các chấn thương dây chằng và sụn chêm, đặc biệt ACL và sụn chêm. Mục tiêu dài hạn là một kho tri thức đa ngôn ngữ, thân thiện với bệnh nhân, kết hợp bằng chứng y khoa đã được review với kinh nghiệm thực tế được gắn nhãn rõ ràng.

> **Chiến lược khởi đầu: Việt Nam trước, sẵn sàng mở rộng toàn cầu (Vietnam-first, global-ready).** Dự án sẽ thử nghiệm nhu cầu, nội dung, trải nghiệm người dùng và quy trình đóng góp đầu tiên tại Việt Nam. Tuy nhiên kiến trúc dữ liệu, nguồn dẫn, quy tắc quản trị và hệ thống AI phải được thiết kế ngay từ đầu để có thể mở rộng quốc tế mà không phải làm lại.

## Dự án này là gì?

- Một nguồn tri thức có lịch sử thay đổi, có thể review và truy ngược nguồn.
- Cầu nối giữa bằng chứng nghiên cứu, diễn giải chuyên môn và trải nghiệm thực tế của bệnh nhân.
- Nền tảng để xây website thân thiện với bệnh nhân, tìm kiếm, hướng dẫn chuẩn bị quyết định và AI hỏi–đáp có nguồn.
- Một quy trình mở trong đó AI hỗ trợ nghiên cứu, sắp xếp, dịch, kiểm tra và bảo trì; con người vẫn chịu trách nhiệm với những thay đổi có tác động lớn.

## Dự án này không phải là gì?

- Không thay thế bác sĩ hoặc chuyên gia y tế.
- Không chẩn đoán cá nhân hoặc kê/ra phác đồ điều trị cá nhân hóa.
- Trải nghiệm của một bệnh nhân không phải bằng chứng rằng một phương pháp điều trị có hiệu quả.
- Nội dung do AI tạo không được coi là sự thật y khoa nếu chưa có nguồn phù hợp và review cần thiết.
- Repo GitHub công khai không phải nơi lưu hồ sơ bệnh án, MRI/DICOM, dữ liệu sức khỏe có thể nhận dạng hay câu chuyện bệnh nhân riêng tư.

## Nguyên tắc sản phẩm

> **GitHub là nơi quản trị tri thức phía sau. Website tương lai là cửa chính cho bệnh nhân và phần lớn người đóng góp.**

Người bệnh, bác sĩ và nhà nghiên cứu về lâu dài nên có thể đọc, tìm kiếm, hỏi, góp ý và đóng góp qua website đơn giản. GitHub vẫn dành cho người thích làm trực tiếp trên repo, reviewer, maintainer, developer và agent AI.

## Việt Nam trước, nhưng không xây hệ thống chỉ dùng được ở Việt Nam

Trong giai đoạn đầu:
- tiếng Việt là ngôn ngữ chính cho nội dung hướng tới bệnh nhân;
- nghiên cứu người dùng và thử nghiệm UX tập trung ở Việt Nam;
- quy trình khám chữa, bảo hiểm, thuật ngữ và hạn chế tiếp cận tại Việt Nam được lưu như **bối cảnh địa phương**, không biến thành sự thật y khoa chung cho mọi quốc gia;
- evidence, schema, ID, nguồn dẫn và kiến trúc AI vẫn trung tính về quốc gia/ngôn ngữ;
- chỉ mở rộng quốc tế sau khi quy trình đầu–cuối hoạt động ổn ở thị trường đầu tiên.

## Bốn lớp tri thức

1. **Bằng chứng (Evidence)** — guideline, systematic review, thử nghiệm, nghiên cứu quan sát và các nguồn có thể truy ngược.
2. **Diễn giải chuyên môn (Clinical interpretation)** — ý kiến/diễn giải của chuyên gia được ghi rõ nguồn gốc, không tự biến thành bằng chứng.
3. **Kinh nghiệm cộng đồng (Community experience)** — trải nghiệm tự báo cáo, luôn được gắn nhãn là trải nghiệm.
4. **Tổng hợp (Synthesis)** — nội dung đã review, giữ nguyên mức độ chưa chắc chắn, khác biệt giữa nhóm bệnh nhân và mâu thuẫn giữa nguồn.

## Cấu trúc repo

- `knowledge/` — tri thức đã được duyệt để phục vụ người dùng.
- `evidence/` — evidence record và ghi chú nguồn.
- `community-experience/` — quy tắc và kết quả tổng hợp từ trải nghiệm; dữ liệu riêng tư/raw không nằm ở đây.
- `schemas/` — cấu trúc dữ liệu cho máy/agent.
- `agents/` — hướng dẫn cho từng loại agent.
- `docs/` — kiến trúc, sản phẩm, governance, policy và tài liệu hỗ trợ.
- `plans/` — kế hoạch triển khai theo từng giai đoạn.
- `.github/` — workflow đóng góp/review.

## Các quy tắc không được bỏ qua

Trước khi thay đổi dự án hoặc giao agent làm việc, cần tuân thủ:
- `AGENTS.md`
- `MEDICAL_SAFETY.md`
- `PRIVACY.md`
- `GOVERNANCE.md`
- `CONTRIBUTING.md`

Các tài liệu cần chủ dự án ra quyết định phải có bản tiếng Việt hoặc phần tóm tắt tiếng Việt dễ hiểu.

## Trạng thái hiện tại

**Foundation v0.1 đã hoàn thành.** Bước thực thi tiếp theo là một pilot rất hẹp: chứng minh một hành trình hoàn chỉnh cho người Việt vừa được chẩn đoán **ACL có hoặc không kèm tổn thương sụn chêm**.

Pilot chỉ được coi là thành công khi có thể truy ngược:

`câu hỏi bệnh nhân bằng tiếng Việt`
→ `câu trả lời đã duyệt`
→ `knowledge claim`
→ `evidence record`
→ `nguồn gốc có thể kiểm tra`.

Xem kế hoạch chi tiết: [`plans/0002-acl-meniscus-knowledge-pilot.vi.md`](plans/0002-acl-meniscus-knowledge-pilot.vi.md).
