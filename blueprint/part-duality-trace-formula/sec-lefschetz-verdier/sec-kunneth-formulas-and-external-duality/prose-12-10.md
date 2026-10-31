+++
id = "prose-12-10"
kind = "hidden"
title = "Künneth formulas and external duality (2)"
order = 552
+++
To construct trace classes we identify the sheaf of cohomological
correspondences with $c^!$ of $K\boxtimes\mathbb D_XK$ and then evaluate
on the diagonal. The identification rests on a Künneth formula for
exceptional inverse images, which we now set up.

Let $f_i:X_i\to Y_i$, $i=1,2$, be morphisms of separated $k$-schemes of
finite type. For $M_i\in D^b_{\mathrm{ctf}}(X_i,A)$, using base change for compact
supports and the projection formula, we obtain the Künneth isomorphism

$$
R(f_1\times f_2)_!(M_1\boxtimes M_2)
\simeq Rf_{1!}M_1\boxtimes Rf_{2!}M_2.
$$

For the structure maps it reads
$R\Gamma_c(X_1\times X_2,M_1\boxtimes M_2)\simeq R\Gamma_c(X_1,M_1)\otimes^{\mathbf L} R\Gamma_c(X_2,M_2)$.
For $L_i\in D^b_{\mathrm{ctf}}(Y_i,A)$ let

$$
\alpha:f_1^!L_1\boxtimes f_2^!L_2\longrightarrow
(f_1\times f_2)^!(L_1\boxtimes L_2)
$$

be the morphism adjoint, under $R(f_1\times f_2)_!\dashv(f_1\times f_2)^!$,
to the composite

$$
\begin{aligned}
R(f_1\times f_2)_!(f_1^!L_1\boxtimes f_2^!L_2)
&\simeq Rf_{1!}f_1^!L_1\boxtimes Rf_{2!}f_2^!L_2\\
&\xrightarrow{\varepsilon_{f_1}\boxtimes\varepsilon_{f_2}}
L_1\boxtimes L_2,
\end{aligned}
$$

where $\varepsilon_{f_i}$ is the counit of $Rf_{i!}\dashv f_i^!$.
