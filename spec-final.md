# SPEC — AI Product Hackathon

**Nhóm:** 20.5
**Track:** ☑ XanhSM
**Problem statement:** Khách hàng Xanh SM mất thời gian tìm kiếm thông tin dịch vụ, giá cước, chính sách qua nhiều kênh rời rạc — AI chatbot tổng hợp FAQ chính thức + phản hồi mạng xã hội để trả lời tức thì và gợi ý dịch vụ phù hợp ngay trong app.

---

## 1. AI Product Canvas

|   | Value | Trust | Feasibility |
|---|-------|-------|-------------|
| **Câu hỏi** | User nào? Pain gì? AI giải gì? | Khi AI sai thì sao? User sửa bằng cách nào? | Cost/latency bao nhiêu? Risk chính? |
| **Trả lời** | Hành khách Xanh SM (đặc biệt người dùng mới, khách du lịch) mất 5–10 phút tìm thông tin giá cước, khu vực phục vụ, chính sách hoàn tiền qua hotline hoặc website — AI trả lời tức thì (<3s), gợi ý đúng dịch vụ (Car / Premium / Bike / Express) và cung cấp nút đặt xe ngay | AI trả lời sai giá hoặc khu vực phục vụ → user đặt xe nhầm dịch vụ, bị tính phí sai → user thấy disclaimer "Thông tin có thể thay đổi, xác nhận qua app khi đặt xe", có nút "Báo sai" 1 click, agent human escalation qua hotline 1900 2088 | ~$0.002–0.005/query (Gemini Flash), latency <3s, risk chính: thông tin giá/khu vực thay đổi thường xuyên mà knowledge base chưa cập nhật kịp |

**Automation hay augmentation?** ☑ Augmentation
Justify: AI trả lời câu hỏi + gợi ý dịch vụ, nhưng user tự quyết định có đặt xe không. Với câu hỏi phức tạp (khiếu nại, tai nạn), AI escalate sang agent người thật — không tự xử lý.

**Learning signal:**

1. User correction đi vào đâu? → Log "Báo sai" + nội dung câu hỏi/câu trả lời → team content review → cập nhật knowledge base hàng tuần
2. Product thu signal gì? → Implicit: tỷ lệ user click nút dịch vụ sau khi chatbot trả lời (conversion). Explicit: thumbs up/down sau mỗi câu trả lời. Escalation rate (% câu hỏi phải chuyển sang hotline)
3. Data thuộc loại nào? ☑ Domain-specific · ☑ Real-time (giá, khuyến mãi thay đổi) · ☑ Human-judgment (phân loại câu hỏi mạng xã hội)
   Có marginal value không? Có — FAQ Xanh SM + phản hồi mạng xã hội về dịch vụ taxi điện VN là domain rất đặc thù, model chung không có.

---

## 2. User Stories — 4 paths

### Feature 1: Trả lời câu hỏi FAQ về dịch vụ & giá cước

**Trigger:** User mở chatbot trong app Xanh SM → gõ câu hỏi về dịch vụ (VD: "Xanh SM Bike giá bao nhiêu?", "Có phục vụ sân bay Nội Bài không?")

| Path | Câu hỏi thiết kế | Mô tả |
|------|-------------------|-------|
| Happy — AI đúng, tự tin | User thấy gì? Flow kết thúc ra sao? | AI trả lời đúng giá cước Xanh SM Bike (mở cửa 10.000đ + 4.500đ/km), kèm nút "Đặt Xanh SM Bike ngay" → user click đặt xe |
| Low-confidence — AI không chắc | System báo "không chắc" bằng cách nào? | AI hiển thị: "Tôi không chắc chắn về thông tin này. Bạn có thể xác nhận qua Hotline 1900 2088 hoặc kiểm tra trực tiếp khi đặt xe" + nút gọi hotline |
| Failure — AI sai | User biết AI sai bằng cách nào? Recover ra sao? | AI báo sai khu vực phục vụ → user đặt xe thất bại → user thấy nút "Báo thông tin sai" → ghi log → team review trong 24h |
| Correction — user sửa | User sửa bằng cách nào? Data đó đi vào đâu? | User nhấn "Báo sai" + nhập thông tin đúng (tùy chọn) → correction log → content team cập nhật FAQ → model được fine-tune theo chu kỳ |

### Feature 2: Gợi ý dịch vụ phù hợp theo nhu cầu

**Trigger:** User mô tả nhu cầu di chuyển (VD: "Tôi cần đi sân bay lúc 5 giờ sáng với 2 vali lớn", "Tôi muốn đi chơi cả ngày ở Đà Lạt")

