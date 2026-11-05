+++
kind = "proof"
of = "proposition-integral-tate-module--2"
order = 1509006
uses = ["proposition-multiplication-n", "proposition-integral-tate-module--1"]
+++
Since $k$ is algebraically closed, the structure map
$\operatorname{Spec}\bar k\to\operatorname{Spec}k$ is an isomorphism.
Thus $A(k)\simeq A(\bar k)$
(`AlgebraicGeometry.IsAbelianVariety.pointsAddEquivGeometricPoints`).
Surjectivity of multiplication by $\ell$, from
[proposition-multiplication-n], and
[proposition-integral-tate-module--1] show that $A(\bar k)$ is
$\ell$-divisible and that its $\ell$-torsion has $\ell^{2g}$ elements.
These are the two assertions of
`AlgebraicGeometry.IsAbelianVariety.exists_zsmul_eq_and_natCard_torsionBy`.

Apply `AddCommGroup.tateModule.nonempty_linearEquiv_of_natCard_eq`.
It chooses a basis of the $\ell$-torsion and lifts it successively
along multiplication by $\ell$. The lifted elements give compatible
bases at all finite levels. They define $2g$ elements of $T_\ell A$,
and hence a linear map $\mathbf Z_\ell^{2g}\to T_\ell A$.
Reduction modulo every power of $\ell$ proves injectivity. For
surjectivity, write a compatible torsion sequence in these bases;
its integer coefficients agree modulo the successive powers of
$\ell$, so they determine $\ell$-adic integers. This proves that the
linear map is an isomorphism.
