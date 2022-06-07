nums = [0, 1, 0, 3, 12]
nums = [0]
nums = [0, 1, 0]
target = 0  # también se podría inicial como None y asignarle i, si: elif x == 0
from_ = None
to = None


def move_segment(targ=None):
    nums[targ: (targ + to - from_ + 1)] = nums[from_:to + 1]
    targ = targ + (to - from_) + 1  # el siguiente target será el elemento siguiente al final del segmento que acabamos de mover
    return nums, targ


for i, x in enumerate(nums):
    if x != 0:
        if from_ is None:  # si no es un cero, marcamos un punto de entrada para el siguiente segmento a mover. Siempre que no existiese ya uno
            from_ = i
        to = i  # Si no es un cero, siempre marcamos punto de salida
    elif x == 0 and from_ is not None:  # si es un cero, y ya tenemos algo que mover... lo movemos
        nums, target = move_segment(targ=target)
        from_ = None  # el punto de inicio del segmento lo ponemos a None hasta que encontremos otro NO cero

if from_ is not None:  # si termina en NO cero, no habremos movido el último segmento durante el bucle, así que lo hacemos ahora. Lo podemos comprobar porque from_ no es None
    nums, target = move_segment(targ=target)
if to:  # si "to" es distinto de None, significa que hemos movido algo a lo largo de la ejecución, así que tendremos que rellenar con ceros hasta el final
    nums[target:len(nums)] = [0] * (len(nums) - target)

print(nums)
# assert nums == [0]
