from dataclasses import dataclass
from datetime import datetime
import pandas as pd


@dataclass
class LandingSite:
    name: str
    lat: float                  # Deg (-90 a 90)
    lon: float                  # Deg (-180 a 180)
    dispersion_m: float = 50.0  # sigma in m (standard desviation)


@dataclass
class MissionWindow:
    start_date: datetime
    end_date: datetime
    step_hours: float = 1.0


@dataclass
class RiskReport:
    site: LandingSite
    prob_energy_success: float
    prob_comms_success: float
    expected_solar_uptime: float
    expected_comms_uptime: float
    worst_blackout_hours: float
    viability_score: float
    mc_samples_df: pd.DataFrame
