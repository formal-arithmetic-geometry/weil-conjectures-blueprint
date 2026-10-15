+++
id = "sk-prop-av-deg-pullback"
kind = "proposition"
title = "Degree of a pullback under a finite morphism"
lean = ["AlgebraicGeometry.Scheme.Hom.degree_pullback"]
order = 544
uses = ["sk-def-av-ample-degree", "sk-def-av-pic"]
tags = ["sketch"]
+++
Let $f:X\to Y$ be a finite surjective morphism of proper varieties of
dimension $g$ over a field $k$, let $\cM$ be an ample invertible
$\cO_Y$-module and let $\deg(f)=[k(X):k(Y)]$ be the degree of $f$.
Then

$$
\deg_{f^*\cM}(X)=\deg(f)\cdot\deg_{\cM}(Y),
$$

the degrees being those of [sk-def-av-ample-degree].
