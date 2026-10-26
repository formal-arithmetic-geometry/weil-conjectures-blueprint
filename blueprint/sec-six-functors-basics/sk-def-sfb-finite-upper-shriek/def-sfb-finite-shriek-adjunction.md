+++
id = "def-sfb-finite-shriek-adjunction"
kind = "theorem"
title = "The adjunction $Rf_!\\dashv Rf^!$ on bounded below objects of étale origin"
lean = ["AlgebraicGeometry.ProEtale.rightDerivedUpperShriekHomEquiv", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekCounit", "AlgebraicGeometry.ProEtale.rightDerivedUpperShriekAdjunction"]
order = 2514
uses = ["def-sfb-finite-derived-lower-shriek", "def-sfb-finite-upper-shriek", "def-weil-pbc-etale-origin-witness", "lem-cbc-proetale-extension-zero-comparison", "lem-sfb-finite-upper-shriek-bounded-below", "thm-sfb-finite-lower-shriek-left-adjoint", "thm-weil-pbc-site-comparison"]
+++
Let $\Lambda$ be a finite ring, let $f\colon X\to Y$ admit a compactification, and let $Y$ be
quasi-compact. For $K\in D(X_{\mathrm{proét}},\Lambda)$ bounded below of étale origin
([def-weil-pbc-etale-origin-witness]) and $L\in D(Y_{\mathrm{proét}},\Lambda)$ bounded below,
there is a bijection

$$
\Hom(Rf_!K,L)\simeq\Hom(K,Rf^!L),
$$

natural in $K$ and $L$, between the pro-étale $Rf_!$ of [def-sfb-finite-derived-lower-shriek]
and $Rf^!$ of [def-sfb-finite-upper-shriek]. Its inverse is $g\mapsto\varepsilon_L\circ Rf_!(g)$
for a counit $\varepsilon_L\colon Rf_!Rf^!L\to L$, natural in $L$. Consequently, for full
subcategories $P$ of the bounded below objects of étale origin on $X$ and $Q$ of the bounded
below objects on $Y$ with $Rf_!P\subseteq Q$ and $Rf^!Q\subseteq P$ (for instance the bounded
constructible objects of finite Tor amplitude), the restrictions of $Rf_!$ and $Rf^!$ are
adjoint.
