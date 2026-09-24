+++
id = "lemma-nagata-projective-is-proper"
kind = "lemma"
title = "Projective morphisms are proper"
order = 180
uses = ["def-nagata-projective-morphism"]
+++
**Status.** Not formalized, and not needed: Mathlib has no class of
projective morphisms of schemes, so the statement cannot be phrased in Lean.
The formalized route proves the cases it uses directly:
[lemma-nagata-projective-space-base-change-proper] for projective space and
[lemma-nagata-affine-blowup-proper] for the affine blow-up.

Every projective morphism of schemes is proper.

## Proof

Let $(V_i)$ be an affine open cover of $X$. By the relative-Proj
construction and its restriction isomorphisms,
$\mathbf P^r_X\times_XV_i$ is the affine Proj of the polynomial graded
algebra $\Gamma(V_i,\mathcal O_X)[T_0,\ldots,T_r]$. The verified affine
Proj instance
`Proj.instIsProperToSpecZeroOfFiniteTypeSubtypeMemOfNatNat` makes
each of these structural maps proper. Applying the verified target-locality
instance `AlgebraicGeometry.IsProper.instIsZariskiLocalAtTarget`
gives that $\mathbf P^r_X\to X$ is proper. A closed immersion is proper, and the
composite of proper morphisms is proper by
`AlgebraicGeometry.IsProper.comp`; applying this to
$Y\hookrightarrow\mathbf P^r_X\to X$ proves the claim.
