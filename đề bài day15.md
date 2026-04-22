Danh sách hoạt động chi tiết để các nhóm follow
Ngày tổng kết Phase 1 - từ recap đến mini project nhóm

Mục tiêu của tài liệu
Tài liệu này mô tả nhóm cần làm gì theo từng khung giờ, đầu ra cần nộp ở mỗi hoạt động, và checklist để không bị lệch mục tiêu trong ngày.

1. Mục tiêu cuối ngày của mỗi nhóm
Đến cuối ngày, mỗi nhóm cần hoàn thành:

Một bộ worksheet buổi sáng;

Một mini project proposal dạng 5-7 slide hoặc 1 poster/1-page proposal;

Một kết luận rõ ràng về deployment, cost, reliability và định hướng Track Phase 2;

Các phiếu chấm peer review cho những đội còn lại trong zone.

2. Checklist chuẩn bị đầu ngày
Nhóm đã có đủ thành viên 4-6 người.

Nhóm đã chọn chủ đề hoặc scenario card.

Nhóm đã cử các vai trò chính: Product lead, Architect, Cost lead, Reliability lead, Presenter.

Nhóm đã có nơi ghi chép chung (giấy A3 hoặc file chung).

3. Buổi sáng - hoạt động và đầu ra
3.1. 08:00-08:15 | Khởi động và mini reflection
Nhóm cần làm gì?

Mỗi người viết nhanh 3 ý: điều học được nhiều nhất, điểm yếu nhất, hướng muốn đi sâu;

Cử một người tổng hợp để nhóm nhìn thấy điểm mạnh/điểm yếu chung.

Đầu ra cần có:

3-5 ý tổng hợp của nhóm về hiện trạng năng lực.

3.2. 08:15-08:40 | Hoạt động 1 - Learning Timeline
Mục tiêu: Xác định nhóm đã build được gì trong 15 ngày và chọn đúng dự án để phân tích production.

Nhóm cần làm gì?

Liệt kê 2-3 kỹ năng nhóm tự tin nhất;

Mô tả ngắn sản phẩm/agent nhóm đã làm hoặc scenario được chọn;

Chốt 1 chủ đề sẽ theo xuyên suốt cả ngày.

Câu hỏi nhóm phải trả lời:

Sản phẩm này giải quyết bài toán gì?

Ai là người dùng chính?

Vì sao chủ đề này phù hợp để phân tích deployment và cost?

Đầu ra: Worksheet 0.

3.3. 08:40-09:25 | Hoạt động 2 - Enterprise Deployment Clinic
Mục tiêu: Hiểu vì sao deploy demo và deploy enterprise là hai bài toán khác nhau.

Nhóm cần làm gì?

Xác định bối cảnh tổ chức/khách hàng sử dụng hệ thống;

Liệt kê dữ liệu mà hệ thống sẽ động đến;

Đánh giá mức độ nhạy cảm của dữ liệu;

Liệt kê 3 ràng buộc enterprise lớn nhất;

Chọn Cloud, On-prem hoặc Hybrid;

Viết 2 lý do vì sao chọn mô hình đó.

Gợi ý thảo luận:

Có cần audit trail không?

Dữ liệu có được rời khỏi tổ chức không?

Có cần tích hợp hệ thống cũ hoặc quy trình phê duyệt không?

Nếu trả lời sai thì ai bị ảnh hưởng đầu tiên?

Đầu ra: Worksheet 1.

3.4. 09:35-10:15 | Hoạt động 3 - Cost Anatomy Lab
Mục tiêu: Bóc tách cost của AI system thay vì chỉ nhìn vào token/API.

Nhóm cần làm gì?

Ước lượng số user/ngày, request/ngày, peak traffic;

Ước lượng input/output tokens nếu dùng LLM API;

Liệt kê các lớp cost: token, compute, storage, human review, logging, maintenance;

Tính sơ bộ cost ở mức MVP;

Suy nghĩ xem khi số user tăng 5x hoặc 10x thì phần nào tăng mạnh nhất.

Câu hỏi nhóm phải trả lời:

Cost driver lớn nhất của hệ thống là gì?

Hidden cost nào dễ bị quên nhất?

