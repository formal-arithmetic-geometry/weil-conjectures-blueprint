+++
id = "def-weil-pbc-ample-invertible-module"
kind = "definition"
title = "Ample invertible module on a scheme (absolute ampleness)"
uses = ["def-pc-scheme", "def-pur-sheaf-tensor-product", "def-sc-invertible-module"]
lean = ["AlgebraicGeometry.Scheme.Modules.IsAmple"]
order = 1623
+++
Let $X$ be a scheme [def-pc-scheme] and $\mathcal L$ an invertible $\mathcal O_X$-module [def-sc-invertible-module]. For $n\ge0$ write $\mathcal L^{\otimes n}$ for the $n$-fold tensor product $\mathcal L\otimes_{\mathcal O_X}\dots\otimes_{\mathcal O_X}\mathcal L$ [def-pur-sheaf-tensor-product] (with $\mathcal L^{\otimes0}=\mathcal O_X$). For a global section $s\in\Gamma(X,\mathcal L^{\otimes n})$ put $X_s=\{x\in X:\ s_x\notin\mathfrak m_x(\mathcal L^{\otimes n})_x\}$, where $s_x$ is the germ of $s$ in the stalk $(\mathcal L^{\otimes n})_x$ and $\mathfrak m_x$ is the maximal ideal of the local ring $\mathcal O_{X,x}$; equivalently, $X_s$ is the set of points where the value of $s$ in $(\mathcal L^{\otimes n})_x\otimes_{\mathcal O_{X,x}}\kappa(x)$ is nonzero. $\mathcal L$ is *ample* if (1) $X$ is quasi-compact, and (2) for every $x\in X$ there exist $n\ge1$, $s\in\Gamma(X,\mathcal L^{\otimes n})$ and an affine open $U\subseteq X$ [def-pc-scheme] with $x\in U$ and $U=X_s$. This is the absolute notion of Stacks Project, Properties, Definition 01PS (EGA II 4.5.3).
