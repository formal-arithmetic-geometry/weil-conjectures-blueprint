+++
id = "lemma-nagata-cartier-total-transform-blowup"
kind = "lemma"
title = "Total transform of a Cartier ideal under a blow-up"
order = 289
lean = ["AlgebraicGeometry.Scheme.IdealSheafData.IsInvertible.comap_blowupMap"]
uses = ["def-nagata-blowup-chart-ring", "def-nagata-effective-cartier-ideal"]
+++
Let $\mathcal L\subseteq\mathcal O_T$ be an effective Cartier ideal and let
$T'\to T$ be a blow-up. Then the extended ideal
$\mathcal L\mathcal O_{T'}$ is again effective Cartier, and in particular
is invertible.

## Proof

Work over an affine open $\operatorname{Spec}(A)\subseteq T$ on which
$\mathcal L=(x)$ with $x$ a non-zero-divisor. A standard chart of the
blow-up has ring $A[I/a]\subseteq A_a$. If
$x(y/a^n)=0$ in this chart, then $a^mxy=0$ in $A$ for some $m$; regularity
of $x$ gives $a^my=0$, hence $y/a^n=0$. Thus the image of $x$ is regular
on every blow-up chart. It generates the extended ideal there, so these
local equations make $\mathcal L\mathcal O_{T'}$ an effective Cartier
ideal, hence an invertible one.
