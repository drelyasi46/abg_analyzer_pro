"""
abg_engine.py
Core ABG interpretation engine (acid-base analysis)
"""
from core.compensation import Compensation
from core.anion_gap import AnionGap
from core.mixed_disorders import MixedDisorders

class ABGEngine:

    def analyze(self, ph, pco2, hco3, na=None, cl=None, albumin=None):

        report = []

        # -------------------------
        # 1. pH interpretation
        # -------------------------
        if ph < 7.35:
            report.append("Acidemia")
        elif ph > 7.45:
            report.append("Alkalemia")
        else:
            report.append("Normal pH")

        # -------------------------
        # 2. Primary disorder
        # -------------------------
        if ph < 7.35:

            # Metabolic acidosis
            if hco3 < 22:
                report.append("Primary: Metabolic Acidosis")

                low, expected, high = Compensation.winters_formula(hco3)
                report.append(f"Winter expected PaCO2: {expected:.1f}")

                if pco2 < low:
                    report.append("Concomitant Respiratory Alkalosis (overcompensation)")
                elif pco2 > high:
                    report.append("Concomitant Respiratory Acidosis (inadequate compensation)")
                else:
                    report.append("Appropriate respiratory compensation")

            # Respiratory acidosis
            elif pco2 > 45:
                report.append("Primary: Respiratory Acidosis")

                acute = Compensation.acute_respiratory_acidosis_expected_hco3(pco2)
                chronic = Compensation.chronic_respiratory_acidosis_expected_hco3(pco2)

                report.append(f"Expected HCO3 (acute): {acute:.1f}")
                report.append(f"Expected HCO3 (chronic): {chronic:.1f}")

        elif ph > 7.45:

            # Metabolic alkalosis
            if hco3 > 26:
                report.append("Primary: Metabolic Alkalosis")

                low, expected, high = Compensation.metabolic_alkalosis_expected_pco2(hco3)
                report.append(f"Expected PaCO2: {expected:.1f}")

            # Respiratory alkalosis
            elif pco2 < 35:
                report.append("Primary: Respiratory Alkalosis")

                acute = Compensation.acute_respiratory_alkalosis_expected_hco3(pco2)
                chronic = Compensation.chronic_respiratory_alkalosis_expected_hco3(pco2)

                report.append(f"Expected HCO3 (acute): {acute:.1f}")
                report.append(f"Expected HCO3 (chronic): {chronic:.1f}")

        # -------------------------
        # 3. Anion gap analysis
        # -------------------------
        if na is not None and cl is not None:

            ag = AnionGap.calculate(na, cl, hco3)
            report.append(f"Anion Gap: {ag:.1f}")

            if albumin is not None:
                cag = AnionGap.corrected_anion_gap(ag, albumin)
                report.append(f"Corrected AG: {cag:.1f}")

            ratio = AnionGap.delta_ratio(ag, hco3)

            if ratio is not None:
                report.append(f"Delta Ratio: {ratio:.2f}")
                report.append(MixedDisorders.interpret_delta_ratio(ratio))

        return report