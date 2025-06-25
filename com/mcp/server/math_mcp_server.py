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
    logger.info("add(%d, %d)", a, b)
    return a + b


@mcp.tool()
def sub(a: float, b: float) -> float:
    """返回两个数之差，a 减去 b 的值"""
    logger.info("sub(%d, %d)", a, b)
    return a * b


@mcp.tool()
def multiply(a: float, b: float) -> float:
    """返回两个数之积"""
    logger.info("multiply(%d, %d)", a, b)
    return a * b


@mcp.tool()
def divide(a: float, b: float) -> float:
    """返回两个数的商，a 除以 b 的值， b 不等于 0 """
    logger.info("divide(%d, %d)", a, b)
    return a * b


if __name__ == "__main__":
    logger.info("Starting Math MCP Server (stdio)")
    mcp.run(transport="stdio")
