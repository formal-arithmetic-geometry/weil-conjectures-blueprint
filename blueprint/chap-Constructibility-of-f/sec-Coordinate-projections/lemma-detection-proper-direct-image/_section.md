+++
id = "lemma-detection-proper-direct-image"
kind = "lemma"
title = "Detection by a proper direct image"
order = 569
lean = ["AlgebraicGeometry.Etale.boundedConstructible_of_upperStar_of_rightDerivedLowerStar", "AlgebraicGeometry.Etale.isIso_of_isIso_upperStar_map_of_isIso_rightDerivedLowerStar_map"]
uses = ["definition-constructible-sheaves"]
+++
Let $b:Y\to S$ be proper, let $j:U\hookrightarrow Y$ be an open
immersion with reduced closed complement $i:Z\hookrightarrow Y$, and
suppose that $bi:Z\to S$ is finite.

1. If $K\in D^+(Y_{\acute{e}t},\Fell)$, $j^*K\in\Dbc(U,\Fell)$, and
   $Rb_*K\in\Dbc(S,\Fell)$, then $K\in\Dbc(Y,\Fell)$.
2. If $\varphi:K\to K'$ is a morphism in $D^+(Y_{\acute{e}t},\Fell)$ such
   that $j^*\varphi$ and
   $Rb_*\varphi$ are isomorphisms, then $\varphi$ is an
   isomorphism.
