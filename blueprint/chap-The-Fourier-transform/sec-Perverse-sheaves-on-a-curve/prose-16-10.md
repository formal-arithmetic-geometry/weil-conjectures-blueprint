+++
id = "prose-16-10"
kind = "hidden"
title = "Perverse sheaves on a curve (1)"
order = 1236
+++
To apply Theorem [theorem-weights-sums-squared-traces] to the
transform of a pure lisse sheaf $M$, we need to know that the
transform of $(j_*M)[1]$ is again a lisse sheaf on a dense open,
placed in degree $-1$. Although the transform sends the constant sheaf
to a skyscraper (Lemma [lemma-fourier-transform-constant-sheaf]), it preserves
the perverse heart, which on a smooth curve has an elementary
description in terms of ordinary cohomology sheaves and punctual
support.

We can read off the shape of this description from the stalk formula.
The stalk of the transform of $G[1]$ at $y$ is
$R\Gamma_c(\mathbf A^1,G\otimes\mathcal L_{\psi(yx)})[2]$. For a sheaf $G$
without punctual sections $H^0_c$ vanishes, and the proof of
Proposition [proposition-fourier-transform-perverse-heart] below shows
that $H^2_c$ is nonzero only at finitely many $y$. So the transform lives in
degrees $-1$ and $0$, with a punctual sheaf in
degree $0$. This suggests allowing skyscrapers in
degree $0$ in ${}^pD^{\le0}$. Orthogonality then forces the condition on
the other side. A sheaf in degree $0$ lies in ${}^pD^{\ge1}$ only if it
receives no nonzero map from a skyscraper, that is, only if it has no
punctual subsheaf. The perverse t-structure on a curve is the
t-structure built from these two conditions.

What we finally use about it is the list of its simple objects
(Lemma [lemma-simple-objects]). By this list, an exact equivalence
must send an irreducible middle extension to an irreducible middle
extension or to an irreducible punctual sheaf.

Recall that a *t-structure* on a triangulated category $D$ is a
pair of full subcategories $D^{\le0}\supset D^{\le-1}$ and
$D^{\ge0}\supset D^{\ge1}$, where $D^{\le n}=D^{\le0}[-n]$ and
$D^{\ge n}=D^{\ge0}[-n]$, such that $\Hom(A,B)=0$ for $A\in D^{\le0}$
and $B\in D^{\ge1}$, and every object sits in a triangle $A\to K\to
B\to$ with $A\in D^{\le0}$ and $B\in D^{\ge1}$. Its *heart* is
$D^{\le0}\cap D^{\ge0}$. For the ordinary t-structure the heart is the
category of sheaves. We write $D^{[a,b]}=D^{\ge a}\cap D^{\le b}$.
The triangle is unique up to unique isomorphism. As for the
ordinary t-structure, it gives truncation functors and cohomology
objects of $K$ in the heart. A functor is *t-exact* if it
preserves both subcategories.

Let $C$ be a smooth curve over a perfect field. The perverse
t-structure is built from punctual sheaves.
