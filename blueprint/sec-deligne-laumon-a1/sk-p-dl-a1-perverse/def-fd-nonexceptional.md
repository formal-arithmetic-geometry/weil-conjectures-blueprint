+++
id = "def-fd-nonexceptional"
kind = "definition"
title = "Fourier-nonexceptional middle extension"
order = 3082
uses = ["def-fd-artin-schreier-sheaf", "def-weil-pbc-constructible-complexes", "def-wf-constant-weil-twist", "def-wf-middle-extension"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.IsFourierNonexceptional"]
+++
Let $\psi$ be an additive character of $k_0$, let
$j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion and
let $\mathcal M$ be a lisse Weil sheaf on $U_0$ (in the lisse convention
of [def-weil-pbc-constructible-complexes]). Its middle extension
$j_*\mathcal M$ is *Fourier-nonexceptional* if, after geometric base
change, it is neither a constant sheaf (up to a constant Weil twist,
which does not change the underlying sheaf) nor the Artin–Schreier sheaf
$\mathcal L_{\psi(ax)}$ of [def-fd-artin-schreier-sheaf] for any $a\in k$.
Using $j^*j_*\mathcal M=\mathcal M$, this is the following condition on
$U=U_0\otimes k$: $\mathcal M$ is not geometrically constant (its
underlying sheaf on $U$ is not constant), and for no $a\in k$ is
$\mathcal M$ geometrically irreducible with $\mathcal L_{\psi(ax)}|_U$ as
a geometric constituent (equivalently, $\mathcal M|_U\cong\mathcal
L_{\psi(ax)}|_U$, the Artin–Schreier sheaves being irreducible).
