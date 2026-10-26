+++
id = "prop-cohomological-finiteness"
kind = "theorem"
title = "Compact-support finiteness and Frobenius"
lean = ["AlgebraicGeometry.WeilComplex.exists_subsingleton_compactlySupportedCohomology", "AlgebraicGeometry.WeilComplex.exists_subsingleton_cohomology", "AlgebraicGeometry.WeilSheaf.subsingleton_compactlySupportedCohomology_adicConstant", "AlgebraicGeometry.WeilSheaf.finrank_cohomology_zero_adicConstant", "AlgebraicGeometry.WeilSheaf.frobenius_cohomology_zero_adicConstant", "AlgebraicGeometry.WeilComplex.nonempty_equiv_compactlySupportedCohomology_cohomology", "AlgebraicGeometry.WeilSheaf.subsingleton_cohomology_adicConstant_of_isProper", "AlgebraicGeometry.WeilSheaf.exists_linearEquiv_cohomology_zero_adicConstant", "AlgebraicGeometry.WeilSheaf.nonempty_equiv_compactlySupportedCohomology_cohomology"]
order = 3265
tags = ["latex:proposition"]
uses = ["def-weil-finite-field-fiber", "def-weil-geometric-hypotheses", "def-weil-global-geometric-frobenius", "def-weil-ordinary-compact-cohomology", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "def-weil-weil-sheaf-complex", "sk-lem-finite", "sk-prop-sfb-qlbar-colimit-x", "det-lem-coefficient-finite-descent-sections"]
+++
Fix the finite-field datum
$p,a,q,k_0,k$, where $q=p^a$, choose a prime $\ell\neq p$, write
$\Ql=\mathbf Q_\ell$, choose an algebraic closure $\Qlb$ of $\Ql$, and
choose a finite extension $E/\Ql$ contained in $\Qlb$, regarded as a condensed
ring. Let $Y_0$ be a
separated finite-type
$k_0$-scheme, put $Y=Y_0\times_{k_0}k$, and let $(K,\theta)$ be a Weil
complex in the sense of [def-weil-weil-sheaf-complex]: $K\in\Dbc(Y,E)$ and
$\theta:Lg_Y^*K\xrightarrow{\sim}K$ (for an object of $D^b_{c,\mathrm W}(Y,E)$
take $(\operatorname{For}(K),\theta_K)$). Write $E_Y=p_Y^*E$ for the constant
Weil sheaf. Then the
$E$-coefficient abbreviations mean
$H^i(Y,E)=H^i(Y,E_Y)$ and $H_c^i(Y,E)=H_c^i(Y,E_Y)$. The
ordinary and compact-support
cohomology groups $H^i(Y,K)$ and $H_c^i(Y,K)$ are finite-dimensional, vanish outside a
finite interval, and carry the
geometric Frobenius
automorphism. If $Y_0$ is
proper, the
canonical isomorphism

$$
H_c^i(Y,K)\xrightarrow{\sim}H^i(Y,K)
$$

is Frobenius-equivariant.
If $Y$ has dimension $e\in\mathbf Z_{\geq0}$ and $K=E_Y$ is the
constant Weil sheaf, then

$$
H_c^i(Y,E)=0\qquad\text{for }i<0\text{ or }i>2e.
$$

For proper $Y$, the
ordinary cohomology also
satisfies $H^i(Y,E)=0$ for $i<0$ or $i>2e$. In
particular, if $X_0/\Fq$ is smooth,
proper, geometrically connected of pure dimension
$d\in\mathbf Z_{\geq0}$, and $X=X_0\times_{\Fq}k$, then

$$
H^i(X,\Ql)=0\qquad\text{for }i\notin[0,2d].
$$

Moreover, if $Y_0$ is geometrically connected (neither properness nor
smoothness is needed), then $H^0(Y,E)\cong E$, and the
geometric Frobenius acts as the
identity on this group; in particular $H^0(X,\Ql)\cong\Ql$ with
$F=\mathrm{id}$ for every smooth, separated finite-type, geometrically
connected $X_0$.
