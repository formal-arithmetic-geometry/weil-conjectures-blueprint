+++
id = "lemma-weil-sf-well-defined-def-weil-pbc-completed-base-change-map"
kind = "lemma"
title = "Well-definedness certificate for def:weil-pbc-completed-base-change-map"
order = 1996
uses = ["def-weil-pbc-completed-base-change-map", "lemma-weil-pbc-direct-image-r-lim", "lemma-weil-pbc-level-map-derived-limit", "lemma-weil-pbc-perfect-projection-formula"]
+++
With $S=Lg^*_{\mathrm{comp}}Rf_*K$ and
$T=Rf'_*L(g')^*_{\mathrm{comp}}K$, the ordered expression

$$
S\xrightarrow{s}A_\infty\xrightarrow{H}B_\infty
\xrightarrow{V'}D_\infty\xrightarrow{t}T
$$

is a morphism $S\to T$ and is the map
$\operatorname{Ex}^{\mathrm{comp}}_{\square,K}$ of Definition
[def-weil-pbc-completed-base-change-map]. The endpoint comparisons
$s,t$ and the limit projection-formula map $H$ are isomorphisms.

## Proof

Symmetric monoidality of $Lg^*$ identifies the defining completed-pullback
tower with the $A_n$ tower. The perfect projection formula then gives the
map $H:A_\infty\to B_\infty$, while finite exchange gives the compatible
tower map $V':B_\infty\to D_\infty$ recorded by
Lemma [lemma-weil-pbc-level-map-derived-limit]. Direct image commutation
with the product-cone limit gives
$t:D_\infty\xrightarrow{\sim}T$. The target of each factor is the source
of the next one.

At level $n$, $h_n$ is invertible by the perfect projection formula. From
$b_{n+1,n}h_{n+1}=h_na_{n+1,n}$, multiplication by the two inverses gives
$a_{n+1,n}h_{n+1}^{-1}=h_n^{-1}b_{n+1,n}$. Hence the inverse family is a
map of towers, and its derived limit is inverse to $H$. Thus $s,H,t$ are
isomorphisms. Expanding the ordered definition gives the displayed
composite. No invertibility or Frobenius assertion for the whole composite
is made in this certificate.
