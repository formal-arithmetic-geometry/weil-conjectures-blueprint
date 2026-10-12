+++
id = "lem-trf-compactification-graph-operator"
kind = "lemma"
title = "Extension by zero of a Frobenius coefficient morphism"
order = 2716
uses = ["def-trf-frobenius-coefficient-morphism", "def-trf-global-operator", "def-trf-graph-correspondence", "def-trf-scheme-frobenius", "def-weil-extension-by-zero", "lem-trf-adjoint-mate", "lem-trf-compactification-cohomology", "lem-trf-frobenius-open-square", "lem-trf-open-ctf", "lem-trf-open-square-exchange", "lem-weil-pbc-comparison-pullback", "prop-compactification-coherence-detailed", "prop-functor-package", "prop-trf-graph-operator"]
+++
Fix the global finite-field datum and the coefficient ring
$A=A_{E,n}$. Let $j_0:X_0\hookrightarrow\bar X_0$ be a
compactification over $k_0$ of a separated finite-type $k_0$-scheme,
with base change $j:X\hookrightarrow\bar X$ to $k$, and write
$\Phi=\Phi_X$, $\bar\Phi=\Phi_{\bar X}$ for the $q$-power scheme
Frobenii of [def-trf-scheme-frobenius]. For $m\geq0$ let

$$
b_m:L\bar\Phi^{m*}j_!\xrightarrow{\ \sim\ }j_!L\Phi^{m*}
$$

be the comparison isomorphism of [lem-trf-open-square-exchange] for the
Cartesian square of [lem-trf-frobenius-open-square] with
$(h,\bar h)=(\Phi^m,\bar\Phi^m)$. Let $K\in D^b_{ctf}(X,A)$ carry an
explicit etale-origin witness.

1. *Extension of coefficient morphisms.* For every morphism
$v:L\Phi^{m*}K\to K$ put
$$
\bar v=j_!v\circ b_m:\;L\bar\Phi^{m*}j_!K\longrightarrow j_!K .
$$
If $\psi:L\Phi^*K\to K$ is a Frobenius coefficient morphism of
[def-trf-frobenius-coefficient-morphism] (no invertibility assumed),
then $\bar\psi$ is a Frobenius coefficient morphism on
$j_!K\in D^b_{ctf}(\bar X,A)$, and its iterates are the extensions of
the iterates of $\psi$:
$$
(\bar\psi)_m=\overline{\psi_m}=j_!\psi_m\circ b_m\qquad(m\geq1).
$$
1. *Stalks.* Let $\bar y$ be a geometric point of $\bar X$ with
$\bar\Phi^m\bar y=\bar y$, and let $\bar v_{\bar y}$, $v_{\bar y}$ be
the induced stalk endomorphisms (through
$(L\bar\Phi^{m*}M)_{\bar y}\cong M_{\bar y}$). If $\bar y$ lies in
$X$, then $(j_!K)_{\bar y}=K_{\bar y}$ and $\bar v_{\bar y}=v_{\bar y}$;
otherwise $(j_!K)_{\bar y}=0$.
1. *Global operators.* For the graph correspondences
$c=(\operatorname{id}_X,\Phi^m)$ and
$\bar c=(\operatorname{id}_{\bar X},\bar\Phi^m)$ of
[def-trf-graph-correspondence], the comparison
$C_{j,K}:R\Gamma_c(X,K)\xrightarrow{\sim}R\Gamma(\bar X,j_!K)$ of
[lem-trf-compactification-cohomology] intertwines the global
operators of [def-trf-global-operator]:
$$
C_{j,K}\circ T_c(v)=T_{\bar c}(\bar v)\circ C_{j,K}.
$$
