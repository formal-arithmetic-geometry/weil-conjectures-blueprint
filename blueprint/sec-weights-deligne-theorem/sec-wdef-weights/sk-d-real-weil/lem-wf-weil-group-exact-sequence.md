+++
id = "lem-wf-weil-group-exact-sequence"
kind = "lemma"
title = "Exactness of the Weil-group sequence"
lean = ["MonoidHom.exact_weilGroupDeg"]
order = 3936
uses = ["def-tw-frobenius-action", "def-wf-fundamental-representation", "def-wf-weil-group"]
+++
Let $X_0$ be a geometrically connected separated finite-type
$k_0$-scheme with $X=X_0\times_{k_0}k$, and let $\Phi_X$ be the
geometric Frobenius of [def-tw-frobenius-action]. For the Weil
group
$W(X_0)=\pi_1(X_0,\bar x)\times_{\operatorname{Gal}(k/k_0)} \langle\Phi_X\rangle$ of [def-wf-fundamental-representation] and
its degree map $\deg$ of
[def-wf-weil-group], the map $\deg$ is a surjective group
homomorphism whose kernel is the geometric fundamental group
$\pi_1(X)$, and it sends every lift of $\Phi_X$ to $1$;
equivalently, the sequence

$$
1\longrightarrow\pi_1(X)\longrightarrow W(X_0)
\xrightarrow{\deg}\mathbf Z\longrightarrow0
$$

is exact.
