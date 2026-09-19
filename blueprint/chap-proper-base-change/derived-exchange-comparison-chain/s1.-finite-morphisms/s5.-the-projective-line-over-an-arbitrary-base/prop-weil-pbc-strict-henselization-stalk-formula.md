+++
id = "prop-weil-pbc-strict-henselization-stalk-formula"
kind = "theorem"
title = "Strict-henselization stalk formula"
order = 723
tags = ["latex:proposition"]
uses = ["def-weil-pbc-pointed-etale-neighbourhoods", "def-weil-pbc-strict-henselization-limit", "lemma-weil-pbc-affine-neighbourhood-cofinal", "lemma-weil-pbc-etale-cohomology-continuity", "lemma-weil-pbc-fibre-product-limit"]
+++
For quasi-compact quasi-separated $f:X\to S$, torsion $F$, and $q\geq0$,

$$
(R^qf_*F)_{\bar s}\cong
H^q(X\times_SS_{(\bar s)},F|).
$$

For $K\in D^+(X_{\mathrm{et}})$ this lifts to

$$
(Rf_*K)_{\bar s}\xrightarrow{\sim}
R\Gamma(X\times_SS_{(\bar s)},K|)
$$

in $D^+(\mathbf{Ab})$.

## Proof

The stalk is the colimit over $\mathcal N_{\bar s}^{\mathrm{op}}$ of
$H^q(X\times_SV,F|)$. Replace the index by affine neighbourhoods, identify
their inverse limit by Lemma [lemma-weil-pbc-fibre-product-limit], and
apply cohomology continuity. For the derived statement, choose a
bounded-below injective complex $J^\bullet$ representing $K$. The chain map
from the stalk complex $(f_*J^\bullet)_{\bar s}$ to the sections complex on
the strict henselization is obtained by restricting each representative
section. Its map on every cohomology group is the preceding isomorphism, so
it is a quasi-isomorphism. This expands Tag `03Q9`.
