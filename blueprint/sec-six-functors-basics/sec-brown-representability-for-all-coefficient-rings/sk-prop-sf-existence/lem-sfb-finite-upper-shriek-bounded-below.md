+++
id = "lem-sfb-finite-upper-shriek-bounded-below"
kind = "lemma"
title = "$Rf^!$ preserves bounded below objects"
lean = ["AlgebraicGeometry.ProEtale.plus_rightDerivedUpperShriek_obj", "AlgebraicGeometry.ProEtale.plusEtaleOrigin_rightDerivedUpperShriek_obj", "AlgebraicGeometry.Etale.plus_rightDerivedUpperShriek_obj"]
order = 2554
uses = ["def-sfb-finite-upper-shriek", "def-weil-pbc-etale-origin-witness", "det-def-sfb-derived-categories", "thm-sfb-finite-lower-shriek-left-adjoint"]
+++
Let $\Lambda$ be a finite ring, let $f\colon X\to Y$ admit a compactification, and let $Y$ be
quasi-compact. If $L\in D(Y_{\mathrm{proét}},\Lambda)$ is bounded below, then $Rf^!L$
([def-sfb-finite-upper-shriek]) is bounded below and of étale origin
([def-weil-pbc-etale-origin-witness]). The étale $f^\times$ of
[thm-sfb-finite-lower-shriek-left-adjoint] preserves bounded below objects as well.
