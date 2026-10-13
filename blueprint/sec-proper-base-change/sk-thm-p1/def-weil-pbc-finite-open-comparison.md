+++
id = "def-weil-pbc-finite-open-comparison"
kind = "definition"
title = "Finite-open comparison map"
order = 1241
uses = ["def-weil-pbc-cartesian-square", "def-weil-pbc-extension-by-zero", "def-weil-pbc-scheme-conventions", "def-weil-pbc-underived-exchange"]
+++
Consider a Cartesian square

$$
\begin{CD}
U @>{j_X}>> X\\
@V{v}VV @VV{\bar v}V\\
V @>{j_Y}>> Y
\end{CD}
$$

with $j_X,j_Y$ open immersions and $\bar v$ finite. For an abelian sheaf
$G$ on $U_{\mathrm{et}}$, define

$$
\beta_{\bar v,j_Y,G}:(j_Y)_!v_*G\longrightarrow
\bar v_*(j_X)_!G
$$

as the morphism adjoint to

$$
v_*G\xrightarrow{\sim}
j_Y^{-1}\bar v_*(j_X)_!G.
$$

The displayed isomorphism is finite base change
$j_Y^{-1}\bar v_*\cong v_*j_X^{-1}$ followed by
$j_X^{-1}(j_X)_!G\cong G$.
