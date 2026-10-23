+++
id = "def-pe-derived-complete"
kind = "definition"
title = "Derived complete complexes and normalized towers"
order = 1210
uses = ["det-def-sfb-pulled-back-coefficients", "det-def-sfb-derived-categories", "def-sfb-derived-tensor-modules", "def-weil-derived-limit"]
lean = ["DerivedCategory.derivedComplete", "DerivedCategory.derivedCompleteIntegral"]
+++
Let $E/\Ql$ be finite, with uniformizer $\pi_E$, let $X$ be a scheme, and let
$\mathcal O_{E,X}=p_X^*\underline{\mathcal O_E}$ and $(\mathcal O_E/\pi_E^n)_X$ be the
integral and finite coefficient sheaves of [det-def-sfb-pulled-back-coefficients]. For
$K\in D(X_{\mathrm{proét}},\mathcal O_E)$ [det-def-sfb-derived-categories] and $n\geq1$ put

$$
K_n=K\otimes^{\mathbf L}_{\mathcal O_{E,X}}(\mathcal O_E/\pi_E^n)_X ,
$$

the derived tensor product of [def-sfb-derived-tensor-modules], with the transition maps
$K_{n+1}\to K_n$ induced by the reductions $(\mathcal O_E/\pi_E^{n+1})_X\to(\mathcal O_E/\pi_E^n)_X$
and the maps $K\to K_n$ induced by $\mathcal O_{E,X}\to(\mathcal O_E/\pi_E^n)_X$. The complex
$K$ is *derived complete* if the canonical map

$$
K\longrightarrow R\varprojlim_n K_n
$$

to the derived limit [def-weil-derived-limit] of the tower $(K_n)_n$ is an isomorphism.

The canonical transitions satisfy the *derived reduction identities*

$$
K_{n+1}\otimes^{\mathbf L}_{(\mathcal O_E/\pi_E^{n+1})_X}(\mathcal O_E/\pi_E^n)_X\simeq K_n
\qquad(n\geq1).
$$

A compatible tower $(C_n)_{n\geq1}$, with $C_n\in D(X_{\mathrm{proét}},\mathcal O_E/\pi_E^n)$,
whose transitions induce isomorphisms
$C_{n+1}\otimes^{\mathbf L}_{(\mathcal O_E/\pi_E^{n+1})_X}(\mathcal O_E/\pi_E^n)_X\simeq C_n$
is called *normalized*.
