+++
id = "lem-sc-second-kummer-divisors"
kind = "lemma"
title = "Second Kummer cohomology of a curve"
order = 1441
lean = ["AlgebraicGeometry.IsCurve.nonempty_addEquiv_sheafH_rootsOfUnitySheaf_two", "AlgebraicGeometry.Scheme.exact_sheafH_rootsOfUnitySheaf_two", "AlgebraicGeometry.Scheme.exists_exact_sheafH_rootsOfUnitySheaf_two", "AlgebraicGeometry.IsCurve.subsingleton_cohomologicalBrauerGroup"]
uses = ["def-br", "def-sc-curves", "def-sc-kummer-sequence", "def-sc-picard-group", "def-weil-pbc-etale-cohomology", "lem-sc-brauer-zero-all-curves", "lem-sc-h1-gm-pic", "lem-sc-kummer-les"]
+++
Let $X$ be a scheme and let $n\geq1$ be invertible on $X$. The Kummer
sequence of [def-sc-kummer-sequence] gives an exact sequence

$$
0\longrightarrow\operatorname{Pic}(X)/n\cdot\operatorname{Pic}(X)\longrightarrow H^2(X_{\Et},\mu_n)
\longrightarrow\operatorname{Br}(X)[n]\longrightarrow0,
$$

where $\operatorname{Pic}(X)=H^1(X_{\Et},\mathbf G_m)$ ([lem-sc-h1-gm-pic]),
$\operatorname{Br}(X)$ is the Brauer group of [def-br], the first map is the
Kummer coboundary and the second is induced by $\mu_n\subseteq\mathbf G_m$.

Now let $C$ be a curve over algebraically closed $k$ in the sense of
[def-sc-curves]. It may be singular, non-reduced, disconnected or
have zero-dimensional components. Let $n>0$ be invertible in $k$.
Then

$$
H^2(C,\mu_n)\simeq\operatorname{Pic}(C)/n,
$$

where $\mu_n$, the Picard group, and cohomology are as in
[def-sc-kummer-sequence], [def-sc-picard-group], [def-weil-pbc-etale-cohomology].
The isomorphism is induced by the coboundary of the Kummer sequence,
$\operatorname{Pic}(C)=H^1(C,\mathbf G_m)\to H^2(C,\mu_n)$
([lem-sc-h1-gm-pic]). In particular $H^2(C_{\Et},\mathbf G_m)=0$
for every such $C$ ([lem-sc-brauer-zero-all-curves]).
