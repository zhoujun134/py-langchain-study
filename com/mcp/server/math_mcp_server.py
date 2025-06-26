# math_server.py
from mcp.server.fastmcp import FastMCP
from colorlog import ColoredFormatter
import logging

# 创建日志器
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

# 创建带颜色的控制台处理器
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.DEBUG)

# 定义颜色格式
formatter = ColoredFormatter(
    "%(log_color)s%(asctime)s - %(levelname)s - %(message)s%(reset)s",
    datefmt="%Y-%m-%d %H:%M:%S,%(03)s",
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    }
)

console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

mcp = FastMCP("math-compute-mcp")


@mcp.tool()
def add(a: float, b: float) -> float:
    """返回两个数之和"""
    result = a + b
    logger.info("sub(%s, %s): %s", a, b, result)
    return result


@mcp.tool()
def sub(a: float, b: float) -> float:
    """返回两个数之差，a 减去 b 的值"""
    result = a - b
    logger.info("sub(%s, %s): %s", a, b, result)
    return result


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """返回两个数之积"""
    result = a * b
    logger.info("multiply(%d, %d): %s", a, b, result)
    return result


@mcp.tool()
def divide(a: float, b: float) -> float:
    """返回两个数的商，a 除以 b 的值， b 不等于 0 """
    result = a / b
    logger.info("divide(%d, %d): %s", a, b, result)
    return result


if __name__ == "__main__":
    logger.info("Starting Math MCP Server (stdio)")
    mcp.run(transport="stdio")