Đội có chỗ nào đang ước lượng quá lạc quan không?

Đầu ra: Worksheet 2.

3.5. 10:15-10:50 | Hoạt động 4 - Cost Optimization Debate
Mục tiêu: Chọn đúng chiến lược tối ưu thay vì tối ưu theo phong trào.

Nhóm cần làm gì?

Chọn 3 chiến lược optimization phù hợp nhất;

Với mỗi chiến lược, viết rõ tiết kiệm phần nào, lợi ích, trade-off và thời điểm áp dụng;

Chốt chiến lược nào làm ngay, chiến lược nào để sau.

Các chiến lược thường gặp:

Model routing;

Semantic caching;

Prompt compression;

Smaller/self-hosted model khi volume đủ lớn;

Selective inference hoặc phân tách user/request.

Đầu ra: Worksheet 3.

3.6. 10:50-11:25 | Hoạt động 5 - Scaling & Reliability Tabletop
Mục tiêu: Luyện phản ứng khi hệ thống gặp tải tăng hoặc provider lỗi.

Nhóm cần làm gì?

Xem xét 3 tình huống: traffic tăng đột biến, provider timeout, response chậm;

Với mỗi tình huống, mô tả tác động tới user;

Ghi phản ứng ngắn hạn và giải pháp dài hạn;

Chọn các metric cần monitor;

Viết fallback proposal.

Gợi ý:

Request nào cần real-time, request nào có thể async?

Có cần queue, circuit breaker hay retry policy không?

Fallback nên là model khác, rule-based flow hay human escalation?

Đầu ra: Worksheet 4.

3.7. 11:25-11:45 | Hoạt động 6 - Skills Map & Track Direction
Mục tiêu: Kết nối dự án với năng lực hiện tại và hướng đi Phase 2.

Nhóm cần làm gì?

Mỗi thành viên tự chấm 1-5 ở ba mảng: Business/Product, Infra/Data/Ops, AI Engineering/Application;

Cả nhóm thảo luận xem điểm mạnh nằm ở đâu;

Chọn Track Phase 2 phù hợp nhất;

Ghi 2-3 kỹ năng cần bù nếu muốn tiếp tục dự án này.

Đầu ra: Worksheet 5.

4. Buổi chiều - làm mini project và thuyết trình theo zone
4.1. 13:30-13:45 | Chia zone và chốt vai trò
Checklist:

Đã biết zone của nhóm.

Đã có presenter và người trả lời Q&A.

Đã thống nhất format nộp bài: slide hoặc poster.

4.2. 14:00-15:10 | Sprint 1 - Xây nội dung proposal
Nhóm cần hoàn thành 7 khối nội dung:

Project overview;

Enterprise context;

Deployment choice;

Cost analysis (MVP + Growth);

Optimization plan;

Reliability plan;

Track recommendation + next step.

4.3. 15:20-16:00 | Sprint 2 - Đóng gói thành bản trình bày
Cấu trúc slide đề xuất:

Tên dự án, user, bài toán

Bối cảnh enterprise và ràng buộc

Kiến trúc triển khai đề xuất

Cost anatomy

Cost optimization

Reliability & scaling

Track đề xuất và bước đi tiếp theo

4.4. 16:10-17:20 | Zone presentation + peer review
Format cho mỗi đội:

5 phút trình bày;

3 phút Q&A/phản biện;

2 phút các đội khác chấm phiếu.

Luật bắt buộc:

Đội không tự chấm mình;

Mỗi đội phải đặt ít nhất 1 câu hỏi thật cho ít nhất 2 đội khác;

Phản biện phải có: 1 điểm mạnh, 1 điểm cần cải thiện, 1 đề xuất thay thế.

5. Checklist nộp cuối ngày
Worksheet 0-5 của nhóm

Slide hoặc poster mini project

Phiếu chấm cho các đội khác trong zone

Kết luận Track Phase 2 của nhóm

6. Mẫu trang ghi chú nhanh của nhóm
Team note sheet

Tên nhóm:
Chủ đề:
3 ràng buộc enterprise lớn nhất:
Cost driver lớn nhất:
3 chiến lược optimize được chọn:
Fallback / reliability plan ngắn gọn:
Track Phase 2 đề xuất: