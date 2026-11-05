+++
id = "prose-A-13"
kind = "hidden"
title = "Elimination of indeterminacy (5)"
order = 1432
+++
Blow-ups commute with flat base change [Stacks, [0805](https://stacks.math.columbia.edu/tag/0805)], because flat
pullback preserves the inclusions $\mathcal I^m\subseteq\mathcal O_T$.
Under a base change that is not flat, the pullbacks of these
inclusions can have kernels.
In that case the blow-up of the pulled-back ideal is the strict
transform of the base change, which can be strictly smaller than the
base change itself.

The gluing argument has to extend a morphism defined on a dense open
$U\subseteq X$ as far as possible. When the target $Y$ is not proper,
the extension can stop before reaching all of $X$. We need a way to say
that a partial map is already extended as far as it can be.

Take $X=Y=\mathbf A^1_k$ and $U=\mathbf A^1\setminus\{0\}$. The
inclusion $t\mapsto t$ extends over $0$. Its graph, the diagonal minus
the origin, is not closed in $X\times Y$. The map $t\mapsto1/t$ does not
extend, even after a blow-up, since blowing up a point on a regular
curve does nothing. Its graph $V(ty-1)$ is closed. In general, a closed
graph means that no limit point lies over $X\setminus U$. A map with
closed graph is therefore not the restriction of a map on a larger open.
Both the hypothesis and the conclusion of
Theorem [theorem-extension-partial-section] are stated in this form.
For proper $Y$ the condition forces the domain to be all of $X$, which
gives Corollary [corollary-extension-proper-target].
