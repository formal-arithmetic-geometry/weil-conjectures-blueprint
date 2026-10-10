+++
id = "sk-cor-plancherel"
kind = "corollary"
title = "P9: Plancherel"
order = 2708
uses = ["sk-lem-orthogonality", "sk-thm-fourier-trace-formula"]
tags = ["sketch"]
+++
Fix, as in [sk-d-real-setup], a field embedding
$\iota:\Qlb\hookrightarrow\mathbf C$; the trace functions take values in
$E\subset\Qlb$, and the absolute value and the complex conjugation below are
those of $\mathbf C$, read through $\iota$. Then for every $n\ge1$ and every
Weil complex $K$ on $\Aone$,

$$
\sum_{y\in\mathbf F_{q^n}}\bigl|\iota\,t_{\FT_\psi(K)}(y)\bigr|^2
=q^n\sum_{x\in\mathbf F_{q^n}}\bigl|\iota\,t_K(x)\bigr|^2 .
$$
