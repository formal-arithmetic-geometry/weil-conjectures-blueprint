+++
id = "sk-prop-av-const-locus"
kind = "section"
title = "The locus of constant fibres is closed"
lean = ["AlgebraicGeometry.isClosed_setOf_subsingleton_image"]
order = 485
uses = ["sk-def-av"]
+++
*Proposition (sketch).*

Let $X$ be a $k$-scheme proper over $k$, $Z$ separated over $k$, $Y$ a
$k$-scheme and $f:X\times_kY\to Z$ a morphism. Then

$$
L:=\{y\in Y: f(X\times_k\{y\})\ \text{is a single point}\}
$$

is closed in $Y$.

## Proof

The morphism $\Phi(x_1,x_2,y)=(f(x_1,y),f(x_2,y))$ makes
$L=\pi(\Phi^{-1}(\Delta_Z))$, where $\Delta_Z\subseteq Z\times_kZ$ is
closed (separation of $Z$) and $\pi:X\times_kX\times_kY\to Y$ is the
base change of the proper morphism $X\times_kX\to\Spec k$, hence proper
and therefore closed.

Uses: [sk-def-av]
