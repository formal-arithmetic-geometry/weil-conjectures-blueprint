+++
id = "lem-wf-boundary-semicontinuity"
kind = "lemma"
title = "Boundary semicontinuity of weights on a curve"
order = 2655
uses = ["d-real-cohom", "d-real-setup", "def-weil-ordinary-compact-cohomology", "def-weil-punctual-weights", "def-wf-middle-extension", "lem-a1-affine-hc2", "lem-wf-boundary-stalk-invariants", "lem-wf-euler-product-middle-extension", "lem-wf-point-count-linear-growth", "p-linear-spectra", "prop-sf-open-closed-triangle-all-stages"]
+++
Let $X_0$ be a curve over $k_0=\mathbf F_q$ in the sense of
[d-real-setup] (smooth, separated, geometrically connected; it need
not be affine, e.g. it may be proper), let $j:U_0\hookrightarrow X_0$ be a dense open
immersion with finite complement $S_0$, and let $\mathcal F$ be a
lisse Weil sheaf of rank $r\ge1$ on $U_0$. Assume that for every
closed point $x\in|U_0|$ and every eigenvalue $\alpha$ of the local
Frobenius $F_x$ on $\mathcal F_{\bar x}$ the inequality

$$
|\iota(\alpha)|^2\le q_x^{\beta}
$$

holds for a real number $\beta$ (i.e. $\mathcal F$ is punctually
$\iota$-mixed of weights at most $\beta$ in the punctual weight
convention of [def-weil-punctual-weights]). Then the same
inequality holds at every boundary point: for every $s\in S_0$ and
every eigenvalue $\alpha$ of $F_s$ on the middle-extension stalk
$(j_*\mathcal F)_{\bar s}$ of
[def-wf-middle-extension],

$$
|\iota(\alpha)|^2\le q_s^{\beta}.
$$

Since $j_*\mathcal F$ restricts to $\mathcal F$ on $U_0$, this says
that $j_*\mathcal F$ has punctual weights at most $\beta$ on all of
$X_0$.
