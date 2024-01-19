import sys
from antlr4 import *
from ExprLexer import ExprLexer
from ExprParser import ExprParser
from ExprVisitor import ExprVisitor

class ExprWhileVisitor(ExprVisitor):
    def __init__(self) -> None:
        super().__init__()
        self.variables = {}
        self.is_break = False
    
    # 实现赋值语句
    def visitAssignment(self, ctx):
        name = ctx.ID().getText()  # 假设赋值语句的左侧是ID
        value = self.visit(ctx.expr())  # 右侧是表达式
        self.variables[name] = value
        return value
    
    # 实现加法和减法
    def visitAddSubExpr(self, ctx):
        if ctx.op.type == ExprParser.ADD:
            return self.visit(ctx.left) + self.visit(ctx.right)
        else:
            return self.visit(ctx.left) - self.visit(ctx.right)

    # 实现乘法和除法
    def visitMulDivExpr(self, ctx):
        if ctx.op.type == ExprParser.MUL:
            return self.visit(ctx.left) * self.visit(ctx.right)
        else:
            return self.visit(ctx.left) / self.visit(ctx.right)

    # 实现取模
    def visitModExpr(self, ctx):
        return self.visit(ctx.left) % self.visit(ctx.right) 

    # 实现整数
    def visitIntExpr(self, ctx):
        return int(ctx.getText())

     # 实现 break 语句
    def visitBreakStat(self, ctx):
        self.is_break = True  # 设置 break 标志
        print('break', self.variables)
        return 0

    # 实现while循环
    def visitWhileLoop(self, ctx):
        while self.visit(ctx.expr()):
            # 逐条处理 whileBody 中的语句
            for stat in ctx.whileBody().getChildren():
                self.visit(stat)
                if self.is_break:  # 检查是否需要跳出循环
                    self.is_break = False  # 重置 break 标志
                    return 0
        return 0

    # 实现关系语句
    def visitRelationalExpr(self, ctx):
        left = self.visit(ctx.left)
        right = self.visit(ctx.right)
        if ctx.op.type == ExprParser.EQ:
            return left == right
        elif ctx.op.type == ExprParser.NEQ:
            return left != right
        elif ctx.op.type == ExprParser.GT:
            return left > right
        elif ctx.op.type == ExprParser.LT:
            return left < right
        elif ctx.op.type == ExprParser.GTEQ:
            return left >= right
        elif ctx.op.type == ExprParser.LTEQ:
            return left <= right
    
    # 实现符号取值语句
    def visitIdExpr(self, ctx):
        name = ctx.ID().getText()
        if name in self.variables:
            return self.variables[name]
        else:
            return None

    # 实现if语句
    def visitIfStatement(self, ctx):
        if self.visit(ctx.expr()):
            return self.visit(ctx.prog(0))
        elif ctx.prog(1):  # 检查是否存在 else 部分
            return self.visit(ctx.prog(1))
        return None
    
    # 实现print语句
    def visitPrintStatement(self, ctx):
        print(self.visit(ctx.expr()))
        return 0
    
def read_file(filename):
    with open(filename, 'r') as f:
        return f.read()

def main():
    argv = sys.argv
    if len(argv) != 2:
        print('Usage: python run.py <filename>')
        return
    input = read_file(argv[1])
    lexer = ExprLexer(InputStream(input))
    stream = CommonTokenStream(lexer)
    parser = ExprParser(stream)
    tree = parser.prog()
    expr = ExprWhileVisitor()
    expr.visit(tree)

if __name__ == '__main__':
    main()
