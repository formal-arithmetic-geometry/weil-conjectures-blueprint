+++
id = "lem-sf-projection-flat-factor-counterexample"
kind = "lemma"
title = "The projection formula fails for a flat factor that is not finitely generated"
order = 2294
uses = ["def-exchange-projection", "def-weil-derived-tensor"]
+++
There are a morphism of ringed spaces $f:X\to Y$, a flat
$\mathcal O_Y$-module $K$ and a complex $E\in D(\mathcal O_X)$ such that
the projection map of the Stacks Project, Cohomology,
Equation 20.54.2.1,
[Tag 0B53](https://stacks.math.columbia.edu/tag/0B53),

$$
Rf_*E\otimes^\mathbf L_{\mathcal O_Y}K
\longrightarrow Rf_*\bigl(E\otimes^\mathbf L_{\mathcal O_X}Lf^*K\bigr),
$$

is *not* an isomorphism, so that finite Tor dimension of the tensor
factor – here flatness, of amplitude $[0,0]$ in the sense of
[def-weil-derived-tensor] – does not suffice for the projection formula
of [def-exchange-projection]. Explicitly: $Y=\operatorname{Spec} \mathbf Z$, $X=\bigsqcup_{n\geq1}\operatorname{Spec}\mathbf Z$ the
infinite disjoint union of copies of $Y$, $f$ the fold map,
$K=\mathbf Q$, and $E=\mathcal O_X$. The projection map is then

$$
\Bigl(\prod_{n\geq1}\mathbf Z\Bigr)\otimes_{\mathbf Z}\mathbf Q
\longrightarrow\prod_{n\geq1}\mathbf Q,
\qquad (a_n)_{n\geq1}\otimes q\longmapsto(a_nq)_{n\geq1},
$$

which is injective but not surjective.

## Proof

For the infinite disjoint union $X=\bigsqcup_{n\geq1}\operatorname{Spec} \mathbf Z$ the direct image is the product,
$f_*\mathcal O_X=\prod_{n\geq1}\mathbf Z$, and $f_*$ is exact, so
$Rf_*E=f_*E$ and the left-hand side is
$(\prod_{n\geq1}\mathbf Z)\otimes_{\mathbf Z}\mathbf Q$. The pullback of
the constant sheaf $\mathbf Q$ is the constant sheaf $\mathbf Q$ on
$X$, whose sections over the $n$-th component are $\mathbf Q$; since
$\mathbf Q$ is flat over $\mathbf Z$ the derived tensor products are
computed by the ordinary ones, so the right-hand side is
$\prod_{n\geq1}\mathbf Q$ and the projection map is the displayed one, as
in [def-exchange-projection] and [def-weil-derived-tensor].
Every element of the tensor product
$(\prod_{n\geq1}\mathbf Z)\otimes_{\mathbf Z}\mathbf Q$ is a finite sum
$\sum_{i=1}^r(a^{(i)}_n)_{n}\otimes q_i$; writing $N$ for a common
denominator of $q_1,\dots,q_r$, its image is a sequence $(b_n)_n$ with
$b_n\in\frac1N\mathbf Z$ for every $n$. The sequence
$(1/n)_{n\geq1}$ is not of this form, because $1/n\notin\frac1N\mathbf Z$
for $n>N$. Hence the projection map is not surjective, and in particular
not an isomorphism, although $K=\mathbf Q$ is flat over $\mathbf Z$, that
is, of Tor amplitude $[0,0]$.
