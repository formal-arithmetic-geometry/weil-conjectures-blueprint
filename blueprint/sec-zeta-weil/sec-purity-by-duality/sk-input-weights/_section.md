+++
id = "sk-input-weights"
kind = "corollary"
title = "Purity of the cohomology of a smooth proper variety"
order = 792
lean = ["AlgebraicGeometry.WeilSheaf.isPureOfWeightOver_cohomology_of_isLisse", "AlgebraicGeometry.WeilSheaf.isLisse_adicConstant", "AlgebraicGeometry.WeilSheaf.isPunctuallyPureOfWeight_adicConstant", "Polynomial.IsMixedOfWeightLE", "TraceDatum.norm_eq_of_mem_roots_charpoly_map_of_pairing", "TraceDatum.isPureOfWeight_map_P_of_pairing"]
uses = ["sk-d-real-weights", "sk-prop-smooth-proper-purity", "sk-cor-dl-general-complex", "sk-prop-sf-comp-proper"]
tags = ["sketch"]
+++
Let $X_0/\mathbf F_q$ be smooth proper of pure dimension $d$, put
$X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$, let $\ell\nmid q$
be a prime, and let
$\iota:\overline{\mathbf Q}_\ell\hookrightarrow\mathbf C$ be a field
embedding. Then every geometric Frobenius eigenvalue $\alpha$ on
$H^i(X_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell)$ satisfies

$$
|\iota(\alpha)|=q^{i/2}.
$$

*Complement.* For every $i$: the constant Weil sheaf is $\iota$-pure of
weight $0$; $H_c^{i}(X,\Qlb)$ is $\iota$-mixed of weights $\le i$; the
comparison $H_c^{i}(X,\Qlb)\to H^{i}(X,\Qlb)$ is a Frobenius-equivariant
isomorphism; and the reciprocal roots of
$\det(1-TF\mid H^i(X,\Ql))$, which are the eigenvalues of $F$ on
$H^i(X,\Ql)\otimes\Qlb=H^i(X,\Qlb)$, satisfy $|\iota(\alpha)|=q^{i/2}$.
