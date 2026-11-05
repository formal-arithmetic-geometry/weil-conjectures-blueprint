+++
id = "lemma-class-of-point--1"
kind = "lemma"
title = "The class of a point (1)"
name_showing = false
order = 868001
aliases = ["bp-r261-1"]
lean = []
uses = ["definition-relative-dualizing-complex", "definition-trace-map"]
+++
This normalization of the class of a closed point is bypassed by the
mainline Lean proof.

In the setting of Theorem [theorem-trace-isomorphism-top-degree], we
have $\operatorname{tr}_X(d)([x])=1$ for every closed point $x$ of $X$.

The mainline has no declaration of this normalization. Its top-degree
argument uses
`AlgebraicGeometry.WeilSheaf.traceIsomorphism_adicConstant`: for
$X_0/\Fq$ smooth, separated, of finite type and geometrically connected
of pure dimension $d$, and $\ell\ne\operatorname{char}\Fq$, there exists
a $\Qbarl$-linear isomorphism

$$
H_c^{2d}(X_0\otimes_{\Fq}\Fbar,\Qbarl(d))\xrightarrow{\sim}\Qbarl
$$

which is invariant under geometric Frobenius. The declaration does not
identify this isomorphism with the trace of Definition
[definition-trace-map], or give its value on a closed-point class.
