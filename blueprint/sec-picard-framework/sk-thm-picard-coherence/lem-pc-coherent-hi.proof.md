+++
kind  = "proof"
of    = "lem-pc-coherent-hi"
+++
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
