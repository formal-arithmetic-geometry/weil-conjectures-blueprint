+++
id = "def-sfb-finite-upper-shriek-plus"
kind = "definition"
title = "Exceptional pullback on $D^+$"
order = 1628
uses = ["def-sfb-finite-upper-shriek", "lem-sfb-finite-upper-shriek-bounded-below"]
lean = ["AlgebraicGeometry.ProEtale.rightDerivedUpperShriekPlus"]
+++
Under the hypothesis of [lem-sfb-finite-upper-shriek-bounded-below], the *exceptional
pullback on bounded below categories*

$$
Rf^{!,+}\colon D^+(Y_{\mathrm{proét}},\mathcal A)\to D^+(X_{\mathrm{proét}},\mathcal A)
$$

is the restriction of $Rf^!$ ([def-sfb-finite-upper-shriek]), which preserves bounded below
objects by [lem-sfb-finite-upper-shriek-bounded-below]. By construction
$\iota\circ Rf^{!,+}=Rf^!\circ\iota$ for the inclusions $\iota\colon D^+\subseteq D$.
