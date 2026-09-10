# Chiến lược ngôn ngữ và bản địa hóa

> Bản tiếng Việt dành cho chủ dự án. Bản canonical: [`TRANSLATION.md`](TRANSLATION.md).

## Nguyên tắc chung

Knee Knowledge Commons phải có nhiều ngôn ngữ nhưng **không được tạo ra nhiều “sự thật y khoa” độc lập theo từng ngôn ngữ**.

Chiến lược hiện tại là **Việt Nam trước, sẵn sàng mở rộng toàn cầu**.

## Giai đoạn đầu tại Việt Nam

- Tiếng Việt là ngôn ngữ chính của nội dung hướng tới bệnh nhân.
- Nghiên cứu người dùng và thử nghiệm UX tập trung tại Việt Nam.
- Thông tin riêng về cách khám chữa, bảo hiểm, thuật ngữ, khả năng tiếp cận dịch vụ... được lưu như **bối cảnh địa phương**.
- Evidence, citation, schema, ID và kiến trúc AI vẫn thiết kế để dùng được quốc tế.

## Khi nào nên dùng tiếng Anh?

Có thể giữ tiếng Anh cho:
- schema/ID để máy và agent đọc;
- tài liệu kỹ thuật/developer;
- architecture;
- metadata evidence gắn với nguồn nghiên cứu quốc tế;
- hợp tác với contributor nước ngoài.

Điều quan trọng là bệnh nhân Việt Nam và chủ dự án **không được bị buộc phải hiểu tiếng Anh kỹ thuật** để sử dụng hoặc điều hành dự án.

## Chính sách dành cho chủ dự án

Bất kỳ tài liệu nào yêu cầu chủ dự án:
- ra quyết định;
- duyệt định hướng;
- hiểu rủi ro đáng kể;
- ưu tiên công việc;
- hiểu policy quan trọng

phải có **bản tiếng Việt** hoặc ít nhất **tóm tắt tiếng Việt** nêu rõ:
- vấn đề;
- vì sao cần làm;
- lợi ích;
- rủi ro/đánh đổi;
- chủ dự án cần quyết định gì;
- điều kiện hoàn thành.

Nếu bản canonical tiếng Anh thay đổi đáng kể, bản Việt phải được cập nhật cùng PR hoặc đánh dấu `STALE` rõ ràng.

## Dịch bằng AI

AI có thể tạo bản dịch nháp. Nhưng nếu việc dịch làm thay đổi ý nghĩa y khoa thì phải review. Không được vì muốn “dễ hiểu” mà biến điều còn chưa chắc chắn thành câu khẳng định chắc chắn.

## Thuật ngữ

Cần có glossary cho các từ có nguy cơ hiểu sai như:
- tên dây chằng;
- kiểu rách sụn chêm;
- thủ thuật/phẫu thuật;
- mốc phục hồi;
- thuật ngữ trong kết quả chẩn đoán/hình ảnh.

Với tiếng Việt nên ghi cả thuật ngữ bác sĩ thường dùng và cách giải thích đời thường cho bệnh nhân khi cần.

## Dịch ngôn ngữ khác với bản địa hóa

Ví dụ một guideline từ quốc gia khác có thể cung cấp evidence y khoa hữu ích, nhưng:
- số điện thoại khẩn cấp;
- cách chuyển tuyến;
- bảo hiểm;
- phạm vi hành nghề;
- khả năng tiếp cận MRI/PT/bác sĩ

không được tự động áp dụng sang Việt Nam hoặc ngược lại.

Hệ thống nên tách ba lớp:

`evidence/claim dùng chung`
→ `cách trình bày theo ngôn ngữ`
→ `bối cảnh theo quốc gia/địa phương`.

Đây là nền tảng để sau này mở rộng ra thế giới mà không phải xây lại kho tri thức.
