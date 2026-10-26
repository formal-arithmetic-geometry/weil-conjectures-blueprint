+++
id = "lem-coef-normalized-dvr-effectivity"
kind = "lemma"
title = "Effectivity of a normalized tower"
order = 2970
uses = ["sk-def-sp-normalized-towers", "det-sp-coefficient-towers-abelian", "def-pe-derived-complete", "sk-prop-pe-milnor", "sk-prop-sfb-qlbar-colimit-x"]
+++
Let $E/\Ql$ be finite, $T$ a scheme, and $\pi_E\in\{\pi_E,\ell\}$; put
$A_n=\mathcal O_E/\pi_E^n$, so that $(A_n)_T=\mathcal O_{E,T}/\pi_E^n$. Let
$(M_n)_n$ be a tower of complexes $M_n\in D(T_{\mathrm{proét}},A_n)$, given as an
object of the derived category of towers of
[det-sp-coefficient-towers-abelian], whose reduction maps

$$
M_m\otimes^{\mathbf L}_{A_m}A_n\longrightarrow M_n\qquad(m\geq n)
$$

are isomorphisms; this is the normalization condition of
[sk-def-sp-normalized-towers], without its constructibility and boundedness
conditions. Put $M=R\varprojlim_mM_m\in D(T_{\mathrm{proét}},\mathcal O_E)$, the
derived limit of [sk-prop-pe-milnor] with each $M_m$ regarded as an
$\mathcal O_{E,T}$-module. Then the canonical maps

$$
M\otimes^{\mathbf L}_{\mathcal O_{E,T}}A_n\xrightarrow{\ \sim\ }M_n
\qquad(n\geq1)
$$

are isomorphisms, compatible with the reduction maps. In particular $M$ is
derived $\pi_E$-complete in the sense of [def-pe-derived-complete], and
$(M_n)_n$ is isomorphic to the tower of reductions of $M$. No
constructibility or boundedness is required for this effectivity assertion.
