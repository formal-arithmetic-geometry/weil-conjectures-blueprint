+++
id = "lemma-nagata-module-strict-transform-exact"
kind = "lemma"
title = "Strict transform preserves universally exact sequences, [stacks-project]"
order = 360
uses = ["def-nagata-module-strict-transform", "lemma-nagata-module-strict-transform-chart", "lemma-nagata-power-torsion-localization"]
+++
**Status.** Bypassed by the formalized route: the Raynaud–Gruson flattening
chain is not formalized. Elimination of indeterminacy is obtained instead
by the route of the chapter *Elimination of indeterminacy after Deligne
and Conrad*, whose output is
`AlgebraicGeometry.exists_admissibleBlowup_isOpenImmersion_strictTransformMap`.

Let $V\to S$ be a morphism and let
$0\to\mathcal M_1\to\mathcal M_2\to\mathcal M_3\to0$ be a sequence of
quasi-coherent $\mathcal O_V$-modules which remains exact after every base
change $T\to S$. For a specified blow-up $S'\to S$, the sequence of
module strict transforms
on $V\times_SS'$,
$0\to\mathcal M'_1\to\mathcal M'_2\to\mathcal M'_3\to0$, is exact.

## Proof

The claim is local on source and base. On an affine blow-up chart, let $a$
be the local equation of the exceptional divisor and let
$0\to M_1\to M_2\to M_3\to0$ be the resulting universally exact sequence.
Surjectivity after quotienting by $a$-power torsion follows by taking a
preimage in $M_2$ and then passing to the quotient; injectivity at $M_1$
follows because an element of $M_1$ killed in the quotient is already
$a$-power torsion. If $x\in M_2$ maps to $a$-power torsion in $M_3$,
then $a^nx$ is the image of some $y\in M_1$. The class of $y$ maps to zero
in $M_2/a^nM_2$; universal injectivity makes
$M_1/a^nM_1\to M_2/a^nM_2$ injective, so $y=a^nz$ for some $z\in M_1$.
Hence $a^n(x-z)=0$ in $M_2$. Thus the class of $x$ comes from the class of
$z$, proving exactness in the middle. The affine chart descriptions glue
by localization compatibility of module strict transform.
