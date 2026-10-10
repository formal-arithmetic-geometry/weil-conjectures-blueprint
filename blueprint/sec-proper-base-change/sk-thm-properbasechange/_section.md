+++
id = "sk-thm-properbasechange"
kind = "section"
title = "Proper base change"
order = 1205
lean = ["AlgebraicGeometry.Etale.isIso_baseChange_of_isProper"]
uses = ["sk-def-conv", "sk-def-exchange", "sk-def-pbc", "sk-thm-p1", "sk-thm-reduction"]
+++
*Theorem (sketch).*

Let $\Lambda$ be a commutative ring, let $f:X\to Y$ be a proper morphism,
and let $g:Y'\to Y$ be an arbitrary morphism, with base change
$f':X'=X\times_YY'\to Y'$ and $g':X'\to X$. For every object $K$ of
$\Dplus(X_{\Et},\Lambda)$ all of whose cohomology sheaves are torsion,
the exchange morphism

$$
\Ex_{\square,K}:g^{-1}Rf_*K\xrightarrow{\ \sim\ }Rf'_*g'^{-1}K
$$

is an isomorphism in $\Dplus(Y'_{\Et},\Lambda)$. In particular
$\mathrm{PBC}(f)$ holds in the sense of [sk-def-pbc].

## Proof

**Step 1 ($\Pone$).** By [sk-thm-p1], for every scheme $S$ the
projection $\Pone_S\to S$ satisfies $\mathrm{PBC}_\Lambda$: the exchange
morphism is an isomorphism, for every base change, on every object of
$\Dplus(\Pone_{S,\Et},\Lambda)$ with torsion cohomology sheaves.

**Step 2 (reduction).** [sk-thm-reduction], applied with the same ring
$\Lambda$, turns this into $\mathrm{PBC}_\Lambda(f)$ for every proper
morphism $f$. Its proof passes to the torsion rings $\Lambda/N\Lambda$ by
restriction of scalars, reduces a bounded below complex with torsion
cohomology to torsion sheaves (truncation triangles, the five lemma) and a
torsion sheaf $F$ to the sheaves $F[N]$ killed by $N$ (filtered colimits,
over which the proper $R^qf_*$ commutes), and then runs the
Chow/composition/cancellation argument in the injective-acyclicity form.

**Step 3 (conclusion).** By [sk-def-pbc], $\mathrm{PBC}_\Lambda(f)$ says
exactly that for every morphism $g:Y'\to Y$ and every
$K\in\Dplus(X_{\Et},\Lambda)$ with torsion cohomology sheaves the exchange
morphism $\Ex_{\square,K}$ is an isomorphism in $\Dplus(Y'_{\Et},\Lambda)$,
which is the assertion.
