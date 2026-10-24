+++
id = "cor-fd-plancherel"
kind = "theorem"
title = "Plancherel identity on the line"
lean = ["AlgebraicGeometry.WeilComplex.traceEnergy_fourierTransform"]
order = 3960
tags = ["latex:corollary"]
uses = ["def-fd-trace-function", "def-fd-transform", "lem-fd-additive-orthogonality", "thm-fd-fourier-trace"]
+++
Fix a field embedding $\iota:\Qlb\hookrightarrow\mathbf C$; the trace functions take values in $E\subset\Qlb$, and the absolute value and complex conjugation below are those of $\mathbf C$, read through $\iota$. Then for every $n\ge1$ and every Weil complex $K$ on $\mathbf A^1$,

$$
\sum_{y\in\mathbf F_{q^n}}
\left|\iota\,t_{\operatorname{FT}_\psi(K)}(y)\right|^2
=q^n\sum_{x\in\mathbf F_{q^n}}
\left|\iota\,t_K(x)\right|^2 .
$$
