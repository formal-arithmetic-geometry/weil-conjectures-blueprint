+++
id = "det-sp-dnc-base-change"
kind = "lemma"
title = "Functoriality and base change of the deformation"
order = 3573
uses = ["det-sp-dnc-definition"]
+++
Let $f\colon X'\to X$ be a morphism of separated finite-type $k$-schemes, let $Z\subset X$ and
$Z'\subset X'$ be closed subschemes with ideals $I$ and $I'$ such that $f^{\cdot}I\subset I'$, and
let $\mathcal D_ZX$, $\mathcal D_{Z'}X'$ be the deformations of [det-sp-dnc-definition].

1. The assignment $a/t\mapsto f^{\cdot}(a)/t$ defines a morphism
   $\widetilde f\colon\mathcal D_{Z'}X'\to\mathcal D_ZX$ over $f\times\mathrm{id}_S$.
1. If $Z'=f^{-1}Z$ schematically, then
   $\mathcal D_{Z'}X'\to X'\times_X\mathcal D_ZX$ is a closed immersion, and it is an isomorphism
   if $f$ is flat. Moreover $\widetilde f_s^{-1}(Z)=Z'$ schematically, where $Z$ and $Z'$ are
   embedded by the zero sections.
1. If $Z'=f^{-1}Z$ schematically, then $\widetilde f$ is proper when $f$ is proper and smooth when
   $f$ is smooth.
