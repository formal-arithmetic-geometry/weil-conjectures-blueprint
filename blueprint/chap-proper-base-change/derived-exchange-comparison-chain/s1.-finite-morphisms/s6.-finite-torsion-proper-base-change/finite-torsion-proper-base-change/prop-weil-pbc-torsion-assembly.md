+++
id = "prop-weil-pbc-torsion-assembly"
kind = "theorem"
title = "Assembly for arbitrary torsion sheaves"
order = 1629
tags = ["latex:proposition"]
uses = ["def-weil-pbc-derived-exchange-detailed", "def-weil-pbc-etale-sheaves", "def-weil-pbc-scheme-conventions", "lem-weil-pbc-direct-image-filtered-colimit", "lem-weil-pbc-five-lemma-transfer", "lem-weil-pbc-prime-factor-devissage", "lem-weil-pbc-torsion-filtered-union", "prop-weil-pbc-reduction-to-projective-line-detailed", "thm-weil-pbc-chow", "thm-weil-pbc-prime-coefficient", "thm-weil-pbc-stein-inputs"]
+++
For every proper $f:X\to Y$, every cartesian base change, and every torsion
abelian sheaf $F$ on $X_{\Et}$, the derived exchange morphism
[def-weil-pbc-derived-exchange-detailed] is an isomorphism in every cohomological
degree. This is the sheaf-level instance of the bounded-below theorem of this
chapter applied to $K=F[0]$, whose exchange isomorphism has these degreewise
maps as its cohomology-sheaf components; the direct assembly from
[thm-weil-pbc-prime-coefficient] given below is the step used in the proof of
the bounded-below theorem.

## Proof

If $nF=0$ and $n=rn'$, the prime-factor devissage sequence expresses $F$
through an $\mathbf F_r$-module sheaf and a sheaf killed by $n'$; the long
exact direct-image sequences, the prime-coefficient case
[thm-weil-pbc-prime-coefficient], and the five-lemma transfer induct on the
number of prime factors of $n$. For arbitrary torsion $F$, the filtered union
of its finite-order subsheaves and the exact filtered-colimit theorem for
direct images pass the isomorphism to the colimit; naturality keeps the
comparison equal to the named exchange morphism of
[def-weil-pbc-derived-exchange-detailed].

**Status.** The statement is made for every proper $f$, while the route above
it reaches it only for $f$ locally of finite presentation —
[thm-weil-pbc-prime-coefficient] carries that hypothesis, and so does the
reduction [prop-weil-pbc-reduction-to-projective-line-detailed], whose proof
uses the Chow lemma [thm-weil-pbc-chow] in the form proved in this chapter.
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
[thm-weil-pbc-chow]. The strictly henselian computation is the comparison
$\Gamma(X,\mathcal{F})=\Gamma(Z,\mathcal{F}|_Z)$ of Lemma 59.91.1 (Tag
[0A0B](https://stacks.math.columbia.edu/tag/0A0B)), which Stacks derives from
Stein factorization (More on Morphisms, Theorem 37.53.5, Tag
[03H2](https://stacks.math.columbia.edu/tag/03H2)) and henselian idempotent
lifting (More on Algebra, Lemma 15.11.8, Tag
[09XK](https://stacks.math.columbia.edu/tag/09XK)). Accordingly it is the
finite-presentation form of [thm-weil-pbc-chow] and the two Stein inputs that
this chapter does not supply; both are supplied in the literature by the two
chains just named, and closing them here means decomposing those chains.
