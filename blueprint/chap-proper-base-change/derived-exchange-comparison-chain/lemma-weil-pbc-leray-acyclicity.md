+++
id = "lemma-weil-pbc-leray-acyclicity"
kind = "lemma"
title = "Leray acyclicity criterion"
order = 1539
uses = ["def-weil-pbc-injective-acyclicity-property"]
+++
If a complex $I^\bullet$ consists of $f'_*$-acyclic sheaves, then the natural
map $\mathcal H^q(f'_*I^\bullet)\to R^qf'_*K$ is an isomorphism whenever
$K\to I^\bullet$ is a quasi-isomorphism.

## Proof

Resolve $K$ by a bounded-below Cartan–Eilenberg double complex
$J^{r,s}$ with vertical differential $d_v:J^{r,s}\to J^{r+1,s}$ resolving
$I^s$ and horizontal differential $d_h:J^{r,s}\to J^{r,s+1}$ lifting the
differential of $I^\bullet$. Set
$d_{\mathrm{tot}}=d_v+(-1)^r d_h$. Applying $f'_*$ and filtering the total
complex by $r$ gives

$$
E_1^{r,s}=R^rf'_*I^s,\qquad
E_2^{r,s}=R^rf'_*\mathcal H^s(K)\Longrightarrow
\mathcal H^{r+s}(Rf'_*K).
$$

The assumed acyclicity makes $E_1^{r,s}=0$ for $r>0$, so the edge map from
the $r=0$ column is the cohomology map of the ordinary complex
$f'_*I^\bullet$. The sign $(-1)^r$ makes the square with the horizontal
differential commute, and the edge morphism is therefore exactly the natural
map $\mathcal H^q(f'_*I^\bullet)\to R^qf'_*K$. Collapse of the first column
proves it is an isomorphism.
