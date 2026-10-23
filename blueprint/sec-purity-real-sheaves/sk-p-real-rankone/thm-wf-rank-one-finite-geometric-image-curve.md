+++
id = "thm-wf-rank-one-finite-geometric-image-curve"
kind = "theorem"
title = "Finite geometric image of a rank-one Weil character on a curve"
lean = ["AlgebraicGeometry.WeilGroup.eq_one_of_conj_invariant", "AlgebraicGeometry.WeilGroup.exists_pow_eq_one_of_continuous", "AlgebraicGeometry.WeilGroup.finite_range_of_continuous"]
order = 3847
uses = ["def-weil-pbc-scheme-conventions", "def-wf-weil-group", "lem-wf-additive-characters-h1", "lem-wf-compact-character-logarithm", "lem-wf-deep-principal-unit-log", "prop-wf-open-curve-h1-no-frobenius-fixed"]
+++
Let $U_0/\mathbf F_q$ be normal, geometrically connected,
separated and of finite type,
pure of dimension one. Put
$U=U_0\times_{\mathbf F_q}\overline{\mathbf F}_q$ and
$\Pi=\pi_1(U,\bar u)$. Let $\ell\nmid q$, let
$E/\mathbf Q_\ell$ be finite, and let

$$
\chi:\hyperref[def-wf-weil-group]{W(U_0,\bar u)}\longrightarrow E^\times
$$

be a continuous character. Then $\chi(\Pi)$ is finite. Equivalently,
there is $N\geq1$ such that $\chi(g)^N=1$ for every $g\in\Pi$.
The scheme and Weil-group conventions are those of
[def-weil-pbc-scheme-conventions], [def-wf-weil-group].
