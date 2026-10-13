+++
id = "lem-wf-finite-constant-h1-pi1"
kind = "lemma"
title = "Finite constant torsors and the etale fundamental group"
order = 2962
uses = ["cor-galois-abelian-h1", "def-weil-pbc-etale-cohomology", "def-wf-weil-group", "thm-galois-fundamental", "thm-galois-lc-etale", "thm-galois-torsor-h1"]
+++
Let $U_0/k_0$ be geometrically connected and separated of finite type,
put $U=U_0\times_{k_0}\overline{k}_0$, and choose a geometric point
$\bar u\to U$. For a finite abelian group $M$, viewed as a constant
etale sheaf on $U$, there is a natural isomorphism

$$
H^1_{\mathrm{\acute et}}(U,M)
\xrightarrow{\sim}
\operatorname{Hom}_{\mathrm{cont}}(\pi_1(U,\bar u),M).
\tag{3.1}
$$

It is natural for automorphisms of the pointed scheme and for the descent
transport attached to a Weil-group element. More precisely, if a lift
$s\in W(U_0,\bar u)$ acts on $\pi_1(U,\bar u)$ by conjugation, its
pullback action on the right side of (3.1) is

$$
f\longmapsto\bigl[g\longmapsto f(s^{-1}gs)\bigr].
$$

The Weil-group and etale-cohomology conventions are those of
[def-wf-weil-group], [def-weil-pbc-etale-cohomology].
