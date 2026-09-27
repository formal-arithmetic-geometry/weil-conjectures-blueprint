+++
id = "sk-prop-av-rigidity"
kind = "section"
title = "The rigidity lemma"
lean = ["AlgebraicGeometry.rigidity"]
order = 489
uses = ["sk-prop-av-const-locus", "sk-prop-av-image-open"]
+++
*Proposition (sketch).*

Let $X,Y,Z$ be $k$-schemes with $X$ proper, connected and reduced over
$k$, $Y$ connected, $Z$ separated, and let $f:X\times_kY\to Z$ be a
morphism with $f(X\times\{y_0\})$ a single point for some
$y_0\in Y(k)$. Then $f$ factors through the projection:
$f=g\circ\mathrm{pr}_2$ for some $g:Y\to Z$.

## Proof

*Step 1.* $L=\{y: f(X\times_k\{y\})\ \text{is a point}\}$ is
closed by [sk-prop-av-const-locus], and nonempty since $y_0\in L$.
*Step 2.* If $y\in L$, then $f(X\times_k\{y\})$ is finite, so by
[sk-prop-av-image-open] there is an open $U_y\ni y$ with
$f(X\times_k\{y'\})$ finite for all $y'\in U_y$; as
$X\times_k\{y'\}$ is connected and a finite scheme is totally
disconnected, $f(X\times_k\{y'\})$ is a point, so $L$ is open.
*Step 3.* $L$ is nonempty, open and closed in the connected $Y$,
hence $L=Y$: $f$ is constant on the fibres of $\mathrm{pr}_2$.
*Step 4 (recorded classical input).* The factorization
$f=g\circ\mathrm{pr}_2$ follows from constancy on the fibres by the
classical rigidity argument; in this blueprint the lemma is applied
only with $X=Y=Z=A$ an abelian variety, so $Z$ is of finite type and
Steps 1–3 apply verbatim.

Uses: [sk-prop-av-const-locus], [sk-prop-av-image-open]
