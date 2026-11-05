+++
id = "theorem-trace-isomorphism-top-degree"
kind = "theorem"
title = "The trace isomorphism in top degree"
order = 865
lean = ["AlgebraicGeometry.ProEtale.subsingleton_H_continuousSheaf_of_two_mul_lt", "AlgebraicGeometry.ProEtale.subsingleton_H_continuousSheaf_of_profinite", "AlgebraicGeometry.WeilSheaf.subsingleton_cohomology_adicConstant", "AlgebraicGeometry.WeilSheaf.traceIsomorphism_adicConstant"]
uses = ["definition-small-pro-etale-site", "definition-tate-twists", "definition-trace-map"]
+++
Let $X/k$ be smooth, proper and connected of pure dimension
$d$, with $k$ algebraically closed. For every admissible
coefficient ring,

$$
H^i(X,\Lambda_X)=0\quad(i\notin[0,2d]),\qquad
H^0(X,\Lambda_X)=\Lambda,
$$

and the map

$$
\operatorname{tr}_X:H^{2d}(X,\Lambda_X)
\xrightarrow{\sim}\Lambda(-d),
$$

the twist by $(-d)$ of the map
$\operatorname{tr}_X(d):H^{2d}(X,\Lambda_X(d))\to\Lambda$ induced on
$H^{2d}$ by $\operatorname{Tr}_X$ of Definition [definition-trace-map],
is an isomorphism.