| Path | Câu hỏi thiết kế | Mô tả |
|------|-------------------|-------|
| Happy — AI đúng, tự tin | User thấy gì? | AI gợi ý Xanh SM Car (đi sân bay sớm, hành lý nhiều) + giải thích lý do + nút "Đặt ngay" và "Xem giá chi tiết" |
| Low-confidence — AI không chắc | System báo thế nào? | AI hiển thị 2 lựa chọn (Car vs Premium) với mô tả ngắn từng loại + "Bạn muốn ưu tiên giá rẻ hay tiện nghi?" → user chọn |
| Failure — AI sai | Recover ra sao? | AI gợi ý Bike cho chuyến đi dài → user phản hồi "không phù hợp" → AI xin lỗi, hỏi lại thông tin (số người, hành lý, khoảng cách) → gợi ý lại |
| Correction — user sửa | Data đi vào đâu? | User chọn dịch vụ khác với gợi ý → implicit signal → cải thiện recommendation model |

### Feature 3: Tổng hợp câu hỏi từ mạng xã hội & so sánh với đối thủ

**Trigger:** User hỏi câu hỏi phổ biến từ cộng đồng (VD: "Xanh SM có tốt hơn Grab không?", "Tài xế Xanh SM có chuyên nghiệp không?")

| Path | Câu hỏi thiết kế | Mô tả |
|------|-------------------|-------|
| Happy — AI đúng, tự tin | User thấy gì? | AI tổng hợp điểm mạnh của Xanh SM (xe điện, không mùi xăng, tài xế được đào tạo 5 sao) dựa trên FAQ chính thức + phản hồi tích cực từ cộng đồng, không nói xấu đối thủ |
| Low-confidence — AI không chắc | System báo thế nào? | AI trả lời: "Đây là ý kiến cộng đồng, có thể không phản ánh đầy đủ. Bạn có thể thử dịch vụ và đánh giá trực tiếp" |
| Failure — AI sai | Recover ra sao? | AI trích dẫn thông tin lỗi thời từ social media → user báo sai → AI thêm disclaimer thời gian nguồn dữ liệu |
| Correction — user sửa | Data đi vào đâu? | User cung cấp trải nghiệm thực tế → ghi nhận làm dữ liệu training cho social crawling pipeline |

---

## 3. Eval metrics + threshold

**Optimize precision hay recall?** ☑ Precision
Tại sao? Chatbot hỗ trợ dịch vụ — trả lời sai thông tin giá/chính sách gây hại trực tiếp (user bị tính phí sai, mất tin tưởng). Thà không trả lời (escalate sang hotline) còn hơn trả lời sai.
Nếu sai ngược lại: Low precision → user nhận thông tin sai về giá, khu vực phục vụ → đặt xe nhầm → khiếu nại → tăng chi phí support

| Metric | Threshold | Red flag (dừng khi) |
|--------|-----------|---------------------|
| Precision câu trả lời đúng (so với FAQ chính thức) | ≥90% | <80% trong 3 ngày liên tiếp |
| Tỷ lệ user click dịch vụ sau chatbot (conversion) | ≥25% | <10% trong 1 tuần |
| Escalation rate (% câu hỏi chuyển hotline) | ≤20% | >40% (AI không đủ năng lực) |
| Thumbs up rate | ≥75% | <60% trong 1 tuần |

---

## 4. Top 3 failure modes

| # | Trigger | Hậu quả | Mitigation |
|---|---------|---------|------------|
| 1 | Giá cước / khuyến mãi thay đổi nhưng knowledge base chưa cập nhật (VD: Xanh SM tung chương trình giảm 30% nhưng chatbot vẫn báo giá cũ) | User đặt xe với kỳ vọng giá sai → thất vọng, khiếu nại, mất tin tưởng. Nguy hiểm vì user KHÔNG BIẾT thông tin sai | Gắn timestamp cho mỗi FAQ entry. Nếu entry >7 ngày chưa verify → tự động thêm disclaimer "Giá có thể đã thay đổi, xác nhận khi đặt xe". Pipeline crawl website Xanh SM hàng ngày |
| 2 | User hỏi câu hỏi về sự cố nghiêm trọng (tai nạn, mất đồ, tài xế có hành vi không phù hợp) nhưng AI cố gắng tự trả lời thay vì escalate | User nhận hướng dẫn không đầy đủ trong tình huống khẩn cấp → nguy hiểm tính mạng hoặc mất quyền lợi | Classifier phát hiện intent "khẩn cấp/khiếu nại nghiêm trọng" → hard-route sang hotline 1900 2088 ngay, không để AI tự xử lý |
| 3 | Social media crawling lấy phải thông tin sai lệch, review giả, hoặc thông tin về đối thủ bị nhầm sang Xanh SM | AI trả lời dựa trên thông tin sai từ mạng xã hội → ảnh hưởng uy tín, có thể vi phạm pháp lý nếu so sánh sai với đối thủ | Phân tầng nguồn dữ liệu: FAQ chính thức (tier 1, luôn ưu tiên) > social media đã verify (tier 2) > social media raw (tier 3, chỉ dùng để brainstorm, không trích dẫn trực tiếp). Không bao giờ so sánh trực tiếp với đối thủ |

