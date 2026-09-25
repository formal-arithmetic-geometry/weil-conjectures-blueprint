+++
id = "prop-trf-levelwise-compact-support"
kind = "theorem"
title = "Levelwise compact support and stalk compatibility"
order = 2524
tags = ["latex:proposition"]
uses = ["def-trf-adic-system", "def-trf-coefficient-conventions", "def-trf-frobenius-operators", "def-weil-finite-field-fiber", "def-weil-pbc-bounded-constructible-tower", "lem-weil-pbc-reconstruction-uniform-tower", "prop-trf-compact-support-perfectness", "prop-trf-trace-formal-laws"]
+++
Fix the global finite-field datum
and the coefficient
conventions, and let
$K_\bullet\in\mathcal D^b_{ctf,\mathrm W,adic}(X,\mathcal O_E)$. Then

$$
P_n=R\Gamma_c(X,K_n),\qquad P_{\bar y,n}=(K_n)_{\bar y}
$$

are normalized systems of perfect $A_n$-complexes, all global and local
Frobenius operators are compatible with the transition maps, and the
realizations

$$
P_{\mathcal O_E}=R\!\varprojlim_n\operatorname{Res}_{n,s}P_n,\qquad
P_{\bar y,\mathcal O_E}=R\!\varprojlim_n\operatorname{Res}_{n,s}P_{\bar y,n}
$$

are the derived-complete perfect complexes over $\mathcal O_E$, with
Frobenius-equivariant realization isomorphisms

$$
R\Gamma_c(X,K_{\mathcal O_E})\xrightarrow{\ \sim\ }P_{\mathcal O_E},
\qquad
(K_{\mathcal O_E})_{\bar y}\xrightarrow{\ \sim\ }P_{\bar y,\mathcal O_E}.
$$

## Proof

Each $K_n$ is a strict Weil complex at $A_n$, so by
[prop-trf-compact-support-perfectness] each $P_n$ and
$P_{\bar y,n}$ is perfect, and each transition map is a morphism of
perfect complexes by the naturality of $R\Gamma_c$ and of stalks;
normalizedness of the systems is the normalizedness of $K_\bullet$ of
[def-trf-adic-system] together with the coefficient-reduction
isomorphisms for the compact-support direct image of the trace-formula chapter. The
Frobenius operators commute with the transitions: the global and local
operators of [def-trf-frobenius-operators] are built from
$\varphi^{[m]}$, which is compatible with the transitions by the
strict Weil structure at every level of [def-trf-adic-system];
consequently the categorical traces of the Frobenius endomorphisms form
the compatible systems of the levelwise traces (the
coefficient-reduction law of the categorical trace,
[prop-trf-trace-formal-laws], item (3), applied to the reductions
$A_{n+1}\to A_n$), which is the statement used in
[thm-trf-integral-adic-trace-formula].
The realization isomorphisms are the uniform-tower reconstruction
[lem-weil-pbc-reconstruction-uniform-tower]
of the proper-base-change chapter, applied over the point $s$ for the compact-support
system and stalkwise for the stalks, with the bounded-constructible
tower bookkeeping of [def-weil-pbc-bounded-constructible-tower];
the Frobenius-equivariance is the compatibility above.
