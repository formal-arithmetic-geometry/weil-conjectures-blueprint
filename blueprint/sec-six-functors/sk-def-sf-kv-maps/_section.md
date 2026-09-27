+++
id = "sk-def-sf-kv-maps"
kind = "section"
title = "The product comparison maps"
order = 2222
uses = ["sec-smooth-purity", "sk-def-sf-exchanges", "sk-def-sf-operations", "sk-thm-sf-kunneth-relative"]
lean = ["AlgebraicGeometry.Etale.HasKunnethComparisons"]
+++
*Definition (sketch).*

For $i=1,2$ let $f_i:X_i\to Y_i$ be separated of finite type between
finite-type $k$-schemes, carrying the ambient datum of
[sk-def-sf-admissible] where $Rf^!$ occurs, put $f=f_1\times f_2$, and let
$L_i\in\Dctf(Y_i,\Lambda)$, $B_i\in\Dctf(X_i,\Lambda)$.

3pt
1. **(i)** The $!$-Künneth
$\mathrm{Ku}_!:Rf_!(B_1\boxtimes B_2)\xrightarrow{\ \sim\ } Rf_{1!}B_1\boxtimes Rf_{2!}B_2$ is [sk-thm-sf-kunneth-relative] for the base
$B=Y_1\times Y_2$, using
$X_1\times X_2=(X_1\times Y_2)\times_B(Y_1\times X_2)$. It is an isomorphism.
1. **(ii)** The *exceptional Künneth*
$\alpha:Rf_1^!L_1\boxtimes Rf_2^!L_2\to Rf^!(L_1\boxtimes L_2)$ is the
exceptional adjoint of
$$
Rf_!\bigl(Rf_1^!L_1\boxtimes Rf_2^!L_2\bigr)
\xrightarrow{\ \mathrm{Ku}_!\ }
Rf_{1!}Rf_1^!L_1\boxtimes Rf_{2!}Rf_2^!L_2
\xrightarrow{\ \varepsilon_1\boxtimes\varepsilon_2\ }
L_1\boxtimes L_2 ,
$$
where the $\varepsilon_i$ are the counits of $Rf_{i!}\dashv Rf_i^!$.
1. **(iii)** The *external Hom* map
$$
\beta:\RHom(E_1,L_1)\boxtimes\RHom(E_2,L_2)
\longrightarrow\RHom\bigl(E_1\boxtimes E_2,L_1\boxtimes L_2\bigr)
$$
is the tensor–Hom transpose of the two evaluations, with the tensor symmetry
and its Koszul signs.
1. **(iv)** For $M\in\Dctf(X,\Lambda)$ and $N\in\Dctf(Y,\Lambda)$, with
$p_X,p_Y$ the projections of $X\times Y$, the *Künneth–Verdier* map is
$$
\begin{aligned}
\kappa_{M,N}:M\boxtimes\mathbb D_YN
&\xrightarrow{\ \beta\ }\RHom\bigl(p_Y^*N,M\boxtimes\omega_Y\bigr)\\
&\xrightarrow{\ \RHom(1,\alpha_{\operatorname{id}_X,a_Y})\ }
\RHom\bigl(p_Y^*N,Rp_X^!M\bigr),
\end{aligned}
$$
using the unit identifications $\RHom(\Lambda_X,M)=M$ and
$\Lambda_X\boxtimes N=p_Y^*N$.

Only $\mathrm{Ku}_!$ is built from isomorphisms; invertibility of
$\alpha,\beta,\kappa$ is the content of [sk-thm-sf-kunneth-verdier].

Uses: `\Cref{def:sf-exchanges}`, `\Cref{def:sf-operations}`, `\Cref{thm:sf-kunneth-relative}`
