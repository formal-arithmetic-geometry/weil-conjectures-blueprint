+++
id = "example-running-example"
kind = "example"
title = "A running example"
order = 271
uses = ["lemma-cohomology-projective-line-trace", "example-closed-support"]
+++
We use the same few schemes throughout:

$$
\{0\}\xrightarrow{\ i\ }\mathbf A^1_k\xleftarrow{\ j\ }\mathbf G_{m,k},
\qquad \mathbf A^1_k\xrightarrow{\ j_\infty\ }\mathbf P^1_k .
$$

The sheaf $j_!\Lambda_{\mathbf G_m}$ is constructible for the
stratification $\mathbf A^1=\mathbf G_m\sqcup\{0\}$. Its stalk is
$\Lambda$ at a geometric point of $\mathbf G_m$ and $0$ at the origin.
It is not lisse on $\mathbf A^1$, and the sequence of part (3) is the
localization sequence

$$
0\to j_!\Lambda_{\mathbf G_m}\to\Lambda_{\mathbf A^1}\to i_*\Lambda\to0 .
$$

We return to this example for compact supports (after
Lemma [lemma-cohomology-projective-line-trace]), for $i^!$ (Example [example-closed-support]) and
for the trace (Section [sec-Compatibilities]).
