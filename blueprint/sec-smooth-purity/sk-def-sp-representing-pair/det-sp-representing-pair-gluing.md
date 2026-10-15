+++
id = "det-sp-representing-pair-gluing"
kind = "lemma"
title = "Representing pairs glue along open covers"
uses = ["det-sp-representing-pair-uniqueness", "det-sf-mate-open-restriction"]
+++
Let $f:X\to Y$ be smooth, $\Lambda_n=\mathbf Z/\ell^n\mathbf Z$, $K\in\Dctf(Y,\Lambda_n)$, and
$X=U\cup V$ an open cover with inclusions $j_U,j_V,j_{U\cap V}$. For an open
$W\subset X$ write $f_W=f\circ j_W$. Let $H\in\Dctf(X,\Lambda_n)$ and
$\varepsilon:Rf_!H\to K$, and for each $W\in\{U,V,U\cap V\}$ let

$$
\varepsilon_W:Rf_{W!}(H|_W)=Rf_!\,j_{W!}j_W^*H\xrightarrow{\ Rf_!(\text{counit})\ }Rf_!H
\xrightarrow{\ \varepsilon\ }K .
$$

If $(H|_W,\varepsilon_W)$ is a representing pair for $K$ relative to $f_W$ for
$W=U$, $V$ and $U\cap V$, then $(H,\varepsilon)$ is a representing pair for $K$
relative to $f$. In particular, if chart models with compatible counits are
given on the members of a cover, the glued model is canonically isomorphic to
$f^!K$.
