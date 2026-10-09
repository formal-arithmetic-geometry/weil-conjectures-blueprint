+++
id = "def-pur-normal-bundle"
kind = "definition"
title = "Normal bundle of a closed section"
order = 1899
uses = ["def-pur-conventions", "def-pur-dnc-section-family", "def-weil-scheme-morphism-properties"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting), in the situation of
[def-pur-dnc-section-family] ($g:V\to B$ with a closed section $s$), the *normal bundle* of the
section is the fibre of the deformation over $t=0$:

$$
N_s=\mathcal D_sV\times_{\widetilde g,\,\mathbf A^1_B,\,0}B ,
$$

with projection $\pi_N:N_s\to B$, inclusion $\iota_0:N_s\to\mathcal D_sV$ and *zero section*
$0_N=(\widetilde s\circ 0,\operatorname{id}):B\to N_s$, so that $\pi_N\circ0_N=\operatorname{id}_B$ and
$\iota_0\circ0_N=\widetilde s\circ0$.

By the Rees description of $\mathcal D_sV$, $N_s$ is the normal cone
$\operatorname{Spec}_B\bigl(\bigoplus_{r\geq0}\mathcal I^r/\mathcal I^{r+1}\bigr)$ of $s$, with $\mathcal I$ the
ideal of $s(B)$; when $g$ is smooth of relative dimension $d$ it is a vector bundle of rank $d$
with zero section $0_N$ ([lem-pur-dnc-section-geometry] (1)). The definition does not use this
identification.
