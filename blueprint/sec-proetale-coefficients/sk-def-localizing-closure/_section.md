+++
id = "sk-def-localizing-closure"
kind = "definition"
title = "The localizing closure"
order = 1281
uses = ["sk-def-sfb-constructible", "sk-prop-integral-criterion"]
lean = ["CategoryTheory.ObjectProperty.localizingClosure", "AlgebraicGeometry.ProEtale.DerivedCategory.localizingConstructibleFiniteTor", "AlgebraicGeometry.ProEtale.CondensedRing.localizingBoundedConstructible"]
tags = ["sketch"]
+++
For admissible $\Lambda$ (that is, $\Lambda\in\{A,\mathbf Z_\ell,\cO_E,\mathbf Q_\ell,E,\Qlb\}$
with $A$ a finite commutative ring killed by a power of $\ell$ and $E/\mathbf Q_\ell$ finite),
let $\Loc(\Dctf(X,\Lambda))$ be the smallest full triangulated subcategory of
$D(X_{\mathrm{proét}},\Lambda)$ containing $\Dctf(X,\Lambda)$ ([sk-def-sfb-constructible])
and closed under arbitrary direct sums. For integral and rational coefficients this is also
$\Loc(\Dbc(X,\Lambda))$, since for $\Lambda=\mathbf Z_\ell,\cO_E,\mathbf Q_\ell,E,\Qlb$ one has
$\Dctf(X,\Lambda)=\Dbc(X,\Lambda)$ ([lem-integral-ctf-equals-bc]).

Brown representability needs a category with arbitrary direct sums, so it is applied to
$\Loc(\Dctf(-,\Lambda))$. It needs two facts: that the objects of $\Dctf(-,\Lambda)$ are
compact generators of $\Loc(\Dctf(-,\Lambda))$ and that proper direct image preserves direct
sums there. For $\cO_E$ the generators are derived complete, but their localizing closure
also contains objects which are not.
