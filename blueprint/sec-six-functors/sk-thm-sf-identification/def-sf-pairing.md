+++
id = "def-sf-pairing"
kind = "definition"
title = "Derived Poincare pairing"
order = 2286
uses = ["def-sf-cup", "def-sf-datum", "def-sf-orientation", "def-sf-pf"]
+++
In the setting of [def-sf-datum] and [def-sf-orientation], let
$X$ be smooth proper geometrically connected of pure dimension $d$ and let
$K\in D^b_{ctf}(X,\Lambda)$ be such that $K^\vee$ is perfect on $X$. The
*derived Poincare pairing* is the composite

$$
\beta_K:\ R\Gamma_c(X,K)\otimes^L_\Lambda
R\Gamma\bigl(X,K^\vee(d)\bigr)[2d]\longrightarrow\Lambda,
$$

$$
\begin{array}{lll}
R\Gamma_c(X,K)\otimes^L_\Lambda R\Gamma(X,K^\vee(d))[2d]
&\xrightarrow{\ \smile_c\ }&
R\Gamma_c\bigl(X,K\otimes^L_{\Lambda_X}K^\vee(d)\bigr)[2d]\\[2pt]
&\xrightarrow{\ R\Gamma_c(\operatorname{ev}_K(d))[2d]\ }&
R\Gamma_c\bigl(X,\Lambda_X(d)\bigr)[2d]\\[2pt]
&\xrightarrow{\ \operatorname{Tr}^{\mathrm{sm}}_{a_X,\Lambda}\ }&
\Lambda,
\end{array}
$$

where $\smile_c$ is the mixed-support cup product of
[def-sf-cup], $\operatorname{ev}_K$ is the
evaluation of [def-sf-pf], and
$\operatorname{Tr}^{\mathrm{sm}}_{a_X,\Lambda}$ is the normalized smooth
trace, i.e. the counit of $Ra_{X!}\dashv Ra_X^!$ read through the
orientation of [def-sf-orientation]. A morphism
$b:C\otimes^L_\Lambda D\to\Lambda$ of point complexes is *perfect* if
its tensor–internal-Hom adjoint $D\to C^\vee$ is an isomorphism.
