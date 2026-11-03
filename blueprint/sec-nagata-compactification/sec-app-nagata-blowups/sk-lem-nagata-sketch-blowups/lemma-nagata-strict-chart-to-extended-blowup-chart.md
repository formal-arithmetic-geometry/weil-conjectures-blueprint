+++
id = "lemma-nagata-strict-chart-to-extended-blowup-chart"
kind = "lemma"
title = "Well-definedness of the extended-ideal chart map"
order = 171
lean = ["AlgebraicGeometry.AffineBlowup.baseChangeChartToAway", "AlgebraicGeometry.AffineBlowup.baseChangeChartToAway_mem_chartRing"]
uses = ["def-nagata-strict-chart-to-extended-blowup-chart"]
+++
Let $A\to B$ be a ring map, let $I\subseteq A$ be an ideal, let $a\in I$
with image $b\in B$, and put $J=IB$. There is a unique $B$-algebra
homomorphism

$$
C_a(A,B,I)=B\otimes_AA[I/a]\longrightarrow B_b,
\qquad y\otimes c\longmapsto y\,\overline c,
$$

where $\overline c$ is the image of $c\in A[I/a]\subseteq A_a$ under the
localized map $A_a\to B_b$. Its image lies in the chart ring
$B[J/b]\subseteq B_b$. Consequently $\sigma_a$ is a well-defined
$B$-algebra homomorphism $C_a(A,B,I)\to B[J/b]$.
