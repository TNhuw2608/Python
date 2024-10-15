'''
Xử lý Ma Trận
Yêu cầu:
Nhập 2 matrix A, B.
Cộng 2 matrix
Viết hàm tính matrix hoán vị➔áp dụng để tìm cho A, B
'''

def input_matrix(rows, cols):
    """Nhập vào một ma trận có kích thước rows x cols."""
    matrix = []
    for i in range(rows):
        while True:
            try:
                row = list(map(float, input(f"Nhập hàng {i + 1} (cách nhau bởi dấu cách): ").split()))
                if len(row) != cols:
                    print(f"Vui lòng nhập đúng {cols} số.")
                    continue
                matrix.append(row)
                break
            except ValueError:
                print("Vui lòng chỉ nhập các số.")
    return matrix

def add_matrices(A, B):
    """Cộng hai ma trận A và B."""
    rows = len(A)
    cols = len(A[0])
    result = [[A[i][j] + B[i][j] for j in range(cols)] for i in range(rows)]
    return result

def transpose_matrix(matrix):
    """Tính ma trận hoán vị của matrix."""
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]

def print_matrix(matrix):
    """In một ma trận ra màn hình."""
    for row in matrix:
        print(" ".join(map(str, row)))

def main():
    # Nhập ma trận A
    print("Nhập ma trận A:")
    rows_A = int(input("Nhập số hàng: "))
    cols_A = int(input("Nhập số cột: "))
    A = input_matrix(rows_A, cols_A)

    # Nhập ma trận B
    print("Nhập ma trận B:")
    rows_B = int(input("Nhập số hàng: "))
    cols_B = int(input("Nhập số cột: "))
    
    # Kiểm tra kích thước của ma trận A và B có giống nhau không
    if rows_A != rows_B or cols_A != cols_B:
        print("Kích thước của hai ma trận phải giống nhau để thực hiện phép cộng.")
        return
    
    B = input_matrix(rows_B, cols_B)

    # Cộng ma trận A và B
    sum_matrix = add_matrices(A, B)
    
    # Tính ma trận hoán vị của A và B
    transpose_A = transpose_matrix(A)
    transpose_B = transpose_matrix(B)

    # In kết quả
    print("\nMa trận A:")
    print_matrix(A)
    print("\nMa trận B:")
    print_matrix(B)
    print("\nTổng của hai ma trận A và B:")
    print_matrix(sum_matrix)
    print("\nMa trận hoán vị của A:")
    print_matrix(transpose_A)
    print("\nMa trận hoán vị của B:")
    print_matrix(transpose_B)

# Gọi hàm main để thực thi chương trình
if __name__ == "__main__":
    main()