# Plan 0002 — Pilot Việt Nam: vừa được chẩn đoán ACL ± sụn chêm

> Bản này dành cho chủ dự án. Bản canonical/chi tiết tương ứng: [`0002-acl-meniscus-knowledge-pilot.md`](0002-acl-meniscus-knowledge-pilot.md).

**Trạng thái:** Đã lên kế hoạch

## Mục tiêu

Chứng minh **một chuỗi hoàn chỉnh đầu–cuối** trước khi xây kho tri thức ACL/sụn chêm lớn.

Câu hỏi pilot:

> Một người ở Việt Nam vừa được thông báo có tổn thương ACL, có hoặc không kèm tổn thương sụn chêm. Kết quả đó có nghĩa gì, điều gì có thể/chưa thể kết luận, điều gì thường cần làm rõ tiếp theo và nên chuẩn bị câu hỏi gì khi gặp chuyên gia y tế?

Pilot này **không** nhằm trả lời thay bác sĩ rằng người đó nên mổ hay không, nên tập bài gì, dùng thuốc gì hay khi nào quay lại thể thao.

## Vì sao chọn đúng câu hỏi này?

Nó đủ nhỏ để hoàn thành nhưng đủ khó để kiểm tra kiến trúc dự án:
- AI phải phân biệt ACL đơn thuần, sụn chêm đơn thuần và ACL + sụn chêm;
- không được áp dụng guideline ngoài phạm vi đối tượng của nó;
- phải giải thích được điều chưa chắc chắn bằng tiếng Việt dễ hiểu;
- mọi claim quan trọng phải truy ngược được về nguồn;
- phải tách evidence quốc tế với bối cảnh khám chữa riêng tại Việt Nam;
- AI hỗ trợ nhưng không được tự trở thành người quyết định y khoa.

## Bạn — chủ dự án — cần làm gì?

Bạn **không cần tự đọc hàng chục paper**.

Vai trò của bạn trong pilot là:
1. Đưa ra hoặc duyệt một nhóm nhỏ câu hỏi thực tế mà bệnh nhân Việt Nam thường thắc mắc khi mới được chẩn đoán.
2. Đọc bản tiếng Việt cuối và kiểm tra xem người không chuyên có hiểu được không.
3. Khi đủ an toàn, giúp tìm khoảng 5–10 người từng/đang trải qua ACL hoặc sụn chêm để thử trải nghiệm.
4. Giúp tìm reviewer phù hợp như bác sĩ chấn thương chỉnh hình/y học thể thao và/hoặc chuyên gia phục hồi chức năng tùy nội dung.
5. Quyết định pilot đã đủ hữu ích để nhân rộng hay cần sửa lại.

Agent AI lo phần tìm nguồn, trích xuất, tạo evidence record, kiểm tra citation, phát hiện mâu thuẫn/phạm vi, soạn bản nháp và chuẩn bị nội dung cho reviewer.

## Chuỗi cần chứng minh

```text
Câu hỏi thật của bệnh nhân Việt Nam
        ↓
Nguồn y khoa gốc
        ↓
Evidence records có cấu trúc
        ↓
Kiểm tra phạm vi + citation + mâu thuẫn
        ↓
Tổng hợp tri thức
        ↓
Human review phù hợp
        ↓
Bài giải thích tiếng Việt đã duyệt
        ↓
AI Q&A chỉ dựa trên knowledge đã duyệt
        ↓
Người dùng có thể truy lại nguồn
```

## Các gói công việc

### WP1 — Xác định câu hỏi thật của bệnh nhân

Tạo bộ câu hỏi ngắn xoay quanh thời điểm vừa được chẩn đoán, ví dụ:
- “Đứt/rách ACL nghĩa là gì?”
- “Có kèm rách sụn chêm thì có ý nghĩa gì?”
- “Chỉ từ một dòng MRI có thể biết được những gì và chưa biết được gì?”
- “Tổn thương nào đi kèm có thể làm thay đổi cuộc trao đổi với bác sĩ?”
- “Tôi nên chuẩn bị câu hỏi gì khi đi khám tiếp?”

Ở bước này **không tự viết kết luận y khoa**.

### WP2 — Agent xây danh sách nguồn nhỏ nhưng chất lượng

Ưu tiên:
- guideline lớn và hiện hành;
- systematic review khi cần;
- consensus/research chất lượng cho khoảng trống guideline chưa giải đáp;
- tài liệu giáo dục bệnh nhân chính thức chỉ dùng bổ trợ cách diễn đạt, không thay thế evidence review.

Mỗi nguồn phải ghi rõ **đối tượng áp dụng và đối tượng bị loại trừ**.

### WP3 — Tạo evidence record

