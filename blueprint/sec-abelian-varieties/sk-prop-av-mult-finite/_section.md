+++
id = "sk-prop-av-mult-finite"
kind = "section"
title = "Finiteness of the fibres of the multiplication map"
order = 554
uses = ["sk-def-av", "sk-def-av-mult-n", "sk-prop-av-ample-positive", "sk-prop-av-mult-hom", "sk-prop-av-mult-n-pullback", "sk-prop-av-pqf-finite", "sk-prop-av-symmetric-ample"]
+++
*Proposition (sketch).*

Let $A$ be an abelian variety over $k$ and $n\ge1$. Then $[n]:A\to A$
is finite; in particular $A[n]=\ker[n]$ is a finite group scheme.

## Proof

By [sk-prop-av-symmetric-ample] there is an ample $\cN$ with
$[-1]^*\cN\cong\cN$, and by [sk-prop-av-mult-n-pullback]
$[n]^*\cN\cong\cN^{\otimes n^2}$. If a fibre $[n]^{-1}(y)$ had
positive dimension it would contain a proper curve $C$ on which $[n]$
is constant, so $\cO_C\cong[n]^*\cN|_C\cong\cN^{\otimes n^2}|_C$; but
the restriction of an ample module to a closed subscheme is ample and
an ample module on a proper curve has positive degree
([sk-prop-av-ample-positive]), hence is not trivial — contradiction.
Thus every fibre of $[n]$ is finite; since $[n]$ is proper ($A$ is
proper and $A$ is separated) and quasi-finite, it is finite by
[sk-prop-av-pqf-finite]. The kernel is the fibre over $e$.

Uses: [sk-def-av-mult-n], [sk-def-av], [sk-prop-av-ample-positive], [sk-prop-av-mult-hom], [sk-prop-av-mult-n-pullback], [sk-prop-av-pqf-finite], [sk-prop-av-symmetric-ample]
