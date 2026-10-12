+++
id = "cor-wf-rank-one-degree-factorization-curve"
kind = "theorem"
title = "Finite-order part times a degree character"
order = 2873
tags = ["latex:corollary"]
uses = ["d-ab-rankone", "d-monodromy", "def-weil-pbc-scheme-conventions", "def-wf-weil-group", "lem-wf-weil-group-exact-sequence"]
+++
Let $U_0/\mathbf F_q$ be normal, geometrically connected,
separated and of finite type, pure of dimension one; put
$U=U_0\times_{\mathbf F_q}\overline{\mathbf F}_q$ and
$\Pi=\pi_1(U,\bar u)$; let $\ell\nmid q$, let $E/\mathbf Q_\ell$ be finite, and let
$\chi:\hyperref[def-wf-weil-group]{W(U_0,\bar u)}\to E^\times$ be a
continuous character with finite geometric image $\chi(\Pi)$. Choose $s$ with $\deg(s)=1$ and put
$c=\chi(s)$. Then $(W(U_0,\bar u),\deg,s)$ is a degree datum in the sense
of [d-monodromy] with $P=\Pi$, and for it the function
$\varepsilon=\chi_{\mathrm{fin}}$ of [d-ab-rankone] (with $\gamma=s$ and
$z=c$), namely $\varepsilon(w)=\chi(w)c^{-\deg(w)}$, is a finite-order
character $\varepsilon:W(U_0,\bar u)\to E^\times$ with
$\varepsilon(s)=1$, $\varepsilon(W(U_0,\bar u))=\chi(\Pi)$, and

$$
\chi(w)=\varepsilon(w)c^{\deg(w)}
\qquad(w\in W(U_0,\bar u)).
$$

The scheme and Weil-group conventions are those of
[def-weil-pbc-scheme-conventions], [def-wf-weil-group].