Agent dùng schema đã có để lưu:
- nguồn;
- loại nghiên cứu/guideline;
- nhóm bệnh nhân;
- bối cảnh tổn thương;
- ngoại lệ/phạm vi không áp dụng;
- giới hạn;
- trạng thái review;
- mức chắc chắn chỉ khi nguồn/phương pháp thực sự hỗ trợ.

### WP4 — Kiểm tra phạm vi, mâu thuẫn và citation

Trước khi viết nội dung cho bệnh nhân, phải trả lời rõ:
- nguồn này dành cho ACL đơn thuần, sụn chêm đơn thuần hay ACL + sụn chêm?
- có đang áp dụng khuyến cáo cho nhóm bị guideline loại trừ không?
- các nguồn uy tín có mâu thuẫn không?
- citation có thực sự hỗ trợ đúng claim không?
- có đang biến điều “chưa chắc” thành kết luận chắc chắn không?

### WP5 — Soạn một trang tiếng Việt duy nhất

Nội dung gợi ý:
1. Câu trả lời ngắn.
2. ACL/sụn chêm được hiểu thế nào từ thông tin hiện có.
3. Điều gì chưa thể kết luận chỉ từ chẩn đoán/báo cáo.
4. Yếu tố hoặc tổn thương đi kèm có thể quan trọng.
5. Thông tin nào thường cần làm rõ tiếp.
6. Câu hỏi nên chuẩn bị khi gặp bác sĩ/chuyên gia phù hợp.
7. Điều chưa chắc chắn hoặc nguồn không áp dụng trực tiếp.
8. Nguồn và trạng thái review.

### WP6 — Human review

Các claim làm thay đổi ý nghĩa y khoa phải được reviewer có chuyên môn phù hợp kiểm tra.

AI không được là người duyệt cuối duy nhất.

### WP7 — Prototype AI hỏi–đáp

Sau khi knowledge page được duyệt, thử một AI assistant tối thiểu chỉ được phép lấy từ approved knowledge.

Nó phải:
- dẫn nguồn;
- phân biệt evidence, local context và community experience;
- biết nói “repo chưa đủ dữ liệu để kết luận”;
- không biến câu trả lời giáo dục thành quyết định điều trị cá nhân.

Dùng Gemini, OpenAI hay model khác đều được; hệ thống không được phụ thuộc cố định một hãng.

### WP8 — Thử với nhóm nhỏ tại Việt Nam

Mục tiêu là kiểm tra sản phẩm, **không phải nghiên cứu lâm sàng**.

Khoảng 5–10 người là đủ cho vòng đầu để xem họ có:
- hiểu nội dung không;
- biết cái gì chưa chắc không;
- tìm được câu hỏi cần hỏi bác sĩ không;
- phân biệt bằng chứng với kinh nghiệm/ý kiến không;
- hiểu nguồn ở đâu không;
- chỉ ra chỗ khó hiểu hoặc còn thiếu không.

Không đưa dữ liệu sức khỏe nhận dạng được vào GitHub.

## Pilot không làm gì?

Chưa làm:
- bách khoa ACL đầy đủ;
- bách khoa sụn chêm đầy đủ;
- engine quyết định mổ/không mổ;
- phác đồ rehab cá nhân;
- AI đọc MRI/DICOM để chẩn đoán;
- xếp hạng bác sĩ/bệnh viện;
- thu hồ sơ bệnh nhân riêng tư trên GitHub;
- mở rộng quốc tế ngay.

## Khi nào coi là thành công?

Phải chứng minh được chuỗi:

`Câu hỏi bệnh nhân bằng tiếng Việt`
→ `câu trả lời đã duyệt`
→ `canonical knowledge claim`
→ `evidence record`
→ `nguồn gốc có thể kiểm tra`.

Ngoài ra:
- claim quan trọng đã có human review phù hợp;
- phạm vi và ngoại lệ của nguồn nhìn thấy rõ;
- không trộn ACL đơn thuần / meniscus đơn thuần / ACL + meniscus;
- mâu thuẫn hoặc thiếu evidence không bị che đi;
- bối cảnh Việt Nam không bị biến thành bằng chứng toàn cầu;
- người dùng mục tiêu hiểu được bản tiếng Việt;
- prototype AI không trả lời vượt khỏi approved knowledge;
- không có dữ liệu sức khỏe định danh trong Git history.

## Sau pilot bạn cần quyết định gì?

Chỉ có ba lựa chọn:
- **Lặp lại:** pilot chưa đủ tốt → sửa và chạy lại.
- **Mở rộng:** pipeline đã ổn → dùng cùng mẫu cho hành trình tiếp theo.
- **Thiết kế lại:** phát hiện kiến trúc/evidence workflow có vấn đề → sửa nền móng trước khi mở rộng.

Hành trình tiếp theo phải được chọn dựa trên **vấn đề thông tin quan trọng nhất của bệnh nhân Việt Nam**, không phải vì phần đó dễ code hơn.
