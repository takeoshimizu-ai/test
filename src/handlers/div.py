from decimal import Decimal, ROUND_HALF_UP, InvalidOperation, getcontext
import azure.functions as func

getcontext().prec = 28

def _format_result(value: Decimal) -> str:
    q = Decimal('0.000001')
    rounded = value.quantize(q, rounding=ROUND_HALF_UP)
    s = format(rounded.normalize(), 'f')
    if s == '-0':
        s = '0'
    return s

def main(req: func.HttpRequest) -> func.HttpResponse:
    A = req.params.get('A')
    B = req.params.get('B')
    try:
        if A is None or B is None:
            raise ValueError('missing')
        a = Decimal(A)
        b = Decimal(B)
    except (InvalidOperation, ValueError):
        return func.HttpResponse('Invalid or missing parameter A or B', status_code=400, headers={'Access-Control-Allow-Origin': '*'}, mimetype='text/plain')

    if b == 0:
        return func.HttpResponse('Division by zero', status_code=401, headers={'Access-Control-Allow-Origin': '*'}, mimetype='text/plain')

    result = a / b
    out = _format_result(result)
    return func.HttpResponse(out, status_code=200, headers={'Access-Control-Allow-Origin': '*'}, mimetype='text/plain')
