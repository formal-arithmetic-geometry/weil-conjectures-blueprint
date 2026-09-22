+++
id = "lem-pc-curves-are-sc"
kind = "lemma"
title = "Smooth projective curves are curves in the earlier sense"
order = 4259
lean = ["AlgebraicGeometry.isCurve_of_isSmoothProjectiveCurve"]
uses = ["def-pc-smooth-projective-curve", "def-pc-curve", "def-pc-dimension", "prop-pc-XK-integral"]
+++
Let $k$ be a field and let $X$ be a smooth projective curve
[def-pc-smooth-projective-curve] over $k$. Then $X$ is a *curve over $k$*
in the sense of the curve-calculation chapter: $X$ is nonempty, separated,
of finite type over $k$ and of dimension $\le1$, and smooth over $k$.

## Proof

By [def-pc-smooth-projective-curve] $X$ is a curve [def-pc-curve] over $k$,
hence a variety: integral, with $X\to\operatorname{Spec}(k)$ separated and
of finite type [def-pc-curve]; in particular $X$ is nonempty, separated, of
finite type and, being a curve, of dimension $1$. Its structure morphism is
smooth by hypothesis, and the smooth-curve definition requires exactly:
nonempty, separated scheme of finite type of dimension $\le1$, smooth over
$k$. This proves the claim. (The same applies to base changes $X_K$: see
the base-change lemma of the divisors chapter and
[prop-pc-XK-integral].)

Unresolved dependencies: def:sc-curves, def:weil-pbc-scheme-conventions, lem:sc-base-change-curve
