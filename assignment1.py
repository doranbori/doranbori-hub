class Matrix:
    def __init__(self, elements):
        """행렬

        Args:
            elements: 크기가 `n`인 리스트 `m`개로 이루어진 리스트
        """
        if isinstance(elements, list) :
            first_row = len(elements[0])
            for row in elements :
                if isinstance(row, list) :
                    if len(row) != first_row :
                        raise ValueError("행의 길이가 같아야 합니다!")
                
                else :
                    raise ValueError("행은 리스트로 입력")
        else : 
            raise ValueError("행렬은 이중리스트로 입력")        
        self.elements = elements
        self.shape = (len(elements), len(elements[0]) if elements else 0)

    def __str__(self):
        """행렬의 문자열 형식
        
        Examples:

            >>> print(Matrix([[1, 2], [3, 4], [5, 6]]))
            [[1, 2], [3, 4], [5, 6]]
        """
        return str(self.elements)

    def __repr__(self):
        """행렬의 선언 문자열 형식
        
        Examples:

            >>> Matrix([[1, 2], [3, 4], [5, 6]])
            Matrix([[1, 2], [3, 4], [5, 6]])
        """
        return f"Matrix{(self.elements)}"

    def __add__(self, other):
        """행렬의 덧셈

        행렬이 아닌 경우 예외 처리도!

        Args:
            other: 더할 m×n 행렬.
        """
        if not (isinstance(other, Matrix) and other.shape == self.shape) :
            raise ValueError("행렬의 크기가 같아야합니다!")
        
        results = []
        for i in range(self.shape[0]) :
            row = []
            for j in range(self.shape[0]) :
                row.append(self.elements[i][j] + other.elements[i][j])
            results.append(row)

        return Matrix(results)
    def __sub__(self, other):
        """행렬의 뺄셈

        Args:
            other: 뺄 m×n 행렬.
        """
        if not (isinstance(other, Matrix) and other.shape == self.shape) :
            raise ValueError("행렬의 크기가 같아야합니다!")
        
        results = []
        for i in range(self.shape[0]) :
            row = []
            for j in range(self.shape[1]) :
                row.append(self.elements[i][j] - other.elements[i][j])
            results.append(row)
        
        return Matrix(results)


    def __iadd__(self, other):
        """in-place 덧셈

        행렬을 새로 생성하지 않고 원소의 값을 수정! 행렬이 아닌 경우 예외처리도!

        Args:
            other: 더할 m×n 행렬.
        """
        if not (isinstance(other, Matrix) and other.shape == self.shape) :
            raise ValueError("행렬의 크기가 같아야합니다!")
        
        for i in range(self.shape[0]):
            for j in range(self.shape[1]):
                self.elements[i][j] = self.elements[i][j] + other.elements[i][j]

        return Matrix(self.elements)
    
    # __sub__는 __neg__를 응용하시면 좋을 것 같습니다!

    def __neg__(self):
        """음연산

        행렬의 모든 원소의 부호를 바꾸는 연산 -A를 정의합니다.
        """
        results = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.elements[i][j] * (-1))
            results.append(row)
        
        return Matrix(results)

    def __mul__(self, other):
        """행렬곱

        행렬이 아닌 경우 예외처리도!

        Args:
            other: 곱할 n×k 행렬.
        """
        if not (isinstance(other, Matrix) and other.shape[0] == self.shape[1]) :
            raise ValueError("앞 행렬의 열 개수와 뒷 행렬의 행 개수가 같아야 합니다!")
        
        results = []
        for m in range(self.shape[0]):
            row = []
            for n in range(other.shape[1]):
                atom_sum = 0
                for k in range(self.shape[1]):
                    atom_sum += self.elements[m][k] * other.elements[k][n]
                row.append(atom_sum)
            results.append(row)

        return Matrix(results)            


    def __rmul__(self, other):
        """스칼라배

        스칼라(`int`나 `float`)이 아닌 경우 예외처리도!

        Args:
            other: 곱할 스칼라.
        """
        if not (isinstance(other, int) or isinstance(other, float)) :  
            raise ValueError("실수를 입력해주세요!")
        
        results = []
        for i in range(self.shape[0]):
            row = []
            for j in range(self.shape[1]):
                row.append(self.elements[i][j] * other)
            results.append(row)
        
        return Matrix(results)

    def __imul__(self, other):
        """in-place 곱셈

        행렬을 새로 생성하지 않고 내부 값을 수정! 행렬이나 스칼라가 아닌 경우 예외처리도!

        Args:
            other: 곱할 n×k 행렬 또는 스칼라.
        """
        if not (isinstance(other, int) or isinstance(other, float) or (isinstance(other, Matrix) and other.shape[0] == self.shape[1])) :
            raise ValueError("실수를 입력해주세요!")

        if isinstance(other, int) or isinstance(other, float) :
            for i in range(self.shape[0]) :
                for j in range(self.shape[1]) :
                    self.elements[i][j] = self.elements[i][j] * other
            return self.elements
        
        elif isinstance(other, Matrix) and other.shape[0] == self.shape[1] :
            for m in range(self.shape[0]):
                for _ in range(self.shape[1]):
                    row = []
                    for k in range(other.shape[1]):
                        atom_sum = 0
                        for n in range(other.shape[0]) :
                            atom_sum += self.elements[m][n] * other.elements[n][k]
                        row.append(atom_sum)
                self.elements[m] = row
            return self.elements
        
        else :
            raise ValueError("크기가 맞는 행렬이나 실수를 입력해주세요!")
            


    def __contains__(self, other):
        """원소 포함 확인

        Args:
            other: 행렬에 속해 있는 지 확인할 스칼라.
        """
        for i in range(self.shape[0]) :
            for j in range(self.shape[1]) :
                if self.elements[i][j] == other :
                    return True
                
        return False


    def __len__(self):
        """행렬의 차원

        행렬의 차원, 즉 행의 개수(m)을 반환합니다.
        """
        return len(self.elements)

    def __iter__(self):
        """행렬의 반복자

        차례대로 각 행을 리스트 형태로 반환합니다. `yield`와 `Generator`를 사용해 구현하세요!

        Examples:

            >>> for col in Matrix([[1, 2], [3, 4], [5, 6]]):
            ... print(col)
            [1, 2]
            [3, 4]
            [5, 6]
        """
        for i in self.elements :
            yield i

    def row(self, i):
        """`i`번째 행을 리스트 형태로 반환합니다. 0부터!"""
        return self.elements[i]

    def col(self, j):
        """`j`번째 열을 리스트 형태로 반환합니다. 0부터!"""
        results = []
        for row in self.elements :
            results.append(row[j])

        return results
        
    def __getitem__(self, key):
        """행렬의 아이템

        여러 개를 적으면 `tuple` 형식으로 키가 들어옵니다(예를 들어, matrix[2, 3]에서 key=(2, 3)).
        `int`가 하나 들어온 경우 해당 번째의 행을 리스트 형태로 반환합니다.
        `int`가 두 개 들어온 경우 해당 위치의 원소를 반환합니다.

        마찬가지로 0부터임을 잘 생각해주세요!

        Args:
            *key: 얻을 원소 또는 행의 위치
        """
        if isinstance(key, int) :
            return self.elements[key]
        
        elif isinstance(key, tuple) and len(key) == 2 :
            return self.elements[key[0]][key[1]]
        
        else :
            raise ValueError("길이가 1 또는 2인 key로 입력해주세요!")



    def __eq__(self, other):
        """두 행렬이 같은 지 확인합니다.

        행렬이 같다는 것은 같은 위치의 원소가 모두 같다는 것을 의미합니다!

        Args:
            other: 행렬
        """
        if not (isinstance(other, Matrix) and other.shape == self.shape) :
            raise ValueError("행렬의 크기가 같아야합니다!")
        
        for i in range(self.shape[0]) :
            for j in range(self.shape[1]) :
                if not self.elements[i][j] == other.elements[i][j] :
                    return False
                
        return True


# 테스트 코드

A = Matrix([[1, 2], [3, 4]])
B = Matrix([[5, 6], [7, 8]])

print(A + B)                  # [[6, 8], [10, 12]]
print(A - B)                    # [[-4, -4], [-4, -4]]
print(A * B)                    # [[19, 22], [43, 50]]
print(3 * A)                    # [[3, 6], [9, 12]]
print(2 in A)
print(A.row(0))
print(B.col(0))
print(A[1, 0])                  # 3
for row in A:
    print(row, end=", ")        # [1, 2], [3, 4]