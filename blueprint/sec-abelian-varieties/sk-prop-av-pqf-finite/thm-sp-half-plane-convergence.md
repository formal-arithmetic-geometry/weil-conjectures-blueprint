+++
id = "thm-sp-half-plane-convergence"
kind = "theorem"
title = "Half-plane convergence"
lean = ["CategoryTheory.Functor.truncationCouple_isHalfPlane", "CategoryTheory.Functor.convergesTo_truncationCouple", "CategoryTheory.Functor.truncationCoupleAbutmentIso", "CategoryTheory.ExactCouple.IsHalfPlane", "CategoryTheory.ExactCouple.halfPlaneFiltration", "CategoryTheory.ExactCouple.isFiniteSeparated_halfPlaneFiltration", "CategoryTheory.ExactCouple.halfPlaneConvergenceData", "CategoryTheory.ExactCouple.convergesTo_halfPlaneFiltration", "CategoryTheory.ExactCouple.isRegular_of_isHalfPlane", "CategoryTheory.ExactCouple.isComplete_of_isHalfPlane", "CategoryTheory.ExactCouple.derivedIter_d_eq_zero_of_isHalfPlane", "CategoryTheory.ExactCouple.halfPlaneDerivedIterEIsoGr"]
order = 533
uses = ["def-sp-convergence", "def-sp-exact-couple", "def-sp-filtration"]
+++
Let $(D,E_2,\alpha,f,g)$ be the exact couple of
[def-sp-exact-couple]. Assume $D^{p,q}=0$ for $q<a$, and $E_2^{p,q}=0$ unless
$p\geq0$ and $q\geq a$. Put $A^n=D^{0,n}$. Then total degree $n$ contains
only $a\leq q\leq n$, and each entry $E_r^{p,q}$ has stabilized when

$$
 r>\max(q-a+1,\,p),
$$

with the canonical identification $E_r^{p,q}=E_{r+1}^{p,q}$ supplied by page
cohomology. For $q\leq n$, set
$G_qA^n=\operatorname{im}(D^{n-q,q}\xrightarrow{\alpha^{n-q}}A^n)$, and set
$G_qA^n=A^n$ for $q\geq n$. The decreasing filtration
[def-sp-filtration] $F^pA^n=G_{n-p}A^n$ is finite, exhaustive and separated,
and $E_\infty^{p,q}\cong F^pA^{p+q}/F^{p+1}A^{p+q}$. The couple is regular
and complete in the sense of [def-sp-convergence].
