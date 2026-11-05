+++
kind = "proof"
of = "lemma-internal-adjunction-two-exchange-formulas--1"
order = 830002
uses = ["lemma-kunneth-formula-compact-supports--3"]
+++
The adjunction $Rf_!\dashv f^!$ lives on the localizing
categories $\Loc(D^b_{\mathrm{ctf}}(X,\Lambda))$ and $\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$, and the functors in the argument preserve
them. Pullback is exact, preserves direct sums, and carries the
constructible generators to constructible objects by
Proposition [proposition-six-operations-dctf], so it maps $\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$ into
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
Proposition [proposition-comparison-etale-derived-category] and [Stacks, [0GL5](https://stacks.math.columbia.edu/tag/0GL5)], and for
rational coefficients it is Proposition [proposition-projection-formula-rational-coefficients].
For integral coefficients we compactify $f=pj$, with $j$ an open
immersion and $p$ proper, and combine
Lemma [lemma-projection-formula-integral-coefficients] with
$j_!(M\otimes^{\mathbf L}j^*N)
 \simeq j_!M\otimes^{\mathbf L}N$.

By Proposition [proposition-six-operations-dctf], both $\cHom_Y(Rf_!K,L)$ and
$Rf_*\cHom_X(K,f^!L)$ belong to $D^b_{\mathrm{ctf}}(Y,\Lambda)$, so we may test the
comparison map between them by Yoneda inside the full subcategory
$\Loc(D^b_{\mathrm{ctf}}(Y,\Lambda))$. For every object $N$ of this category we obtain, by the adjunctions and the
projection formula,

$$
\begin{aligned}
\Hom_Y(N,\cHom_Y(Rf_!K,L))
&\simeq\Hom_Y(N\otimes^{\mathbf L}Rf_!K,L)\\
&\simeq\Hom_Y(Rf_!(f^*N\otimes^{\mathbf L}K),L)\\
&\simeq\Hom_X(f^*N\otimes^{\mathbf L}K,f^!L)\\
&\simeq\Hom_Y(N,Rf_*\cHom_X(K,f^!L)).
\end{aligned}
$$

The composite bijection is induced by the map
(10.1). By Yoneda this map is an isomorphism,
which is (10.2).

*Source:* the proof of Lemma [lemma-internal-adjunction-two-exchange-formulas].
