+++
kind  = "proof"
of    = "lem-weil-extension-by-zero-exact"
+++
By [lem-weil-extension-by-zero-adjunction], $j_!$ is a left adjoint, so it
preserves all colimits, in particular finite ones. For finite limits use the
presheaf construction of [def-weil-extension-by-zero]: finite limits of
presheaves are computed objectwise, and on an object over $U$ the presheaf
is the corresponding value of the given sheaf, while on other objects it is
zero. Hence the presheaf construction preserves finite limits. Sheafification
of $\mathcal A$-valued presheaves preserves finite limits, since filtered
colimits are exact in the Grothendieck abelian category $\mathcal A$. So
$j_!$ preserves finite limits, and an additive functor between abelian
categories preserving finite limits and finite colimits is exact.
