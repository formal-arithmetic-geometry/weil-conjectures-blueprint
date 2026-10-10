+++
id = "lem-wf-curve-h1-dual-tate-module"
kind = "lemma"
title = "Untwisted integral classes form the dual Tate module"
order = 2621
uses = ["def-sc-jacobian", "def-weil-pbc-etale-cohomology", "def-wf-abelian-tate-module", "lem-wf-curve-finite-level-pd", "lem-wf-curve-kummer-jacobian-tate-module", "lem-wf-geometric-jacobian-galois-action", "thm-av-final", "thm-pod-equivariance-of-the-twisted-pairing"]
+++
Let $C_0/k_0$ be a smooth projective geometrically connected curve,
let $C=C_0\times_{k_0}\overline{k}_0$, and let $J$ be its
Jacobian, equipped with the canonical semilinear
$\operatorname{Gal}(\overline{k}_0/k_0)$-action of
[lem-wf-geometric-jacobian-galois-action]. Put
$A_n=\mathbf Z/\ell^n\mathbf Z$. There is a natural Galois-equivariant
isomorphism

$$
\varprojlim_n H^1_{\mathrm{\acute et}}(C,A_n)
\xrightarrow{\sim}
\operatorname{Hom}_{\mathbf Z_\ell}(T_\ell J,\mathbf Z_\ell).
\tag{4.1}
$$

Here $\ell\ne\operatorname{char}k_0$, and the inverse limit uses the
reduction maps in the coefficient system.
The Tate module and etale cohomology are those of
[def-wf-abelian-tate-module], [def-weil-pbc-etale-cohomology].
