+++
kind  = "proof"
of    = "cor-fin-deligne-open-finite-coefficients"
+++
First let $K=F$ be a sheaf. Decompose its underlying finite
torsion group into its finitely many primary parts, and filter
the $\ell$-primary part by
$F\supset\ell F\supset\ell^2F\supset\cdots\supset0$.
These subsheaves and quotients are constructible by
[thm-constructible-serre]; each quotient is
annihilated by $\ell$. Its derived direct image is computed
over $\mathbf F_\ell$ by
[lem-fin-coefficients-forgetful-direct-image], and is bounded
constructible by [cor-fin-deligne-open-over-field].
The finite sequence of long exact cohomology sequences proves
the same assertion for the underlying finite additive sheaf of
$Rj_*F$, with a finite cohomological range. Its inherited
$A$-action preserves constructibility: on any stratum where
the additive sheaf is finite locally constant, the finitely many
endomorphisms defining the $A$-action are locally constant
matrices after an etale trivialization. Refining those
trivializations makes it a locally constant finite $A$-module
sheaf. Thus the assertion holds with its original coefficients.
For bounded $K$, use its finitely many cohomology sheaves and
the finite truncation triangles, equivalently
[thm-sp-truncation-e2]. The finite union of their ranges
bounds $Rj_*K$; kernels, cokernels and extensions preserve
constructibility by [thm-constructible-serre].
