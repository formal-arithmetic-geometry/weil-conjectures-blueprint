+++
id = "prop-exc-open-adjoint"
kind = "theorem"
title = "The right adjoint for an open immersion"
order = 1853
tags = ["latex:proposition"]
uses = ["def-weil-derived-pullback-tensor-hom", "def-weil-extension-by-zero", "def-weil-finite-torsion-constructibility", "def-weil-pbc-proetale-site", "def-weil-scheme-morphism-properties", "lem-weil-extension-by-zero-adjunction", "lem-weil-extension-by-zero-exact"]
+++
Let $A$ be a finite commutative ring, including the
finite coefficient rings
$A_{E,n}$,
and let $j:U\hookrightarrow X$ be a
open immersion.
On the small pro-etale sites,
extension by zero has the
inverse image as its
right adjoint on the entire ordinary derived categories:

$$
j_!:D(U_{\mathrm{proet}},A)\rightleftarrows
D(X_{\mathrm{proet}},A):j^*.
$$

In particular, the right adjoint is constructed without a constructibility
or finite-Tor hypothesis.
