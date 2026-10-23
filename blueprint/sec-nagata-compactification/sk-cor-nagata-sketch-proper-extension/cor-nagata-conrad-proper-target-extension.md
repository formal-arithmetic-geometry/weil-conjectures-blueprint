+++
id = "cor-nagata-conrad-proper-target-extension"
kind = "theorem"
title = "Extension of a rational map to a proper target (Conrad)"
order = 332
lean = ["AlgebraicGeometry.exists_admissibleBlowup_extend_of_isProper"]
tags = ["latex:corollary"]
uses = ["def-nagata-admissible-blowup", "def-nagata-global-blowup", "lemma-nagata-conrad-morphism-is-quasi-domination", "lemma-nagata-conrad-quasi-domination-proper-target", "prop-nagata-global-blowup-cover-independent"]
+++
Let $X$ be a quasi-compact quasi-separated scheme with a morphism
$x\colon X\to S$, let $U\subseteq X$ be a dense quasi-compact open, and let
$y\colon Y\to S$ be proper. Then for every $S$-morphism $f\colon U\to Y$
there are a $U$-admissible blow-up $\pi\colon\widetilde X\to X$ and a
morphism $\widetilde f\colon\widetilde X\to Y$ with
$y\circ\widetilde f=x\circ\pi$ whose restriction to $\pi^{-1}(U)$ is
$f\circ\pi|_{\pi^{-1}(U)}$.
