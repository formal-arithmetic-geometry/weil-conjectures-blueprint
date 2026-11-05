+++
kind = "proof"
of = "theorem-cohomology-curves--5"
order = 360014
uses = ["theorem-cohomology-curves--1", "theorem-cohomology-curves--2", "lemma-removing-finitely-many-points--1", "lemma-reduction-unipotent-local-system", "lemma-normalization-constant-sheaf", "lemma-finite-morphisms-cohomology", "lemma-sheaves-finite-support-finite-morphisms", "proposition-smooth-proper-curves-torsion-prime--1", "proposition-smooth-proper-curves-torsion-prime--2", "proposition-smooth-proper-curves-torsion-prime--3", "proposition-smooth-proper-curves-torsion-prime--5", "proposition-cohomology-smooth-affine-curve--2", "proposition-cohomology-smooth-affine-curve--3", "proposition-cohomology-smooth-affine-curve--4", "proposition-p-torsion-smooth-proper-curve--1", "proposition-p-torsion-smooth-proper-curve--2", "proposition-p-torsion-smooth-proper-curve--3", "proposition-p-torsion-smooth-proper-curve--4", "lemma-p-torsion-affine-curve-characteristic"]
+++
The eight assertions are proved simultaneously for constructible
$\mathbf F_\ell$-sheaves on reduced curves. Choose finitely many disjoint
irreducible opens with dense union on which $F$ is finite locally
constant. The finite-support calculation
[lemma-sheaves-finite-support-finite-morphisms] and
[lemma-removing-finitely-many-points--1] reduce to extension by zero
from these opens. Apply [lemma-reduction-unipotent-local-system], extend
the finite étale cover to a finite morphism of reduced curves, and
commute finite direct image with extension by zero. The filtration and
its retraction reduce the assertions to constant prime-field sheaves
extended by zero. Normalization
[lemma-normalization-constant-sheaf], finite direct image
[lemma-finite-morphisms-cohomology], and the finite-support calculation
reduce these to the smooth constant case. There one uses the Kummer
and Artin–Schreier calculations, together with
[theorem-cohomology-curves--1] and [theorem-cohomology-curves--2].

Take the fifth assertion of this package. For smooth proper constant
coefficients, Kummer gives finiteness when $\ell$ is invertible in $k$,
and Artin–Schreier gives it in characteristic $\ell$
[proposition-p-torsion-smooth-proper-curve--4]. The finite-support terms
are finite, and finiteness passes through the short exact sequences
and the retraction.
