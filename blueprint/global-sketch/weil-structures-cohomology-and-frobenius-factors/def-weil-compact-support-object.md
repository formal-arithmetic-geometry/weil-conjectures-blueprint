+++
id = "def-weil-compact-support-object"
kind = "definition"
title = "Compact-support image of a derived Weil object"
order = 83
uses = ["def-all-coefficient-compact-support", "def-compact-support-exchange", "def-derived-weil-object", "def-weil-finite-coefficient-datum", "prop-compact-support-base-change", "prop-compact-support-coefficient-passage"]
+++
Fix an auxiliary finite coefficient datum
$(\ell,\Qlb;E,\mathcal O_E,\varpi_E)$ and let
$\Lambda\in\{E,\Qlb\}$. Let $f_0:X_0\to Y_0$ be a separated
finite-type morphism between finite-type $k_0$-schemes, with geometric
fiber $f:X\to Y$.
For a derived Weil object $(K,\theta_K)$ with
$K\in D^b_c(X,\Lambda)$, specialize the compact-support exchange of
Definition [def-compact-support-exchange] to the Cartesian Frobenius
square. Choose a compactification

$$
X_0\xrightarrow{j_0}\overline X_0\xrightarrow{p_0}Y_0
$$

of $f_0$, let
$X\xrightarrow{j}\overline X\xrightarrow{p}Y$ be its geometric fiber,
and denote the geometric Frobenius of $\overline X$ by
$g_{\overline X}$. Define

$$
\begin{aligned}
\theta_{Rf_!K}:Lg_Y^*Rf_!K
&\xrightarrow{\operatorname{FrEx}_{f,!}(K)}Rf_!Lg_X^*K\\
&\xrightarrow{Rf_!(\theta_K)}Rf_!K.
\end{aligned}
$$

Here $\operatorname{FrEx}_{f,!}$ is literally the compactification
composite

$$
Lg_Y^*Rp_*j_!K
\xrightarrow{\operatorname{Ex}_{*,p,g_Y}(j_!K)}
Rp_*Lg_{\overline X}^*j_!K
\xrightarrow{Rp_*(\operatorname{Ex}_{j,g_{\overline X}})}
Rp_*j_!Lg_X^*K;
$$

its first arrow is proper base change and its second arrow is
open-extension exchange.
