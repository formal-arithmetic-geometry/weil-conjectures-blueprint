+++
id = "prose-18-07"
kind = "hidden"
title = "Perverse sheaves on a curve"
order = 728
+++
The Plancherel formula says nothing about the transform as a sheaf. To apply Theorem [sk-thm-wrp-l2-dictionary] to the
transform of a pure lisse sheaf $M$, we need to know that the
transform of $(j_*M)[1]$ is again a lisse sheaf on a dense open,
placed in degree $-1$. Although the transform sends the constant sheaf
to a skyscraper (Proposition [sk-thm-inversion]), it preserves
the perverse heart, which on a smooth curve has an elementary
description in terms of ordinary cohomology sheaves and punctual
support.

The shape of this description can be read off from the stalk formula.
The stalk of the transform of $G[1]$ at $y$ is
$R\Gamma_c(\mathbf A^1,G\otimes\mathcal L_{\psi(yx)})[2]$, with
cohomology $H^0_c,H^1_c,H^2_c$ in degrees $-2,-1,0$. For a sheaf
without punctual sections $H^0_c$ vanishes, and $H^2_c$ is nonzero only
at the finitely many $y$ for which $\mathcal L_{\psi(-yx)}$ is a quotient
of $G$. So the transform lives in degrees $-1$ and $0$, with a punctual
sheaf in degree $0$. Once skyscrapers in degree $0$ are allowed in
${}^pD^{\le0}$, orthogonality forces the condition on the other side:
a sheaf in degree $0$ lies in ${}^pD^{\ge1}$ only if it receives no
nonzero map from a skyscraper, that is, only if it has no punctual
subsheaf. The perverse t-structure on a curve is the t-structure built
from these two conditions. The two facts we need are that these classes form a
t-structure with abelian heart (Lemma [sk-lem-wft-curve-heart]) and the
list of simple objects of the heart (Lemma [sk-lem-wft-curve-simples]),
which is what Proposition [sk-p-dl-a1-middle] combines with
exactness.

Recall that a *t-structure* on a triangulated category $D$ is a
pair of full subcategories $D^{\le0}\supset D^{\le-1}$ and
$D^{\ge0}\supset D^{\ge1}$, where $D^{\le n}=D^{\le0}[-n]$ and
$D^{\ge n}=D^{\ge0}[-n]$, such that $\Hom(A,B)=0$ for $A\in D^{\le0}$
and $B\in D^{\ge1}$, and every object sits in a triangle $A\to K\to B\to$ with $A\in D^{\le0}$ and $B\in D^{\ge1}$. Its *heart* is
$D^{\le0}\cap D^{\ge0}$, and for the ordinary t-structure it is the
category of sheaves. We write $D^{[a,b]}=D^{\ge a}\cap D^{\le b}$.
The triangle is unique up to unique isomorphism, and as for the
ordinary t-structure it gives truncation functors and cohomology
objects of $K$ in the heart. A functor is *t-exact* if it
preserves both subcategories.

Let $C$ be a smooth curve over a perfect field. A constructible
sheaf is called punctual if its support is a finite set of closed
points. We define two classes of objects of
$D^b_c(C_{\mathrm{pro}\acute{e}t},\overline{\mathbf Q}_\ell)$ by

$$
\begin{split}
{}^pD^{\le0}&=\{K:\mathcal H^aK=0\ (a>0),\
\mathcal H^0K\text{ is punctual}\},\\
{}^pD^{\ge0}&=\{K:\mathcal H^aK=0\ (a<-1),\
\mathcal H^{-1}K\text{ has no nonzero punctual subsheaf}\}.
\end{split}
$$

By Lemma [sk-lem-wft-curve-heart] below they form a t-structure, the
perverse t-structure. We write ${}^pD^{[a,b]}$ and ${}^p\mathcal H^n$
for its subcategories and cohomology objects, and call the objects of
its heart perverse sheaves on $C$.
For $C=C_0\times_{k_0}k$, a *perverse Weil sheaf* is a
Frobenius-equivariant object in the heart of this geometric t-structure,
with morphisms as in Definition [sk-def-sf-weil-complexes].

On the line, the two basic examples are $E[1]$ and the skyscraper
$\delta_0$, and by Proposition [sk-thm-inversion] the Fourier
transform exchanges them up to a Tate twist. This is the simplest
instance of the exactness proved in
Proposition [sk-p-dl-a1-perverse].
