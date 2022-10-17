import numpy as np

def get_rxn():
    rxn = input("Enter reactions in the form 2H2 + O2 -> 2H20:\n\t")
    # split rxn
    rxn = rxn.replace(" ", "").strip().split('->')

    out = []
    for side in rxn:
        side = side.split('+')
        side = [term.replace('_', '').upper() for term in side]
        out.append(side)
    return(out)

def get_all_rxn():
    all_rxns = []
    print('enter rxns. when complete, type STOP')
    while True:
        rxn = get_rxn()
        if rxn[0][0].upper().strip() == 'STOP':
            return all_rxns
        else:
            all_rxns.append(rxn)


def get_detailed_info(side):
    side = side.split('+') # TODO UPDATE to work with get rxn
    side_terms = []
    side_list_terms = []
    for term in side:
        term = term.replace('_', '').upper()

        # check if term has coef
        term_list = [n for n in term]

        coef = 1
        if term_list[0].isdigit():
            # term DOES have coef
            coef = int(term_list.pop(0))

        # loop through all species in term
        spec_info = {}
        while len(term_list) > 0:
            species = term_list.pop(0).upper()

            # check if subscript

            # ensure not end
            subscript = 1
            if len(term_list) != 0:
                if term_list[0].isdigit():
                    subscript = int(term_list.pop(0))

            spec_info[species] = subscript

            side_list_terms.append([term, coef, species, subscript, coef*subscript])

        side_terms.append({term:{'coef':coef, 'species':spec_info}})


    return(side_terms, side_list_terms)

def print_detailed_info(rxn):
    lhs, rhs = rxn
    print('Detailed Information:')
    print('\t\tTerm\tCoef\tSpecies\tSubscript\tTotal Num of Species')
    print('Reactants:')
    side_list = get_detailed_info(lhs)[1]
    for term in side_list:
        print('\t\t'.join(str(t) for t in term))

    print('\nProducts:')
    side_list = get_detailed_info(rhs)[1]
    for term in side_list:
        print('\t\t'.join(str(t) for t in term))

def get_stoich_vector(rxn):
    all_terms = {}
    for i in range(len(rxn)):
        coef_multiplier = i*2-1 #0-1->-1 for lhs. 2-1->1 for rhs
        side = rxn[i].split('+')
        for term in side:
            coef = get_coef(term) * coef_multiplier
            all_terms[term] = coef
    print(all_terms)

def get_coef(term):
    term = term.replace('_', '').upper()
    term_list = [n for n in term]
    coef = 1
    if term_list[0].isdigit():
        # term DOES have coef
        coef = int(term_list.pop(0))

    return coef

def get_stoich_matrix():
    # TODO add multiple rxns
    pass

a = get_all_rxn()
print(a)
#rxn = get_rxn()
#print_detailed_info(rxn)
#get_stoich_matrix(rxn)