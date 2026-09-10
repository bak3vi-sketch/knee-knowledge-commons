# Lộ trình phát triển

> Bản này dành cho chủ dự án và người đọc tiếng Việt. Bản kỹ thuật/canonical tương ứng: [`ROADMAP.md`](ROADMAP.md).

Lộ trình của Knee Knowledge Commons được chia theo **điều kiện hoàn thành**, không chạy theo ngày tháng. Chỉ mở rộng khi giai đoạn trước đã chứng minh được rằng quy trình đủ an toàn, có nguồn và thực sự hữu ích.

## Chiến lược chung — Việt Nam trước, sẵn sàng toàn cầu

Dự án sẽ phát triển và thử nghiệm sản phẩm đầu tiên tại Việt Nam. Tuy nhiên kiến trúc dữ liệu, evidence, citation, schema, AI gateway và governance phải giữ tính quốc tế để sau này mở rộng bằng cách bản địa hóa, không phải xây lại.

Thông tin riêng của Việt Nam như hệ thống khám chữa, bảo hiểm, thuật ngữ, cách chuyển tuyến và khả năng tiếp cận dịch vụ phải được tách thành **bối cảnh địa phương**, không trộn vào bằng chứng y khoa chung.

## Giai đoạn 0 — Nền móng

**Mục tiêu:** làm cho dự án khó bị AI hoặc contributor vô tình lái sai hướng.

Đã có:
- mission, governance, privacy, medical safety;
- rule cho agent;
- mô hình evidence/content;
- kiến trúc hệ thống;
- template đóng góp và review;
- cấu trúc pilot ACL + sụn chêm.

**Trạng thái:** hoàn thành Foundation v0.1.

## Giai đoạn 1A — Pilot Việt Nam: vừa được chẩn đoán ACL ± sụn chêm

**Mục tiêu:** chứng minh một chuỗi đầu–cuối duy nhất trước khi xây kho ACL/sụn chêm lớn.

Câu hỏi pilot:

> Một người ở Việt Nam vừa được thông báo có tổn thương ACL, có thể kèm tổn thương sụn chêm. Kết quả đó có nghĩa gì, điều gì có thể/chưa thể kết luận, điều gì thường cần làm rõ tiếp theo và nên chuẩn bị câu hỏi gì khi gặp chuyên gia y tế?

Cần tạo được:
- bộ nguồn nhỏ nhưng chất lượng;
- evidence record có phạm vi và ngoại lệ rõ;
- kiểm tra riêng isolated ACL / isolated meniscus / ACL + meniscus;
- kiểm tra citation và mâu thuẫn;
- một trang giải thích tiếng Việt đã review;
- một prototype AI hỏi–đáp chỉ dựa trên nội dung đã duyệt;
- phản hồi thử nghiệm từ nhóm nhỏ người dùng Việt Nam khi phù hợp.

**Điều kiện hoàn thành:** truy ngược được từ câu hỏi tiếng Việt → câu trả lời → claim → evidence record → nguồn gốc, đồng thời nhìn thấy giới hạn và phạm vi áp dụng.

## Giai đoạn 1B — Mở rộng ACL + sụn chêm

Chỉ làm sau khi 1A thành công.

Các hành trình tiếp theo có thể gồm:
- hiểu các lựa chọn và yếu tố ảnh hưởng đến quyết định điều trị;
- chuẩn bị đi khám / chuẩn bị phẫu thuật nếu có;
- prehab;
- các giai đoạn và cách đánh giá phục hồi;
- khái niệm quay lại chạy và thể thao;
- các thiếu hụt thông tin người bệnh thường gặp.

Không mở rộng theo kiểu tạo thật nhiều bài. Mỗi hành trình phải dùng lại được cùng một pipeline evidence → review → content.

## Giai đoạn 2 — Hệ thống đóng góp

**Mục tiêu:** bác sĩ, nhà nghiên cứu và bệnh nhân có thể đóng góp mà không phải học GitHub.

Website sau này sẽ cung cấp form/hội thoại thuận tiện. Agent xử lý phần chuẩn hóa, kiểm tra và chuẩn bị PR. GitHub vẫn là nơi quản lý tri thức công khai và lịch sử thay đổi.

Dữ liệu sức khỏe riêng tư không được đi vào public Git history.

## Giai đoạn 3 — Website MVP tại Việt Nam

**Mục tiêu:** người bình thường dùng tốt trên điện thoại.

Ưu tiên các hành trình:
- vừa chấn thương;
- đã có chẩn đoán/báo cáo hình ảnh;
- đang tìm hiểu lựa chọn điều trị;
- chuẩn bị phẫu thuật;
- đang phục hồi;
- chuẩn bị quay lại chạy/thể thao;
- muốn đóng góp hoặc báo lỗi nội dung.

Website phải ưu tiên tiếng Việt, mobile-first và không buộc người dùng biết GitHub.

## Giai đoạn 4 — AI hỏi–đáp có nguồn

AI chỉ nên trả lời dựa trên knowledge đã duyệt, hiển thị nguồn và mức độ chưa chắc chắn. Hệ thống phải trung lập nhà cung cấp để có thể dùng Gemini, OpenAI hoặc model khác tùy chất lượng, chi phí và privacy.

Trước khi mở rộng ngôn ngữ, phải có bộ test tiếng Việt cho các tình huống khó: hỏi điều trị cá nhân, citation sai, evidence mâu thuẫn, thiếu dữ liệu, privacy và các tình huống cần chuyển sang chuyên gia.

## Giai đoạn 5 — Trí tuệ cộng đồng

Khi đã có đủ trải nghiệm cộng đồng theo cấu trúc, AI có thể giúp tổng hợp:
- những điều người bệnh ước biết sớm;
- sai lầm thông tin thường gặp;
- điểm nghẽn trong hành trình;
- những câu hỏi nghiên cứu mới.

Không được suy ra hiệu quả điều trị chỉ từ câu chuyện bệnh nhân nếu chưa có phương pháp nghiên cứu phù hợp.

## Giai đoạn 6 — Mở rộng quốc tế

Chỉ mở rộng khi hệ thống tại Việt Nam đủ ổn để **localize chứ không rebuild**.

Mở rộng có thể gồm:
- quốc gia/ngôn ngữ khác;
- nhiều loại chấn thương gối hơn;
- mạng lưới bác sĩ/researcher quốc tế;
- governance phân tán hơn;
- so sánh khoảng trống thông tin giữa các hệ thống y tế.

## Chủ dự án cần tập trung vào gì?

Bạn không cần tự đọc và trích hàng loạt nghiên cứu. Vai trò quan trọng nhất là:
- xác định vấn đề thật của bệnh nhân Việt Nam;
- ưu tiên hành trình nào làm trước;
- kiểm tra nội dung có dễ hiểu hay không;
- tìm/thu hút reviewer phù hợp;
- quyết định khi nào một pilot đủ tốt để mở rộng;
- giữ dự án đúng sứ mệnh ban đầu.
