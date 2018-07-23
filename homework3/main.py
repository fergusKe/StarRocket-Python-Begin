# import core
# import core as c
import lib.core as c  # 封包: lib, 模組: core
import random

# c.add(3, 5, 7, 9, 11)
# c.test()

# 1. 程式包裝
# 1.1 把 99 乘法表包裝成函式，可做 n1 * n2 乘法
# def list(n1, n2):
	# return
# 1.2 把四則運算機包裝成函式
# 1.3 將以上函式包裝在你自己的模組和封包中，並且在主程式成功使用
# 使用系統內建的模組 random 產生 1~100 間的亂數


# 1.1 把 99 乘法表包裝成函式，可做 n1 * n2 乘法
c.add(1, 5)
# c.sub(7, 3)
# c.mul(3, 6)
# c.divi(12, 5)

# 1.2 把四則運算機包裝成函式
# c.mul_99()

# 1.3 將以上函式包裝在你自己的模組和封包中，並且在主程式成功使用
# 使用系統內建的模組 random 產生 1~100 間的亂數
# random1 = random.randint(1, 100)
# random2 = random.randint(1, 100)
# c.add(random1, random2)