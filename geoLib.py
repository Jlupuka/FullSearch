def get_spn(self, evenLope: dict[str, str]) -> list[str]:
    return [str(abs(float(a1) - float(a2))) for a1, a2 in zip(evenLope['lowerCorner'].split(),
                                                              evenLope['upperCorner'].split())]
