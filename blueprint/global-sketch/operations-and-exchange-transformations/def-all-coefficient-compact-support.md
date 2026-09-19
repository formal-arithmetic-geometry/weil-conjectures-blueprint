+++
id = "def-all-coefficient-compact-support"
kind = "definition"
title = "Integral, rational, and algebraically closed compact-support functors"
order = 50
uses = ["def-compact-support-direct-image", "def-finite-reduction", "def-qbar-ambient-derived-category", "def-qbar-coefficient-category", "def-strict-reduction-tower", "def-weil-derived-complete-integral", "def-weil-finite-coefficient-datum", "def-weil-rational-coefficients", "prop-finite-compact-support-coefficient-change", "prop-ramified-coefficient-change", "thm-qbar-functor-descent", "thm-rational-lattice-localization"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ of
Definition [def-weil-finite-coefficient-datum]. Let
$f:X\to Y$ be separated and of finite type. For
$K\in D^b_c(X,\mathcal O_E)$, put
$K_n=\operatorname{red}_{X,n}(K)$ and define

$$
Rf_!K=
R\varprojlim_n\operatorname{Res}_{Y,n} Rf_{!,n}K_n
\in D(Y_{\mathrm{proet}},\widehat{\mathcal O}_{E,Y}).
$$

For $K_E\in D^b_c(X,E)$, choose an integral lattice
$K_{\mathcal O_E}$ supplied by
Theorem [thm-rational-lattice-localization] and define

$$
Rf_!K_E=(Rf_!K_{\mathcal O_E})\otimes^L_{\mathcal O_E}E
\in D(Y_{\mathrm{proet}},E_Y).
$$

The localization theorem makes this independent of the lattice. For a
finite extension $E\subset L$, its
scalar-extension comparison is represented by the finite-level
comparisons over $\mathcal O_E\subset\mathcal O_L$. Passing to the
common finite coefficient stage defines the ambient $\Qlb$-coefficient
functor

$$
Rf_!:D^b_c(X,\Qlb)\longrightarrow D(Y,\Qlb).
$$
