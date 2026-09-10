# Quản trị dự án

> Bản tiếng Việt dành cho chủ dự án và cộng đồng Việt Nam. Bản canonical: [`GOVERNANCE.md`](GOVERNANCE.md).

Knee Knowledge Commons là dự án cộng đồng, nhưng **độ phổ biến, tự động hóa bằng AI hay chức danh chuyên môn đều không được phép bỏ qua quy trình kiểm tra bằng chứng và an toàn**.

## Vai trò

- **Maintainer:** giữ roadmap, release, sức khỏe repo và thực thi governance.
- **Clinical reviewer:** chuyên gia đủ phù hợp để kiểm tra ý nghĩa y khoa trong phạm vi chuyên môn của họ.
- **Evidence reviewer:** kiểm tra nguồn, phương pháp, mức chắc chắn và việc tóm tắt có đúng với nguồn không.
- **Community reviewer:** người có trải nghiệm thực tế, giúp kiểm tra độ rõ ràng, câu hỏi còn thiếu và cách phản ánh trải nghiệm cộng đồng.
- **Technical maintainer:** lo website, data, security, AI integration, test và deploy; họ không được quyết định sự thật y khoa chỉ vì họ biết kỹ thuật.
- **AI agent:** hỗ trợ tìm nguồn, trích xuất, format, dịch, kiểm tra citation, phát hiện trùng/lỗi và chuẩn bị PR; agent **không phải người phê duyệt cuối**.

## Phân loại thay đổi

### Class A — rủi ro thấp
Ví dụ lỗi chính tả, link hỏng, format, tài liệu kỹ thuật không làm thay đổi ý nghĩa y khoa. Chỉ cần review maintainer thông thường.

### Class B — cấu trúc / sản phẩm
Ví dụ schema, taxonomy, navigation, UX hoặc bản dịch không làm thay đổi ý nghĩa y khoa. Cần maintainer phù hợp và test khi cần.

### Class C — thay đổi ý nghĩa y khoa
Bất kỳ claim mới/sửa nào về chẩn đoán, điều trị, phẫu thuật, phục hồi, tiên lượng, chống chỉ định hoặc quay lại vận động. Phải có nguồn truy được và human review có chuyên môn phù hợp trước khi trở thành knowledge đã duyệt cho bệnh nhân.

### Class D — an toàn / privacy quan trọng
Ví dụ cảnh báo đi cấp cứu, cách xử lý dữ liệu bệnh nhân, consent, xóa dữ liệu, quyền truy cập hoặc disclosure AI. Ngoài review bình thường còn cần review riêng về safety/privacy.

## Tính toàn vẹn của evidence

- Citation phải thực sự hỗ trợ claim đứng gần nó.
- Không tự suy ra “mức bằng chứng cao” chỉ vì loại nghiên cứu nghe có vẻ mạnh.
- Trải nghiệm bệnh nhân vẫn là community knowledge, không phải bằng chứng hiệu quả điều trị.
- Không được che kết quả mâu thuẫn, tiêu cực hoặc không có khác biệt.

## Xung đột lợi ích

Người đóng góp/reviewer cần khai báo lợi ích tài chính, nghề nghiệp, phòng khám, thiết bị, sản phẩm hoặc phương pháp điều trị có liên quan. Khai báo không đồng nghĩa tự động loại khỏi review, nhưng giúp cộng đồng đánh giá minh bạch.

## Quy tắc merge

Agent AI có thể mở PR nhưng không được là người duyệt duy nhất cho Class C hoặc D. Khi cộng đồng reviewer lớn hơn, branch protection và CODEOWNERS phải được siết chặt hơn.

## Thay đổi governance

Muốn sửa `GOVERNANCE.md`, `MEDICAL_SAFETY.md`, `PRIVACY.md` hoặc các bất biến cốt lõi phải dùng PR riêng, nói rõ:
- vì sao cần đổi;
- rủi ro;
- phương án khác;
- tác động chuyển đổi.

Chủ dự án cần được cung cấp giải thích tiếng Việt dễ hiểu trước khi phê duyệt thay đổi loại này.
