+++
id = "sk-i-global-additivity"
kind = "lemma"
title = "Open–closed trace additivity"
order = 3516
uses = ["sk-d-operator", "sk-d-six", "sk-d-trace", "sk-d-weil", "sk-p-trace", "sk-prop-sf-open-closed-triangle", "sk-thm-sf-package", "sk-i-relative-frob"]
tags = ["sketch"]
+++
Here $X=X_0\times_{k_0}k$ for a separated $k_0$-scheme $X_0$ of finite type,
$A$ is a finite commutative $\ell$-primary ring, Frobenius correspondences
and their global operators $T_{c_m}$ are those of Definition [sk-d-weil], and
$j:U\hookrightarrow X$, $i:Z\to X$ denote the base changes of $j_0,i_0$ to $k$.

Let $j_0:U_0\hookrightarrow X_0$ be open with reduced closed
complement $i_0:Z_0\to X_0$, and let $K\in\Dctf(X,A)$. A Frobenius
correspondence $\psi$ on $K$ induces Frobenius correspondences on
$j^*K$, $i^*K$, $j_!j^*K$ and $Ri_*i^*K$, whose stalk maps are the
restrictions of $\psi_m$. Writing $T_{c_m}$ also for the global
operators of the induced Frobenius correspondences on $U$ and $Z$, for
every $m\geq1$

$$
 \operatorname{tr}_A(T_{c_m}(\psi_m)\mid R\Gamma_c(X,K))
 =\operatorname{tr}_A(T_{c_m}\mid R\Gamma_c(U,j^*K))
 +\operatorname{tr}_A(T_{c_m}\mid R\Gamma_c(Z,i^*K)).
$$
