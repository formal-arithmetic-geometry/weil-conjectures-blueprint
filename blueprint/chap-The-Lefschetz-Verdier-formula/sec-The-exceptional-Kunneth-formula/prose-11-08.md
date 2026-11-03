+++
id = "prose-11-08"
kind = "hidden"
title = "The exceptional Künneth formula (1)"
order = 900
+++
A cohomological correspondence $u:c_2^*K\to c_1^!K$ is a morphism on
$C$. To obtain from it a class on the fixed locus, we must first view
it as a section of $c^!$ of a single complex on $X\times X$, which can
then be restricted to the diagonal. In linear algebra this is the
identification $\operatorname{Hom}(V,W)=W\otimes V^\vee$, under which
the trace becomes evaluation. Its sheaf version is the isomorphism
$\cHom(p_2^*K,p_1^!K)\simeq K\boxtimes\mathbb D_XK$ of
Lemma [lemma-external-duality-trace-morphism]. Here $p_1,p_2:X\times X\to X$
are the projections and $M\boxtimes N=p_1^*M\otimes^{\mathbf L} p_2^*N$ is the
external tensor product in $D((X\times X)_{\mathrm{pro}\acute{e}t},A)$. Applying $c^!$ to it, we obtain
$\cHom(c_2^*K,c_1^!K)$. On the point the isomorphism is exactly
$\operatorname{Hom}(V,V)=V\otimes V^\vee$.

The isomorphism comes from Künneth formulas for $Rf_!$, $Rf_*$, $f^!$,
$\cHom$ and Verdier duals. For $Rf_!$ the formula follows directly from
base change for compact supports and the projection formula. For
ordinary direct images it follows from smooth and proper base change
(Proposition [proposition-ordinary-external-kunneth], Section [sec-The-Kunneth-formula]).
The formula for $f^!$
(Proposition [proposition-exceptional-external-kunneth]) needs a
dévissage on the coefficients, starting from constant coefficients,
where for smooth $f$ the functor $f^!$ is a twist and a shift.

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
