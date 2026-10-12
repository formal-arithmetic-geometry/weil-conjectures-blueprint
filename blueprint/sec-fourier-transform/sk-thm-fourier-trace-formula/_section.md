+++
id = "sk-thm-fourier-trace-formula"
kind = "theorem"
title = "P8: the Fourier trace formula"
order = 3046
uses = ["sk-def-ft", "sk-def-trace", "sk-lem-as-properties", "sk-prop-stalk"]
tags = ["sketch"]
+++
For $y\in\mathbf F_{q^n}$ and a Weil complex $K$ on $\Aone$,

$$
t_{\FT_\psi(K)}(y)
=-\sum_{x\in\mathbf F_{q^n}}t_K(x)\,\psi\bigl(\Tr_{\mathbf F_{q^n}/k_0}(xy)\bigr).
$$

Thus, up to the sign coming from the shift $[1]$, the trace function of the
transform is the classical Fourier transform of the trace function of the
input.
