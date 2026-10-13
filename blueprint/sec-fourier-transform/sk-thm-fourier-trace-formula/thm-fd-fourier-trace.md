+++
id = "thm-fd-fourier-trace"
kind = "theorem"
title = "Fourier trace formula"
order = 3051
uses = ["cor-trf-point-counting", "def-fd-additive-character", "def-fd-trace-function", "def-fd-transform", "lem-fd-as-trace", "lem-fd-stalk-formula", "thm-trf-grothendieck-lefschetz-qbar"]
+++
For $y\in\mathbf F_{q^n}$ and a Weil complex $K$ on $\mathbf A^1$,

$$
t_{\operatorname{FT}_\psi(K)}(y)
=-\sum_{x\in\mathbf F_{q^n}}t_K(x)\ \psi\Bigl(\operatorname{Tr}_{\mathbf F_{q^n}/k_0}(xy)\Bigr),
$$

where $t_K$ is the trace function of [def-fd-trace-function].
