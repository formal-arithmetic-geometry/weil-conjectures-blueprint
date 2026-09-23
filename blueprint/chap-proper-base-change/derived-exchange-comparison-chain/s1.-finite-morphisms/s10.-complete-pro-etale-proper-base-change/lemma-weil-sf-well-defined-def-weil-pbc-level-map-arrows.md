+++
id = "lemma-weil-sf-well-defined-def-weil-pbc-level-map-arrows"
kind = "lemma"
title = "Well-definedness certificate for def:weil-pbc-level-map-arrows"
order = 1868
uses = ["def-weil-pbc-level-map-arrows", "lemma-weil-pbc-perfect-projection-formula", "prop-weil-pbc-proet-finite-level-transport"]
+++
For $n\geq1$, the tuple $(h_n,v_n,h'_n,v'_n)$ belongs to

$$
\operatorname{Hom}(A_n,B_n)\times
\operatorname{Hom}(A_n,C_n)\times
\operatorname{Hom}(C_n,D_n)\times
\operatorname{Hom}(B_n,D_n),
$$

and $h_n,h'_n$ are isomorphisms. Under finite-level pro-etale transport,
the fourth component is the unit–counit exchange map $\xi_{K_n}$.

## Proof

Perfectness of $P_n$ makes
$\pi_{f,K,n}:(Rf_*K)\otimes^LP_n\to Rf_*K_n$ and
$\pi_{f',E,n}:(Rf'_*E)\otimes^LP_n\to Rf'_*E_n$ isomorphisms.
Derived pullback preserves the first isomorphism, giving the stated type and
invertibility of $h_n$; the second gives the same facts for $h'_n$.
Symmetric monoidality of derived pullback gives

$$
Lg^*((Rf_*K)\otimes^LP_n)\simeq
(Lg^*Rf_*K)\otimes^LP_n,
$$

so tensoring $\xi_K$ with $1_{P_n}$ has type $A_n\to C_n$.
Proposition [prop-weil-pbc-proet-finite-level-transport] transports the
finite etale-origin exchange to a map $B_n\to D_n$ and identifies that map
with the unit–counit formula $\xi_{K_n}$. These are exactly the four
components asserted above; no rectangle or tower equation is used here.
