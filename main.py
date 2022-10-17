import numpy as np

rxn = input("Enter reactions in the form 2H2 + O2 -> 2H20:\n\t")

# split rxn
rxn = rxn.replace(" ", "").strip().split('->')
rhs, lhs = rxn

def get_detailed_info(side):
    side = side.split('+')
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

def print_detailed_info(rhs, lhs):
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

print_detailed_info(rhs, lhs)