+++
id = "pur713-def-open-shriek-module"
kind = "definition"
title = "Module-object extension by zero"
order = 1839
tags = ["latex:bpdefinition"]
uses = ["pur713-def-coefficient-map", "pur713-input-coefficient-structure", "pur713-input-open-projection"]
+++
Assume Inputs [pur713-input-coefficient-structure] and [pur713-input-open-projection]. Let $j:U\hookrightarrow X$ be an open immersion and $T\in\{\mathcal O_E,E,\overline{\mathbf Q}_\ell\}$. For a $j^{-1}_{\mathbf Z}\mathcal R_{X,T}$-module $N$, let $j_!^{\mathcal R_{X,T}}N$ be the abelian sheaf $j_{!,\mathbf Z}N$ with the $\mathcal R_{X,T}$-action

$$
\mathcal R_{X,T}\otimes_{\mathbf Z}j_{!,\mathbf Z}N
\xrightarrow{\pi^{-1}_{j,\mathcal R_{X,T},N}}
j_{!,\mathbf Z}(j^{-1}_{\mathbf Z}\mathcal R_{X,T}\otimes_{\mathbf Z}N)
\longrightarrow j_{!,\mathbf Z}N,
$$

the second map being $j_{!,\mathbf Z}$ of the action of $N$, and $\pi$ as in Input [pur713-input-open-projection]; its associativity and unit identities follow from the compatibility clause of that input. Define

$$
j_{!,T}:=j_!^{\mathcal R_{X,T}}\circ\operatorname{Res}_{\alpha_{j,T}}:
\mathsf{Mod}(U_{\Proet},T)\longrightarrow\mathsf{Mod}_{j^{-1}_{\mathbf Z}\mathcal R_{X,T}}(U_{\Proet})\longrightarrow\mathsf{Mod}(X_{\Proet},T),
$$

with $\alpha_{j,T}$ of Definition [pur713-def-coefficient-map]. This is the open-extension construction of the governing reference, §8.1. The underlying abelian sheaf of $j_{!,T}M$ is $j_{!,\mathbf Z}M$.
