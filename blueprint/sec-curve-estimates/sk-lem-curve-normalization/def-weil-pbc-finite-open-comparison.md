+++
id = "def-weil-pbc-finite-open-comparison"
kind = "definition"
title = "Finite-open comparison map"
lean = ["AlgebraicGeometry.Etale.finiteOpenComparison"]
order = 1484
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions", "def-weil-pbc-underived-exchange", "lemma-weil-pbc-finite-exchange"]
+++
Consider a Cartesian square

$$
\begin{CD}
U @>{j_X}>> X\\
@V{v}VV @VV{\bar v}V\\
V @>{j_Y}>> Y
\end{CD}
$$

with $j_X,j_Y$ open immersions and $\bar v$ finite. Let $\mathcal A$ be a
Grothendieck abelian coefficient category as in
[lemma-weil-pbc-finite-exchange] (concrete, with forgetful functor reflecting
isomorphisms, preserving filtered colimits and compatible with
sheafification; for instance abelian groups or $\Lambda$-modules). For an
$\mathcal A$-valued sheaf $G$ on $U_{\mathrm{et}}$, define

$$
\beta_{\bar v,j_Y,G}:(j_Y)_!v_*G\longrightarrow
\bar v_*(j_X)_!G
$$

as the morphism adjoint to

$$
v_*G\xrightarrow{\sim}
j_Y^{-1}\bar v_*(j_X)_!G.
$$

The displayed isomorphism is $v_*$ of the unit isomorphism
$G\xrightarrow{\sim}j_X^{-1}(j_X)_!G$, followed by the inverse of the finite
base change isomorphism $j_Y^{-1}\bar v_*\cong v_*j_X^{-1}$ of
[lemma-weil-pbc-finite-exchange]. The construction is natural in $G$, so
$\beta$ is a natural transformation $(j_Y)_!v_*\to\bar v_*(j_X)_!$.
