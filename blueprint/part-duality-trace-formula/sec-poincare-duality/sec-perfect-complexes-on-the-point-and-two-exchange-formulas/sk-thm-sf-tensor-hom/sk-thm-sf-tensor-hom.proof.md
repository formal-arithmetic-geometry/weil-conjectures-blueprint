+++
kind = "proof"
of = "sk-thm-sf-tensor-hom"
uses = ["sk-rem-sf-pf-done", "sk-thm-sf-pf-adic", "sk-thm-sf-pf-field", "sk-thm-sf-pf-proetale", "sk-thm-sf-ctf-stability", "sk-prop-ctf-finite-comparison"]
+++
We check each isomorphism by Yoneda: after applying
$\Hom(N,-)$, the adjunctions and the projection formula turn both sides
into the same Hom group. The only care needed is that the test objects
$N$ lie in the localizing category on which $Rf_!\dashv f^!$ is defined.

We will use the adjunction $Rf_!\dashv f^!$ on the localizing
categories $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ and $\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$, so we first check that the functors in the argument preserve
them. Pullback is exact, preserves direct sums, and carries the
constructible generators to constructible objects by
Proposition [sk-thm-sf-ctf-stability]. Hence it maps $\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$ into
$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$. For the same reasons, tensoring with a fixed
constructible complex preserves the localizing category. In particular,
for $N\in\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$ the objects $f^*N\otimes^{\mathbf L}K$ and
$N\otimes^{\mathbf L}Rf_!K$ lie in $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ and
$\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$, respectively.

The second step of the computation below is the projection formula

$$
Rf_!(f^*N\otimes^{\mathbf L}K)\simeq N\otimes^{\mathbf L}Rf_!K
\qquad(N\in\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))).
$$

For finite coefficients it follows from
Proposition [sk-prop-ctf-finite-comparison] and [Stacks, Tag 0GL5](https://stacks.math.columbia.edu/tag/0GL5), and for
rational coefficients it is Proposition [sk-thm-sf-pf-field].
For integral coefficients we compactify $f=pj$, with $j$ an open
immersion and $p$ proper, and combine
Lemma [sk-thm-sf-pf-adic] with
$j_!(M\otimes^{\mathbf L}j^*N) \simeq j_!M\otimes^{\mathbf L}N$.

By Proposition [sk-thm-sf-ctf-stability], both $\cHom_Y(Rf_!K,L)$ and
$Rf_*\cHom_X(K,f^!L)$ belong to $D^b_{\mathrm{ctf}}(Y,\Lambda)$, so we may test the
comparison map between them by Yoneda inside the full subcategory
$\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$. For every object $N$ of this category the adjunctions and the
projection formula give

$$
\begin{aligned}
\Hom_Y(N,\cHom_Y(Rf_!K,L))
&\simeq\Hom_Y(N\otimes^{\mathbf L}Rf_!K,L)\\
&\simeq\Hom_Y(Rf_!(f^*N\otimes^{\mathbf L}K),L)\\
&\simeq\Hom_X(f^*N\otimes^{\mathbf L}K,f^!L)\\
&\simeq\Hom_Y(N,Rf_*\cHom_X(K,f^!L)).
\end{aligned}
$$

The composite bijection is induced by the comparison map built from
evaluation and the counit, so by Yoneda this map is an isomorphism,
which proves (11.1). Taking $L=\omega_Y$ and
using $f^!\omega_Y=\omega_X$, we get (11.2).
For (11.3), note that both $f^!\mathbb D_YL$ and
$\mathbb D_Xf^*L$ lie in $D^b_{\mathrm{ctf}}(X,\Lambda)$. Since tensoring with
$f^*L$ preserves $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$, we may test on objects $M$
of this category:

$$
\begin{aligned}
\Hom_X(M,f^!\mathbb D_YL)
&\simeq\Hom_Y(Rf_!M,\cHom_Y(L,\omega_Y))\\
&\simeq\Hom_Y(Rf_!M\otimes^{\mathbf L}L,\omega_Y)\\
&\simeq\Hom_X(M\otimes^{\mathbf L}f^*L,f^!\omega_Y)\\
&\simeq\Hom_X(M,\mathbb D_Xf^*L).
\end{aligned}
$$

Again, the bijection is induced by evaluation and the counit, and Yoneda
gives (11.3).

It remains to compare the double-dual maps. For proper $f$ we have
$Rf_!=Rf_*$, and the isomorphism (11.2) is adjoint
to the pairing

$$
Rf_*K\otimes^{\mathbf L}Rf_*\mathbb D_XK
\longrightarrow Rf_*(K\otimes^{\mathbf L}\mathbb D_XK)
\longrightarrow Rf_*\omega_X\longrightarrow\omega_Y.
$$

Using (11.2) for $K$ and for $\mathbb D_XK$, we
view both $Rf_*\delta_K$ and $\delta_{Rf_*K}$ as maps
$Rf_*K\to\mathbb D_YRf_*\mathbb D_XK$. Up to the symmetry of the
tensor product, both are adjoint to this pairing. For
$\delta_{Rf_*K}$ this holds because (11.2) for
$K$ carries evaluation on $Y$ to the pairing. For
$Rf_*\delta_K$ it holds because $\delta_K$ is adjoint to evaluation
on $X$ and (11.2) for $\mathbb D_XK$ is adjoint
to the analogous pairing. Hence the two maps agree.
