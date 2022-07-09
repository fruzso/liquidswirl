import numpy as np

from liquidswirl.services.mix_calculator_service import MixCalculatorService 

class ReductionPlannerService:
    def __init__(
        self, 
        monthly_amount_ml,
        start_nicotine_cc,
        goal_nicotine_cc,
        nicotine_premix_cc,
        reduction_time,
    ):
        self.monthly_amount_ml = monthly_amount_ml
        self.start_nicotine_cc = start_nicotine_cc #mg/ml
        self.goal_nicotine_cc = goal_nicotine_cc #mg/ml
        self.nicotine_premix_cc = nicotine_premix_cc #mg/ml
        self.reduction_time = reduction_time #months
        
    def plan_by_concentration(self):
        plan = []

        for nicotine_cc in np.arange(self.start_nicotine_cc, self.goal_nicotine_cc-0.1, -0.1):
            nicotine_cc = round(nicotine_cc,2)

            nicotine_ml = self._get_nicotine_ml(nicotine_cc)
            nicotine_mg = self._get_nicotine_mg(nicotine_ml)

            plan.append(
                {   
                    "base_ml": self.monthly_amount_ml,
                    "nicotine_cc": nicotine_cc,
                    "nicotine_ml": nicotine_ml,
                    "nicotine_mg": nicotine_mg,
                    "nicotine_premix_cc": self.nicotine_premix_cc,
                    "final_ml": self.monthly_amount_ml + nicotine_ml 
                }
            )    
            
    
    def _get_nicotine_ml(self, nicotine_cc):
        mix_calculator_service = MixCalculatorService(
            base_ml=self.monthly_amount_ml,
            base_nicotine_cc=nicotine_cc,
            nicotine_ml=None,
            nicotine_premix_cc=self.nicotine_premix_cc
        )

        nicotine_ml = mix_calculator_service.get_nicotine_ml()
        return nicotine_ml

    def _get_nicotine_mg(self, nicotine_ml):
        mix_calculator_service = MixCalculatorService(
            base_ml=self.monthly_amount_ml,
            base_nicotine_cc=None,
            nicotine_ml=nicotine_ml,
            nicotine_premix_cc=self.nicotine_premix_cc
        )
        nicotine_mg = mix_calculator_service.get_nicotine_mg()
        return nicotine_mg

    def plan_by_time(self):
        # TODO
        for month in range(self.reduction_time):
            pass
