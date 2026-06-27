"""
mixed_disorders.py
Interpretation of mixed acid-base disorders using delta ratio
"""

class MixedDisorders:

    @staticmethod
    def interpret_delta_ratio(ratio):
        """
        Interpret delta ratio in metabolic acidosis
        """

        if ratio is None:
            return "Cannot calculate Delta Ratio"

        if ratio < 0.4:
            return "Pure Normal Anion Gap Metabolic Acidosis (NAGMA)"

        if 0.4 <= ratio < 0.8:
            return "Mixed NAGMA + High Anion Gap Metabolic Acidosis"

        if 0.8 <= ratio <= 2:
            return "Pure High Anion Gap Metabolic Acidosis (HAGMA)"

        if ratio > 2:
            return "HAGMA + Metabolic Alkalosis OR Chronic Respiratory Acidosis"

        return "Indeterminate pattern"