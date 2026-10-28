+++
id = "sk-thm-sf-comp-composition"
kind = "proposition"
title = "Composition and base change for $Rf_!$"
order = 2521
uses = ["sk-def-localizing-closure", "sk-prop-sf-comp-coherence", "sk-def-nagata-sketch-data", "sk-prop-proper-base-change-unbounded"]
lean = ["AlgebraicGeometry.Etale.nonempty_iso_rightDerivedLowerShriek_comp"]
tags = ["sketch"]
+++
For every admissible $\Lambda$, the following statements hold on
$\Loc(\Dctf(-,\Lambda))$ ([sk-def-localizing-closure]) for the functors
$Rf_!$ of [sk-prop-sf-comp-coherence], and restrict to $\Dctf(-,\Lambda)$.

1. For separated morphisms of finite type $X\xrightarrow{f}Y\xrightarrow{g}Z$
   there is a canonical isomorphism $Rg_!\circ Rf_!\simeq R(gf)_!$. These
   isomorphisms are associative and compatible with the identity
   $R(\mathrm{id})_!=\mathrm{id}$.
2. Let $v:Y'\to Y$ be a morphism, $f':X'\to Y'$ the base change of $f$ along
   $v$, and $u:X'\to X$ the projection. The base change map
   $v^*Rf_!\to Rf'_!u^*$ is an isomorphism. For a compactification
   $f=p\circ j$ ([sk-def-nagata-sketch-data]) with base change $f'=p'\circ j'$
   and projection $v':\overline X'\to\overline X$, it is the composite of the
   isomorphism $v'^*j_!\simeq j'_!u^*$ with proper base change for $p$
   ([sk-prop-proper-base-change-unbounded]), and it is compatible with
   composing cartesian squares.
