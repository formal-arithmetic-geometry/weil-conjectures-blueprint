+++
id = "lem-rp-hc2-eigenvalue-determinant-weight"
kind = "lemma"
title = "Eigenvalues of $H_c^2$ are determinant weights"
order = 3000
uses = ["cor-mg-rankone-weight-from-element", "def-real-weil-representation-operations", "def-weil-punctual-weights", "def-wf-determinantal-weight", "def-wf-tate-twist", "def-wf-weil-category", "def-wf-weil-group", "lem-a1-affine-hc2", "lem-tw-tate-twist-weight-shift", "lem-wf-determinantal-weight-exists", "p-real-operations"]
+++
Let $U_0$ be a smooth geometrically connected affine curve, let
$U=U_0\times_{k_0}k$, and let $\mathcal G_0$ be a lisse
Weil sheaf on $U_0$ with local
generic fiber $V$, with the geometric Frobenius $F$ acting on
$H_c^2(U,\mathcal G)$ (the Weil structure on the identified module
$V_{\pi_1(U)}(-1)$ of [lem-a1-affine-hc2], the
Tate twist $(-1)$). If
$\alpha$ is an eigenvalue of $F$ on
$H_c^2(U,\mathcal G)$, then

$$
\frac{\log\bigl(|\iota(\alpha q^{-1})|^2\bigr)}{\log(q)}
$$

is a determinant weight of $\mathcal G_0$.
