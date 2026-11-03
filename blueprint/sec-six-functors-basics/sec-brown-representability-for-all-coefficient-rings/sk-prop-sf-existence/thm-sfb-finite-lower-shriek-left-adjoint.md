+++
id = "thm-sfb-finite-lower-shriek-left-adjoint"
kind = "theorem"
title = "The étale exceptional inverse image $f^\\times$"
lean = ["AlgebraicGeometry.Etale.rightDerivedUpperShriek", "AlgebraicGeometry.Etale.rightDerivedUpperShriekAdjunction", "AlgebraicGeometry.Etale.isLeftAdjoint_rightDerivedLowerShriek"]
order = 2552
uses = ["def-sfb-finite-shriek-adjunction-compactification"]
+++
Let $\Lambda$ be a finite ring and let $f\colon X\to Y$ admit a compactification, with chosen
compactification $c(f)$. Put $f^\times:=Rf^!_{c(f)}\colon D(Y_{\et},\Lambda)\to D(X_{\et},\Lambda)$.
Then the étale derived lower shriek $Rf_!$ on the unbounded derived categories is left
adjoint to $f^\times$.
