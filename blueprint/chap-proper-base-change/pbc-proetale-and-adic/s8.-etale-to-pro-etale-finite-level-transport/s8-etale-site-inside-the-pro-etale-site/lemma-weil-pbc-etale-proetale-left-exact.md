+++
id = "lemma-weil-pbc-etale-proetale-left-exact"
kind = "lemma"
title = "Finite-limit preservation of the inclusion"
order = 1867
uses = ["def-weil-pbc-etale-proetale-inclusion", "lemma-weil-pbc-etale-proetale-functor"]
+++
The functor $\iota_X$ preserves the terminal object and fiber products, hence
is left exact.

## Proof

The terminal object in both A2 sites is $1_X:X\to X$, and $\iota_X$ fixes it.
For a diagram $U\to W\leftarrow V$ of etale $X$-objects, its fiber product in
both over-categories has underlying scheme $U\times_WV$ with the same two
projections and structural map to $X$. Etale morphisms are stable under base
change and composition, so this is again an etale object. Thus the canonical
map

$$
\iota_X(U\times_WV)\longrightarrow
\iota_XU\times_{\iota_XW}\iota_XV
$$

is the identity on $U\times_WV$, and is an isomorphism. Terminal objects and
fiber products generate finite limits.
