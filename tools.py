from langchain_core.tools import tool
from sympy import sympify

@tool
def calculate_math_expression(expression: str) -> float:
    """
    Evaluate a mathematical expression and return the numerical result.
    """

    try:
        expr = sympify(expression)

        result = expr.evalf()
    
    except Exception:
        return "Invalid mathematical expression."
    
    return result
