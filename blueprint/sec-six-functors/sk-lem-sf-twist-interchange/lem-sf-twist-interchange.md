+++
id = "lem-sf-twist-interchange"
kind = "lemma"
title = "Internal Hom with an invertible twist"
lean = ["AlgebraicGeometry.Etale.exists_isLocallyConstantSheaf_tateObject", "AlgebraicGeometry.Etale.isIso_derivedHomTensorMap_tateObject", "AlgebraicGeometry.Etale.nonempty_iso_derivedHom_tateObject_shift"]
order = 2520
uses = ["def-coefficient-twists-detailed", "def-sf-datum", "def-weil-derived-pullback-tensor-hom", "lem-sf-hom-finite-projective", "prop-sf-dualizable", "prop-sf-dualizable-hom"]
+++
In the setting of [def-sf-datum], let $K$ be perfect over
$\Lambda_X$, let $M\in D^b_{ctf}(X,\Lambda)$ and $m\in\mathbf Z$. Then
$\Lambda(m)_X$ is invertible locally constant of rank one and the canonical
map
$R\mathcal H om_X(K,M\otimes^L_{\Lambda_X}\Lambda(m)_X)\to R\mathcal H om_X(K,M)\otimes^L_{\Lambda_X}\Lambda(m)_X$ is an
isomorphism; in particular
$R\mathcal H om_X(K,\Lambda_X(m)[n])\cong K^\vee(m)[n]$.
