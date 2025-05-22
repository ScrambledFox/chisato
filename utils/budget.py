import logging
from utils.config import get_config


def do_planned_budget_check():
    """
    Perform planned budget checks.

    Budgets: {'general': {'currency': 'EUR'}, 'income': {'predicited_monthly_income': 3524.0}, 'budgets': {'groceries': 600.0, 'savings': 500.0, 'vehicle_maintenance': 100.0}, 'static_costs': {'rent': 1316.38, 'utilities': 131.9, 'internet': 61.5, 'insurance': 199.63, 'taxes': 125.01, 'subscriptions': 30.32}}
    """
    budgets = get_config("budgets.toml")

    all_income_categories = budgets["income"]
    # sum all income
    total_income = sum(all_income_categories.values())
    logging.info(f"Total planned income: {total_income}")

    static_costs_categories = budgets["static_costs"]
    # sum all static costs
    total_static_costs = sum(static_costs_categories.values())
    logging.info(f"Total planned static costs: {total_static_costs}")

    budgets_categories = budgets["budgets"]
    # sum all budgets
    total_budgets = sum(budgets_categories.values())
    logging.info(f"Total planned budgets: {total_budgets}")

    # Calculate the remaining budget
    remaining_budget = total_income - total_static_costs - total_budgets
    warning_threshold = budgets["general"]["warning_threshold"]

    # Check if the remaining budget is negative
    if remaining_budget < 0:
        logging.error(f"Warning: Remaining budget ({remaining_budget}) is negative!")
    elif remaining_budget < warning_threshold:
        logging.warning(
            f"Warning: Remaining budget ({remaining_budget}) is below the warning threshold of {warning_threshold}!"
        )
    else:
        logging.info(f"Remaining budget: {remaining_budget}")


def do_budget_checks():
    """
    Perform budget checks for the current month.
    """

    # # Get the current month and year
    # now = datetime.now()
    # current_month = now.month
    # current_year = now.year

    # # Check if the budget for the current month has been set
    # budget = db.get_budget(current_month, current_year)
    # if not budget:
    #     print(f"No budget set for {current_month}/{current_year}.")
    #     return

    # # Check if the budget has been exceeded
    # expenses = db.get_expenses(current_month, current_year)
    # if expenses > budget:
    #     print(f"Budget exceeded! Expenses: {expenses}, Budget: {budget}")
    # else:
    #     print(f"Budget is within limits. Expenses: {expenses}, Budget: {budget}")


def do_budget_prognosis_check():
    """
    Perform budget prognosis checks.
    """
    pass
