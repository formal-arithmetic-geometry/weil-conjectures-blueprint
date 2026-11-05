+++
kind = "proof"
of = "proposition-fourier-inversion"
order = 1232
uses = ["definition-ind-etale-pro-etale-weakly", "definition-small-pro-etale-site", "proposition-topos-functoriality", "lemma-artin-schreier-character-sheaf", "lemma-integral-linear-character", "definition-compactification-refinement", "lemma-schematic-closure-uniqueness", "proposition-compactifying-union-two-opens", "lemma-affine-covers-dense-intersection", "proposition-composition-base-change-rf-shriek", "proposition-projection-formula-rational-coefficients", "proposition-extension-zero-restriction-closed-subscheme"]
+++
The composite of two transforms is again an integral
transform, and we compute its kernel. It will turn out to be the
constant sheaf on the diagonal, twisted by $(-r)$, which up to this twist
is the kernel of the identity functor. Let $r_{ij}$ be the projections of
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
by Lemma [lemma-integral-linear-character]. Thus the unshifted convolution
is supported on the diagonal, so the localization triangle identifies
it canonically with the direct image of its restriction to the
diagonal. There the unit trivialization of the character sheaf and
the trace map for the vector bundle identify the restriction with
$E(-r)[-2r]$. Since the shift $[2r]$ cancels $[-2r]$, we obtain the first
inversion formula. If instead the two kernels use the same character, then
$x-z$ is replaced by $x+z$, the support is the antidiagonal, and we
obtain the second formula. Since the traces and unit trivializations
used here are defined over $k_0$, these isomorphisms commute with the
Weil structures.
