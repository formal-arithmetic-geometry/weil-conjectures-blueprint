+++
id = "def-sc-gm-ga"
kind = "definition"
title = "The multiplicative group, the additive group, and their finite subgroups"
order = 2267
uses = ["def-sc-gm-torsor", "def-sc-group-scheme", "def-sc-group-scheme-subgroup", "def-sc-kummer-sequence"]
+++
Let $k$ be a field. The *multiplicative group* is the
group scheme
$\mathbf G_m=\Spec k[t,t^{-1}]$, with comultiplication, counit and
antipode the $k$-algebra maps $m^*(t)=t\otimes t$,
$\varepsilon(t)=1$, $i^*(t)=t^{-1}$, in the sense of
[def-sc-group-scheme]. The *additive group* is
$\mathbf G_a=\Spec k[y]$, with $m^*(y)=y\otimes1+1\otimes y$,
$\varepsilon(y)=0$, $i^*(y)=-y$. For $n\geq1$,

$$
\mu_n:=\Spec k[t]/(t^n-1)\subseteq\mathbf G_m
$$

is the *group scheme of $n$-th roots of unity*, and, when
$\operatorname{char}k=p>0$,

$$
\alpha_p:=\Spec k[y]/(y^p)\subseteq\mathbf G_a
$$

is the *Frobenius kernel* of $\mathbf G_a$; both are closed
subgroup schemes, the closed
immersion being the one induced by the displayed surjections of
coordinate rings.
