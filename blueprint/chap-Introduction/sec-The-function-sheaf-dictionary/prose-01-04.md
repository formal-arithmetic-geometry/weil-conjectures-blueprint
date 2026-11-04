+++
id = "prose-01-04"
kind = "hidden"
title = "The function–sheaf dictionary"
order = 9
+++
The proof of purity does not treat one variety at a time. It cuts a
variety into pieces and fibres it over other varieties, and point counts
behave simply under both operations. If $Z_0\subset X_0$ is closed with
complement $U_0$, then $\#X_0(\mathbf F_q)=\#U_0(\mathbf F_q)+\#Z_0(\mathbf F_q)$,
and for a morphism $f:X_0\to Y_0$,

$$
\#X_0(\mathbf F_q)=\sum_{y\in Y_0(\mathbf F_q)}\#f^{-1}(y)(\mathbf F_q).
$$

On the right we sum a function on $Y_0$ that is not constant. To follow
such sums with cohomology, we replace functions by sheaves.

The sheaves in question are *constructible*: there is a decomposition
of $X$ into finitely many locally closed pieces on each of which the sheaf
is locally constant with finite stalks. After passing to the limit, the
stalks are finite-dimensional $\mathbf Q_\ell$-vector spaces instead. A *Frobenius
structure* on a constructible sheaf $K$ on $X$ is an isomorphism
$F^*K\simeq K$, and a sheaf with a Frobenius structure is a *Weil
sheaf*. The same definitions apply to complexes of sheaves
(Section [sec-Weil-complexes]). Let $x$ be a point of $X_0$ over
$\mathbf F_{q^m}$. The corresponding point $\bar x$ of $X$ is fixed by $F^m$,
so the stalk of $(F^m)^*K$ at $\bar x$ is $K_{\bar x}$. Iterating the
Frobenius structure gives an isomorphism $(F^m)^*K\simeq K$, and on the
stalk at $\bar x$ it becomes an endomorphism $\operatorname{Frob}_x$ of
$K_{\bar x}$. Its trace defines the *trace function*

$$
t_K:X_0(\mathbf F_{q^m})\longrightarrow\mathbf Q_\ell,\qquad x\longmapsto
\operatorname{Tr}(\operatorname{Frob}_x\mid K_{\bar x}),
$$

where for a complex the trace is the alternating sum of the traces on the
cohomology groups. The constant sheaf has trace function $1$.

Operations on functions correspond to operations on sheaves. For example, pulling back
a function along $f$ corresponds to the inverse image $f^*K$, and the
product of two functions to the tensor product. Similarly, summing a function over
the fibres of $f$ corresponds to the direct image with compact supports
$Rf_!K$, whose stalk at a point $\bar y$ is the compactly supported
cohomology of $K$ on the fibre over $\bar y$. The resulting identity
$t_{Rf_!K}(y)=\sum_{f(x)=y}t_K(x)$ is a form of the trace formula
(Corollary [corollary-trace-functions-direct-image-compact]). When $f$ is the
map to a point, it is (b) with coefficients in $K$. The one further operation
we need is a Fourier transform, explained in Section [sec-The-Deligne-Laumon-theorem].
This correspondence between functions and sheaves is Grothendieck's
*function–sheaf dictionary* [sga4-5, Sommes trig.]:

| functions on $X_0(\mathbf F_{q^m})$ | Weil complexes on $X$ |
|---|---|
| $t\mapsto t\circ g$ | $g^*K$ |
| $t\cdot t'$ | $K\otimes^{\mathbf L}L$ |
| $t\mapsto\bigl(y\mapsto\sum_{f(x)=y}t(x)\bigr)$ | $Rf_!K$ |
| $t=t|_{U}+t|_{Z}$ | $j_!j^*K\to K\to i_*i^*K\to$ |
| $\sum_xt(x)$ | $R\Gamma_c(X,K)$ with its Frobenius |
| $t\mapsto\bigl(y\mapsto-\sum_xt(x)\psi(\operatorname{Tr}_{\mathbf F_{q^m}/\mathbf F_q}(xy))\bigr)$ | $Rp_{2!}(p_1^*K\otimes\mathcal K_\psi)[1]$ |

Proposition [proposition-function-sheaf-dictionary] states and proves the
first five lines. The last line is built from the first three, as we explain
in Section [sec-The-Deligne-Laumon-theorem]. Since $Rf_!$ of a sheaf is a
complex, we work in derived categories throughout.
