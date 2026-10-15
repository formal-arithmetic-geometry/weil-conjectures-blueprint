+++
id = "thm-sc-constant-invariance"
kind = "theorem"
title = "Base-change invariance for constant sheaves"
order = 1039
uses = ["def-sc-curves", "def-sc-field-extension", "def-sc-genus", "lem-sc-base-change-curve", "lem-sc-brauer-zero", "lem-sc-cohomological-dimension", "lem-sc-compactification", "lem-sc-genus-invariant", "lem-sc-kummer-les", "lem-sc-pic-affine", "lem-sc-pic-proper-ntorsion", "lem-sc-primitive-root", "thm-av-final", "thm-sc-jacobian-representability", "thm-sc-proper-cohomology"]
+++
Let $k\subseteq k'$ be algebraically closed, let $C$ be a
smooth separated connected curve over $k$, let
$\overline C$ be a compactification of $C$
([lem-sc-compactification]; thus $\overline C=C$ when $C$
is proper), and let
$g:=g(\overline C)$ ([def-sc-genus]). Let $n\geq1$ be
prime to $\operatorname{char}k$.
For every $q\geq0$, the pullback map of
[def-sc-field-extension]

$$
\rho^q_{k'/k}(C,\mathbf F_n):H^q(C_{\Et},\mathbf F_n)
\longrightarrow H^q((C_{k'})_{\Et},\mathbf F_n)
$$

is an isomorphism; if $C$ is proper it is compatible with the
identifications of [lem-sc-pic-proper-ntorsion] and
[lem-sc-genus-invariant], and if $C$ is affine with the
identifications of [lem-sc-pic-affine].
