class hex2rgb():
    def __init__(self, hex_color: str) -> None:
        hex_color = hex_color.lstrip('#') # 去除标识字符
        if len(hex_color) == 3: hex_color = "".join([c * 2 for c in hex_color]) # 处理三位 HexColor
        self.cr = int(hex_color[0:2], 16) # 转换
        self.cg = int(hex_color[2:4], 16) # 转换
        self.cb = int(hex_color[4:6], 16) # 转换
    #
    def r(self): return self.cr
    def g(self): return self.cg
    def b(self): return self.cb
    def rgb(self): return (self.cr, self.cg, self.cb)