+++
id = "prop-weil-pbc-scalar-extension"
kind = "theorem"
title = "Compatibility with finite scalar extension"
order = 1347
uses = ["def-weil-pbc-rational-category"]
tags = ["latex:proposition"]
+++
For a finite extension $E\subset E'$, derived scalar extension is an exact
functor
$$
 T_{E'/E}=E'\otimes_E^L-:
 \Dbc(T,E)\longrightarrow\Dbc(T,E').
$$
Choose $T_{E/E}=\operatorname{id}$ literally. For $E\subset E'\subset E''$,
derived tensor associativity gives a specified exact natural isomorphism
$$
 a_{E'',E',E}:T_{E''/E'}T_{E'/E}
 \xrightarrow{\sim}T_{E''/E}.
$$
These associators satisfy the unit equations and the pentagon for four
nested fields. Exactness supplies natural shift comparisons
$$
 \sigma_{E'/E,K}:T_{E'/E}(K[1])
 \xrightarrow{\sim}(T_{E'/E}K)[1]
$$
which commute with the associators.

There are coherent natural isomorphisms
$$
 E'\otimes_E^LRf_{*,E}K\xrightarrow{\sim}
 Rf_{*,E'}(E'\otimes_E^LK)
$$
and analogous isomorphisms for pullback. Under these isomorphisms, scalar
extension of the $E$-exchange map is the $E'$-exchange map.
