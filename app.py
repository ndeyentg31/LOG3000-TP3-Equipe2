from flask import Flask, request, render_template
from operators import add, subtract, multiply, divide
"""Ce fichier gère le serveur Flask et les calculs de la calculatrice web."""

app = Flask(__name__)

OPS = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide,
}

def calculate(expr: str):

    """
    Analyse une expression et effectue le calcul demandé.

    Args:
        expr (str): Expression contenant deux nombres et un opérateur.

    Returns:
        float: Résultat de l'opération.

    Raises:
        ValueError: Si l'expression est vide ou invalide.
    """
    if not expr or not isinstance(expr, str):
        raise ValueError("empty expression")

    s = expr.replace(" ", "") # Permet de traiter les expressions même si elles contiennent des espaces.

    op_pos = -1
    op_char = None

    for i, ch in enumerate(s):
        if ch in OPS:
            if op_pos != -1:
                raise ValueError("only one operator is allowed") # Empêche plusieurs opérations dans une même expression.
            op_pos = i
            op_char = ch

    if op_pos <= 0 or op_pos >= len(s) - 1:
        # operator at start/end or not found
        raise ValueError("invalid expression format")

    left = s[:op_pos]
    right = s[op_pos+1:]

    try:
        a = float(left)
        b = float(right)
    except ValueError:
        raise ValueError("operands must be numbers")

    return OPS[op_char](a, b)

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Gère l'affichage et les interactions avec la calculatrice.

    Entrée :
        Requête GET ou POST contenant une expression à calculer.

    Sortie :
        Page HTML affichant la calculatrice et le résultat
        du calcul ou un message d'erreur.
    """
    result = ""
    if request.method == 'POST':
        expression = request.form.get('display', '')
        try:
            result = calculate(expression)
        except Exception as e:
            result = f"Error: {e}"
    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)