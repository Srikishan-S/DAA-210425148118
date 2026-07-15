import math


def standard_error_estimation(y, predicted=None, n=None):
    """Compute standard error based on residuals.

    Interpreting the user's formula as:
        SE = sqrt( sum( y - Ybar ) / (n - 2) )

    Since Ybar depends on the provided y values (and the name Y is usually the
    response vector), we compute:
        Ybar = mean(y)
        residuals = y_i - Ybar

    If `predicted` is provided, it is ignored because the formula you gave does not
    involve predicted values.

    Parameters
    ----------
    y : list[float]
        Observed values.
    predicted : list[float] | None
        Accepted for compatibility; not used in the current formula.
    n : int | None
        Sample size. If not provided, uses len(y).

    Returns
    -------
    float
        Standard error value.
    """
    if y is None or len(y) == 0:
        raise ValueError("y must be a non-empty list of numbers")

    y = [float(v) for v in y]
    if n is None:
        n = len(y)

    if n - 2 <= 0:
        raise ValueError("n must be greater than 2 so that (n-2) is positive")

    ybar = sum(y) / len(y)
    numerator = sum((val - ybar) for val in y)
    # Note: For real data, sum(y - mean(y)) should be 0; this matches the user formula.
    return math.sqrt(numerator / (n - 2))


def _parse_number_list(s):
    parts = s.split(",")
    out = []
    for p in parts:
        p = p.strip()
        if p:
            out.append(float(p))
    return out


def main():
    print("Standard Error Estimation")
    print("Enter observed values y as comma-separated numbers (e.g., 1,2,3,4):")
    y_str = input("y = ").strip()
    y = _parse_number_list(y_str)

    n_str = input("Enter n (or press Enter to use len(y)): ").strip()
    n = None
    if n_str:
        n = int(n_str)

    try:
        se = standard_error_estimation(y=y, n=n)
        print(f"Standard Error = {se}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
