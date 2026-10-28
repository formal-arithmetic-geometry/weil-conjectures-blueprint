+++
id = "def-weil-extension-by-zero"
kind = "definition"
title = "Extension by zero"
order = 1124
lean = ["AlgebraicGeometry.ProEtale.openImmersionLowerShriek", "AlgebraicGeometry.ProEtale.mem_essImage_or_isEmpty_costructuredArrow_op_overMap"]
uses = ["def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties"]
+++
Let $\mathcal A$ be a Grothendieck abelian coefficient category, for instance the
modules over a finite commutative ring $A$; this includes the rings $A_{E,n}$ of the
finite-torsion coefficient construction [def-weil-finite-torsion-constructibility]. Let $U$
and $\overline X$ be schemes, let $j:U\hookrightarrow\overline X$ be an open immersion
[def-weil-scheme-morphism-properties] of schemes, and use the small pro-etale
sites [def-weil-pbc-proetale-site]. For an $\mathcal A$-valued sheaf $M$ on
$U_{\mathrm{proet}}$, define extension by zero by sheafifying the presheaf

$$
 P_M(V)=
 \begin{cases}
 M(V\to U),&\text{if }V\to\overline X\text{ factors through }U,\\
 0,&\text{otherwise}.
 \end{cases}
$$

Such a factorization is unique because $j$ is an open immersion. Restriction
is the restriction in $M$ whenever the source factors through $U$, and is the
zero map otherwise. This defines the functor

$$
 j_!: \Sh(U_{\mathrm{proet}},\mathcal A)
 \longrightarrow \Sh(\overline X_{\mathrm{proet}},\mathcal A)
$$

by its action on sections and sheafification. Equivalently, $P_M$ is the left Kan extension of
$M$ along the localization functor $U_{\mathrm{proet}}\to\overline X_{\mathrm{proet}}$, so $j_!$ is
the sheafification of that left Kan extension.
