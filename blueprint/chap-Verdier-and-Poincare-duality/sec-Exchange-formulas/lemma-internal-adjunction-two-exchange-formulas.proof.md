+++
kind = "proof"
of = "lemma-internal-adjunction-two-exchange-formulas"
order = 831
uses = ["proposition-exact-products", "proposition-milnor-sequence", "definition-lisse-sheaves", "proposition-inverting-ell", "definition-pro-etale-base-change-map", "definition-projection-formula-map", "proposition-composition-base-change-rf-shriek", "proposition-forgetting-supports-composition", "lemma-extension-scalars-preserves-dctf", "lemma-change-coefficients-direct-image", "proposition-six-operations-change-coefficients"]
+++
We check each isomorphism by Yoneda. After applying
$\Hom(N,-)$, we identify both sides with the same Hom group by the
adjunctions and the projection formula. We only have to make sure that the test objects
$N$ lie in the [localizing category](@definition-localizing-subcategory) on which $\href{@proposition-construction-independence-rf-shriek}{Rf_!}\dashv \href{@theorem-existence-exceptional-inverse-image}{f^!}$ is defined.

The adjunction $\href{@proposition-construction-independence-rf-shriek}{Rf_!}\dashv \href{@theorem-existence-exceptional-inverse-image}{f^!}$ lives on the [localizing
categories](@definition-localizing-subcategory) [$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$](@definition-localizing-subcategory) and [$\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$](@definition-localizing-subcategory), and the functors in the argument preserve
them. Indeed, pullback is exact, preserves direct sums, and carries the [constructible](@definition-constructible-sheaves) generators to [constructible](@definition-constructible-sheaves) objects by
Proposition [proposition-six-operations-dctf], so it maps [$\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$](@definition-localizing-subcategory) into
[$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$](@definition-localizing-subcategory). For the same reasons, tensoring with a fixed [constructible complex](@definition-constructible-sheaves) preserves the [localizing category](@definition-localizing-subcategory). In particular,
for $N\in\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Y,\Lambda)})$ the objects $f^*N\otimes^{\mathbf L}K$ and
$N\otimes^{\mathbf L}\href{@proposition-construction-independence-rf-shriek}{Rf_!K}$ lie in [$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$](@definition-localizing-subcategory) and
[$\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$](@definition-localizing-subcategory), respectively.

The second step of the computation below is the projection formula

$$
\href{@proposition-construction-independence-rf-shriek}{Rf_!(f^*N\otimes^{\mathbf L}K)}\simeq N\otimes^{\mathbf L}\href{@proposition-construction-independence-rf-shriek}{Rf_!K}
\qquad(N\in\href{@definition-localizing-subcategory}{\Loc}(\href{@definition-constructible-sheaves}{D^b_{\mathrm{ctf}}(Y,\Lambda)})).
$$

For finite coefficients it follows from
Proposition [proposition-comparison-etale-derived-category] and [Stacks, [0GL5](https://stacks.math.columbia.edu/tag/0GL5)], and for
rational coefficients it is Proposition [proposition-projection-formula-rational-coefficients].
For integral coefficients we compactify $f=pj$, with $j$ an open
immersion and $p$ proper, and combine
Lemma [lemma-projection-formula-integral-coefficients] with
$j_!(M\otimes^{\mathbf L}j^*N)
 \simeq j_!M\otimes^{\mathbf L}N$.

By Proposition [proposition-six-operations-dctf], both $\cHom_Y(\href{@proposition-construction-independence-rf-shriek}{Rf_!K},L)$ and
$Rf_*\cHom_X(K,\href{@theorem-existence-exceptional-inverse-image}{f^!L})$ belong to [$D^b_{\mathrm{ctf}}(Y,\Lambda)$](@definition-constructible-sheaves), so we may test the
comparison map between them by Yoneda inside the full subcategory
[$\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$](@definition-localizing-subcategory). For every object $N$ of this category we obtain, by the adjunctions and the
projection formula,

$$
\begin{aligned}
\Hom_Y(N,\cHom_Y(\href{@proposition-construction-independence-rf-shriek}{Rf_!K},L))
&\simeq\Hom_Y(N\otimes^{\mathbf L}\href{@proposition-construction-independence-rf-shriek}{Rf_!K},L)\\
&\simeq\Hom_Y(\href{@proposition-construction-independence-rf-shriek}{Rf_!(f^*N\otimes^{\mathbf L}K)},L)\\
&\simeq\Hom_X(f^*N\otimes^{\mathbf L}K,\href{@theorem-existence-exceptional-inverse-image}{f^!L})\\
&\simeq\Hom_Y(N,Rf_*\cHom_X(K,\href{@theorem-existence-exceptional-inverse-image}{f^!L})).
\end{aligned}
$$

The composite bijection is induced by the map
(10.1). By Yoneda this map is an isomorphism,
which is (10.2). Taking $L=\href{@definition-verdier-dual-evaluation}{\omega_Y}$ and
using $\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@definition-verdier-dual-evaluation}{\omega_Y}=\href{@definition-verdier-dual-evaluation}{\omega_X}$, we get $e_K$.
For (10.4), on the other hand, note that both $\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@definition-verdier-dual-evaluation}{\mathbb D_YL}$ and
$\href{@definition-verdier-dual-evaluation}{\mathbb D_X}f^*L$ lie in [$D^b_{\mathrm{ctf}}(X,\Lambda)$](@definition-constructible-sheaves). Since tensoring with
$f^*L$ preserves [$\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$](@definition-localizing-subcategory), we may test on objects $M$
of this category:

