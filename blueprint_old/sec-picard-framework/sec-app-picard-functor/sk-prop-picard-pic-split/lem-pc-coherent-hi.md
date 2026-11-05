+++
id = "lem-pc-coherent-hi"
kind = "lemma"
title = "Coherence and finiteness of higher direct images"
order = 642
uses = ["def-pc-morphism-conventions", "lem-pc-finite-support-hi", "lem-pc-projective-coherent-higher-images"]
lean = ["AlgebraicGeometry.Scheme.Modules.isQuasicoherent_higherDirectImage", "AlgebraicGeometry.Scheme.Modules.isFinitePresentation_higherDirectImage", "AlgebraicGeometry.Scheme.Modules.finite_sections_higherDirectImage", "AlgebraicGeometry.Scheme.Modules.exists_isZero_higherDirectImage_restrict", "AlgebraicGeometry.Scheme.Modules.exists_isZero_higherDirectImage"]
+++
Let $f:X\to S$ be a proper morphism with $S$ locally Noetherian and let
$\mathcal{F}$ be a coherent $\mathcal{O}_X$-module. Then $R^if_*\mathcal{F}$ is coherent for all
$i$; locally on $S$ (and globally if $S$ is quasi-compact)
$R^if_*\mathcal{F}=0$ for $i\gg0$ (this vanishing holds more generally for
every quasi-compact separated $f$ and quasi-coherent $\mathcal F$); if $S=\operatorname{Spec}(A)$ with $A$ Noetherian
then the $H^i(X,\mathcal{F})$ are finite $A$-modules. (No bound uniform
over a non-quasi-compact $S$ exists in general: for
$S=\coprod_{n\ge1}\operatorname{Spec}k$, $X=\coprod_n\mathbf P^n_k$ and
$\mathcal F=\mathcal O(-n-1)$ on the $n$-th piece, $R^nf_*\mathcal F\ne0$
for every $n$.)
