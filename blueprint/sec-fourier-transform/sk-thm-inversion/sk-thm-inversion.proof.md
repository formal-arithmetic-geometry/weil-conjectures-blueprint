+++
kind  = "proof"
of    = "sk-thm-inversion"
+++
Proper base change for $Rp_{2!}$ ([sk-prop-sf-cbc]) gives the compatibility
with base change and the formula for the stalks, and the projection formula
([sk-thm-sf-package]) gives the isomorphism for tensor products with
complexes from $S$. Both are natural in $K$ and respect its Weil structure.

For the inversion formulas, let $r_{ij}$ be the projections of
$V\times_SV^\vee\times_SV$ onto pairs of factors. By base change and
the projection formula, the composite of two transforms is the
transform with the convolution kernel

$$
 Rr_{13!}(r_{12}^*\mathcal K_\psi\otimes
                         r_{23}^*\mathcal K_{\psi^{-1}})[2r].
$$

At a point $(x,z)$, the unshifted integral over the middle factor is
the cohomology of the character sheaf attached to
$y\mapsto\psi\langle x-z,y\rangle$, and hence it vanishes for $x\ne z$
by [sk-lem-wft-character-integral]. Thus the unshifted convolution
is supported on the diagonal, and the localization triangle
([sk-prop-sf-open-closed-triangle]) identifies it canonically with the
direct image of its restriction to the diagonal. There the unit
trivialization of the character sheaf ([sk-lem-as-properties]) and the
trace map for the vector bundle ([sk-prop-an]) identify the restriction with
$E(-r)[-2r]$. The shift $[2r]$ cancels $[-2r]$, which gives the first
inversion formula. If the two kernels use the same character, then
$x-z$ is replaced by $x+z$, the support is the antidiagonal, and we
obtain the second formula. In particular, both inversion maps are
defined by localization and the trace map.

For $K=E$ on a line, the same character integral vanishes away from
zero and equals $E(-1)[-2]$ at zero, so with the shift $[1]$ we obtain
$\delta_0(-1)[-1]$. For $K=\delta_0$, the pullback by the first
projection is supported on $\{0\}\times\mathbf A^1$, where the kernel
is trivial and the second projection is an isomorphism; this gives
$E[1]$. Since the traces and unit trivializations used above are
defined over $k_0$, all these identifications are
Frobenius-equivariant.
