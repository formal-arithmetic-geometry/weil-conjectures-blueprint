+++
id = "lem-wf-additive-characters-h1"
kind = "lemma"
title = "Continuous $\\mathbf Z_\\ell$-characters are compatible finite-level classes"
order = 2923
uses = ["def-weil-pbc-etale-cohomology", "def-wf-weil-group", "lem-wf-finite-constant-h1-pi1"]
+++
Let $U_0/k_0$ be geometrically connected and separated of finite type,
put $U=U_0\times_{k_0}\overline{k}_0$, and choose a geometric point
$\bar u\to U$. Put $A_n=\mathbf Z/\ell^n\mathbf Z$. There is a
natural Frobenius-equivariant isomorphism

$$
\operatorname{Hom}_{\mathrm{cont}}(\pi_1(U,\bar u),\mathbf Z_\ell)
\xrightarrow{\sim}
\varprojlim_n H^1_{\mathrm{\acute et}}(U,A_n).
\tag{3.2}
$$

Under the Weil-group action determined by a
degree-one lift $s$, Frobenius on the left is

$$
f\longmapsto\bigl[g\longmapsto f(s^{-1}gs)\bigr].
$$

The cohomology and Weil-group conventions are those of
[def-weil-pbc-etale-cohomology], [def-wf-weil-group].
