+++
id = "lem-weil-pbc-finite-locally-free-degree-locally-constant"
kind = "lemma"
title = "The fibre degree of a finite locally free morphism is locally constant"
uses = ["def-pc-finite-locally-free"]
lean = ["AlgebraicGeometry.finiteLocallyFree_fiberDimension_isLocallyConstant"]
order = 1783
+++
Let $f:Y\to X$ be a finite locally free morphism of schemes [def-pc-finite-locally-free], i.e. finite, flat and locally of finite presentation. For $x\in X$ with residue field $\kappa(x)$ let $Y_x=Y\times_X\operatorname{Spec}\kappa(x)$ be the fibre and
$$\delta_f(x)=\dim_{\kappa(x)}\Gamma(Y_x,\mathcal O_{Y_x}).$$
Then $\delta_f(x)$ is finite for every $x\in X$, and the function $\delta_f:X\to\mathbf Z_{\ge0}$ is locally constant on the underlying topological space of $X$ (every point has an open neighbourhood on which $\delta_f$ is constant). Equivalently, $X=\coprod_{d\ge0}X_d$ with $X_d=\delta_f^{-1}(d)$ open and closed, and $f^{-1}(X_d)\to X_d$ is finite locally free of degree $d$ in the sense of [def-pc-finite-locally-free].
