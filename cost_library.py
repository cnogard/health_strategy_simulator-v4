# cost_library.py

# Core healthcare cost references (used across simulation)
HEALTHCARE_COSTS = {
    "chronic": {
        "per_patient": 6000,  # CMS/Highmark estimate for chronic management
        "national_total": 4.5e12,  # CDC total chronic condition spend
    },
    "cancer": {
        "initial": 50000,      # Avg initial treatment (NCI)
        "continuing": 8000,    # Annual ongoing care
        "end_of_life": 130000, # End-of-life cancer care (NCI, AARP)
        "oop_initial": 2200,   # Out-of-pocket for initial
        "oop_eol": 3823,       # OOP end-of-life
        "avg_total": 150000    # AARP estimate for total cancer care
    },
    "surgery": {
        "gastric_bypass": 24000,  # National average
        "heart_failure": 35000000000  # Total inpatient cost nationally
    }
}

# Medicare-adjusted cost factors (approximate)
MEDICARE_DISCOUNTS = {
    "chronic": 0.7,  # Estimated 30% discount
    "cancer": {
        "initial": 0.75,
        "continuing": 0.8,
        "end_of_life": 0.7,
    },
    "surgery": {
        "gastric_bypass": 0.65,
        "heart_failure": 0.6,
    }
}


# Utility function to retrieve costs with optional Medicare adjustment
def get_cost(category, field, rate_type="base"):
    """
    Retrieve a cost value for a given healthcare category and field.
    If rate_type is 'medicare', apply the Medicare discount if available.
    """
    try:
        base = HEALTHCARE_COSTS[category][field]
        if rate_type == "medicare":
            discount = MEDICARE_DISCOUNTS.get(category)
            if isinstance(discount, dict):
                return base * discount.get(field, 1.0)
            return base * discount
        return base
    except KeyError:
        return 0


# Estimate out-of-pocket costs for uninsured individuals based on health status
def estimate_uninsured_oop(health_status, full_cost):
    """
    Estimate out-of-pocket costs for uninsured individuals based on health status.
    Applies discount ratios derived from real-world negotiation power and complexity.

    Parameters:
        health_status (str): One of "healthy", "chronic", or "high_risk"
        full_cost (float): Estimated full cost of care

    Returns:
        float: Adjusted OOP cost
    """
    discount_factors = {
        "healthy": 0.20,     # Pays 20% of full cost
        "chronic": 0.30,     # Pays 30%
        "high_risk": 0.50    # Pays 50%
    }
    discount = discount_factors.get(health_status, 0.40)  # Default conservative estimate
    return full_cost * discount


# Estimate uninsured out-of-pocket costs by health risk level and year.
def estimate_uninsured_oop_by_year(health_risk_level, year, base_full_cost=10000):
    """
    Estimate uninsured out-of-pocket costs by health risk level and year.
    The costs increase with health risk and over time, reflecting progression.

    Parameters:
    - health_risk_level: str, one of ['healthy', 'chronic', 'high-risk']
    - year: int, simulation year starting at 1
    - base_full_cost: float, baseline full cost for year 1

    Returns:
    - float: estimated uninsured out-of-pocket cost for the given year and health risk
    """
    # Base discount for uninsured (e.g., 20% discount from full cost)
    base_discount = 0.8

    # Growth factors per year to simulate progression
    growth_factors = {
        'healthy': 1.0 + 0.02 * (year - 1),    # ~2% increase per year
        'chronic': 1.0 + 0.05 * (year - 1),    # ~5% increase per year
        'high-risk': 1.0 + 0.10 * (year - 1),  # ~10% increase per year
    }

    base_full_costs = {
        'healthy': 5000,
        'chronic': 10000,
        'high-risk': 15000
    }

    if health_risk_level not in base_full_costs:
        raise ValueError(f"Invalid health risk level: {health_risk_level}")

    base_cost = base_full_costs[health_risk_level] * 0.8
    growth = growth_factors[health_risk_level]
    # Correction factor for 60-year window vs. original 40-year study window
    correction_factor = 40 / 60  # scale down to match original study period
    estimated_oop = base_cost * growth * correction_factor
    return estimated_oop


# Calibrated cost curve for Healthy or Chronic cardiovascular profiles
def get_calibrated_cost_curve(profile_type, years=60):
    """
    Returns a calibrated annual cost curve for Healthy or Chronic cardiovascular profiles.
    Based on validated lifetime cost totals ($75.2K for Healthy, $459K for Chronic).
    """
    inflation = {"healthy": 0.02, "chronic": 0.03}
    totals = {"healthy": 75200, "chronic": 459000}
    if profile_type not in totals:
        raise ValueError("Unsupported profile type for calibrated curve.")
    r = inflation[profile_type]
    base = totals[profile_type] / sum([(1 + r) ** i for i in range(years)])
    return [base * (1 + r) ** i for i in range(years)]

def determine_profile_type(cv_risk_score):
    """
    Map cardiovascular risk score to profile type.
    0 = Healthy, 1–2 = Chronic, 3+ = Unclassified/High Risk
    """
    if cv_risk_score == 0:
        return "healthy"
    elif cv_risk_score in [1, 2]:
        return "chronic"
    else:
        return None

def estimate_high_risk_curve(years=60, base=10000, inflation=0.05):
    """
    Placeholder cost curve for high-risk individuals (non-cardiovascular).
    """
    return [base * (1 + inflation) ** i for i in range(years)]