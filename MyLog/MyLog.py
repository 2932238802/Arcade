import inspect

def MyLog(message=""):
    # 获取调用栈信息
    frame = inspect.currentframe().f_back  # 获取上一层调用栈 # type: ignore # 行号
    filename = frame.f_code.co_filename    # 文件名 # type: ignore # 行号
    lineno = frame.f_lineno                # type: ignore # 行号
    
    print(f"[{filename}:{lineno}] {message}")