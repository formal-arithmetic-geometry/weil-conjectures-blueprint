+++
id = "lem-fd-first-formula"
kind = "lemma"
title = "The first Fourier formula"
order = 3954
uses = ["def-fd-transform", "def-wf-tate-twist", "lem-fd-stalk-formula", "sk-prop-sfb-finite-extension-compatibility"]
+++
Let $S=\operatorname{Spec}k$ with $k$ finite or algebraically closed and $V=\mathbf A^1_k$. Let $\underline{E}$ be the constant sheaf with value $E$ (the unit of $D^b_c(-,E)$) and $\delta_0=i_{0*}\underline{E}$ the skyscraper with value $E$ at the origin $i_0:\{0\}\hookrightarrow V^\vee$ (resp. $V$), placed in degree $0$. Then, in $D^b_c(V^\vee,E)$,

$$
\operatorname{FT}_\psi(\underline{E})\cong\delta_0(-1)[-1],\qquad
\operatorname{FT}_\psi(\delta_0)\cong\underline{E}[1],
$$

where $\delta_0(-1)$ is the Tate twist $(-1)$ of $\delta_0$. (The transform of [def-fd-transform] is $E$-linear; the same formulas for the constant sheaf $\overline{\mathbf Q}_\ell$ and the $\overline{\mathbf Q}_\ell$-skyscraper follow by the extension of scalars $-\otimes_E\overline{\mathbf Q}_\ell$.)
