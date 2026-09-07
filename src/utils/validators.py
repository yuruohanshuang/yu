"""
validators - 
Date:2026/9/7
"""
# src/utils/validators.py
"""数据校验工具模块."""
import re

PHONE_RE = re.compile(r"^1[3-9]\d{9}$")
EMAIL_RE = re.compile(r"^[\w.+-]+@[\w-]+\.[a-zA-Z]{2,}$")


def is_valid_phone(phone: str) -> bool:
    """校验中国大陆手机号."""
    return bool(PHONE_RE.match(str(phone)))


def is_valid_email(email: str) -> bool:
    """校验邮箱格式."""
    return isinstance(email, str) and bool(EMAIL_RE.match(email))


def is_valid_password(pwd: str) -> tuple[bool, int, str]:
    """校验密码强度.

    Returns:
        (是否合格, 等级 0-3, 描述).
    """
    if not isinstance(pwd, str) or len(pwd) < 8:
        return False, 0, "至少 8 位"
    score = sum([
        any(c.isdigit() for c in pwd),
        any(c.islower() for c in pwd),
        any(c.isupper() for c in pwd),
        any(c in "!@#$%^&*" for c in pwd),
    ])
    return True, score, ["弱", "弱", "中等", "强", "非常强"][score]


def validate_user_data(name: str, phone: str, *,
                       email: str | None = None,
                       password: str | None = None) -> tuple[bool, list[str]]:
    """综合校验用户数据，返回 (是否全部合格, 错误列表)."""
    errs: list[str] = []
    if not name or len(name) < 2:
        errs.append("姓名至少 2 字符")
    if not is_valid_phone(phone):
        errs.append("手机号格式不正确")
    if email is not None and not is_valid_email(email):
        errs.append("邮箱格式不正确")
    if password is not None:
        ok, _, desc = is_valid_password(password)
        if not ok:
            errs.append(f"密码: {desc}")
    return not errs, errs


if __name__ == "__main__":
    print(is_valid_phone("13800138000"))
    print(is_valid_email("a@b.com"))
    print(validate_user_data("张三", "13800138000",
                             email="z@s.com", password="Abc12345"))