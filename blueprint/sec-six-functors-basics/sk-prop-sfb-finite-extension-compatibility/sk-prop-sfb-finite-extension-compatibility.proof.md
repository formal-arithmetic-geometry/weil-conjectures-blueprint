+++
kind  = "proof"
of    = "sk-prop-sfb-finite-extension-compatibility"
uses = ["sk-prop-sfb-qlbar-colimit-x"]
+++
The coefficient changes and their compatibility are [def-sfb-subfield-coefficient-map],
[def-sfb-subfield-to-qlbar-coefficient-map] and [lem-sfb-subfield-coefficient-map-comp].
Flatness is [lem-sfb-subfield-flat] and [lem-sfb-qlbar-flat]; with it the comparisons of
[sk-def-sfb-coefficient-comparisons] are defined, and (Pull) is an isomorphism by construction.
(Push) for $F/E$ is [lem-sfb-subfield-push-iso], and (Push) for $E\subseteq\Qlb$ and proper $f$
is [lem-sfb-qlbar-push-iso-proper]. In both cases (Shriek) is an isomorphism by
[lem-sfb-derived-lower-shriek-hom-iso]: its proper part $g$ is proper, so (Push) for $g$ is an
isomorphism.

For $E\subseteq\Qlb$ and a non-proper $f$, (Push) need not be an isomorphism: for
$f\colon\coprod_{n\in\mathbf N}Y\to Y$ the fold map, $Rf_*$ is a countable product, and on the
unit objects (Push) compares $\overline{\mathbf Q}_{\ell,Y}\otimes_{E_Y}\prod_nE_Y=\operatorname{colim}_F\prod_nF_Y$
(by [sk-prop-sfb-qlbar-colimit-x], $F$ running over the finite extensions of $E$) with
$\prod_n\overline{\mathbf Q}_{\ell,Y}$; a constant section given by a sequence whose $n$-th term generates an
extension of $E$ of degree $\ge n$ is not in the image, since it is defined over no finite
extension $F$.
