+++
id = "sk-cor-nagata-sketch-proper-extension"
kind = "section"
title = "Extension to a proper target"
order = 222
uses = ["sk-thm-nagata-sketch-conrad"]
lean = ["AlgebraicGeometry.exists_admissibleBlowup_extend_of_isProper"]
+++
*Corollary (sketch).*

Let $X$ be a quasi-compact quasi-separated scheme with a morphism $X\to S$,
let $U\subseteq X$ be a dense quasi-compact open, and let $Y\to S$ be
proper. Then for every $S$-morphism $f\colon U\to Y$ there are a
$U$-admissible blow-up $\pi\colon X'\to X$ and an $S$-morphism
$g\colon X'\to Y$ (over $S$ via $X'\to X\to S$) whose restriction to
$\pi^{-1}(U)$ is $f\circ\pi|_{\pi^{-1}(U)}$.

## Proof

Replace $Y$ by $Y\times_SX$: then $f$ becomes a section over $U$ of the
proper morphism $Y\times_SX\to X$, with closed image over $U$ because that
morphism is separated. Apply [sk-thm-nagata-sketch-conrad] with $V=U$. The
resulting partial extension $g\colon W\to Y\times_SX$ on an open
$W\supseteq\pi^{-1}(U)$ of $X'$ has closed graph in
$(Y\times_SX)\times_XX'$, which is proper over $X'$; so $W\to X'$ is both
proper and an open immersion. Its image is dense, hence all of $X'$, and
$g$ followed by the projection to $Y$ is the required $S$-morphism.
