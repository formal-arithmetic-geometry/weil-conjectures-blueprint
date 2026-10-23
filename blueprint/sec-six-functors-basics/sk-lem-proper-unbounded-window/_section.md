+++
id = "sk-lem-proper-unbounded-window"
kind = "lemma"
title = "Proper direct image of unbounded complexes"
order = 2254
uses = ["sk-lem-proper-heart-bound", "sk-cor-ambient-ind-derived"]
tags = ["sketch"]
+++
Let $\Lambda=E$ or $\Qlb$, and let $p\colon X\to Y$ and $d$ be as in [sk-lem-proper-heart-bound]. Write
$\Dic^{\leq b}(X,\Lambda)$ and $\Dic^{\geq a}(X,\Lambda)$ for the objects of $\Dic(X,\Lambda)$
([sk-cor-ambient-ind-derived]) with cohomology in degrees $\leq b$, respectively $\geq a$. Then
$Rp_*\colon\D(X_{\mathrm{proét}},\Lambda)\to\D(Y_{\mathrm{proét}},\Lambda)$ maps $\Dic(X,\Lambda)$ into $\Dic(Y,\Lambda)$, and

$$
Rp_*\bigl(\Dic^{\leq b}(X,\Lambda)\bigr)\subset\Dic^{\leq b+2d+1}(Y,\Lambda),
\qquad
Rp_*\bigl(\Dic^{\geq a}(X,\Lambda)\bigr)\subset\Dic^{\geq a}(Y,\Lambda).
$$

Moreover, for $K\in\Dic(X,\Lambda)$ and every integer $q$, the canonical truncation maps
$K\leftarrow\tau_{\leq q}K\to\tau_{\geq q-2d-1}\tau_{\leq q}K$ induce an isomorphism in
$\IndCons(Y,\Lambda)$

$$
\mathcal H^q(Rp_*K)\simeq\mathcal H^q\bigl(Rp_*\tau_{\geq q-2d-1}\tau_{\leq q}K\bigr).
$$
