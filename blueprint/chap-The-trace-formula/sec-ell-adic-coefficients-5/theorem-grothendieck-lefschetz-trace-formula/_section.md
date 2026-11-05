+++
id = "theorem-grothendieck-lefschetz-trace-formula"
kind = "theorem"
title = "Grothendieck–Lefschetz trace formula"
order = 1017
lean = ["AlgebraicGeometry.WeilComplex.finsum_trace_compactlySupportedCohomology_eq", "AlgebraicGeometry.Etale.isPerfect_compactlySupportedGlobalSections", "AlgebraicGeometry.WeilComplex.exists_subsingleton_compactlySupportedCohomology", "AlgebraicGeometry.WeilSheaf.finiteDimensional_stalkObj", "AlgebraicGeometry.WeilComplex.exists_finset_isZero_homologySheaf"]
uses = ["definition-small-pro-etale-site", "definition-constructible-sheaves", "definition-weil-structure", "definition-trace-function", "definition-frobenius-operator", "definition-categorical-trace", "proposition-six-operations-change-coefficients"]
+++
Let $X_0$ be separated and of finite type over $\mathbf F_q$, put
$X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$, and suppose
that $\ell\nmid q$. Let

$$
\Lambda\in\{A,\mathbf Z_\ell,\mathcal O_E,\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell\},
\qquad K\in D^b_{\mathrm{ctf}}(X,\Lambda),
$$

with a Weil structure as in Definition [definition-weil-structure].
Here $A$ is any finite commutative $\ell$-primary ring, and for
integral and rational coefficients, $D^b_{\mathrm{ctf}}(X,\Lambda)=\Dbc(X,\Lambda)$.
Let $\operatorname{Frob}_{X,K}$
be the geometric Frobenius on $R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)$, and let
$\operatorname{Frob}_{y,m}$ be the Frobenius acting on the stalk $K_{\bar y}$ at
$y\in X_0(\mathbf F_{q^m})$. Then for every $m\geq1$ we have, in $\Lambda$,

$$
\operatorname{tr}_{\Lambda}
\bigl(\operatorname{Frob}_{X,K}^m\mid R\Gamma_c(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}
\operatorname{tr}_{\Lambda}
\bigl(\operatorname{Frob}_{y,m}\mid K_{\bar y}\bigr).
\tag{12.3}
$$

The complexes inside the traces are perfect over $\Lambda$, and the
formula is compatible with the change-of-coefficients maps of
Proposition [proposition-six-operations-change-coefficients]. For $\Lambda=\mathbf Q_\ell,E,\overline{\mathbf Q}_\ell$, it reads

$$
\sum_i(-1)^i\operatorname{Tr}
\bigl(\operatorname{Frob}_{X,K}^m\mid H_c^i(X_{\mathrm{pro}\acute{e}t},K)\bigr)
=\sum_{y\in X_0(\mathbf F_{q^m})}\sum_j(-1)^j
\operatorname{Tr}\bigl(\operatorname{Frob}_{y,m}\mid H^j(K_{\bar y})\bigr),
\tag{12.4}
$$

where all sums over degrees are finite.
