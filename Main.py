import yfinance as yf
import lang.zn.py
import importlib

# 选择语言
language = input("Choose language / 选择语言 (en/zh): ").strip().lower()
if language not in ['en', 'zh']:
    language = 'zh'

# 动态导入语言模块
lang_module = importlib.import_module(f'lang.{language}')
L = lang_module.text  # 获取语言字典

#print(tsla.info)  # 打印所有信息
trailingPE = stock.info.get('trailingPE', None)  # 市盈率
forwardPE = stock.info.get('forwardPE', None)  # 预期市盈率
trailingPegRatio = stock.info.get('trailingPegRatio', None)  # Trailing PEG比率
enterpriseToEbitda = stock.info.get('enterpriseToEbitda', None)  # EV/EBITDA
priceToSales = stock.info.get('priceToSalesTrailing12Months', None)  # 市销率

# 定义评估股票函数
def evaluate_stock(trailingPE, forwardPE, trailingPegRatio, enterpriseToEbitda, priceToSales):
    low_count = 0
    high_count = 0
    reasonable_count = 0
    evaluation_result = []  # 用于存储评估信息
    
    print("\U00000031 市盈率",trailingPE)      # 市盈率
    if trailingPE < 15:
        print("\U0000200D 市盈率低，低估。")
        low_count += 1
    elif trailingPE > 25:
        print("\U0001F62E 市盈率高，高估。")
        high_count += 1
    else:
        print("\U0001F197 市盈率中,合理。")
        reasonable_count += 1

    print("\U00000032 预期市盈率",forwardPE)       # 预期市盈率
    if forwardPE < 15:
        print("\U0000200D 预期市盈率低,低估。")
        low_count += 1
    elif forwardPE > 25:
        print("\U0001F62E 预期市盈率高,高估。")
        high_count += 1
    else:
        print("\U0001F197 预期市盈率中,合理。")
        reasonable_count += 1
        
    print("\U00000033 PEG比率",trailingPegRatio)        # Trailing PEG Ratio
    if trailingPegRatio < 1:
        print("\U0000200D PEG:小1,低估。")
        low_count += 1
    elif trailingPegRatio == 1:
        print("\U0001F197 PEG:于1,合理。")
        reasonable_count += 1
    else:
        print("\U0001F62E PEG:大1,高估。")
        high_count += 1

    print("\U00000034 EV/EBITDA",enterpriseToEbitda) # EV/EBITDA
    if enterpriseToEbitda < 10:
        print("\U0000200D EV/EBITDA低,低估。")
        low_count += 1
    elif enterpriseToEbitda > 20:
        print("\U0001F62E EV/EBITDA高,高估。")
        high_count += 1
    else:
        print("\U0001F197 EV/EBITDA中,合理。")
        reasonable_count += 1
            
    print("\U00000035 市销率",priceToSales) # 市销率
    if priceToSales < 1:
        print("\U0000200D 市销率低,低估。")
        low_count += 1
    elif priceToSales > 5:
        print("\U0001F62E 市销率高,高估。")
        high_count += 1
    else:
        print("\U0001F197 市销率中,合理。")
        reasonable_count += 1
        
            # 计算最终评估结果
    if low_count > high_count and low_count > reasonable_count:
        final_evaluation = "\U0000200D\U0000200D\U0000200D低估"
    elif high_count > low_count and high_count > reasonable_count:
        final_evaluation = "\U0001F62E\U0001F62E\U0001F62E高估"
    else:
        final_evaluation = "\U0001F197\U0001F197\U0001F197合理"
        
    return final_evaluation
final_evaluation = evaluate_stock(trailingPE, forwardPE, trailingPegRatio, enterpriseToEbitda, priceToSales)
print(f"最终估值: {final_evaluation}")
