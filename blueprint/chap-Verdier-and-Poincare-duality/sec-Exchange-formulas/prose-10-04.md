+++
id = "prose-10-04"
kind = "hidden"
title = "Exchange formulas (3)"
order = 822
+++
On the geometric point we have $\omega_s=\Lambda_s$, so $\delta$ is the
evaluation map of Lemma [lemma-perfect-complexes-geometric-point].

The proof of biduality uses only the exchange formulas that follow from
adjunctions. We first write down the comparison maps. Let $f:X\to Y$
be a morphism, $K\in D^b_{\mathrm{ctf}}(X,\Lambda)$ and $L\in D^b_{\mathrm{ctf}}(Y,\Lambda)$. The
map

$$
Rf_*\cHom_X(K,f^!L)\longrightarrow\cHom_Y(Rf_!K,L)
\tag{10.1}
$$

is the tensor–Hom adjoint of the composite

$$
\begin{aligned}
Rf_*\cHom_X(K,f^!L)\otimes^{\mathbf L}Rf_!K
&\simeq Rf_!\bigl(f^*Rf_*\cHom_X(K,f^!L)\otimes^{\mathbf L}K\bigr)\\
&\longrightarrow Rf_!\bigl(\cHom_X(K,f^!L)\otimes^{\mathbf L}K\bigr)
\longrightarrow Rf_!f^!L\xrightarrow{\varepsilon_f}L
\end{aligned}
$$

of the projection formula, the counit of $f^*\dashv Rf_*$, evaluation
and the counit $\varepsilon_f$ of $Rf_!\dashv f^!$. For $L=\omega_Y$,
using $f^!\omega_Y=f^!a_Y^!\Lambda_s=\omega_X$, it is a map
$Rf_*\mathbb D_XK\to\mathbb D_YRf_!K$. The map
$f^!\mathbb D_YL\to\mathbb D_Xf^*L$ is the tensor–Hom adjoint of the
map $f^!\mathbb D_YL\otimes^{\mathbf L}f^*L\to f^!\omega_Y=\omega_X$
that corresponds under $Rf_!\dashv f^!$ to

$$
Rf_!(f^!\mathbb D_YL\otimes^{\mathbf L}f^*L)
\simeq Rf_!f^!\mathbb D_YL\otimes^{\mathbf L}L
\xrightarrow{\varepsilon_f\otimes1}\mathbb D_YL\otimes^{\mathbf L}L
\longrightarrow\omega_Y,
$$

the last arrow being evaluation.
