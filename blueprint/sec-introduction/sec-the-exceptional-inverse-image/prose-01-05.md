+++
id = "prose-01-05"
kind = "hidden"
title = "The exceptional inverse image"
order = 11
+++
Of the six operations, $f^!$ is the one whose construction needs an idea,
and it is shaped by Poincaré duality. Let $X$ be smooth of pure dimension $d$ over an
algebraically closed field $k$, let $a:X\to\operatorname{Spec}k$ be its
structure map, and let $\Lambda$ be a coefficient ring such as
$\mathbf Z/\ell^n$ with $\ell$ invertible in $k$. We want perfect pairings

$$
H_c^i(X,\Lambda)\times H^{2d-i}(X,\Lambda(d))\longrightarrow\Lambda
$$

between cohomology with compact supports and cohomology with
coefficients in the Tate twist $\Lambda(d)$
(Definition [sk-def-sp-tate-twist]); for $\Lambda=\mathbf Z/\ell^n$ this
is the sheaf $\mu_{\ell^n}^{\otimes d}$.
For a manifold one proves duality by working locally and gluing, and in
algebraic geometry the device that makes this possible is a right
adjoint $a^!$ of the direct image with compact supports $Ra_!$, the
functor whose cohomology groups are the $H^i_c$. This right adjoint is
called the *exceptional inverse image*. Once
$a^!$ exists, duality says two things: that $\cHom(-,a^!\Lambda)$ is a
perfect duality on constructible complexes (Verdier duality), and that
$a^!\Lambda\simeq\Lambda_X(d)[2d]$, where $\Lambda_X$ is the constant
sheaf (smooth purity). The pairing is
evaluation followed by the counit $Ra_!a^!\Lambda\to\Lambda$, and the
twist $(d)$, the shift $[2d]$ and the trace all come from the
isomorphism of smooth purity. The same right adjoint, for a general morphism $f$, is
what makes the trace formula local: the local term at a fixed point is
computed from $f^!$.

So the main theorem of Part “The six operations” is that $f^!$ exists and has the
expected finiteness (Theorem [sk-thm-existence]). Existence is a general
fact about triangulated categories: Brown representability produces a
right adjoint of any triangulated functor out of a compactly generated
triangulated category that preserves direct sums, and the problem
is to put $Rf_!$ in a setting where this applies. Finiteness, that
$f^!$ carries constructible complexes to constructible complexes, is a
geometric statement; it reduces to an explicit computation for the
projective line and to Deligne's theorem that direct images along open
immersions preserve constructibility.
