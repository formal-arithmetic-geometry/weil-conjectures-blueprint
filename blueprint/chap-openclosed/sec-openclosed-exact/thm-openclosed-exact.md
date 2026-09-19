+++
id = "thm-openclosed-exact"
kind = "theorem"
title = "The open–closed exact sequence"
order = 986
lean = ["AlgebraicGeometry.Etale.openClosedShortComplexFunctor", "AlgebraicGeometry.Etale.shortExact_openClosedShortComplex", "AlgebraicGeometry.Etale.shortExact_openClosedShortComplex_moduleCat"]
uses = ["lemma-openclosed-vanishing-lowershriek", "lemma-openclosed-vanishing-lowerstar", "prop-openclosed-conservative", "prop-openclosed-lowerstar-fully-faithful"]
+++
Let $(j,i)$ be a complementary pair on $X$ and let
$\mathcal F\in\shv{\et X}$. Then

$$
0\longrightarrow j_!j^*\mathcal F
\xrightarrow{\ \alpha_{\mathcal F}\ }\mathcal F
\xrightarrow{\ \beta_{\mathcal F}\ }i_*i^*\mathcal F\longrightarrow0
$$

is a short exact sequence in $\shv{\et X}$, naturally in $\mathcal F$: the
two maps are the components of natural transformations, so the sequence is a
short complex of endofunctors $j_!j^*\Rightarrow\mathrm{id}\Rightarrow i_*i^*$
of $\shv{\et X}$ whose evaluation at $\mathcal F$ is the displayed one, and it
is short exact at every $\mathcal F$.

## Proof

*It is a complex.* By the adjunction $j_!\dashv j^*$ and
[lemma-openclosed-vanishing-lowerstar],

$$
\Hom(j_!j^*\mathcal F,i_*i^*\mathcal F)
\cong\Hom(j^*\mathcal F,j^*i_*i^*\mathcal F)=0,
$$

so $\beta_{\mathcal F}\circ\alpha_{\mathcal F}=0$ with no computation.

*After $j^*$.* The functor $j^*$ is exact. Applying it to the complex
and using that the unit $\mathrm{id}\to j^*j_!$ is an isomorphism and that
$j^*i_*=0$ by [lemma-openclosed-vanishing-lowerstar], the complex becomes

$$
0\to j^*\mathcal F\to j^*\mathcal F\to0\to0,
$$

in which the first map is the identity by the triangle identity for
$j_!\dashv j^*$. This is short exact.

*After $i^*$.* The functor $i^*$ is exact. Applying it and using
$i^*j_!=0$ from [lemma-openclosed-vanishing-lowershriek] and the counit
isomorphism $i^*i_*\cong\mathrm{id}$ from
[prop-openclosed-lowerstar-fully-faithful], the complex becomes

$$
0\to0\to i^*\mathcal F\to i^*\mathcal F\to0,
$$

in which the second map is the identity, again by a triangle identity. This
is short exact.

*Descent of exactness.* Let $M$ be any of the three homology objects of
the complex. Since $j^*$ and $i^*$ are exact they commute with homology, so
$j^*M=0$ and $i^*M=0$ by the two previous paragraphs. The map $0\to M$ is
therefore an isomorphism after $j^*$ and after $i^*$, hence an isomorphism by
[prop-openclosed-conservative], that is, $M=0$. All three homology
objects vanish, so $\alpha_{\mathcal F}$ is a monomorphism,
$\beta_{\mathcal F}$ is an epimorphism, and $\alpha_{\mathcal F}$ is a kernel
of $\beta_{\mathcal F}$.

*Naturality in $\mathcal F$.* Nothing is to be proved: $\alpha$ and
$\beta$ are a counit and a unit, hence natural transformations, so the short
complex exists already at the level of endofunctors of $\shv{\et X}$ and the
complex above is its evaluation at $\mathcal F$.
