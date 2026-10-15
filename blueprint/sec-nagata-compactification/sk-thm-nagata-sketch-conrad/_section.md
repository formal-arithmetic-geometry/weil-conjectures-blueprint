+++
id = "sk-thm-nagata-sketch-conrad"
kind = "theorem"
title = "Extension of a partial section after an admissible blow-up"
order = 103
uses = ["sk-def-nagata-sketch-quasidomination", "sk-prop-nagata-sketch-zmt"]
lean = ["AlgebraicGeometry.exists_admissibleBlowup_extend_partialSection"]
tags = ["sketch"]
+++
Let $X$ be a quasi-compact and quasi-separated scheme, let
$U\subseteq V\subseteq X$ be quasi-compact opens with $U$ dense in $X$,
and let $p\colon Y\to X$ be separated and of finite type with $Y$
quasi-compact and quasi-separated. Let $f\colon U\to Y$ be a section of
$p$ over $U$ whose image is closed in $p^{-1}(V)$. There are a
$V$-admissible blow-up $\pi\colon\widetilde X\to X$, an open
$W\subseteq\widetilde X$ containing $\pi^{-1}(U)$ and a morphism
$g\colon W\to Y$ with $p\circ g=\pi|_W$ extending $f$ (that is,
$g|_{\pi^{-1}(U)}=f\circ\pi|_{\pi^{-1}(U)}$), whose graph is closed in
$Y\times_X\widetilde X$.
