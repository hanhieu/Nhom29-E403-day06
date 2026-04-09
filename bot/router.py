import chainlit as cl
from bot.handlers.chat import handle_chat
from bot.handlers.driver_registration import run_driver_registration_flow
from bot.tools.intent_detector import detect_intent

BOT_NAME = "XanhSM"


async def route(message: cl.Message):
    intent = await detect_intent(message.content)

    if intent == "driver_registration":
        confirm = await cl.AskActionMessage(
            content=(
                "Bạn muốn **đăng ký làm tài xế xe máy điện Xanh SM**?\n"
                "Mình sẽ hỗ trợ bạn điền form đăng ký ngay bây giờ."
            ),
            author=BOT_NAME,
            actions=[
                cl.Action(name="confirm", value="yes", label="✅ Xác nhận", payload={"value": "yes"}),
                cl.Action(name="confirm", value="no",  label="❌ Không phải", payload={"value": "no"}),
            ],
            timeout=60,
        ).send()

        if confirm and confirm.get("payload", {}).get("value") == "yes":
            await run_driver_registration_flow()
            return

        # Người dùng từ chối hoặc timeout → xử lý như câu hỏi thông thường
        user_type = cl.user_session.get("user_type")
        await handle_chat(message.content, user_type)
        return

    user_type = cl.user_session.get("user_type")
    await handle_chat(message.content, user_type)
