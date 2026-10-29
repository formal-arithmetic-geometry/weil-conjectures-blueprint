+++
id = "prose-18-06"
kind = "hidden"
title = "Why the perverse heart, and t-structures recalled"
order = 4188
+++
The Plancherel formula says nothing about the transform as a sheaf. To apply Theorem [sk-thm-wrp-l2-dictionary] to the
transform of a pure lisse sheaf $M$, we need to know that the
transform of $(j_*M)[1]$ is again a lisse sheaf on a dense open,
placed in degree $-1$. Although the transform sends the constant sheaf
to a skyscraper (Proposition [sk-thm-inversion]), it preserves
the perverse heart, which on a smooth curve has an elementary
description in terms of ordinary cohomology sheaves and punctual
support.

Recall that a *t-structure* on a triangulated category $D$ is a
pair of full subcategories $D^{\le0}\supset D^{\le-1}$ and
$D^{\ge0}\supset D^{\ge1}$, where $D^{\le n}=D^{\le0}[-n]$ and
$D^{\ge n}=D^{\ge0}[-n]$, such that $\Hom(A,B)=0$ for $A\in D^{\le0}$
and $B\in D^{\ge1}$, and every object sits in a triangle $A\to K\to
B\to$ with $A\in D^{\le0}$ and $B\in D^{\ge1}$. Its *heart* is
$D^{\le0}\cap D^{\ge0}$, and for the ordinary t-structure it is the
category of sheaves. We write $D^{[a,b]}=D^{\ge a}\cap D^{\le b}$.
The triangle is unique up to unique isomorphism, and as for the
ordinary t-structure it gives truncation functors and cohomology
objects of $K$ in the heart. A functor is *t-exact* if it
preserves both subcategories.

On the line, the two basic examples are $E[1]$ and the skyscraper
$\delta_0$, and by Proposition [sk-thm-inversion] the Fourier
transform exchanges them up to a Tate twist. This is the simplest
instance of the exactness proved in
Proposition [sk-p-dl-a1-perverse].
