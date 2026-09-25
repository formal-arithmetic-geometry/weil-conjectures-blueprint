+++
id = "lem-wf-invariant-character-extension"
kind = "lemma"
title = "Extending an invariant geometric character"
order = 2852
uses = ["def-wf-algebraic-character", "def-wf-arithmetic-monodromy-extension", "def-wf-geometric-monodromy-group", "def-wf-weil-group", "lem-wf-weil-group-constant-extension", "lem-wf-weil-group-exact-sequence"]
+++
Let $X_0$ be normal and geometrically connected, let
$H=H_{\mathrm{geom}}$, choose a degree-one element
$s\in W(X_0)$, and put
$\alpha(h)=\rho(s)h\rho(s)^{-1}$. If an algebraic character
$\chi:H\to\mathbf G_m$ satisfies $\chi\circ\alpha^m=\chi$ for
some $m>0$, then $\chi\circ\rho|_{\pi_1(X)}$ extends to a
rank-one character of the Weil group after replacing
$k_0=\mathbf F_q$ by $k_m=\mathbf F_{q^m}$.

## Proof

Here $H$ is the geometric Zariski closure of
[def-wf-geometric-monodromy-group], and $\chi$ is a regular
group homomorphism as in [def-wf-algebraic-character].
By [lem-wf-weil-group-constant-extension], the Weil group over
$k_m$ identifies with

$$
W_m:=\{w\in W(X_0):\deg(w)\in m\mathbf Z\};
$$

its geometric kernel is still $\pi_1(X)$, while its normalized
degree is $\deg_{k_m}(w)=\deg(w)/m$. The exact sequence
in [def-wf-weil-group], exact by
[lem-wf-weil-group-exact-sequence], then gives every member of
$W_m$ a unique form
$\gamma s^{ma}$, with $\gamma\in\pi_1(X)$ and $a\in\mathbf Z$.
Define

$$
\widetilde\chi(\gamma s^{ma})=\chi(\rho(\gamma)).
$$

This is well defined by uniqueness of the displayed form. To check
multiplication, write $w_1=\gamma s^{ma}$ and
$w_2=\delta s^{mb}$. The semidirect-product calculation of
[def-wf-arithmetic-monodromy-extension] gives

$$
\rho\bigl(\gamma(s^{ma}\delta s^{-ma})\bigr)
=\rho(\gamma)\alpha^{ma}(\rho(\delta)).
$$

Therefore, using $\chi\circ\alpha^m=\chi$,

$$
\begin{aligned}
\widetilde\chi(w_1w_2)
&=\chi\bigl(\rho(\gamma)\alpha^{ma}(\rho(\delta))\bigr)\\
&=\chi(\rho(\gamma))\chi(\rho(\delta))
=\widetilde\chi(w_1)\widetilde\chi(w_2).
\end{aligned}
$$

It is continuous because its restriction to the open degree-zero
subgroup is the continuous map $\chi\circ\rho$, and each degree
component is its translate. Finally its restriction to
$\pi_1(X)$ is exactly $\chi\circ\rho|_{\pi_1(X)}$, which proves
the assertion.

We may, and do, take the target to be a finite coefficient field.
Indeed the lisse representation is defined over some finite
$E_0/\mathbf Q_\ell$, while the regular map $\chi$ and the finitely
many equations used to define the chosen weight space have coefficients
in a finite extension $E_1/\mathbf Q_\ell$. After replacing them by
the compositum $E=E_0E_1$, all values of
$\chi(\rho(\gamma))$ lie in $E^\times$, and the extended character
$\widetilde\chi$ is $E^\times$-valued.
