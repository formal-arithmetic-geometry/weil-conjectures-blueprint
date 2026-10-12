+++
kind  = "proof"
of    = "prop-trf-scheme-galois-comparison"
+++
Write $F_X^{(q)}$ for absolute $q$-power Frobenius.
The canonical trivialization of
[lem-trf-absolute-frobenius-site], iterated $a$ times, gives
$L(F_X^{(q)})^*\simeq\operatorname{id}$.
The factorization [prop-trf-frobenius-factorization] gives
$\Phi=g_\gamma F_X^{(q)}$, where $g_\gamma=g_\sigma^{-1}$
as in [def-trf-scheme-frobenius]. Thus functoriality of pullback
and this specified trivialization give

$$
L\Phi^*=L(F_X^{(q)})^*Lg_\gamma^*
\xrightarrow{\sim}Lg_\gamma^*.
$$

This defines $\kappa$. For $\Phi^m=g_\gamma^mF_X^{(q^m)}$ the
same construction is the multiplicative iterate $\kappa^{(m)}$:
the relative Frobenius maps compose to the corresponding power maps.
The resulting identifications therefore respect both the
factorization and addition of the exponents.
