+++
kind  = "proof"
of    = "lemma-weil-pbc-torsion-assembly"
+++
If $nF=0$ and $n=rn'$, the prime-factor devissage sequence expresses $F$
through an $\mathbf F_r$-module sheaf and a sheaf killed by $n'$; the long
exact direct-image sequences, the prime-coefficient case
[lemma-weil-pbc-prime-proper-base-change], and the five-lemma transfer induct on the
number of prime factors of $n$. For arbitrary torsion $F$, the filtered union
of its finite-order subsheaves and the exact filtered-colimit theorem for
direct images pass the isomorphism to the colimit; naturality keeps the
comparison equal to the named exchange morphism of
[def-weil-pbc-derived-exchange].

**Status.** The route above reaches the statement for every proper $f$:
neither [lemma-weil-pbc-prime-proper-base-change] nor the reduction
[prop-weil-pbc-reduction-to-projective-line] carries a finite-presentation
hypothesis, since the Chow lemma [lemma-weil-pbc-chow-factorization] used in
the reduction is proved for every proper morphism over an affine base. For the
general proper morphism the classical statement is Etale Cohomology,
Theorem 59.91.11 (Tag [095T](https://stacks.math.columbia.edu/tag/095T)):
"Let $f:X\to Y$ be a proper morphism of schemes. Let $g:Y'\to Y$ be a morphism
of schemes ... Let $\mathcal{F}$ be an abelian torsion sheaf on
$X_{\acute{e}tale}$. Then the base change map $g^{-1}Rf_*\mathcal{F}\to
Rf'_*(g')^{-1}\mathcal{F}$ is an isomorphism." Its proof follows the same
route as the one above: the reduction to $\mathbf P^1_S\to S$ for every
scheme $S$ is Etale Cohomology, Lemma 59.91.10 (Tag
[0A4F](https://stacks.math.columbia.edu/tag/0A4F)), and the strictly henselian
computation is the comparison $\Gamma(X,\mathcal{F})=\Gamma(Z,\mathcal{F}|_Z)$
of Lemma 59.91.1 (Tag [0A0B](https://stacks.math.columbia.edu/tag/0A0B)), which
Stacks derives from Stein factorization (More on Morphisms, Theorem 37.53.5,
Tag [03H2](https://stacks.math.columbia.edu/tag/03H2)) and henselian
idempotent lifting (More on Algebra, Lemma 15.11.8, Tag
[09XK](https://stacks.math.columbia.edu/tag/09XK)). Accordingly the only
inputs of this route that the chapter does not supply are the two Stein
inputs [thm-weil-pbc-stein-inputs]; they are supplied in the literature by
the chain just named, and closing them here means decomposing that chain.
