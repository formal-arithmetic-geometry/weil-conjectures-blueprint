+++
id = "lem-sc-kummer-les"
kind = "lemma"
title = "Consequences of the Kummer sequence"
lean = ["AlgebraicGeometry.Scheme.kummer\u03b4\u2080", "AlgebraicGeometry.Scheme.kummer\u03b4\u2081", "AlgebraicGeometry.IsCurve.sheafH_rootsOfUnitySheaf_of_subsingleton"]
order = 935
uses = ["def-sc-curves", "def-sc-kummer-sequence", "lem-sc-brauer-zero", "lem-sc-h1-gm-pic", "lem-sc-kummer-exact", "lem-sc-primitive-root"]
+++
Let $C$ be a curve over algebraically
closed $k$ (not necessarily connected, reduced or smooth) and let $n$ be prime to $\operatorname{char}k$.
Assume $H^2(C_{\Et},\mathbf G_m)=0$
(for smooth connected $C$ this is [lem-sc-brauer-zero]). Then, under the canonical
identification of [lem-sc-h1-gm-pic], there is a canonical short
exact sequence

$$
0\to\mathcal O_C(C)^\times/\mathcal O_C(C)^\times{}^{\,n}
\to H^1(C_{\Et},\mu_n)\to\operatorname{Pic}(C)[n]\to0,
$$

and

$$
H^2(C_{\Et},\mu_n)=\operatorname{coker}\bigl(n:
\operatorname{Pic}(C)\to\operatorname{Pic}(C)\bigr),
$$

and, if $C$ is connected,
$H^0(C,\mu_n)=\mu_n(k)=\mathbf Z/n\mathbf Z$
([lem-sc-primitive-root]). In particular
$H^1(C_{\Et},\mu_n)=\operatorname{Pic}(C)[n]$ when
$\mathcal O_C(C)^\times$ is $n$-divisible (e.g. when
$C$ is proper and connected, so $\mathcal O_C(C)^\times=k^\times$ if $C$
is moreover reduced).
