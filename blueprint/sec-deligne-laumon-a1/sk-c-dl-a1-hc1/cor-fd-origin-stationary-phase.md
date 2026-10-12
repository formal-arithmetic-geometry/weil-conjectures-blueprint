+++
id = "cor-fd-origin-stationary-phase"
kind = "theorem"
title = "The origin fiber is the stationary-phase contribution"
order = 3119
tags = ["latex:corollary"]
uses = ["def-fd-nonexceptional", "def-fd-transform", "def-weil-ordinary-compact-cohomology", "def-wf-middle-extension", "lem-a1-unramified-nonexceptional", "lem-fd-stalk-at-origin", "lem-wf-boundary-stalk-invariants", "prop-a1-fourier-middle-extension"]
lean = ["AlgebraicGeometry.LAdicWeilSheaf.LisseOnDenseOpen.nonempty_equiv_stalk_origin_of_isFourierPartner"]
+++
Let $\psi$ be an additive character of $k_0$, let
$j:U_0\hookrightarrow\mathbf A^1_{k_0}$ and
$j':U'_0\hookrightarrow A'_0$ be dense open immersions into
the line and the dual line, and let $\mathcal M$ and $\mathcal M'$ be
lisse Weil sheaves on $U_0$ and $U'_0$ whose middle extensions
correspond under the Fourier transform of [def-fd-transform]:
$\operatorname{FT}_\psi(j_{!*}\mathcal M[1])\cong j'_{!*}\mathcal M'[1]$,
i.e. $\operatorname{FT}_\psi((j_*\mathcal M)[1])\cong(j'_*\mathcal M')[1]$.
Then the degree $-1$ part of the fiber at
the origin of the dual line is the $H_c^1$-term of the local Fourier
exact sequence at the origin:

$$
\mathcal H^{-1}\Bigl(\operatorname{FT}_\psi(j_{!*}\mathcal M[1])_{0'}\Bigr)
\cong H_c^1(\mathbf A^1_{k_0},j_*\mathcal M)\;\cong\;(j'_*\mathcal M')_{0'}\;=\;\bigl(\mathcal M'_{\bar\eta}\bigr)^{I_{0'}},
$$

the last identification being the invariants of the local inertia
$I_{0'}$ at the origin of the dual line (trivial if $0'\in U'_0$): the
stationary phase term is therefore the origin part of the transformed
middle extension. Moreover $H_c^2(\mathbf A^1_{k_0},j_*\mathcal M)=0$.
All these identifications are *Frobenius-equivariant*: the origin $0'$
is a $k_0$-rational point, and the geometric Frobenius of $k_0$ acting
on $H_c^1(\mathbf A^1_{k_0},j_*\mathcal M)$ corresponds to the local
Frobenius $F_{0'}$ on the stalk $(j'_*\mathcal M')_{0'}$ of the Weil
sheaf $j'_*\mathcal M'$, and to the action of a Frobenius lift on
$(\mathcal M'_{\bar\eta})^{I_{0'}}$.
