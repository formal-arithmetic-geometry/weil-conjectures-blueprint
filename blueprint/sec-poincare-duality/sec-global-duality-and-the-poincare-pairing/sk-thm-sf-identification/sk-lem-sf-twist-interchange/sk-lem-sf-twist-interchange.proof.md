+++
kind  = "proof"
of    = "sk-lem-sf-twist-interchange"
+++
Write $\otimes$ for $\otimes^L_{\Lambda_X}$. The canonical map
$c_{M,N}:\RHom_X(K,M)\otimes N\to\RHom_X(K,M\otimes N)$ is the adjoint of
$\mathrm{ev}\otimes1_N:\RHom_X(K,M)\otimes N\otimes K\to M\otimes N$ (up to the
symmetry); the map of the statement is its inverse, once $c_{M,T}$ is shown
to be invertible. Let $T^{-1}$ be an inverse of $T$, with
$T\otimes T^{-1}\cong\Lambda_X$, so that $-\otimes T$ is an autoequivalence
with quasi-inverse $-\otimes T^{-1}$, in particular left and right adjoint to
it. For every $N$ the adjunctions give natural bijections

$$
\operatorname{Hom}\bigl(N,\RHom_X(K,M)\otimes T\bigr)
\cong\operatorname{Hom}\bigl(N\otimes T^{-1}\otimes K,M\bigr)
\cong\operatorname{Hom}\bigl(N\otimes K,M\otimes T\bigr)
\cong\operatorname{Hom}\bigl(N,\RHom_X(K,M\otimes T)\bigr),
$$

and following $1_{\RHom_X(K,M)\otimes T}$ through them (Yoneda) shows that the
resulting isomorphism $\RHom_X(K,M)\otimes T\cong\RHom_X(K,M\otimes T)$ is
the adjoint of $\mathrm{ev}\otimes1_T$, i.e. $c_{M,T}$. This argument uses
neither a generator ($\Lambda_X$ does not generate $\Dctf$, and
[sk-lem-sf-determination] propagates invertibility only) nor any property of
$K$. For $K$ dualizable it is also the composite
$\RHom_X(K,M\otimes T)\cong K^\vee\otimes M\otimes T\cong\RHom_X(K,M)\otimes T$
of two instances of the identification of [sk-prop-sf-dualizable-biduality].
For the last assertion,
by def:coefficient-twists each $\Lambda(m)_X$ is invertible, locally
constant of rank one, with $\Lambda(m)\otimes\Lambda(-m)\cong\Lambda_X$, so
$T=\Lambda(m)_X[n]$ is invertible; take $M=\Lambda_X$.
