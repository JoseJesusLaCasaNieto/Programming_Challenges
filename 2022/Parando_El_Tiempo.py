# /*
#  * Crea una función que sume 2 números y retorne su resultado pasados
#  * unos segundos.
#  * - Recibirá por parámetros los 2 números a sumar y los segundos que
#  *   debe tardar en finalizar su ejecución.
#  * - Si el lenguaje lo soporta, deberá retornar el resultado de forma
#  *   asíncrona, es decir, sin detener la ejecución del programa principal.
#  *   Se podría ejecutar varias veces al mismo tiempo.
#  */

import asyncio

async def asyn_sum(a, b, secs):
    await asyncio.sleep(secs)
    print(f"\nLa suma de {a} y {b} es: {a+b}")

async def main():
    await asyn_sum(1, 5, 3)
    await asyn_sum(4, 8, 2)

asyncio.run(main())




