from docx.shared import Length


def twip_to_point(twip: Length) -> float:
    return twip / 20
