+++
id = "lem-wf-curve-kummer-jacobian-tate-module"
kind = "lemma"
title = "Kummer identifies curve cohomology with the Jacobian Tate module"
lean = ["AlgebraicGeometry.Scheme.kummerTorsionEquiv"]
order = 3830
uses = ["def-coefficient-twists-detailed", "def-sc-jacobian", "def-sc-kummer-sequence", "def-sc-pic0", "def-wf-abelian-tate-module", "lem-sc-global-functions", "lem-sc-h1-gm-pic", "lem-sc-kummer-exact", "lem-wf-geometric-jacobian-galois-action", "thm-sc-jacobian-representability"]
+++
Let $C_0/k_0$ be a smooth projective geometrically connected curve, put
$C=C_0\times_{k_0}\overline{k}_0$, and let $J$ be its
Jacobian, equipped with the canonical semilinear
$\operatorname{Gal}(\overline{k}_0/k_0)$-action of
[lem-wf-geometric-jacobian-galois-action]. For
$\ell\ne\operatorname{char}k_0$, the
Kummer twist gives natural
Galois-equivariant isomorphisms

$$
H^1(C,A_n(1))\xrightarrow{\sim}J[\ell^n](\overline{k}_0).
$$

Here $A_n=\mathbf Z/\ell^n\mathbf Z$, and these isomorphisms are
compatible with the transition maps.
The Jacobian, Tate module, and twist in this display are those of
[def-sc-jacobian], [def-wf-abelian-tate-module], [def-coefficient-twists-detailed].
