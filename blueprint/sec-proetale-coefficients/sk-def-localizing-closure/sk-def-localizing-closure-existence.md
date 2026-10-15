+++
id = "det-def-localizing-closure-existence"
kind = "lemma"
title = "The localizing closure exists"
uses = ["det-def-sfb-constructible-tor-amplitude", "sk-prop-sfb-module-category"]
+++
Let $\Lambda$ be a condensed ring, $X$ a scheme and $\mathcal S$ a class of objects of
$D(X_{\mathrm{proét}},\Lambda)$ (for instance $\mathcal S=\Dctf(X,\Lambda)$,
[det-def-sfb-constructible-tor-amplitude]).

1. $D(X_{\mathrm{proét}},\Lambda)$ has arbitrary (small) direct sums, computed termwise on
   complexes, and the direct sum of distinguished triangles is distinguished.
2. The intersection of all full triangulated subcategories of $D(X_{\mathrm{proét}},\Lambda)$
   that contain $\mathcal S$, are closed under isomorphisms, and are closed under arbitrary
   direct sums, is again such a subcategory. It is denoted $\Loc(\mathcal S)$; it is the
   smallest localizing subcategory containing $\mathcal S$.
3. $\Loc(\mathcal S)$ is closed under direct summands, hence thick; and
   $\mathcal S\subseteq\mathcal S'\subseteq\Loc(\mathcal S)$ implies
   $\Loc(\mathcal S')=\Loc(\mathcal S)$.
