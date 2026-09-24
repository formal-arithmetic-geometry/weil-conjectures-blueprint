+++
id = "lemma-weil-pbc-torsion-assembly"
kind = "lemma"
title = "Torsion coefficient assembly"
order = 1829
uses = ["def-weil-pbc-derived-exchange", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-prime-factor-devissage", "lemma-weil-pbc-chow-factorization", "lemma-weil-pbc-direct-image-filtered-colimit", "lemma-weil-pbc-five-lemma-transfer", "lemma-weil-pbc-prime-factor-induction", "lemma-weil-pbc-prime-proper-base-change", "lemma-weil-pbc-torsion-filtered-union", "prop-weil-pbc-reduction-to-projective-line", "thm-weil-pbc-stein-inputs"]
+++
For every torsion abelian sheaf $F$ and every proper Cartesian square, the
specific map $\operatorname{Ex}_{\square,F}$ is an isomorphism.

## Proof

Write $F=\varinjlim_nF[n]$ and commute both sides of exchange with the
filtered colimit. Induct on the number of prime factors of $n$ through
$0\to F[\ell]\to F[n]\to F[n]/F[\ell]\to0$; the quotient is killed by
$n/\ell$. Prime coefficients are handled by the preceding lemma, and the
five-lemma transfer handles the induction step. Naturality shows at every
stage that the comparison is the S0 exchange map.

## Detailed form

For every proper $f:X\to Y$, every cartesian base change, and every torsion
abelian sheaf $F$ on $X_{\Et}$, the derived exchange morphism
[def-weil-pbc-derived-exchange] is an isomorphism in every cohomological
degree. This is the sheaf-level instance of the bounded-below theorem of this
chapter applied to $K=F[0]$, whose exchange isomorphism has these degreewise
maps as its cohomology-sheaf components; the direct assembly from
[lemma-weil-pbc-prime-proper-base-change] given below is the step used in the proof of
the bounded-below theorem.

## Proof

If $nF=0$ and $n=rn'$, the prime-factor devissage sequence expresses $F$
through an $\mathbf F_r$-module sheaf and a sheaf killed by $n'$; the long
exact direct-image sequences, the prime-coefficient case
[lemma-weil-pbc-prime-proper-base-change], and the five-lemma transfer induct on the
number of prime factors of $n$. For arbitrary torsion $F$, the filtered union
of its finite-order subsheaves and the exact filtered-colimit theorem for
direct images pass the isomorphism to the colimit; naturality keeps the
comparison equal to the named exchange morphism of
[def-weil-pbc-derived-exchange].

**Status.** The statement is made for every proper $f$, while the route above
it reaches it only for $f$ locally of finite presentation —
[lemma-weil-pbc-prime-proper-base-change] carries that hypothesis, and so does the
reduction [prop-weil-pbc-reduction-to-projective-line], whose proof
uses the Chow lemma [lemma-weil-pbc-chow-factorization] in the form proved in this chapter.
For the general proper morphism the classical statement is Etale Cohomology,
Theorem 59.91.11 (Tag [095T](https://stacks.math.columbia.edu/tag/095T)):
"Let $f:X\to Y$ be a proper morphism of schemes. Let $g:Y'\to Y$ be a morphism
of schemes ... Let $\mathcal{F}$ be an abelian torsion sheaf on
$X_{\acute{e}tale}$. Then the base change map $g^{-1}Rf_*\mathcal{F}\to
Rf'_*(g')^{-1}\mathcal{F}$ is an isomorphism." Its proof follows the same
route as the one above, with the same two inputs in their general forms. The
reduction to $\mathbf P^1_S\to S$ for every scheme $S$ is Etale Cohomology,
Lemma 59.91.10 (Tag [0A4F](https://stacks.math.columbia.edu/tag/0A4F)), and
that reduction applies Chow's lemma in the variant of Limits, Lemma 32.12.1
(Tag [0202](https://stacks.math.columbia.edu/tag/0202)), whose hypotheses are
only that $f$ is separated of finite type over a quasi-compact quasi-separated
base; the finite-presentation hypothesis enters in its proof only as an
intermediate device, through the closed immersion of a finite-type scheme into
a finitely presented one (Proposition 32.9.6, Tag
[01ZJ](https://stacks.math.columbia.edu/tag/01ZJ)), Chow's lemma in the
finitely presented case, and base change along that closed immersion — which
is exactly the approximation chain prescribed in the note at
[lemma-weil-pbc-chow-factorization]. The strictly henselian computation is the comparison
$\Gamma(X,\mathcal{F})=\Gamma(Z,\mathcal{F}|_Z)$ of Lemma 59.91.1 (Tag
[0A0B](https://stacks.math.columbia.edu/tag/0A0B)), which Stacks derives from
Stein factorization (More on Morphisms, Theorem 37.53.5, Tag
[03H2](https://stacks.math.columbia.edu/tag/03H2)) and henselian idempotent
lifting (More on Algebra, Lemma 15.11.8, Tag
[09XK](https://stacks.math.columbia.edu/tag/09XK)). Accordingly it is the
finite-presentation form of [lemma-weil-pbc-chow-factorization] and the two Stein inputs that
this chapter does not supply; both are supplied in the literature by the two
chains just named, and closing them here means decomposing those chains.
