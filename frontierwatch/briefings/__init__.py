from frontierwatch.briefings.biotech import BiotechBriefing
from frontierwatch.briefings.computing_ai import ComputingAIBriefing
from frontierwatch.briefings.economics import EconomicsBriefing
from frontierwatch.briefings.energy import EnergyBriefing
from frontierwatch.briefings.monetary_policy import MonetaryPolicyBriefing
from frontierwatch.briefings.securities_futures import SecuritiesFuturesBriefing

BRIEFINGS = {
    "biotech": BiotechBriefing,
    "computing-ai": ComputingAIBriefing,
    "economics": EconomicsBriefing,
    "energy": EnergyBriefing,
    "monetary-policy": MonetaryPolicyBriefing,
    "securities-futures": SecuritiesFuturesBriefing,
}

__all__ = ["BRIEFINGS"]
