+++
id = "sk-def-sf-admissible"
kind = "section"
title = "Admissibility datum: an explicit hypothesis"
order = 1503
lean = ["AlgebraicGeometry.ProEtale.AmbientExceptionalAdjointData", "AlgebraicGeometry.ProEtale.HasUniformCohomologicalDimensionLE"]
+++
*Definition (sketch).*

Let $f:X\to Y$ be separated of finite type with a chosen compactification
$X\xrightarrow{j}\overline X\xrightarrow{p}Y$. Say that $f$ *carries the
ambient exceptional right adjoint datum at $A$* when
$\operatorname{FullCD}(p,A;c)$ holds for some $c$ (that is, the higher direct
images of $p$, and of all its base changes, vanish above $c$ on *every*
sheaf of $A$-modules) and $Rf_{!,n}$ has a right adjoint $Rf_n^{\times}$ on the
ordinary derived categories of the small pro-étale sites, compatibly with
refinements; the two *preservation* clauses are that $Rf_n^{\times}$
preserves the constructible intervals and the finite-Tor subcategory. This is
the hypothesis def:weil-ambient-exceptional-adjoint and
def:weil-exceptional-adjoint-admissibility of the framework chapter,
restated here for convenience of reading. It is an *assumption*, not a
definition of a property: which morphisms satisfy it is a theorem, and is
prop:sf-rf-shriek-preservation and cor:sf-existence-general below.
