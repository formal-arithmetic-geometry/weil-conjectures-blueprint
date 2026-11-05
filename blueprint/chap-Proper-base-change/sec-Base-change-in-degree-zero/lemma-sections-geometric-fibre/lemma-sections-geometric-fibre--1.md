+++
id = "lemma-sections-geometric-fibre--1"
kind = "lemma"
title = "Sections over the strict localization and the geometric fibre"
name_showing = false
order = 332001
aliases = ["bp-r100-1"]
lean = ["AlgebraicGeometry.Etale.strictLocalizationPullback_sections", "AlgebraicGeometry.Etale.bijective_restrictAlong_fibreToStrictLocalization"]
+++
Let $f:X\to Y$ be proper, let $F$ be an étale sheaf of abelian groups on
$X$, and let $\bar y:\operatorname{Spec}\Omega\to Y$ be a geometric point
with $\Omega$ separably closed. Put

$$
S=Y_{(\bar y)}=\operatorname{Spec}\mathcal O^{\mathrm{sh}}_{Y,\bar y},
\qquad T=X\times_Y S.
$$

1. Every section of $F|_T$ is the pullback of a section of $F$ over
   $X\times_Y V$ for some pointed affine étale neighbourhood $(V,v)$ of
   $\bar y$. If a section over $X\times_Y V$ pulls back to zero on $T$,
   then it already restricts to zero over $X\times_Y V'$ for some pointed
   affine étale refinement $(V',v')\to(V,v)$.
2. If $\Omega$ is algebraically closed, the factorization
   $\operatorname{Spec}\Omega\to S\to Y$ induces a map $X_{\bar y}\to T$
   along which restriction is a bijection

$$
\Gamma(T,F|_T)\xrightarrow{\sim}
\Gamma(X_{\bar y},F|_{X_{\bar y}}).
$$
