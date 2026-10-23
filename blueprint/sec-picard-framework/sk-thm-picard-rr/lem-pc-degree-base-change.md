+++
id = "lem-pc-degree-base-change"
kind = "lemma"
title = "Degree: base change and tensor products"
lean = ["AlgebraicGeometry.Scheme.Modules.degree_pullback", "AlgebraicGeometry.Scheme.Modules.degree_pullback_of_isPullback", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.eulerChar_cokernel_whiskerRight", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.eulerChar_tensorObj_dual_toModules", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.degree_dual_toModules", "AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.degree_dual_toModules_eq_one", "AlgebraicGeometry.Scheme.Modules.degree_tensorObj", "AlgebraicGeometry.Scheme.degree_tensorObj_pullback_fst"]
order = 737
uses = ["def-pc-base-change", "def-pc-degree-line-bundle", "def-pc-divisor-line-bundle", "def-pc-euler-characteristic", "def-nagata-invertible-ideal", "def-sc-invertible-module", "pqf-lem-affine-vanishing", "lem-pc-euler-additive", "lem-pc-euler-characteristic-well-defined", "lem-pc-flat-base-change-cohom", "lem-pc-proper-base-change", "lem-sc-point-cartier", "lem-sc-smooth-regular", "lem-sc-regular-dim1-dvr"]
+++
Let $k$ be a field and $X$ a proper scheme over $k$.

1. (Base change) For an invertible $\mathcal{O}_X$-module $\mathcal{L}$
and a field extension $K/k$:
$\deg_{X_K}(\mathcal{L}\otimes_kK)=\deg_X(\mathcal{L})$.
1. (Tensor products and effective divisors) Suppose moreover that $X$ is
smooth of relative dimension $1$ over $k$, and let $\mathcal{L},\mathcal{M}$
be invertible $\mathcal{O}_X$-modules. Then
$\deg(\mathcal{L}\otimes\mathcal{M})=\deg(\mathcal{L})+\deg(\mathcal{M})$.
If $D\subset X$ is an effective Cartier divisor and
$\mathcal{M}=\mathcal{O}_X(D)$, then
$$
\chi(X,\mathcal{L}\otimes\mathcal{M})=\chi(X,\mathcal{L})+\dim_kH^0(D,\mathcal{O}_D),\qquad
\deg(\mathcal{M})=\dim_kH^0(D,\mathcal{O}_D),
$$
so that $\chi(X,\mathcal{L}\otimes\mathcal{M})=\deg(\mathcal{L})+\chi(X,\mathcal{M})$;
if $D$ is a $k$-rational point then $\deg(\mathcal{O}_X(D))=1$, and for a
finite sum $D=\sum_in_i[P_i]$ ($n_i\ge0$) of $k$-rational points
$\deg(\mathcal{O}_X(D))=\sum_in_i$. Finally, for a field extension $K/k$,
an invertible $\mathcal{L}'$ on $X_K$ and $\mathcal{M}$ as above,
$\deg_{X_K}(\mathcal{L}'\otimes\mathcal{M}_K)=\deg_{X_K}(\mathcal{L}')+\deg_X(\mathcal{M})$.
1. (Additivity) For a short exact sequence of coherent modules
$0\to\mathcal{F}_1\to\mathcal{F}_2\to\mathcal{F}_3\to0$:
$\chi(X,\mathcal{F}_2)=\chi(X,\mathcal{F}_1)+\chi(X,\mathcal{F}_3)$
([lem-pc-euler-additive]).
