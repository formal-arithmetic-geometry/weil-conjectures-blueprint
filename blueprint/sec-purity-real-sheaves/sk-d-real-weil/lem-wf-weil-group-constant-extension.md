+++
id = "lem-wf-weil-group-constant-extension"
kind = "lemma"
title = "Weil group after a finite constant-field extension"
order = 2882
uses = ["def-tw-frobenius-action", "def-weil-finite-field-fiber", "def-weil-pbc-scheme-conventions", "def-wf-weil-group", "lem-wf-weil-group-exact-sequence"]
+++
Let $X_0$ be a
separated finite-type
$\mathbf F_q$-scheme with geometrically connected fibre
$X=X_0\times_{\mathbf F_q}\overline{\mathbf F}_q$. For $m\geq1$,
put

$$
X_0^{(m)}=X_0\times_{\mathbf F_q}\mathbf F_{q^m}
$$

and regard it as an $\mathbf F_{q^m}$-scheme. Under the natural map to
$X_0$, its Weil group identifies with

$$
W(X_0^{(m)})
\xrightarrow{\;\sim\;}
W(X_0)^{[m]}:=\deg^{-1}(m\mathbf Z)\subseteq W(X_0).
$$

Its geometric subgroup is still $\pi_1(X)$, and its normalized degree is

$$
\deg_{\mathbf F_{q^m}}(w)=\deg_{\mathbf F_q}(w)/m.
$$

In particular, if $s\in W(X_0)$ has degree one, then $s^m$ has degree
one for the $\mathbf F_{q^m}$-Weil group.
