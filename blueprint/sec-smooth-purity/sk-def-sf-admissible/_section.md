+++
id = "sk-def-sf-admissible"
kind = "definition"
title = "Admissibility datum: an explicit hypothesis"
order = 1845
lean = ["AlgebraicGeometry.ProEtale.HasAmbientExceptionalRightAdjoint", "AlgebraicGeometry.ProEtale.HasUniformCohomologicalDimensionLE"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be separated of finite type with a chosen compactification
$X\xrightarrow{j}\overline X\xrightarrow{p}Y$. Two data of different
strength are distinguished by name.

- **(1)** *The ambient exceptional right adjoint datum.* Say that $f$
*carries the ambient exceptional right adjoint datum at $A$* (for short:
*the ambient datum*) when $\operatorname{FullCD}(p,A;c)$ holds for some
$c$ (that is, the higher direct images of $p$, and of all its base changes
along objects of the pro-étale site of $Y$, vanish in degrees $>c$ on
*every* pro-étale sheaf of $A$-modules). By Brown representability this
bound makes $Rf_{!,n}$ preserve coproducts, so that $Rf_{!,n}$ has a right
adjoint $Rf_n^{\times}$ on the unbounded derived categories of the small
pro-étale sites.
- **(2)–(3)** *The preservation clauses.* Every right adjoint
$Rf_n^{\times}$ of $Rf_{!,n}$ carries $D^b_c(Y,A)$ into $D^b_c(X,A)$ and
each constructible interval $D_c^{[a,b]}(Y,A)$ into
$D_c^{[a+c_f^-,b+c_f^+]}(X,A)$ for some integers $c_f^\pm$ independent of
$a,b$ (2), and carries $\Dctf(Y,A)$ into $\Dctf(X,A)$ (3).

Say that $f$ is *exceptional-adjoint admissible at $A$* (for short:
*carries the admissibility datum*) when (1), (2) and (3) all hold.

The admissibility datum is strictly stronger than the ambient datum (1): it is
(3) that makes the restriction $Rf^{\times}|_{\Dctf}$ of the ambient functor a
functor of the small categories, and when (1)–(3) hold that restriction
coincides, by uniqueness of adjoints, with the constructible exceptional
adjoint $Rf^!$ of [sk-def-sf-operations] (vi). Both data are *assumptions*,
not properties that hold in general.

*Warning: the ambient datum is not satisfied in general.* Its
$\operatorname{FullCD}$ clause quantifies over *every* pro-étale sheaf
of $A$-modules, and this fails for the structure morphism $p$ of an elliptic
curve $E$ over $\overline{\mathbf F}_p$ with $A=\mathbf F_r$, $r\ne p$: there is
a pro-étale $A$-module sheaf (not of étale origin) with nonzero cohomology in
every degree $n\ge1$, $Rp_*$ does not preserve the coproduct of its shifts, and
no right adjoint of $Rp_!=Rp_*$ exists on $D(E_{\Proet},A)$ or on
$D^+(E_{\Proet},A)$ ([sk-rem-sf-fullcd-scope]). Hence neither (1) nor the
admissibility datum may be presupposed for the structure morphism of a
smooth proper variety. For the constructible exceptional adjoint $Rf^!$ of
[sk-def-sf-operations] (vi), by contrast, the analogues of all three clauses
are theorems for every separated finite-type morphism of finite-type
$k$-schemes: the adjunction on $\Dctf$, with compatible units and counits
([sk-prop-sf-existence] (c)), and the two preservation clauses with explicit
constants ([sk-prop-sf-rf-shriek-preservation] (iv),
[sk-thm-sf-ctf-stability] (v)).
