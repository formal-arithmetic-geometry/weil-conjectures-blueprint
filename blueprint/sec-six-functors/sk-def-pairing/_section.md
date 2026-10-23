+++
id = "sk-def-pairing"
kind = "definition"
title = "Perfect pairing"
order = 3307
uses = ["sk-def-sp-trace"]
tags = ["sketch"]
+++
A pairing $P\otimes^{\mathbf L}Q\to\Lambda$ of perfect complexes, a morphism in
$D(\Lambda)$, is *perfect* if its adjoint $Q\to R\operatorname{Hom}_\Lambda(P,\Lambda)$
is an isomorphism.

*Complement.* Let $X/k$ be smooth and separated of pure dimension $d$, with $k$
algebraically closed, let $\Lambda$ be an admissible coefficient ring, let
$K\in\Dctf(X,\Lambda)$ be perfect over $\Lambda_X$, and put
$K^\vee=\cHom_X(K,\Lambda_X)$, with evaluation
$\ev_K:K\otimes^{\mathbf L}K^\vee\to\Lambda_X$. Let

$$
\operatorname{Tr}_X:R\Gamma_c\bigl(X,\Lambda_X(d)\bigr)[2d]\longrightarrow\Lambda
$$

be the map induced on $R\Gamma_c$ by the smooth trace of $a_X$ [sk-def-sp-trace].
The *derived Poincaré pairing* is the composite

$$
\begin{aligned}
\beta_K:\ R\Gamma_c(X,K)\otimes^{\mathbf L}_\Lambda R\Gamma\bigl(X,K^\vee(d)\bigr)[2d]
&\xrightarrow{\ \smile_c\ }
R\Gamma_c\bigl(X,K\otimes^{\mathbf L}K^\vee(d)\bigr)[2d]\\
&\xrightarrow{\ R\Gamma_c(\ev_K(d))[2d]\ }
R\Gamma_c\bigl(X,\Lambda_X(d)\bigr)[2d]
\xrightarrow{\ \operatorname{Tr}_X\ }\Lambda,
\end{aligned}
$$

where $\smile_c$ is the mixed-support cup product, formed from the projection
formula for $Ra_{X!}$ and the counit $a_X^*Ra_{X*}\to\mathrm{id}$. The evaluation
arrow lands in $R\Gamma_c(X,\Lambda_X(d))[2d]$, whose cohomology is not
concentrated in degree $0$ (for $X=\mathbf P^1_k$, $d=1$, $K=\Lambda_X$ it lives in
degrees $-2$ and $0$); the smooth trace $\operatorname{Tr}_X$ selects the
top-degree summand and fixes the normalization.
