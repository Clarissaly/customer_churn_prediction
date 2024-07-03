def format_model_inputs(input_dict):
    contract_type_mapper = {'Month-to-Month': 1, 'One Year': 12, 'Two Year': 24}

    num_referrals = int(input_dict['num_referrals'])
    contract_type = input_dict['contract_type']
    num_dependents = int(input_dict['num_dependents'])
    tenure_months = int(input_dict['tenure_months'])
    total_monthly_fee = float(input_dict['total_monthly_fee'])
    age = int(input_dict['age'])
    zip_code = int(input_dict['zip_code'])
    avg_long_distance_fee_monthly = float(input_dict['avg_long_distance_fee_monthly'])
    total_charges_quarter = float(input_dict['total_charges_quarter'])
    paperless_billing = 1 if input_dict['paperless_billing'] == 'Yes' else 0

    # Convert contract_type to numerical value
    contract_type_encoded = contract_type_mapper[contract_type]


    model_inputs = [
        num_referrals, num_dependents, tenure_months, total_monthly_fee,
        age, zip_code, avg_long_distance_fee_monthly, total_charges_quarter,
        contract_type_encoded, paperless_billing
    ]

    return model_inputs

def validate(input_dict):
    errors = []

    required_fields = [
        'num_referrals', 'contract_type', 'num_dependents', 'tenure_months', 'total_monthly_fee',
        'age', 'zip_code', 'paperless_billing', 'avg_long_distance_fee_monthly', 'total_charges_quarter',
    ]

    for field in required_fields:
        if field not in input_dict:
            errors.append(f'{field} not found in request.')
            continue  # Skip further checks for this field if it is missing

        value = input_dict[field]

        if field in ['num_referrals', 'num_dependents', 'tenure_months', 'age', 'zip_code']:
            if not isinstance(value, int):
                errors.append(f'{field} must be of int type.')

        elif field in ['total_monthly_fee', 'avg_long_distance_fee_monthly', 'total_charges_quarter']:
            if not isinstance(value, (int, float)):
                try:
                    float(value)
                except ValueError:
                    errors.append(f'{field} must be numeric.')

    return errors
