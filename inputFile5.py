def get_rule_category(rule):
    # ini comment singleline
    ''' 
    ini comment multiline
    '''
    # ini comment singleline
    """
    ini comment multiline
    """
    rule_product = rule[product]
    if len(rule_product) == 0:
        return EPSILON_RULE_KEY
    elif len(rule_product) == 1:
        if rule_product[0].islower:
            return TERMINAL_RULE_KEY
        else:
            return UNARY_RULE_KEY
    elif len(rule_product) == 2:
        return BINARY_RULE_KEY
    else:
        return 5
    print (fr + 'fr123')
    len((4 == ( 4 + 1 )))
    