---

## 5. ROI 3 kịch bản

|   | Conservative | Realistic | Optimistic |
|---|-------------|-----------|------------|
| **Assumption** | 500 query/ngày, 60% resolve không cần hotline, triển khai 5 tỉnh | 3.000 query/ngày, 75% resolve, triển khai 20 tỉnh | 10.000 query/ngày, 85% resolve, tích hợp toàn app 60 tỉnh |
| **Cost** | ~$5/ngày inference + $500/tháng maintenance | ~$25/ngày + $1.000/tháng | ~$80/ngày + $2.000/tháng |
| **Benefit** | Giảm 300 cuộc gọi hotline/ngày (~15 phút/cuộc × 50.000đ/phút agent) = ~225M VND/tháng tiết kiệm | Giảm 2.250 cuộc gọi/ngày = ~1,35 tỷ VND/tháng + tăng conversion đặt xe 5% | Giảm 8.500 cuộc gọi/ngày = ~5,1 tỷ VND/tháng + tăng retention 8% + data flywheel cho personalization |
| **Net** | Dương từ tháng 1 | ROI ~10x trong 3 tháng | ROI ~20x + competitive moat từ data |

**Kill criteria:** Nếu precision <80% sau 2 tuần fine-tuning, HOẶC escalation rate >40% liên tục 1 tháng (AI không giải quyết được câu hỏi thực tế) → dừng, review lại knowledge base và pipeline crawling trước khi tiếp tục.

---

## 6. Mini AI spec

**Xanh SM AI Support Chatbot** giải quyết bài toán: hành khách mất thời gian tìm thông tin dịch vụ qua nhiều kênh rời rạc (website, hotline, mạng xã hội), đặc biệt người dùng mới và khách du lịch chưa quen với hệ sinh thái Xanh SM.

**Cho ai:** Hành khách đang dùng app Xanh SM, đặc biệt nhóm chưa quen dịch vụ, cần so sánh các gói (Car / Premium / Bike / Express), hoặc gặp vấn đề sau chuyến đi.

**AI làm gì (Augmentation):** Trả lời câu hỏi FAQ tức thì dựa trên knowledge base từ website chính thức Xanh SM + dữ liệu mạng xã hội đã được kiểm duyệt. Sau khi trả lời, AI gợi ý dịch vụ phù hợp với nhu cầu và cung cấp nút CTA (đặt xe, xem giá, gọi hotline). User luôn là người quyết định cuối cùng. Câu hỏi phức tạp/khẩn cấp được escalate sang agent người thật.

**Quality (Precision-first):** Ưu tiên precision ≥90% — thà không trả lời còn hơn trả lời sai thông tin giá/chính sách. Threshold escalation 20% là mức chấp nhận được cho giai đoạn đầu.

**Risk chính:** Knowledge base stale (giá/khuyến mãi thay đổi nhanh) và social media noise. Mitigated bằng: timestamp + auto-disclaimer cho FAQ cũ, phân tầng nguồn dữ liệu (tier 1 FAQ chính thức luôn override), hard-route cho intent khẩn cấp.

**Data flywheel:** Mỗi lần user tương tác → thumbs up/down + correction log → cập nhật knowledge base hàng tuần → model tốt hơn → escalation rate giảm → tiết kiệm chi phí hotline → reinvest vào data quality. Dữ liệu domain-specific (FAQ taxi điện VN + phản hồi cộng đồng Xanh SM) có marginal value cao vì model chung không có.

**Stack đề xuất:** Gemini Flash (low latency, cost-effective) + RAG trên knowledge base FAQ + social media crawler (Facebook, Google Reviews) với tier-based trust scoring + intent classifier để route câu hỏi khẩn cấp.
