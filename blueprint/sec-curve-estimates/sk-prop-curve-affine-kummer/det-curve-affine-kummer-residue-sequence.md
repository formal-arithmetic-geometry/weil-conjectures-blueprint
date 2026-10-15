+++
id = "det-curve-affine-kummer-residue-sequence"
kind = "proposition"
title = "The residue sequence for $\\mu_n$-torsors on a punctured curve"
uses = ["det-curveestimate-canonical-mu", "lem-sc-kummer-exact", "lem-sc-kummer-les", "lem-sc-divisor-class-curve", "lem-sc-pic-proper-decomposition", "thm-av-final", "thm-sc-jacobian-representability", "lem-sc-base-change-curve", "def-sc-field-extension"]
+++
Let $k$ be algebraically closed, $\overline C$ a smooth proper connected
curve of genus $g$ over $k$, $D=\{x_1,\dots,x_r\}$ a set of $r\geq1$ closed
points, $j:U=\overline C\setminus D\hookrightarrow\overline C$, and $n\geq1$
prime to $\operatorname{char}k$.

1. *(Kummer torsors.)* $H^1(U_{\mathrm{ét}},\mu_n)$ is the group of
   isomorphism classes of pairs $(L,\alpha)$ of a line bundle $L$ on $U$ and
   an isomorphism $\alpha:L^{\otimes n}\xrightarrow{\sim}\cO_U$, with group
   law $(L,\alpha)(L',\alpha')=(L\otimes L',\alpha\otimes\alpha')$.
2. *(Residues.)* For such a pair choose a line bundle $\overline L$ on
   $\overline C$ with $\overline L|_U\cong L$, and let $s=\alpha^{-1}(1)$,
   a rational section of $\overline L^{\otimes n}$, regular and nowhere
   vanishing on $U$. Then
   $\partial(L,\alpha):=(\operatorname{ord}_x(s)\bmod n)_{x\in D}\in(\Z/n)^D$
   is independent of the choices and defines a homomorphism $\partial$.
3. *(Exactness.)* The sequence

$$
0\longrightarrow H^1(\overline C,\mu_n)\xrightarrow{\ j^*\ }H^1(U,\mu_n)
\xrightarrow{\ \partial\ }(\Z/n)^D\xrightarrow{\ \sum\ }\Z/n\longrightarrow0
$$

   is exact, and $H^1(U,\mu_n)\cong(\Z/n)^{2g+r-1}$ noncanonically.
4. *(Base change.)* For an extension $k\subseteq k'$ of algebraically closed
   fields the sequence for $(\overline C_{k'},D_{k'})$ receives the pullback
   maps from the sequence for $(\overline C,D)$, with the identity on
   $(\Z/n)^D=(\Z/n)^{D_{k'}}$ and on $\Z/n$; hence the pullback map
   $H^1(U,\mu_n)\to H^1(U_{k'},\mu_n)$ is an isomorphism.
