+++
id = "lem-pc-flat-base-change-cohom"
kind = "lemma"
title = "Cohomology and flat base change"
order = 668
uses = ["def-pc-base-change", "def-pc-morphism-conventions", "def-pc-scheme", "lem-pc-affine-morphism-hi", "lem-pc-affine-vanishing", "lem-pc-cech-computes", "lem-pc-finite-support-hi", "lem-sc-cech-spectral"]
+++
Let

$$
\begin{array}{ccc}
X' & \xrightarrow{g'} & X\\[-2pt]
\downarrow{\scriptstyle f'} & & \downarrow{\scriptstyle f}\\[-2pt]
S' & \xrightarrow{g} & S
\end{array}
$$

be a cartesian diagram of schemes, let $\mathcal{F}$ be a quasi-coherent
$\mathcal{O}_X$-module with $\mathcal{F}'=(g')^*\mathcal{F}$, and assume $g$ is flat and $f$
is quasi-compact and quasi-separated. Then the base change map

$$
g^*R^if_*\mathcal{F}\;\longrightarrow\;R^if'_*\mathcal{F}'
$$

is an isomorphism for all $i\ge0$; if $S=\operatorname{Spec}(A)$, $S'=\operatorname{Spec}(B)$,
then

$$
H^i(X,\mathcal{F})\otimes_AB\;\cong\;H^i(X',\mathcal{F}')\qquad\text{for all }i .
$$
