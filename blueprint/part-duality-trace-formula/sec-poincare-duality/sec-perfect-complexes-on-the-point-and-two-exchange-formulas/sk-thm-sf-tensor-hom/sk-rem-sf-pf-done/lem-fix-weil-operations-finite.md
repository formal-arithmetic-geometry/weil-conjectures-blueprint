+++
id = "lem-fix-weil-operations-finite"
kind = "lemma"
title = "Weil structures on operations: finite and integral coefficients"
order = 3476
uses = ["lem-fix-weil-operations", "def-weil-weil-sheaf-complex", "def-weil-frobenius-detailed", "fix-lem-exchanges", "def-exchange-projection", "thm-pur-weil-equivariance-of-purity-and-trace"]
+++
This is the companion of [lem-fix-weil-operations] for $\Lambda=A$ finite and
$\Lambda=\mathcal O_E$. Let $f_0:X_0\to Y_0$ be a separated finite-type
morphism over the finite base field, $f:X\to Y$ its geometric fiber, and
$g_X,g_Y$ the geometric-Frobenius automorphisms of
[def-weil-frobenius-detailed]. For strict Weil data $(K,\varphi_K)$ on $X$
([def-weil-weil-sheaf-complex]) define, for $\diamond=*,!$,

$$
g_Y^*Rf_\diamond K
\xrightarrow{\mathrm{Ex}_\diamond}
Rf_\diamond g_X^*K
\xrightarrow{Rf_\diamond(\varphi_K)}
Rf_\diamond K.
$$

For $Y$ the point this gives the ordinary and the compactly supported global
Frobenius on $R\Gamma(X,K)$ and $R\Gamma_c(X,K)$. Tensor, evaluation and the
projection maps are equivariant; together with the equivariance of the smooth
trace ([thm-pur-weil-equivariance-of-purity-and-trace]) this makes the
Poincaré pairing equivariant, with the prescribed Tate action.
