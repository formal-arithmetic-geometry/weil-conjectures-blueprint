+++
id = "def-fd-nonexceptional"
kind = "definition"
title = "Fourier-nonexceptional middle extension"
order = 3999
uses = ["def-fd-artin-schreier-sheaf", "sk-lem-coefficient-heart", "sk-def-sf-weil-complexes", "def-wf-constant-weil-twist", "def-wf-middle-extension"]
lean = ["AlgebraicGeometry.WeilSheaf.LisseOnDenseOpen.IsFourierNonexceptional"]
+++
Let $\psi$ be an additive character of $k_0$, let
$j:U_0\hookrightarrow\mathbf A^1_{k_0}$ be a dense open immersion and
let $\mathcal M$ be a lisse Weil sheaf on $U_0$: a lisse
$\overline{\mathbf Q}_{\ell,U}$-module on $U_{\mathrm{proét}}$ ([sk-lem-coefficient-heart]) with a
Weil structure ([sk-def-sf-weil-complexes]). Its middle extension
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
