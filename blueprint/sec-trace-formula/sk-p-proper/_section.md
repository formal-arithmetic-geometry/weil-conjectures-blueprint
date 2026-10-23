+++
id = "sk-p-proper"
kind = "theorem"
title = "Proper pushforward and Lefschetz–Verdier"
order = 3489
uses = ["sk-d-corr", "sk-d-integral", "sk-d-proper-pushforward", "sk-d-trace-class", "sk-def-sf-kv-maps", "sk-p-pairing", "sk-thm-sf-comp-composition", "sk-thm-sf-kunneth-verdier", "sk-thm-sf-package"]
lean = ["AlgebraicGeometry.ProEtale.GeometricOperations.borelMoorePushforward_traceClass"]
tags = ["sketch"]
+++
Let $u:c_2^*K\to c_1^!K$ be a cohomological correspondence on $(X,K)$ for a
correspondence $c=(c_1,c_2):C\to X\times X$, with $K\in\Dctf(X,A)$. Recall
that when $c_2$ is proper, $u$ acts on $R\Gamma_c(X,K)$ by the endomorphism
$T_c(u)$ in $D(A)$, the composite of the ordinary unit
$R\Gamma_c(X,K)\to R\Gamma_c(C,c_2^*K)$ (using $Rc_{2*}=Rc_{2!}$), of $u$, of
the identification $R\Gamma_c(C,c_1^!K)\simeq R\Gamma_c(X,Rc_{1!}c_1^!K)$ and
of the exceptional counit $\varepsilon_{c_1}$.

Let $f:X\to Y$ and $g:C\to D$ be proper, and let $b=(b_1,b_2):D\to Y\times Y$
satisfy $b_ig=fc_i$. Set $K'=Rf_*K$, and let $u'$ be the pushed correspondence
on $(Y,K')$ of Definition [sk-d-proper-pushforward]. With the induced proper
map $h:F_c\to F_b$ one has

$$
\operatorname{Tr}_b(u')=h_*\operatorname{Tr}_c(u).
$$

If $X$ and $C$ are proper over $k$, this gives

$$
\operatorname{tr}_A(T_c(u)\mid R\Gamma(X,K))
=\int_{F_c}\operatorname{Tr}_c(u)
=\sum_B\operatorname{LT}_B(u),
$$

for any finite open-and-closed decomposition $F_c=\coprod B$.
