+++
id = "sk-cor-tf-point-counting"
kind = "corollary"
title = "Point counting and the zeta function"
order = 3865
uses = ["sk-def-sf-weil-complexes", "sk-thm-tf-uniform-formula", "sk-thm-trace-transport"]
tags = ["sketch"]
+++
Let $X_0$ be separated and of finite type over $\mathbf F_q$, put
$X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$, and for a closed point
$x\in|X_0|$ let $d_x=[\kappa(x):\mathbf F_q]$ be its degree.

Give $\Lambda_X$ the Weil structure of constant sheaves defined after
[sk-def-sf-weil-complexes]. For every coefficient
ring $\Lambda$ of [sk-thm-tf-uniform-formula] and every $m\geq1$,

$$
 \operatorname{tr}_{\Lambda}
    (\operatorname{Frob}_{X,\Lambda_X}^m\mid R\Gamma_c(X_{\mathrm{pro\acute et}},\Lambda_X))
   =\#X_0(\mathbf F_{q^m})\cdot1_{\Lambda}.
 \tag{1}
$$

For $\Lambda=\Ql,E,\overline{\mathbf Q}_\ell$ this gives

$$
 \#X_0(\mathbf F_{q^m})
   =\sum_i(-1)^i\operatorname{Tr}
      (\operatorname{Frob}_{X,\Lambda_X}^m\mid H_c^i(X_{\mathrm{pro\acute et}},\Lambda_X)),
$$

and

$$
 \begin{aligned}
 Z(X_0,T)
   &:=\exp\left(\sum_{m\geq1}
          \#X_0(\mathbf F_{q^m})\frac{T^m}{m}\right)\\
   &=\prod_{x\in|X_0|}(1-T^{d_x})^{-1}
     =\prod_i\det(1-T\operatorname{Frob}_{X,\Lambda_X}\mid H_c^i(X_{\mathrm{pro\acute et}},\Lambda_X))^{(-1)^{i+1}}.
 \end{aligned}
$$

The first two series lie in $1+T\mathbf Z[[T]]$, and the last equality
holds in $\Lambda[[T]]$. Moreover $Z(X_0,T)$ belongs to
$\mathbf Q(T)$.