$$
\begin{aligned}
\Hom_X(M,\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@definition-verdier-dual-evaluation}{\mathbb D_YL})
&\simeq\Hom_Y(\href{@proposition-construction-independence-rf-shriek}{Rf_!M},\cHom_Y(L,\href{@definition-verdier-dual-evaluation}{\omega_Y}))\\
&\simeq\Hom_Y(\href{@proposition-construction-independence-rf-shriek}{Rf_!M}\otimes^{\mathbf L}L,\href{@definition-verdier-dual-evaluation}{\omega_Y})\\
&\simeq\Hom_X(M\otimes^{\mathbf L}f^*L,\href{@theorem-existence-exceptional-inverse-image}{f^!}\href{@definition-verdier-dual-evaluation}{\omega_Y})\\
&\simeq\Hom_X(M,\href{@definition-verdier-dual-evaluation}{\mathbb D_X}f^*L).
\end{aligned}
$$

Again, the bijection is induced by the map defined before the lemma, and by Yoneda
we get (10.4).

The comparison of [double-dual maps](@definition-verdier-dual-evaluation) is used in the proof of [biduality](@theorem-verdier-biduality) for
$f=a_X$, where it identifies $R\Gamma(X,\href{@definition-verdier-dual-evaluation}{\delta_K})$
with the [double-dual map](@definition-verdier-dual-evaluation) of the perfect complex $R\Gamma(X,K)$. Both
maps are determined by pairings, and we compare the pairings.
For proper $f$ we have
$\href{@proposition-construction-independence-rf-shriek}{Rf_!}=Rf_*$, and the isomorphism $e_K$ is adjoint
to the pairing

$$
Rf_*K\otimes^{\mathbf L}Rf_*\href{@definition-verdier-dual-evaluation}{\mathbb D_XK}
\longrightarrow Rf_*(K\otimes^{\mathbf L}\href{@definition-verdier-dual-evaluation}{\mathbb D_XK})
\longrightarrow Rf_*\href{@definition-verdier-dual-evaluation}{\omega_X}\longrightarrow\href{@definition-verdier-dual-evaluation}{\omega_Y}.
$$

Using $e_K$ and $e_{\href{@definition-verdier-dual-evaluation}{\mathbb D_XK}}$, we
view both $Rf_*\href{@definition-verdier-dual-evaluation}{\delta_K}$ and [$\delta_{Rf_*K}$](@definition-verdier-dual-evaluation) as maps
$Rf_*K\to\href{@definition-verdier-dual-evaluation}{\mathbb D_Y}Rf_*\href{@definition-verdier-dual-evaluation}{\mathbb D_XK}$. Up to the symmetry of the
tensor product, both are adjoint to this pairing. Indeed, for [$\delta_{Rf_*K}$](@definition-verdier-dual-evaluation) this holds because under $e_K$
evaluation on $Y$ corresponds to the pairing. Similarly, for $Rf_*\href{@definition-verdier-dual-evaluation}{\delta_K}$ it holds because [$\delta_K$](@definition-verdier-dual-evaluation) is adjoint to evaluation
on $X$ and $e_{\href{@definition-verdier-dual-evaluation}{\mathbb D_XK}}$ is adjoint
to the analogous pairing.
