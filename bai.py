import sympy as sp

# Khai báo biến x là ký hiệu toán học
x = sp.Symbol('x')

# Nhập hàm số cần tính đạo hàm (Ví dụ: x^2 + sin(x))
f = x**2 + sp.sin(x)

# Tính đạo hàm bậc 1
dao_ham = sp.diff(f, x)

print(f"Hàm số: f(x) = {f}")
print(f"Đạo hàm f'(x) = {dao_ham}")