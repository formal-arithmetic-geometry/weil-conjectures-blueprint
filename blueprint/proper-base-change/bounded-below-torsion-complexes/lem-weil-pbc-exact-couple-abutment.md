+++
id = "lem-weil-pbc-exact-couple-abutment"
kind = "lemma"
title = "Abutment identification"
order = 1186
lean = ["AlgebraicGeometry.Etale.truncationExactCoupleMap_abutment"]
uses = ["def-weil-pbc-hypercohomology-filtrations-detailed", "def-weil-pbc-truncation-exact-couples-detailed", "def-weil-pbc-derived-exchange"]
+++
In total degree $n$, the map on the abutments of the spectral sequences of
[def-weil-pbc-hypercohomology-filtrations-detailed] is

$$
 \mathcal H^n(\Ex_{\square,K}):
 g^{-1}\mathcal H^n(Rf_*K)\longrightarrow
 \mathcal H^n(Rf'_*g'^{-1}K),
$$

with the image filtrations of
[def-weil-pbc-truncation-exact-couples-detailed].

## Proof

Choose $a$ with $\mathcal H^q(K)=0$ for $q<a$. In both couples of
[def-weil-pbc-truncation-exact-couples-detailed], their terms $D^{p,q}$ vanish
for $q<a$, since $\tau_{\leq q}K=0$. The $E_2^{p,q}$ terms vanish for $q<a$
and for $p<0$, the latter because right-derived direct image on a sheaf has no
negative cohomology. Thus the hypotheses of the half-plane convergence theorem
hold for both couples. By the couple-morphism lemma, their morphism induces,
for every $n$, a map of the abutments of the two spectral sequences of
[def-weil-pbc-hypercohomology-filtrations-detailed] respecting their filtered
structures. The abutments are $\mathcal H^n(g^{-1}Rf_*K)$ and $\mathcal
H^n(Rf'_*g'^{-1}K)$ with the image filtrations supplied by the truncation
triangles of [def-weil-pbc-truncation-exact-couples-detailed]. More
explicitly, the canonical abutment is $D^{0,n}$, and its map is the component
$t_D^{0,n}$, obtained by applying the exchange morphism of
[def-weil-pbc-derived-exchange] to $\tau_{\leq n}K$. Both functors carry
$\tau_{\geq n+1}K$ to complexes with no cohomology in degrees $\leq n$, so the
truncation triangle identifies these $D^{0,n}$ terms with the displayed
degree-$n$ cohomology of the whole complexes. Naturality of exchange in
$\tau_{\leq n}K\to K$ identifies $t_D^{0,n}$ with $\mathcal
H^n(\Ex_{\square,K})$, as required.

Unresolved dependencies: lem:sp-couple-morphism, def:sp-convergence, thm:sp-half-plane-convergence
