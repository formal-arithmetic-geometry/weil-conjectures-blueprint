+++
id = "sk-cor-tf-trace-function-pushforward"
kind = "corollary"
title = "Trace functions and direct image with compact support"
order = 610
uses = ["sk-def-sf-weil-complexes"]
tags = ["sketch"]
+++
Let $f_0:X_0\to Y_0$ be a morphism of separated $\mathbf F_q$-schemes
of finite type, with geometric base change $f:X\to Y$, and let
$(K,\phi)$ be a Weil complex on $X$ with $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ for an
admissible $\Lambda$. Give $Rf_!K\in D^b_{\mathrm{ctf}}(Y,\Lambda)$ the Weil
structure induced by $\phi$ (after Definition [sk-def-sf-weil-complexes]).
Then for every $m\geq1$ and $y\in Y_0(\mathbf F_{q^m})$,

$$
t_{Rf_!K,m}(y)=\sum_{\substack{x\in X_0(\mathbf F_{q^m})\\ f_0(x)=y}}
t_{K,m}(x).
$$
