+++
id = "def-weil-pbc-extension-by-zero"
kind = "definition"
title = "Extension by zero for open immersions"
order = 1238
uses = ["def-cbc-open-immersion-square", "def-weil-pbc-etale-sheaves", "def-weil-pbc-etale-site", "def-weil-pbc-geometric-stalks", "def-weil-pbc-scheme-conventions"]
+++
For an open immersion $j:U\hookrightarrow X$, *extension by zero* is the
exact functor

$$
j_!:\Ab(U_{\Et})\longrightarrow\Ab(X_{\Et})
$$

left adjoint to $j^{-1}$, acting on geometric stalks by

$$
(j_!F)_{\bar x}=
\begin{cases}
F_{\bar x_U},&\bar x\text{ lies in }U,\\
0,&\bar x\text{ lies in }X\setminus U,
\end{cases}
$$

where $\bar x_U$ is $\bar x$ regarded as a geometric point of $U$. Being
exact, it acts degreewise on complexes. For a finite commutative ring
$\Lambda$ the same construction is used for sheaves of $\Lambda$-modules.
