+++
kind  = "proof"
of    = "lem-pc-projective-noetherian-rf-perfect"
+++
The projective morphism $f$ is separated, so the finite intersections of
members of $\mathcal U$ are affine. By [lem-pc-rf-base-change-flat-module]
the Cech complex $\check C^\bullet(\mathcal U,\mathcal G)$ is
quasi-isomorphic to its bounded truncation $K$, whose terms are flat over
$A$ (this is also checked directly below).

Each term of the Cech complex is a finite direct sum of flat
$A$-modules. To check this explicitly, write an affine
intersection as $U=\operatorname{Spec}(B)$ and
$\mathcal G|_U=\widetilde M$. For any injection $N'\to N$ of
$A$-modules, let $Q$ be the kernel of
$M\otimes_A N'\to M\otimes_A N$. At a prime $\mathfrak q$ of
$B$, with inverse image $\mathfrak p$ in $A$, the module
$M_{\mathfrak q}$ is flat over $A_{\mathfrak p}$ by relative
flatness. Localizing the displayed map at $\mathfrak q$
therefore gives an injection, so $Q_{\mathfrak q}=0$ for every
$\mathfrak q$. Consequently $Q=0$, proving that $M$ is flat
over $A$.

The cohomology modules $\Gamma(S,R^qf_*\mathcal G)$ of this bounded flat
complex ([lem-pc-cech-resolution]) are finite over $A$ by
[lem-pc-projective-coherent-finiteness].
Applying [lem-pc-noetherian-flat-complex-perfect] gives a
bounded finite projective representative in $D(A)$.
