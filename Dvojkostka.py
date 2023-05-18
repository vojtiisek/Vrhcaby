import math
import random

class Dvojkostka:
    def __init__(self) -> None:
        pass

    def hod_dvojkostkou(self) -> list:

        prvni_hod = random.randint(1, 6)
        druhy_hod = random.randint(1, 6)
        if (prvni_hod == druhy_hod):
            return [prvni_hod for _ in range(4)]
        else:
            return [prvni_hod, druhy_hod]