import math

def calculate_standard_error(y_actual, y_predicted, n, p=2):
    """
    Calculates the Standard Error of the Estimate using pure Python.
    
    Parameters:
    y_actual (list): The actual true y values.
    y_predicted (list): The predicted y values from the model.
    n (int): The number of observations.
    p (int): Number of parameters estimated (default is 2 for simple linear regression).
    """
    # 1. Calculate the Sum of Squared Errors (SSE)
    # zip() pairs the actual and predicted values together so we can subtract them
    sse = sum((actual - predicted) ** 2 for actual, predicted in zip(y_actual, y_predicted))
    
    # 2. Calculate degrees of freedom
    degrees_of_freedom = n - p
    
    # 3. Calculate and return Standard Error
    standard_error = math.sqrt(sse / degrees_of_freedom)
    return standard_error

# ==========================================
# Example Usage
# ==========================================

# 1. Define inputs as standard Python lists
x = [1, 2, 3, 4, 5]
y = [20,40,60,80,100]
n = len(y)

# 2. Provide predicted values 
# (Normally you'd calculate these with a model, but here we hardcode the 
# estimates that a linear regression line would output for these x values)
predicted_values = [18, 38, 58, 78, 98]  # Example predicted values

# 3. Calculate standard error
see = calculate_standard_error(y, predicted_values, n)

# 4. Display Results
print("--- Data Inputs ---")
print(f"x values: {x}")
print(f"y actual: {y}")
print(f"n (count): {n}\n")

print("--- Model Predictions ---")
print(f"y predicted: {predicted_values}\n")

print("--- Final Result ---")
# {:.4f} formats the result to 4 decimal places
print(f"Standard Error of the Estimate: {see:.4f}")