+++
id = "lem-sf-twist-interchange"
kind = "lemma"
title = "Internal Hom with an invertible twist"
order = 2293
uses = ["def-coefficient-twists-detailed", "def-sf-datum", "def-weil-derived-pullback-tensor-hom", "lem-sf-hom-finite-projective", "prop-sf-dualizable", "prop-sf-dualizable-hom"]
+++
In the setting of [def-sf-datum], let $K$ be perfect over
$\Lambda_X$, let $M\in D^b_{ctf}(X,\Lambda)$ and $m\in\mathbf Z$. Then
$\Lambda(m)_X$ is invertible locally constant of rank one and the canonical
map
$R\mathcal H om_X(K,M\otimes^L_{\Lambda_X}\Lambda(m)_X)\to R\mathcal H om_X(K,M)\otimes^L_{\Lambda_X}\Lambda(m)_X$ is an
isomorphism; in particular
$R\mathcal H om_X(K,\Lambda_X(m)[n])\cong K^\vee(m)[n]$.

## Proof

By [def-coefficient-twists-detailed] each $\Lambda(m)_X$ is invertible locally
constant of rank one with
$\Lambda(m)_X\otimes^L\Lambda(-m)_X\cong\Lambda_X$, so
$T_m=-\otimes^L\Lambda(m)_X$ is an exact autoequivalence; an exact
equivalence commutes with the derived internal Hom, and both sides of the
asserted map are exact functors of $M$ agreeing on the generator
$M=\Lambda_X$. For $K$ perfect the asserted map is the identification of
[prop-sf-dualizable-hom] twisted by the invertible local system
$\Lambda(m)_X$, and one computes it locally with a bounded complex
of finite projective modules, where the identification is termwise by
[lem-sf-hom-finite-projective] with compatible differentials and
independent of the chosen resolutions; the coefficient dual and the derived
internal Hom are those of [prop-sf-dualizable] and
[def-weil-derived-pullback-tensor-hom]. The last display is the case
$M=\Lambda_X$ together with the shift of the second variable.
