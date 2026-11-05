+++
kind = "proof"
of = "proposition-kummer-duality-integral-tate-module--2"
order = 1094005
uses = ["proposition-kummer-duality-integral-tate-module--1", "proposition-kummer-duality-integral-tate-module--3", "proposition-smooth-proper-curves-torsion-prime", "lemma-finite-morphisms-cohomology", "theorem-cohomology-curves"]
+++
For $m=\ell^n$, define

$$
\Psi_n(t)(y)=\operatorname{Tr}\bigl(t\mathbin{\cup}K_m^{-1}(y)\bigr).
$$

Here $K_m$ is the Kummer isomorphism of
[proposition-kummer-duality-integral-tate-module--1]. Lean constructs
cup product with $t$ as the connecting map of the extension of
$\mu_m$ by itself attached to the torsor; the trace is degree modulo
$m$. This is `AlgebraicGeometry.Scheme.EtaleTorsor.picPairing`.

To prove that a zero character forces a section, first count the
continuous characters $G\to\mathbf Z/\ell^j$ using the torsor
description of $H^1$ and the cohomology of a smooth proper curve
([proposition-smooth-proper-curves-torsion-prime]). The count is
$\ell^{2gj}$, where $g$ is the genus. If $t$ has no section, its
monodromy is $\ell^a$ times a surjective character for some $a<n$.
The corresponding torsor has connected total space, and cup product
with it surjects onto $H^2(C,\mu_m)\simeq\mathbf Z/m$.

This surjectivity follows from the long exact sequence of the torsor
extension: the middle term has at most $m$ classes in degree two,
the end term has exactly $m$, and the next cohomology group vanishes.
The bounds use cohomology under finite morphisms
([lemma-finite-morphisms-cohomology]), the calculation of $H^2$ on the
connected covering curve, and [theorem-cohomology-curves].
If $\Psi_n(t)=0$, the trace isomorphism forces $\ell^a$ to annihilate
this surjective cup product, giving $\ell^n\mid\ell^a$, a contradiction.
This is `AlgebraicGeometry.Scheme.EtaleTorsor.exists_section_of_picPairing_eq_zero`.

Isomorphic torsors induce the same connecting map and hence the same
character. Apply [proposition-kummer-duality-integral-tate-module--3]
to obtain the Frobenius identity. For reduction, the equality of
monodromy characters produces a morphism of torsors compatible with
$A_{n+1}\to A_n$. Naturality of the connecting maps, the Kummer
sequences and the degree traces gives
$\Psi_n(t)(\ell y)=\Psi_{n+1}(t')(y)\bmod\ell^n$, as in
`AlgebraicGeometry.Scheme.EtaleTorsor.picPairing_zsmul_of_monodromy`.
