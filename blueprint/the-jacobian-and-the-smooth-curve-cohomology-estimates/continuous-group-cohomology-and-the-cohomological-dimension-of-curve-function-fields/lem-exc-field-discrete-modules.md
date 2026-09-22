+++
id = "lem-exc-field-discrete-modules"
kind = "lemma"
title = "Étale modules on a field and discrete Galois modules"
order = 4520
lean = ["AlgebraicGeometry.Etale.sheafOverField_equiv_discreteGaloisModule"]
uses = ["def-exc-continuous-cohomology"]
+++
Let $K$ be a field, fix $K^{\rm sep}$, put
$G=\operatorname{Gal}(K^{\rm sep}/K)$, and let $A$ be a finite commutative
ring. The geometric fibre functor identifies étale $A$-module sheaves on
$\operatorname{Spec}K$ with discrete continuous
[def-exc-continuous-cohomology] $A[G]$-modules, as exact abelian categories
with their section functors. Sections correspond to invariants.

## Proof

Finite étale field objects are finite disjoint unions of finite separable
extensions. They form a covering basis for the small étale site. By finite
Galois theory they correspond to finite continuous $G$-sets. For a module
sheaf $F$, its geometric fibre is
$$
M=\varinjlim_{L/K\ \mathrm{finite\ Galois}}F(\operatorname{Spec}L),
\qquad L\subset K^{\rm sep}.
$$
Field automorphisms give a $G$-action. A section defined over $L$ is fixed
by $\operatorname{Gal}(K^{\rm sep}/L)$, so this module is discrete
continuous in the sense of [def-exc-continuous-cohomology].

For a finite separable extension $L/K$, put
$H=\operatorname{Gal}(K^{\rm sep}/L)$. The natural map $F(L)\to M^H$ is
injective: equality in the colimit holds after a finite extension, which is
an étale cover, and the separated sheaf axiom gives equality over $L$. For
surjectivity, represent $m\in M^H$ by a section $s$ over a finite Galois
$E/K$ containing $L$. There are only finitely many cosets of
$\operatorname{Gal}(K^{\rm sep}/E)$ in $H$. For representatives of these
cosets, the equalities $h\cdot m=m$ hold after finitely many further
extensions. Choose a common finite Galois extension $E'/K$. The pullback of
$s$ to $E'$ is invariant under $\operatorname{Gal}(E'/L)$: elements fixing
$E$ already fix a section pulled back from $E$, and the chosen
representatives give the remaining equalities. Galois descent for the cover
$\operatorname{Spec}E'\to\operatorname{Spec}L$, which is the sheaf equalizer
axiom, therefore descends this section to $F(L)$.

Conversely, from a discrete continuous module $M$ assign to a finite étale
object with finite $G$-set $S$ the module $\operatorname{Hom}_G(S,M)$. A
covering is a jointly surjective family of finite $G$-sets; compatible
functions on its members glue uniquely. This defines a module sheaf, and its
geometric fibre is $M$, since each element is fixed by an open subgroup. The
preceding computation of $F(L)$ shows the two constructions are inverse on
all basis objects, including their restriction maps. The fibre functor is
exact; thus this is an exact equivalence. At $L=K$ the formula for sections
is exactly $M^G$. Consequently it also identifies their right derived
section functors, since an exact equivalence takes injective resolutions to
injective resolutions. No finiteness of $M$ is required.

Unresolved dependencies: def:weil-pbc-etale-site, def:weil-pbc-etale-sheaves, thm:galois-fundamental, prop:weil-pbc-geometric-stalks-exact
