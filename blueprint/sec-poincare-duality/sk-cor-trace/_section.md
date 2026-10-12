+++
id = "sk-cor-trace"
kind = "corollary"
title = "The trace isomorphism"
order = 2746
uses = ["sk-def-trace-cup", "sk-lem-finite", "sk-prop-an", "sk-thm-purity-transport", "sk-thm-regular", "sk-thm-sf-identification", "sk-thm-smooth-purity"]
tags = ["sketch"]
+++
In the setting of [sk-def-pairing] with $X_0$ in addition
*proper*, for the constant sheaf $K=\Lambda_X$,

$$
\operatorname{tr}^{(-d)}_X:H^{2d}(X,\Lambda)\xrightarrow{\ \sim\ }
\Lambda(-d)
$$

is an isomorphism, and it is the map produced by the duality at $i=0$;
its twist $\operatorname{tr}^{(-d)}_X(d):H^{2d}(X,\Lambda(d))\to\Lambda$
sends the class of a $k$-point $x\in X(k)$ (the image in
$H^{2d}(X,\Lambda(d))$ of the fundamental class $[x\subset X]$ of
[sk-thm-regular], $c=d$) to $1$. This is not an independent
convention: it follows from [sk-thm-regular](c), which identifies the
fundamental class with the isomorphism assembled from smooth purity of
$a_X$ and of $a_{\Spec k}=\mathrm{id}$, together with the compatibility
of smooth purity and of the counits with composition
([sk-thm-smooth-purity], [sk-thm-purity-transport]). Here
$[x\subset X]$ is defined at $\Lambda=A_{E,n}$; at $\Oe$ it means the
compatible system of the finite-level classes, and at $E$, $\Qlb$ its
image under scalar extension.
