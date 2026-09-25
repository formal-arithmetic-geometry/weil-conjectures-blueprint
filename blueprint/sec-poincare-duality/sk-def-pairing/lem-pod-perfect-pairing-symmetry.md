+++
id = "lem-pod-perfect-pairing-symmetry"
kind = "lemma"
title = "Symmetry of perfect pairings"
order = 2589
uses = ["def-pod-perfect-derived-pairing", "def-pod-perfect-point-complex", "lem-pod-perfect-point-double-dual"]
+++
In the Poincare duality conventions of this chapter, let
$\Lambda\in\{A,\mathcal O_E,E,\Qlb\}$ and let $C,D$ be
perfect point complexes over
$\Lambda$. A morphism
$b:C\otimes^L_\Lambda D\to\Lambda$ is
perfect if and only if its
tensor–internal-Hom adjoint in the first variable,
$C\to D^\vee$, is an isomorphism.

## Proof

Let $b^\sharp:D\to C^\vee$ be the adjoint appearing in
[def-pod-perfect-derived-pairing], and let
${}^\sharp b:C\to D^\vee$ be the adjoint in the first variable. The
two are exchanged by the symmetry isomorphism
$C\otimes^L_\Lambda D\cong D\otimes^L_\Lambda C$ of the tensor product
and by the identification of the two internal-Hom functors, so that
${}^\sharp b=(b^\sharp)^\vee\circ\kappa_C$ with
$\kappa_C:C\to C^{\vee\vee}$ the canonical map. The objects $C$ and
$D$ are perfect point complexes in the sense of
[def-pod-perfect-point-complex], so $\kappa_C$ is an isomorphism by
[lem-pod-perfect-point-double-dual] and duality is an equivalence on
them; hence ${}^\sharp b$ is an isomorphism if and only if
$b^\sharp$ is. This is the asserted equivalence.
