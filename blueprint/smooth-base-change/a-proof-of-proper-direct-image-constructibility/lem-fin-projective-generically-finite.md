+++
id = "lem-fin-projective-generically-finite"
kind = "lemma"
title = "A projective family with finite generic fibre is generically finite"
order = 5193
lean = ["AlgebraicGeometry.IsProjectiveHom.isFinite_of_generic_finite"]
+++
Let $A$ be a Noetherian domain with fraction field $K$, and let
$D\to\operatorname{Spec}A$ be projective. If $D_K$ has dimension at most
zero, this morphism is finite after restriction to a nonempty open of
$\operatorname{Spec}A$.

## Proof

Embed $D$ into $\mathbf P^N_A$. The finite $K$-scheme $D_K$ is affine with
Artinian coordinate ring. An invertible module on an Artinian ring is free
on each local factor, hence is free of rank one. For sufficiently large $m$,
the exact sequence of its ideal sheaf, twisted by $\mathcal O(m)$, together
with Serre vanishing, shows that
$$
H^0(\mathbf P^N_K,\mathcal O(m))\longrightarrow H^0(D_K,\mathcal O(m)|_{D_K})
$$
is surjective. Choose a generator on $D_K$ and lift it to a homogeneous
polynomial $P$. If $D_K$ is empty, any homogeneous polynomial suffices.
Clear denominators so that $P$ is defined over an open of the base.

The closed subset $D\cap V_+(P)$ is proper over the base and has empty
generic fibre; remove its closed image. Now $D$ is a closed subscheme of the
affine $D_+(P)$, so it is affine over the remaining affine base. Its
coordinate algebra is finite as a base module by the coherent-finiteness
theorem for projective morphisms, applied to $\mathcal O_D$. An affine
morphism with finite coordinate algebra is finite.

Unresolved dependencies: def:weil-pbc-scheme-conventions, lem:weil-pbc-proper-closed-image, lem:pc-projective-coherent-finiteness, def:pc-projective-space-twist, lem:pc-projective-space-serre-vanishing
