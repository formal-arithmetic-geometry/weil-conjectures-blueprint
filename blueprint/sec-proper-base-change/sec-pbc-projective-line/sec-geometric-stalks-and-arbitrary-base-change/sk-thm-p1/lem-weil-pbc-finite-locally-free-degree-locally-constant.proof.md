+++
kind = "proof"
of = "lem-weil-pbc-finite-locally-free-degree-locally-constant"
+++
For each $x\in X$ the fibre morphism $Y_x\to\operatorname{Spec}\kappa(x)$ is finite as a base change of $f$, so $\Gamma(Y_x,\mathcal O_{Y_x})$ is a finite $\kappa(x)$-module and $\delta_f(x)<\infty$. The rank of the finite flat morphism $f$ of finite presentation at $x$ (the rank of the finite locally free module $f_*\mathcal O_Y$ at $x$) is a locally constant function of $x$. Working on an affine chart $\operatorname{Spec}A\subseteq X$ over which $f$ is $\operatorname{Spec}A\to\operatorname{Spec}B$, the rank at $x=\mathfrak p$ is the rank of the free $A_{\mathfrak p}$-module $B_{\mathfrak p}$, which equals $\dim_{\kappa(\mathfrak p)}\kappa(\mathfrak p)\otimes_AB=\delta_f(x)$. Hence $\delta_f$ is locally constant.

For each $d$, the set $X_d=\delta_f^{-1}(d)$ is open, and closed since its complement is the union of the other open sets $X_{d'}$. Finite, flat and locally of finite presentation are preserved by restriction to the open $X_d$, and the fibre degree of the restriction $f^{-1}(X_d)\to X_d$ at a point equals $\delta_f$ at that point, namely $d$. So the restriction is finite locally free of degree $d$.
