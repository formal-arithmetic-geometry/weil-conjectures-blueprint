+++
id = "prop-fd-l2-upper-weight-shift"
kind = "theorem"
title = "The transform raises the $L^2$-weight by at most one; KW §6"
order = 2981
tags = ["latex:proposition"]
uses = ["def-weil-punctual-weights", "def-wf-l2-norm", "lem-fd-l2-plancherel-shift", "lem-wf-l2-upper"]
+++
Let $j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion,
let $\mathcal F$ be a lisse Weil sheaf on $U_0$, punctually
$\iota$-mixed with weights at most $w$ in the sense of
[def-weil-punctual-weights], and put
$\mathcal K_0:=j_!\mathcal F$. Then the Fourier–Deligne transform
satisfies

$$
\bigl\|\operatorname{FT}_\psi(\mathcal K_0)\bigr\|\;\le\;w+1
$$

in the $L^2$-weight parameter of [def-wf-l2-norm]: the
Plancherel shift of [lem-fd-l2-plancherel-shift] together with
the upper bound [lem-wf-l2-upper] shows that the $L^2$-weight of
the transform exceeds the upper weight of the input by at most one —
the weight-shift step of Chapter I, §6, of the Kiehl–Weissauer
route: the Plancherel identity transports the $L^2$-weight into the
dual line, and the $L^2$-dictionary of the real-sheaf section
identifies it with the weight of the real transformed object.

## Proof

Step 1: the input complex is normalised. The trace function of
$\mathcal K_0=j_!\mathcal F$ agrees with the trace function of
$\mathcal F$ at every $k_m$-point of $U_0$ and vanishes at the
points of the finite set $\mathbf A^1_{k_0}\setminus U_0$: the
compact-support direct image has the same fibres on the open
($\mathcal F$ is lisse, hence its stalks there are those of
$\mathcal F$), and the fibres over the complement are zero, the
construction being the extension by zero of the recollement. Hence
the sums of squares of [def-wf-l2-norm] over $\mathbf A^1_{k_0}$
and over $U_0$ coincide and

$$
\|\mathcal K_0\|=\|\mathcal F\| .
$$

Step 2: the Plancherel shift. By [lem-fd-l2-plancherel-shift]
applied to the Weil complex $\mathcal K_0$ on $\mathbf A^1_{k_0}$,

$$
\bigl\|\operatorname{FT}_\psi(\mathcal K_0)\bigr\|
=\|\mathcal K_0\|+1=\|\mathcal F\|+1 .
$$

Step 3: the upper bound. The input $\mathcal F$ is lisse and
punctually $\iota$-mixed of weights at most $w$ in the sense of
[def-weil-punctual-weights], so by
[lem-wf-l2-upper] of the weight-foundations chapter, $\|\mathcal F\|\le w$.
Combining the two displayed identities with this inequality gives
the announced bound $\|\operatorname{FT}_\psi(\mathcal K_0)\|\le w+1$,
which is the positivity–Plancherel version of the Fourier weight
shift (the $\iota$-real rigidity that reads the $L^2$-weight as a
weight is the $L^2$-dictionary of the real-sheaf section of
the weight-foundations chapter).
