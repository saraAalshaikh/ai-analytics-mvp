from typing import Any, Dict, Optional


def success_response(
    agent: str,
    message: str,
    data: Optional[Dict[str, Any]] = None
) -> Dict[str, Any]:
    return {
        "success": True,
        "agent": agent,
        "message": message,
        "data": data or {}
    }


def error_response(
    agent: str,
    message: str,
    error: Optional[str] = None
) -> Dict[str, Any]:
    return {
        "success": False,
        "agent": agent,
        "message": message,
        "error": error,
        "data": {}
    }
