+++
kind  = "proof"
of    = "prop-weil-pbc-strict-henselization-stalk-formula"
+++
The stalk is the colimit over pointed etale neighbourhoods, whose inverse
limit is the strict henselization by
[def-weil-pbc-strict-henselization-limit]; the fibre product
commutation of [lemma-weil-pbc-fibre-product-limit] replaces $X\times_SS_{(\bar
s)}$ by the limit of the $X\times_SV$, and
[lemma-weil-pbc-etale-cohomology-continuity] identifies the colimit of
cohomologies with the cohomology of the limit. On a bounded-below K-injective
[def-weil-pbc-kinjective-resolutions] representative the same argument gives
the derived statement.

The stalk is the colimit over $\mathcal N_{\bar s}^{\mathrm{op}}$ of
$H^q(X\times_SV,F|)$. Replace the index by affine neighbourhoods, identify
their inverse limit by Lemma [lemma-weil-pbc-fibre-product-limit], and
apply cohomology continuity. For the derived statement, choose a
bounded-below injective complex $J^\bullet$ representing $K$. The chain map
from the stalk complex $(f_*J^\bullet)_{\bar s}$ to the sections complex on
the strict henselization is obtained by restricting each representative
section. Its map on every cohomology group is the preceding isomorphism, so
it is a quasi-isomorphism. This expands Tag `03Q9`.
