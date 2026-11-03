+++
id = "def-sfb-compactification-over-field"
kind = "definition"
title = "The chosen compactification over a field"
lean = ["AlgebraicGeometry.compactificationOverField"]
order = 2727
uses = ["lem-sfb-compactification-over-base", "sk-def-nagata-sketch-data"]
+++
Let $k$ be a field. Let $X$ be separated and of finite type over $k$, let $Y$ be separated and
quasi-compact over $k$, and let $f\colon X\to Y$ be a morphism of $k$-schemes. The *chosen
compactification* $c_f=(X\xrightarrow{i_f}Z_f\xrightarrow{p_f}Y)$ of $f$ is one compactification
of $f$ ([sk-def-nagata-sketch-data]), fixed once and for all by choice from the nonempty set of
compactifications of $f$ given by [lem-sfb-compactification-over-base] with
$S=\operatorname{Spec}k$.
