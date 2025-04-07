# write functions here, don't add input('') statements here!

def get_assessment_value(value):
    assessment_value = value * .6
    return assessment_value

def get_tax_assets(assessment_value):
    tax_cut = assessment_value / 100
    assessment_value = tax_cut * .72
    return assessment_value