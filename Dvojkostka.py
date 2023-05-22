import random

class Dvojkostka:

    def hod_dvojkostkou() -> list:

        prvni_hod = random.randint(1, 6)
        druhy_hod = random.randint(1, 6)
        if (prvni_hod == druhy_hod):
            print([prvni_hod for _ in range(4)])
            return [prvni_hod for _ in range(4)]
        else:
            print([prvni_hod, druhy_hod])
            return [prvni_hod, druhy_hod]