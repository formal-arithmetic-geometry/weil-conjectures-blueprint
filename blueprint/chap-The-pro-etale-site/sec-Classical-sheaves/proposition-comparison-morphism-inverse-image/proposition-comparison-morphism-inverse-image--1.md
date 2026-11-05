+++
id = "proposition-comparison-morphism-inverse-image--1"
kind = "proposition"
title = "The comparison morphism and its inverse image (1)"
name_showing = false
order = 112001
aliases = ["bp-r031-1"]
lean = ["AlgebraicGeometry.Scheme.toProEt", "AlgebraicGeometry.Scheme.isContinuous_toProEt", "AlgebraicGeometry.Scheme.preservesFiniteLimits_toProEt", "AlgebraicGeometry.ProEtale.comparisonLowerStar"]
uses = ["definition-small-pro-etale-site"]
+++
Let $X$ be a scheme and $A$ a Grothendieck abelian category. We take
schemes in universe $u$, and morphisms and the Grothendieck abelian
structure on $A$ in universe $u+1$.
The inclusion of étale objects

$$
i_X:X_{\acute{e}t}\longrightarrow X_{\mathrm{pro}\acute{e}t}
$$

is continuous and preserves finite limits. It defines the restriction functor

$$
\nu_{X,*}:\Sh(X_{\mathrm{pro}\acute{e}t},A)
\longrightarrow\Sh(X_{\acute{e}t},A),
\qquad (\nu_{X,*}G)(U)=G(i_XU).
$$
