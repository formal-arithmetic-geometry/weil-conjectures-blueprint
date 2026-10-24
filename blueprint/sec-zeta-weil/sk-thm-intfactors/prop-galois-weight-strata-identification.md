+++
id = "prop-galois-weight-strata-identification"
kind = "theorem"
title = "Identification of the stratum root multisets"
lean = ["Polynomial.roots_reverse_weilStratumPoly"]
order = 4137
tags = ["latex:proposition"]
uses = ["def-weil-normalized-integral-fraction", "def-weil-numbers", "def-weil-ordinary-reciprocal-roots", "prop-galois-weight-strata"]
+++
In the situation of [prop-galois-weight-strata], for every integer
$i$ with $0\leq i\leq2d$ the
reciprocal-root multiset of
$Q_i$, equivalently the root multiset of
$Q_i^\#(U)=U^{\deg Q_i}Q_i(U^{-1})$, is exactly the submultiset of the
roots of $A^\#$ satisfying the weight-$i$
$q$-Weil condition when $i$ is odd, and
exactly the submultiset of the roots of $B^\#$ satisfying that condition
when $i$ is even; the multiset is therefore determined by the weight
condition alone and does not depend on the ordering of the roots.
