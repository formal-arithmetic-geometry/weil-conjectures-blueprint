+++
kind = "proof"
of = "sk-prop-wgen-relative-line"
uses = ["sk-lem-wgen-triangle-weights"]
+++
We stratify the target so that over each stratum, $G$ is lisse off a
subscheme that is finite over the base. Then
Theorem [sk-p-dl-general-relative-line] and Lemma [sk-l-dl-general-quasifinite]
apply. Take a finite mixed filtration of $G$. In the long exact
sequences of $R^ip_!$ for its steps, the bound $w+i$ passes from the
pure quotients to $G$ by Lemma [sk-lem-wgen-triangle-weights], so we
may assume that $G$ is pure and constructible of weight $v\leq w$. We first
construct the strata over an integral affine target
$Y_0=\operatorname{Spec}R$, so that $\mathbf A^1_{Y_0}$ is integral.
Choose a dense open $U$ on which
$G$ is lisse. Since the locus where $G$ is lisse is stable under
Frobenius, we may replace $U$ by the intersection of its finitely many
Frobenius conjugates, so that $U$ is defined over $k_0$. Then so are
the ideal $I\subset R[T]$ of its reduced complement and the choices
below. If the complement is nonempty, choose a nonzero $g\in I$
and invert its nonzero leading coefficient $b$. The resulting monic
relation shows that $R_b[T]/I$ is finite over $R_b$. If $g$ has degree
zero, the complement is empty over $D(b)$.

Thus over $D(b)$ the complement is finite, while the open $U$ is
smooth of relative dimension one with affine fibres, each of which is
an affine line minus finitely many points. We apply
Theorem [sk-p-dl-general-relative-line] on $U$ and
Lemma [sk-l-dl-general-quasifinite] on the complement, and we obtain the
bound over $D(b)$ from the localization sequence on the source.

For a general target, we may pass to its reduction, since nilpotents
do not change the étale site. We take disjoint integral affine opens
containing the generic points of its components and perform this
construction on each of them. Their union is open, and its complement
has smaller dimension, so that we may argue by induction on this closed
complement.

Finally, by base change and Lemma [sk-lem-wgen-triangle-weights],
applied to the open union and its closed complement in the target, we
obtain the bound over all of $Y_0$.
