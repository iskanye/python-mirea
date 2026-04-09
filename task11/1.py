import numpy as np


def main(D, K, S, W, X):
    """
    Вычисляет след от выражения:
    tr(K + W - (S - D)^8 - ((S + W)^{-1} + D - (K + S * X)))
    """
    # Вычисляем (S - D)^8
    term1 = np.linalg.matrix_power(S - D, 8)

    # Вычисляем (S + W)^{-1}
    term2 = np.linalg.inv(S + W)

    # Вычисляем K + S * X
    term3 = K + S @ X

    # Собираем всё выражение
    result = K + W - term1 - (term2 + D - term3)

    # Возвращаем след матрицы
    return np.trace(result)


def test():
    """Test the main function with various test cases."""
    # Test 1: Identity matrices
    identity = np.array([
        [1.0, 0.0, 0.0],
        [0.0, 1.0, 0.0],
        [0.0, 0.0, 1.0]
    ])

    result1 = main(identity, identity, identity, identity, identity)
    expected1 = 7.50
    tolerance = 0.01
    assert abs(result1 - expected1) < tolerance, (
        f"Test 1 failed: Expected {expected1}, got {result1}"
    )
    print(f"Test 1 passed: {result1:.2e}")

    # Test 2: Random matrices
    D = np.array([[0.91, 0.91, 0.95], [0.32, 0.71, 0.65], [0.44, 0.29, 0.79]])
    K = np.array([[0.79, 0.22, 0.61], [0.69, 0.37, 0.92], [0.69, 0.1, 0.44]])
    S = np.array([[0.29, 0.72, 0.95], [0.71, 0.89, 0.82], [0.97, 0.4, 0.45]])
    W = np.array([[0.35, 0.74, 0.36], [0.9, 0.13, 0.63], [0.49, 0.89, 0.67]])
    X = np.array([[0.52, 0.84, 0.62], [0.27, 0.76, 0.7], [0.59, 0.67, 0.03]])

    result2 = main(D, K, S, W, X)
    expected2 = 10.30
    assert abs(result2 - expected2) < tolerance, (
        f"Test 2 failed: Expected {expected2}, got {result2}"
    )
    print(f"Test 2 passed: {result2:.2e}")

    # Test 3: Diagonal matrices
    D3 = np.array([[2.0, 0.0, 0.0], [0.0, 2.0, 0.0], [0.0, 0.0, 2.0]])
    K3 = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    S3 = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    W3 = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])
    X3 = np.array([[1.0, 0.0, 0.0], [0.0, 1.0, 0.0], [0.0, 0.0, 1.0]])

    result3 = main(D3, K3, S3, W3, X3)
    # For diagonal matrices, we can calculate the expected result
    expected3 = 1.50
    assert abs(result3 - expected3) < tolerance, (
        f"Test 3 failed: Expected {expected3}, got {result3}"
    )
    print(f"Test 3 passed: {result3:.2e}")

    print("All tests passed!")


if __name__ == "__main__":
    test()
