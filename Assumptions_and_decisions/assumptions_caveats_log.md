# Assumptions and caveats log

This log contains a list of assumptions and caveats used in this analysis.

## Definitions

Assumptions are red, amber or green (RAG) rated according to the following definitions for quality and impact[^1]:

| RAG rating | Assumption quality | Assumption impact |
|------------|--------------------|-------------------|
| GREEN | Reliable assumption, well understood and/or documented; anything up to a validated & recent set of actual data. | Marginal assumptions; their changes have no or limited impact on the outputs.  |
| AMBER | Some evidence to support the assumption; may vary from a source with poor methodology to a good source that is a few years old. | Assumptions with a relevant, even if not critical, impact on the outputs. |
| RED   | Little evidence to support the assumption; may vary from an opinion to a limited data source with poor methodology. | Core assumptions of the analysis; the output would be drastically affected by their change. |

[^1]: With thanks to the Home Office Analytical Quality Assurance team for these definitions.

## Assumptions and caveats

Assumptions and caveats last updated: 13/03/2023

This analysis contains the following assumptions and caveats:

### Assumption 1: Number of detached houses are more than flats 

* Location: `Assumptions_and_decisions/Quantitative_assumptions/assumptions_in_code.py`
* **Quality**: RED
* **Impact**: AMBER

Detailed description: Total number of detached houses in a local authority are greater than total number of flats.

### Assumption 2: House prices are increasing over time

* Location: `Assumptions_and_decisions/Quantitative_assumptions/assumptions_in_code.py`
* **Quality**: RED
* **Impact**: AMBER

Detailed description: Total sale price of each dwelling type in time 't' should be less than time 't+1'.

### Assumption 3: House prices cannot be negative

* Location: `Assumptions_and_decisions/Quantitative_assumptions/assumptions_in_code.py`
* **Quality**: RED
* **Impact**: AMBER

Detailed description: Total sale price of each dwelling type in a local authority in a year should always be a positive number.

Currently no caveats in this analysis.
