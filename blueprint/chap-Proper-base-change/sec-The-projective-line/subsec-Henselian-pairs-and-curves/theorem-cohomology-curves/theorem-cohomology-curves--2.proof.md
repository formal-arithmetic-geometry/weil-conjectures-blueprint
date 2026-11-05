+++
kind = "proof"
of = "theorem-cohomology-curves--2"
order = 360011
uses = ["theorem-cohomology-curves--1", "lemma-sheaves-finite-support-finite-morphisms", "lemma-finite-morphisms-cohomology"]
+++
For $q\geq3$, apply [theorem-cohomology-curves--1]. To treat $q=2$,
pass to the reduced irreducible components and normalize their
one-dimensional parts. The resulting finite maps are universal
homeomorphisms away from finitely many closed points. The unit map to
the finite sum of their direct images consequently induces an
isomorphism on $H^2$, by
[lemma-sheaves-finite-support-finite-morphisms] and
[lemma-finite-morphisms-cohomology]. Zero-dimensional components have
no positive-degree cohomology; the remaining components are smooth
affine connected curves.

On such a curve the unit $F\to\eta_*\eta^*F$ induces an isomorphism
on $H^2$. The affine generic-point calculation gives
$H^2(C,\eta_*\eta^*F)=0$, first for finite torsion coefficients split by
a finite extension of the function field and then for arbitrary
torsion coefficients by dévissage and filtered colimits.
