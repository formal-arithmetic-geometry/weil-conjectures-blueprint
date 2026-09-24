+++
id = "lemma-weil-pbc-etale-cohomology-continuity"
kind = "lemma"
title = "Etale cohomology continuity"
order = 1669
uses = ["lemma-weil-pbc-fibre-product-limit", "lemma-weil-pbc-finite-hypercover-descent"]
+++
Let $(X_i)$ be a cofiltered inverse system of quasi-compact and
quasi-separated schemes with affine transition maps and limit $X_\infty$.
For a torsion sheaf $F_i$ descending to one stage, the natural map

$$
\varinjlim_{j\geq i}H^q(X_j,F_j)\longrightarrow
H^q(X_\infty,F_\infty)
$$

is an isomorphism.

## Proof

We first recall why finite hypercover data compute the required cohomology.
For an etale hypercover $U_\bullet\to Z$, put

$$
C^r(U_\bullet,F)=\Gamma(U_r,F),\qquad
d=\sum_{a=0}^{r+1}(-1)^a\partial_a^*.
$$

Order split hypercovers by common refinement and set
$H^q_{\mathrm{hyp}}(Z,F)= \varinjlim_{U_\bullet}H^q(C^\bullet(U_\bullet,F))$.
The sheaf equalizer gives $H^0_{\mathrm{hyp}}(Z,F)=\Gamma(Z,F)$. A short
exact sequence of sheaves gives connecting maps after refining so that each
of the finitely many local lifts of a cocycle exists. The resulting functors
form a cohomological delta functor. They are effaceable in positive degree:
given a $q$-cocycle, cover its finitely many degree-$q$ components so that
they lift through a chosen monomorphism into an injective sheaf, then fill the
matching objects successively through degree $q+1$; on this refinement the
cocycle is a coboundary. Hence this delta functor is the universal derived
functor of global sections. Therefore

$$
H^q_{\mathrm{hyp}}(Z,F)=H^q_{\mathrm{et}}(Z,F).
$$

The construction also shows that a degree-$q$ class and a witness that it is
zero use only the $(q+1)$-skeleton of one split hypercover.

Let $\alpha\in H^q(X_\infty,F_\infty)$. Represent it by a cocycle
$c\in C^q(U_\bullet,F_\infty)$ on a split hypercover with finite qcqs
$(q+1)$-skeleton. By the preceding lemma, this skeleton descends to some
$X_j$. Each component of $c$ is, by the definition of the inverse-image
sheaf, locally represented by a section at a finite stage. Refine the finite
degree-$q$ cover once and choose one stage dominating all those
representatives. The equation $dc=0$ consists of finitely many equalities on
the degree-$(q+1)$ components; these equalities descend after one further
increase of the stage. We obtain a cocycle $c_j$ and hence a class
$\alpha_j\in H^q(X_j,F_j)$ mapping to $\alpha$. This proves surjectivity.

For injectivity, suppose $\alpha_j\in H^q(X_j,F_j)$ maps to zero on
$X_\infty$. Choose a finite split hypercover and cocycle $c_j$ representing
it. Vanishing on the limit supplies a refinement
$V_\bullet\to U_\bullet\times_{X_j}X_\infty$ and a cochain
$b\in C^{q-1}(V_\bullet,F_\infty)$ with $db=c_j|_V$. Only the
$(q+1)$-skeleton, the refinement maps, the components of $b$, and the finite
list of equations $db=c_j|_V$ are used. Descend that entire list to one
stage $X_k$ by the preceding lemma and the same section argument. It gives a
null-homotopy for the image of $c_j$ on $X_k$, so $\alpha_j$ is zero in the
filtered colimit. The comparison map is therefore injective.

All constructions commute with restriction and with the transition maps,
so the resulting bijection is the canonical map in the statement. This
expands the continuity input of Tag `03Q6`; neither the hypercover nor
the common finite stage is suppressed.
