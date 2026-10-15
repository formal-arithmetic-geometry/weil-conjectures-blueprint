+++
id = "det-pe-milnor-sequence"
kind = "lemma"
title = "Cohomology of the sequential derived limit"
uses = ["det-pe-products-derived"]
+++
Let $\mathcal R$ be a sheaf of rings on $X_{\mathrm{proét}}$, let
$\cdots\to K_2\xrightarrow{t_1}K_1\xrightarrow{t_0}K_0$ be a tower of complexes of
$\mathcal R$-modules, $T\colon\prod_nK_n\to\prod_nK_n$, $T((k_n)_n)=(t_n(k_{n+1}))_n$, and
$R\varprojlim_nK_n:=\operatorname{Cone}(1-T)[-1]$.

1. For every $q$ there is a natural short exact sequence of sheaves

   $$
   0\to\coker\Bigl(\prod_nH^{q-1}(K_n)\xrightarrow{1-T}\prod_nH^{q-1}(K_n)\Bigr)
   \to H^q\bigl(R\varprojlim_nK_n\bigr)\to\varprojlim_nH^q(K_n)\to0 .
   $$

2. For a tower of modules $(M_n)$ (complexes in degree $0$), $R^p\varprojlim_nM_n:=
   H^p(R\varprojlim_nM_n)$ is $\varprojlim_nM_n$ for $p=0$,
   $\coker(1-T)$ for $p=1$, and $0$ for $p\notin\{0,1\}$.
3. Consequently the sequence in 1 is the Milnor sequence
   $0\to R^1\varprojlim_nH^{q-1}(K_n)\to H^q(R\varprojlim_nK_n)\to\varprojlim_nH^q(K_n)\to0$.
