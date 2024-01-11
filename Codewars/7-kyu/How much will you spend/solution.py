def get_total(costs, items, tax):
    return round(sum(costs.get(item, 0) for item in items) * (1 + tax), 2)