+++
id = "def-sfb-finite-upper-shriek-plus"
kind = "definition"
title = "Exceptional pullback on $D^+$"
lean = ["AlgebraicGeometry.ProEtale.rightDerivedUpperShriekPlus"]
order = 2513
uses = ["def-sfb-finite-upper-shriek", "lem-sfb-finite-upper-shriek-bounded-below"]
+++
For $Y$ quasi-compact, the *exceptional pullback on bounded below categories*

$$
Rf^{!,+}\colon D^+(Y_{\mathrm{proét}},\Lambda)\to D^+(X_{\mathrm{proét}},\Lambda)
$$

is the restriction of $Rf^!$ ([def-sfb-finite-upper-shriek]), which preserves bounded below
objects by [lem-sfb-finite-upper-shriek-bounded-below]. By construction
$\iota\circ Rf^{!,+}=Rf^!\circ\iota$ for the inclusions $\iota\colon D^+\subseteq D$.
