+++
id = "thm-pur-general-admissibility"
kind = "theorem"
title = "Preservation for an affine base, modulo the open-complement condition"
order = 2886
uses = ["cor-pur-smooth-admissibility", "def-exc-open-complement-bound", "def-pur-conventions", "def-sbc-affine-space", "def-weil-ambient-exceptional-adjoint", "def-weil-constructible-intervals", "def-weil-exceptional-adjoint-admissibility", "def-weil-exceptional-inverse-image", "def-weil-finite-tor-amplitude", "def-weil-scheme-morphism-properties", "lem-exc-closed-ambient", "lem-exc-closed-amplitude", "prop-exc-closed-tor", "prop-exc-open-adjoint", "thm-exc-explicit-preservation", "thm-sf-ambient-adjoint-class"]
+++
In the purity conventions of this chapter ([def-pur-conventions] fixed setting),
let $f:X\to Y$ be a
separated finite-type
morphism. The ambient exceptional right adjoint datum of
[def-weil-ambient-exceptional-adjoint] is not assumed (it is false in
general): the right adjoints $Rf^{\times}$, $R(\pi_U)^{\times}$,
$R(i_U)^{\times}$ that the proof forms are the right adjoints relative to the
bounded-below objects of étale origin of [thm-sf-ambient-adjoint-class], and
on bounded constructible coefficients they are the finite-stage exceptional
inverse images $Rf^!$, $R\pi_U^!$, $Ri_U^!$ of
[def-weil-exceptional-inverse-image]. Cover $Y$ by finitely
many affine opens $V\subseteq Y$; for each $V$, $f^{-1}(V)$ is
covered by finitely many affine opens $U\subseteq f^{-1}(V)$, and each
$U\to V$ is affine of finite type, hence a closed subscheme of
$\mathbf A^{d_U}_V$ for some $d_U\in\mathbf Z_{\geq0}$, with open
complement $W_U=\mathbf A^{d_U}_V\setminus U$ in the
[def-sbc-affine-space] affine space. Assume the open-complement
condition of [def-exc-open-complement-bound] for every pair
$(W_U,\mathbf A^{d_U}_V)$ over the finitely many charts, with constants
$c_U$, and put $D=\max_U d_U$ and
$c=\max_U\bigl(c_U+1+2(D-d_U)\bigr)$. Then $Rf^!$
satisfies the analogues of the two preservation clauses of
[def-weil-exceptional-adjoint-admissibility]:

1. for all integers $a\leq b$,
$$
L\in D_c^{[a,b]}(Y,A)\quad\Longrightarrow\quad
Rf^!L\in D_c^{[a-2D,b-2D+c]}(X,A);
$$
1. if $K\in D^b_{ctf}(Y,A)$ has
finite Tor amplitude in
$[a,b]$, then $Rf^!K$ has finite Tor amplitude in
$[a-2D,b-2D+c]$; in particular $Rf^!$ carries
$D^b_{ctf}(Y,A)$ into $D^b_{ctf}(X,A)$.
