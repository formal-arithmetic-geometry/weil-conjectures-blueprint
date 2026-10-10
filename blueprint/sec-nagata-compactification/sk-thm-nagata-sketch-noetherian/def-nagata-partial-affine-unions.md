+++
id = "def-nagata-partial-affine-unions"
kind = "definition"
title = "Partial unions of the selected affine cover"
order = 322
lean = ["AlgebraicGeometry.Scheme.partialAffineOpenUnions"]
uses = ["def-nagata-dense-affine-cover"]
+++
Let $U_1,\ldots,U_n$ be a finite family of open subschemes of a scheme $X$
(for instance the selected dense affine cover of
[def-nagata-dense-affine-cover]). For $r\in\mathbb N$, define

$$
X_r=U_1\cup\cdots\cup U_{\min(r,n)},
$$

so that $X_0=\emptyset$ and $X_r=U_1\cup\cdots\cup U_n$ for $r\geq n$
(which is $X$ when the $U_i$ cover $X$).
