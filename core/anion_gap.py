"""
anion_gap.py
Anion gap and metabolic acidosis analysis utilities
"""

class AnionGap:

    @staticmethod
    def calculate(na, cl, hco3):
        """
        Standard anion gap formula:
        AG = Na - (Cl + HCO3)
        """
        return na - (cl + hco3)

    @staticmethod
    def corrected_anion_gap(ag, albumin):
        """
        Albumin-corrected AG:
        AG + 2.5 * (4 - albumin)
        """
        return ag + 2.5 * (4.0 - albumin)

    @staticmethod
    def delta_ag(ag):
        """
        Delta AG = AG - normal AG (12)
        """
        return ag - 12

    @staticmethod
    def delta_hco3(hco3):
        """
        Delta HCO3 = normal HCO3 (24) - measured HCO3
        """
        return 24 - hco3

    @staticmethod
    def delta_ratio(ag, hco3):
        """
        Delta ratio = (AG - 12) / (24 - HCO3)
        Used for mixed metabolic disorders
        """
        denom = 24 - hco3
        if denom == 0:
            return None
        return (ag - 12) / denom