+++
id = "det-def-localizing-closure-existence"
kind = "lemma"
title = "The localizing closure exists"
lean = ["AlgebraicGeometry.ProEtale.CondensedRing.hasCoproducts_derivedCategory", "CategoryTheory.ObjectProperty.localizingClosure", "CategoryTheory.ObjectProperty.isLocalizing_localizingClosure", "CategoryTheory.ObjectProperty.le_localizingClosure", "CategoryTheory.ObjectProperty.localizingClosure_le", "CategoryTheory.ObjectProperty.localizingClosure_monotone", "CategoryTheory.ObjectProperty.isIdempotentComplete_localizingClosure"]
order = 1282
uses = ["def-weil-finite-tor-amplitude", "det-prop-sfb-module-category"]
+++
Let $\Lambda$ be a condensed ring, $X$ a scheme and $\mathcal S$ a class of objects of
$D(X_{\mathrm{proét}},\Lambda)$ (for instance $\mathcal S=\Dctf(X,\Lambda)$,
[def-weil-finite-tor-amplitude]).

1. $D(X_{\mathrm{proét}},\Lambda)$ has arbitrary (small) direct sums.
2. The intersection of all full triangulated subcategories of $D(X_{\mathrm{proét}},\Lambda)$
   that contain $\mathcal S$, are closed under isomorphisms, and are closed under arbitrary
   direct sums, is again such a subcategory. It is denoted $\Loc(\mathcal S)$; it is the
   smallest localizing subcategory containing $\mathcal S$.
3. $\Loc(\mathcal S)$ is closed under direct summands, hence thick; and
   $\mathcal S\subseteq\mathcal S'\subseteq\Loc(\mathcal S)$ implies
   $\Loc(\mathcal S')=\Loc(\mathcal S)$.
