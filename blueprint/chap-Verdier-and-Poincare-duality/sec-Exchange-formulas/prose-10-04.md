+++
id = "prose-10-04"
kind = "hidden"
title = "Exchange formulas (3)"
order = 829
+++
On the geometric point we have $\href{@definition-verdier-dual-evaluation}{\omega_s}=\Lambda_s$, so [$\delta$](@definition-verdier-dual-evaluation) is the
evaluation map of Lemma [lemma-perfect-complexes-geometric-point].

The proof of [biduality](@theorem-verdier-biduality) uses only the [exchange formulas](@lemma-internal-adjunction-two-exchange-formulas) that follow from
adjunctions. We first write down the comparison maps. Let $f:X\to Y$
be a morphism, $K\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(X,\Lambda)}$ and $L\in \href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Y,\Lambda)}$. The
map

$$
Rf_*\cHom_X(K,\href{@theorem-existence-exceptional-inverse-image}{f^!L})\longrightarrow\cHom_Y(\href{@proposition-construction-independence-rf-shriek}{Rf_!K},L)
\tag{10.1}
$$

is the tensor–Hom adjoint of the composite

$$
\begin{aligned}
Rf_*\cHom_X(K,\href{@theorem-existence-exceptional-inverse-image}{f^!L})\otimes^{\mathbf L}\href{@proposition-construction-independence-rf-shriek}{Rf_!K}
&\simeq \href{@proposition-construction-independence-rf-shriek}{Rf_!}\bigl(f^*Rf_*\cHom_X(K,\href{@theorem-existence-exceptional-inverse-image}{f^!L})\otimes^{\mathbf L}K\bigr)\\
&\longrightarrow \href{@proposition-construction-independence-rf-shriek}{Rf_!}\bigl(\cHom_X(K,\href{@theorem-existence-exceptional-inverse-image}{f^!L})\otimes^{\mathbf L}K\bigr)
\longrightarrow \href{@proposition-construction-independence-rf-shriek}{Rf_!}\href{@theorem-existence-exceptional-inverse-image}{f^!L}\xrightarrow{\varepsilon_f}L
\end{aligned}
$$

of the projection formula, the counit of $f^*\dashv Rf_*$, evaluation
and the counit $\varepsilon_f$ of $\href{@proposition-construction-independence-rf-shriek}{Rf_!}\dashv \href{@theorem-existence-exceptional-inverse-image}{f^!}$. In particular, for $L=\href{@definition-verdier-dual-evaluation}{\omega_Y}$, using $\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@definition-verdier-dual-evaluation}{\omega_Y}=\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@theorem-existence-exceptional-inverse-image}{a_Y^!\Lambda_s}=\href{@definition-verdier-dual-evaluation}{\omega_X}$, it is a map
$Rf_*\href{@definition-verdier-dual-evaluation}{\mathbb D_XK}\to\href{@definition-verdier-dual-evaluation}{\mathbb D_Y}\href{@proposition-construction-independence-rf-shriek}{Rf_!K}$. The map
$\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@definition-verdier-dual-evaluation}{\mathbb D_YL}\to\href{@definition-verdier-dual-evaluation}{\mathbb D_X}f^*L$ is the tensor–Hom adjoint of the
map $\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@definition-verdier-dual-evaluation}{\mathbb D_YL}\otimes^{\mathbf L}f^*L\to \href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@definition-verdier-dual-evaluation}{\omega_Y}=\href{@definition-verdier-dual-evaluation}{\omega_X}$
that corresponds under $\href{@proposition-construction-independence-rf-shriek}{Rf_!}\dashv \href{@theorem-existence-exceptional-inverse-image}{f^!}$ to

$$
\href{@proposition-construction-independence-rf-shriek}{Rf_!}(\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@definition-verdier-dual-evaluation}{\mathbb D_YL}\otimes^{\mathbf L}f^*L)
\simeq \href{@proposition-construction-independence-rf-shriek}{Rf_!}\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@definition-verdier-dual-evaluation}{\mathbb D_YL}\otimes^{\mathbf L}L
\xrightarrow{\varepsilon_f\otimes1}\href{@definition-verdier-dual-evaluation}{\mathbb D_YL}\otimes^{\mathbf L}L
\longrightarrow\href{@definition-verdier-dual-evaluation}{\omega_Y},
$$

the last arrow being evaluation.
