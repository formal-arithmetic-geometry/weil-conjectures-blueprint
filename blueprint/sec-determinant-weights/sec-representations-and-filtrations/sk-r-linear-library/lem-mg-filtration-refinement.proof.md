+++
kind  = "proof"
of    = "lem-mg-filtration-refinement"
+++
For every index with $M_i/M_{i-1}\ne0$, choose a composition series,
using [lem-mg-composition-series-exists]; indices with zero quotient
contribute no factors. Pull the chosen terms back to $M_i$
and concatenate the resulting chains. This refines the displayed
filtration to a composition series in the sense of
[def-mg-weil-composition-series], and its factors are precisely the
factors of the successive quotients. Independence of all choices follows
from [lem-mg-jordan-holder].
