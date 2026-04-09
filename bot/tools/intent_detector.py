"""
Phân loại intent của user message bằng LLM (gpt-4o-mini).
Chạy trước pipeline RAG để routing sớm.
"""

import logging
from openai import AsyncOpenAI
from config import OPENAI_API_KEY

logger = logging.getLogger(__name__)

_client = AsyncOpenAI(api_key=OPENAI_API_KEY)

_SYSTEM_PROMPT = """\
Phân loại intent của tin nhắn người dùng gửi đến chatbot hỗ trợ dịch vụ Xanh SM.

Chỉ trả về đúng một trong các nhãn sau, không giải thích gì thêm:
- driver_registration : người dùng muốn đăng ký / ứng tuyển / nộp đơn làm tài xế xe máy điện hoặc taxi điện Xanh SM
- general             : tất cả các trường hợp còn lại (hỏi thông tin, giá cước, chính sách, v.v.)
"""


async def detect_intent(message: str) -> str:
    """
    Trả về 'driver_registration' hoặc 'general'.
    Fallback về 'general' nếu LLM lỗi.
    """
    try:
        resp = await _client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": _SYSTEM_PROMPT},
                {"role": "user",   "content": message},
            ],
            max_tokens=10,
            temperature=0,
        )
        intent = resp.choices[0].message.content.strip().lower()
        logger.info("[INTENT] %r → %s", message[:60], intent)
        return intent if intent in ("driver_registration", "general") else "general"
    except Exception as e:
        logger.warning("[INTENT] failed (%s), fallback=general", e)
        return "general"
