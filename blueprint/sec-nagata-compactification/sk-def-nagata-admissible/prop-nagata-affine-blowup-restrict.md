+++
id = "prop-nagata-affine-blowup-restrict"
kind = "theorem"
title = "Restriction of an affine blow-up"
order = 188
lean = ["AlgebraicGeometry.AffineBlowup.isPullback_hom_of_isLocalization"]
tags = ["latex:proposition"]
uses = ["def-nagata-affine-blowup", "def-nagata-affine-blowup-restriction-map", "def-nagata-rees-algebra", "def-nagata-rees-piece", "lemma-nagata-rees-degree-zero", "lemma-nagata-rees-localization-degree-zero", "lemma-nagata-rees-piece-mul", "prop-nagata-proj-standard-open", "prop-nagata-rees-graded", "prop-nagata-relative-proj-functoriality"]
+++
Let $s\in A$, let $\varphi\colon A\to B$ be a localization of $A$ away from
$s$, and let $J=IB$. Then the square formed by
$r_\varphi\colon\operatorname{Bl}_J(\operatorname{Spec}B)\to\operatorname{Bl}_I(\operatorname{Spec}A)$
of [def-nagata-affine-blowup-restriction-map], the two structure
morphisms, and $\operatorname{Spec}B\to\operatorname{Spec}A$ is cartesian;
that is, $r_s$ induces an isomorphism
$\operatorname{Bl}_{IA_s}(\operatorname{Spec}A_s)\cong
\operatorname{Bl}_I(\operatorname{Spec}A)\times_{\operatorname{Spec}A}\operatorname{Spec}A_s$
over $\operatorname{Spec}(A_s)$.
