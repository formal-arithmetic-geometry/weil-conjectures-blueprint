+++
id = "lem-pc-coherent-hi"
kind = "lemma"
title = "Coherence and finiteness of higher direct images"
order = 659
uses = ["def-pc-morphism-conventions", "lem-pc-finite-support-hi", "lem-pc-projective-coherent-higher-images"]
lean = ["AlgebraicGeometry.Scheme.Modules.isFinitePresentation_higherDirectImage", "AlgebraicGeometry.Scheme.Modules.finite_sections_higherDirectImage", "AlgebraicGeometry.Scheme.Modules.exists_isZero_higherDirectImage_restrict", "AlgebraicGeometry.Scheme.Modules.exists_isZero_higherDirectImage"]
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

## Proof

The vanishing for sufficiently large $i$, over each affine (or
quasi-compact) open of $S$, follows from the finite
affine-cover bound of [lem-pc-finite-support-hi].
If $f$ is projective, coherence and finite generation are
[lem-pc-projective-coherent-higher-images], applied locally on
the base.
For a general proper $f$ over a locally Noetherian base, coherence of
$R^if_*\mathcal F$ and finiteness of the $H^i(X,\mathcal F)$ over a
Noetherian $A$ are the classical coherence theorem for proper morphisms
(Cohomology of Schemes, Proposition 30.19.1, Tag
[02O5](https://stacks.math.columbia.edu/tag/02O5), and Lemma 30.19.2, Tag
[02O6](https://stacks.math.columbia.edu/tag/02O6)): "Let $S$ be a locally
Noetherian scheme, $f:X\to S$ a proper morphism and $\mathcal F$ a
coherent $\mathcal O_X$-module. Then $R^if_*\mathcal F$ is a coherent
$\mathcal O_S$-module for all $i\geq0$." Its proof reduces to the
projective case above by Chow's lemma (Cohomology of Schemes, Lemma
30.18.1, Tag [0200](https://stacks.math.columbia.edu/tag/0200)) together
with the twisting vanishing and the relative Leray spectral sequence: by
Chow's lemma and Noetherian induction on the support of $\mathcal F$ one
reduces to a coherent module of the form $\pi_*\mathcal G$ for a
projective $\pi:X'\to X$ with $f\circ\pi$ projective, and there the
Leray spectral sequence for $f\circ\pi$ and the projective case conclude.
Over $S=\operatorname{Spec}A$ with $A$ Noetherian,
$H^i(X,\mathcal F)=\Gamma(S,R^if_*\mathcal F)$ is then a finite
$A$-module.
