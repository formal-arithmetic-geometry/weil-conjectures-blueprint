+++
id = "cor-fin-deligne-open-finite-coefficients"
kind = "theorem"
title = "Open direct images with arbitrary finite allowable coefficients"
order = 5814
tags = ["latex:corollary"]
lean = ["AlgebraicGeometry.Etale.mem_Dbc_derivedPushforward_of_isOpenImmersion_finiteCoefficients"]
uses = ["cor-fin-deligne-open-over-field", "lem-fin-coefficients-forgetful-direct-image"]
+++
Let $k$ be a field, let $A$ be a finite ring annihilated by an integer
invertible in $k$, and let $j:X\hookrightarrow Y$ be an open immersion of
finite-type $k$-schemes. For every $K\in\Dbc(X,A)$, one has
$Rj_*K\in\Dbc(Y,A)$.

## Proof

First let $K=F$ be a sheaf. Decompose its underlying finite torsion group
into its finitely many primary parts, and filter the $\ell$-primary part by
$F\supset\ell F\supset\ell^2F\supset\cdots\supset0$. These subsheaves and
quotients are constructible; each quotient is annihilated by $\ell$. Its
derived direct image is computed over $\mathbf F_\ell$ by
[lem-fin-coefficients-forgetful-direct-image], and is bounded constructible
by [cor-fin-deligne-open-over-field].

The finite sequence of long exact cohomology sequences proves the same
assertion for the underlying finite additive sheaf of $Rj_*F$, with a finite
cohomological range. Its inherited $A$-action preserves constructibility: on
any stratum where the additive sheaf is finite locally constant, the
finitely many endomorphisms defining the $A$-action are locally constant
matrices after an étale trivialization. Refining those trivializations makes
it a locally constant finite $A$-module sheaf. Thus the assertion holds with
its original coefficients.

For bounded $K$, use its finitely many cohomology sheaves and the finite
truncation triangles. The finite union of their ranges bounds $Rj_*K$;
kernels, cokernels and extensions preserve constructibility.

Unresolved dependencies: sbc-def-coefficient-conventions, def:weil-pbc-constructible-complexes, def:weil-pbc-derived-categories, def:weil-pbc-scheme-conventions, lem:weil-pbc-constructible-serre, thm:sp-truncation-e2
